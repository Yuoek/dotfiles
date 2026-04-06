
import os
import re
import requests
import sys

def get_video_pages(bv_number):
    base_url = f"https://www.bilibilix.com/video/{bv_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        html_content = response.text
        
        # 解析页面中的视频总数
        match = re.search(r'"page_count":(\d+)', html_content)
        if match:
            page_count = int(match.group(1))
        else:
            page_count = 1  # 如果没有匹配到多页，则只有一个视频
        
        return page_count
    except Exception as e:
        print(f"获取视频页面失败: {e}")
        return 0

def download_video(bv_number, page_count):
    for page in range(1, page_count + 1):
        video_url = f"https://www.bilibilix.com/video/{bv_number}?p={page}"
        print(f"正在下载: {video_url}")
        
        # 使用 you-get 下载视频
        try:
            os.system(f"you-get {video_url}")
        except Exception as e:
            print(f"下载失败: {e}")

def main():
    if len(sys.argv) != 2:
        print("使用方法: python blidown.py BV号")
        return
    
    bv_number = sys.argv[1]
    print(f"正在解析 BV号: {bv_number}")
    
    page_count = get_video_pages(bv_number)
    if page_count > 0:
        print(f"发现 {page_count} 个视频页面")
        download_video(bv_number, page_count)
    else:
        print("未找到相关视频或解析失败")

if __name__ == "__main__":
    main()
