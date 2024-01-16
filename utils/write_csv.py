import json
import os
import argparse
import csv
from utils import test_config


# 读取字典的key值列表和值列表
def get_dict_keys_values(content):
    csv_header = []
    csv_values = []
    for headers in content.keys():  # 把字典的键取出来
        csv_header.append(headers)
        csv_values.append(content[headers])
    #print(csv_header, csv_values)
    return csv_header, csv_values

# 追加写入csv
def write_csv_append(csv_path, content):
    csv_header, csv_values = get_dict_keys_values(content)

    if not os.path.isfile(csv_path):
        with open(csv_path, 'w+', encoding='utf-8-sig', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(csv_header)
            print('新创建一个 {} 文件，表头为：{}'.format(csv_path, csv_header))

    with open(csv_path, 'a+', encoding='utf-8-sig', newline="") as file:
        writer = csv.writer(file)
        data = csv_values
        writer.writerow(data)
        #print(data)

def main(args):
    # post_dict = json.loads(args.post_str)  # 使用 json 进行转换存在一个潜在的问题。json 语法规定 数组或对象之中的字符串必须使用双引号，不能使用单引号
    write_csv_append(args.csv_path, json.loads(args.post_str))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str, default=test_config.CSV_PATH_2)  # csv文件存放地址
    parser.add_argument('--post_str', type=str, default=test_config.POST_STR)  # 保存的数据、字符串
    args = parser.parse_args()
    main(args)
