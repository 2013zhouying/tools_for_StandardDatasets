import os
import argparse
import csv
from utils import test_config

# 查找某个关键词在第几列
def find_key_row(list, key):
    for i,data in enumerate(list):
        if data==key:
            return i

# 解析csv 信息
def extract_csv(csv_path):
    url_lists = []
    line_id = 0
    if not os.path.isfile(csv_path):
        print("{} 这个文件不存在".format(csv_path))
        return int(line_id), url_lists
    with open(csv_path, "r", encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        csv_header = next(reader)
        print('header: ', csv_header)
        i = find_key_row(csv_header, 'img_url')
        for row in reader:
            #print(row)
            url_lists.append(row[i])
            line_id = int(row[0])

    return line_id, url_lists

def main(args):
    extract_csv(args.csv_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_path', type=str, default=test_config.CSV_PATH)  # csv文件存放地址
    args = parser.parse_args()
    main(args)
