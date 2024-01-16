import os

#当前文件的路径
pwd = os.getcwd()
#当前文件的父路径
father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")

# write_csv.py
POST_STR = '{ "id": "1", "time": "2021-06-08 18:23:17", "web": "baidu", "word": "dog", "width": 1080, "height": 720, "img_url": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3446971186,1887251731&fm=26&gp=0.jpg"}'
CSV_PATH = father_path + '/ScarpingData/dog.csv'

# read_csv.py
CSV_PATH_2 = father_path + '/ScarpingData/dog.csv'