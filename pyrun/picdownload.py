# 用 python pic.py https://img3.doubanio.com/view/photo/l/public/p2928985187.webp 下载图片
import sys
import requests

def download_image(url, filename=None):
    try:
        # 添加浏览器请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.douban.com/',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
        
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        if filename is None:
            # 从URL提取文件名
            filename = url.split('/')[-1]
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"图片已下载: {filename}")
        return True
        
    except Exception as e:
        print(f"下载失败: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python pic.py <图片URL> [保存文件名]")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    download_image(url, filename)
