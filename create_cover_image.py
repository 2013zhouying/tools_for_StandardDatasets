import csv
import os
from PIL import Image

mm_file_path = 'data/任务分类.mm'
csv_file_path = 'data/规范数据集信息记录表_规范数据集信息记录表.csv'  # 你需要输入CSV文件的实际路径
cover_images_path = 'data/cover_images'
# 存储生成的JSON文件的目录
output_directory = 'output'  # 你需要输入存储JSON文件的目录路径

# 读取CSV文件，并解析每行生成JSON
datasets_name_list = []
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row_number, row in enumerate(reader, start=1):
        #print(row_number, row['\ufeff数据集名称'], row['数据集路径'] )
        if row['\ufeff数据集名称'] in datasets_name_list:
            print("请注意，数据集名称有重名，重名的是：", row_number, row['\ufeff数据集名称'])
            break
        else:
            datasets_name_list.append(row['\ufeff数据集名称'])


        filename = row['\ufeff数据集名称'] + '.jpg'
        image_path = os.path.join(cover_images_path, filename)
        #print(image_path)
        if os.path.isfile(image_path):
            with Image.open(image_path) as img:
                # 获取图片尺寸
                width, height = img.size

                # 计算需要裁剪的最大正方形尺寸
                new_edge = min(width, height)

                # 计算裁剪的左上角点坐标
                left = (width - new_edge) // 2
                top = (height - new_edge) // 2
                right = (width + new_edge) // 2
                bottom = (height + new_edge) // 2

                # 裁剪图片
                img_cropped = img.crop((left, top, right, bottom))

                # 构建新的文件名和路径以保存裁剪后的图片
                new_filename = f"cover_image.jpg"    # f"{os.path.splitext(filename)[0]}_cropped{os.path.splitext(filename)[1]}"
                output_directory = row['数据集路径']
                new_image_path = os.path.join(output_directory, new_filename)
                #print(new_image_path)

                # 保存裁剪后的图片
                try:
                    img_cropped.save(new_image_path)
                except:
                    print(new_image_path, "Cann't create cover_image.jpg, Permission denied")
        else:
            continue
            print("该图片不存在")

        #break
        

        

        





