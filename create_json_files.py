from utils import read_csv,read_mm
import pandas as pd
import json
import os
import csv

# 映射字典
dict_1 = {
    "\ufeff数据集名称":"dataset_name",
    "数据集路径":"dataset_path",
    "数据集所属组别":"publishing_group",
    "负责人":"dataset_owner",
	"任务大类":"task_categories",
    "任务子类":"subtask_categories",
    "检索关键词":"search_keywords",
	"数据类型":"data_type",
    "标注类型":"annotation_type",
    "数据标注格式":"annotation_format",
	"【建议填】数据集来源":"dataset_source",
    "【建议填】标注方式":"labeling_party",
	"【建议填】拍摄设备":"shooting_device",
    "【建议填】数据集应用产品":"support_product_lines",
}

# 需要填写的模板字典
template_dict_2 = {
    "dataset_name":[],
    "dataset_path":[],
    "publishing_group":[],
    "dataset_owner":[],
	"task_categories": [],
    "subtask_categories":[],
    "search_keywords": [],
	"data_type": [],
    "annotation_type": [],
    "annotation_format": [],
	"dataset_source": {
        "public_dataset": [],
        "company_product_shooting": [],
        "web_crawler(youtube)": [],
        "company_simulation_dataset": [],
        "other":[],
        "unknown":[]
    },
    "labeling_party": {
        "public_annotations": [],
        "purchasing_annotations": [],
        "machine_annotations": [],
        "data_group_annotations": [],
        "other":[],
        "unknown":[]
    },
	"shooting_device": [],
    "support_product_lines": [],
    # 可以根据需要继续添加字段
}

dict_3 = {
    "【建议填】数据集来源": "【建议填】数据集来源占比",
    "【建议填】标注方式":"【建议填】标注方式占比"

}

# CSV文件路径
mm_file_path = 'data/任务分类.mm'
csv_file_path = 'data/规范数据集信息记录表_规范数据集信息记录表.csv'  # 你需要输入CSV文件的实际路径
# 存储生成的JSON文件的目录
json_output_directory = 'output'  # 你需要输入存储JSON文件的目录路径

# 读取CSV文件，并解析每行生成JSON
datasets_name_list = []
j = 0
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row_number, row in enumerate(reader, start=1):
        # print(row_number, row)

        if '/media/3_sdc/datasets/Insta360Det' in row["数据集路径"]:
            j += 1

        
        #print(row_number, row['\ufeff数据集名称'], row['数据集路径'] )
        if row['\ufeff数据集名称'] in datasets_name_list:
            print("请注意，数据集名称有重名，重名的是：", row_number, row['\ufeff数据集名称'])
            break
        else:
            datasets_name_list.append(row['\ufeff数据集名称'])
        
        # 创建一个新的字典副本来存放我们的数据
        output_dict = template_dict_2.copy()
        # 遍历dict_1映射关系，将csv行数据映射到output_dict中
        for csv_field, json_field in dict_1.items():
            #print(csv_field, json_field)
            
            # 使用dict_1中定义的映射填充output_dict
            #print(row[csv_field])
            
            if row[csv_field].strip():
                # 判定csv_field对应的template_dict_2中的值类型来进行处理
                if isinstance(template_dict_2[json_field], list):
                    if csv_field=="任务子类":
                        source_list = row[csv_field].split(', ')  # 将csv中的字符串转换成列表
                        subnode_list = read_mm.find_subnodes_except_first_level(mm_file_path)  # 输出除一级父节点以外的所有子节点的列表
                        normal_elements_with_spaces = read_mm.find_and_combine_elements(source_list, subnode_list)  #将零散的元素组合成.mm文件中的带空格的元素         
                        automatically_supplement_parent_nodes_list = read_mm.check_names_in_mm(mm_file_path, normal_elements_with_spaces)  # 给定一个或多个名称的列表，输出该列表中元素在给定的mm文件中的所有父节点（除根节点和根节点的一级子节点外）名称列表
                        output_dict[json_field] =  automatically_supplement_parent_nodes_list 
                    else:   
                        # 修改前 
                        # output_dict[json_field] = row[csv_field].split(',')
                        # 修改后
                        trimmed_list = [s.lstrip() for s in row[csv_field].split(',')]  # 移除字符串前的空格
                        output_dict[json_field] =  trimmed_list   
                elif isinstance(template_dict_2[json_field], dict):
                    #print(csv_field)
                    if csv_field=="【建议填】数据集来源":
                        output_dict[json_field] = {
                            "Public Dataset": 0,
                            "Insta360 Product Shooting": 0,
                            "WebCrawler": 0,
                            "Insta360 Simulation Dataset": 0,
                            "other":0,
                            "unknown":0
                        }
                        for i in range(len(row[csv_field].split(','))):
                            try:
                                output_dict[json_field][row[csv_field].split(',')[i].lstrip()] = int(row[dict_3[csv_field]].split(',')[i])# #删除列表中每个元素前面的空白字符，可以使用内置的`strip()`方法，它用于去除字符串前后的空白字符
                            except:
                                output_dict[json_field][row[csv_field].split(',')[i].lstrip()] = row[dict_3[csv_field]].split(',')[i]   # row[dict_3[csv_field]].split(',')[i] 有可能为空
                    else:
                        output_dict[json_field] = {
                            "Publicly-available": 0,
                            "Purchased":0,
                            "Auto-labeled":0,
                            "Annotated-by-R&D": 0,
                            "Simulationed": 0,
                            "other":0,
                            "unknown":0
                        }
                        for i in range(len(row[csv_field].split(','))):
                            try:
                                output_dict[json_field][row[csv_field].split(',')[i].lstrip()] = int(row[dict_3[csv_field]].split(',')[i])# #删除列表中每个元素前面的空白字符，可以使用内置的`strip()`方法，它用于去除字符串前后的空白字符
                            except:
                                output_dict[json_field][row[csv_field].split(',')[i].lstrip()] = row[dict_3[csv_field]].split(',')[i]   # row[dict_3[csv_field]].split(',')[i] 有可能为空

                else:
                    output_dict[json_field] = row[csv_field]
        

        json_output_directory = row['数据集路径']
        # 生成json文件名
        json_filename = f'{json_output_directory}/StandardFields.json'
        # 写入JSON文件
        try:
            with open(json_filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(output_dict, jsonfile, ensure_ascii=False, indent=4)
                #j += 1
                #print(row_number, json_filename)
                
        except:
            print(row_number, json_filename)
        #break
print(j)
print('JSON files are generated successfully.')



