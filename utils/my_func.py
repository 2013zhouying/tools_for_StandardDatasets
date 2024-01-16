import time
from utils import test_config
import argparse

# 保存图片的字典信息
def extract_image_post(line_id, web, search_words, width, height, img_url):
    current_time = time.strftime("%Y-%m-%d", time.localtime())
    temp = {
        "id": str(line_id),
        "scarp_time":current_time,
        'web':web,
        'word': search_words,
        'width':width,
        'height':height,
        'img_url': img_url
    }
    return temp

# 保存视频的字典信息
def extract_video_post(line_id, web, search_words, video_name, video_url):
    current_time = time.strftime("%Y-%m-%d", time.localtime())
    temp = {
        'id': str(line_id),
        'scarp_time': current_time,
        'web':web,
        'search_word': search_words,
        'video_name': video_name,
        'video_url': video_url
    }
    return temp


