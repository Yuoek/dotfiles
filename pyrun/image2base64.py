# 用python png2base64.py yu.png, feature.jpg后，python 将图片转为base64,其中图片格式有png, jpg等，并保存为yu_png.md, feature_jpg.md, 并显示原图片信息, 并在md中直接显示图片， 写出image2base64.py 代码
#!/usr/bin/env python3
"""
图片转Base64编码工具
用法: python image2base64.py <图片文件1> <图片文件2> ...
"""

import sys
import os
import base64
import mimetypes
from PIL import Image
import argparse

def get_image_info(image_path):
    """获取图片信息"""
    try:
        with Image.open(image_path) as img:
            info = {
                'format': img.format,
                'mode': img.mode,
                'size': img.size,
                'width': img.width,
                'height': img.height,
                'filename': os.path.basename(image_path)
            }
            return info
    except Exception as e:
        print(f"无法读取图片信息: {e}")
        return None

def image_to_base64(image_path):
    """将图片转换为Base64编码"""
    try:
        # 获取图片的MIME类型
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            # 根据文件扩展名确定MIME类型
            ext = os.path.splitext(image_path)[1].lower()
            if ext == '.png':
                mime_type = 'image/png'
            elif ext in ['.jpg', '.jpeg']:
                mime_type = 'image/jpeg'
            elif ext == '.gif':
                mime_type = 'image/gif'
            elif ext == '.bmp':
                mime_type = 'image/bmp'
            elif ext == '.webp':
                mime_type = 'image/webp'
            else:
                mime_type = 'application/octet-stream'
        
        # 读取图片文件并编码
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            base64_data = base64.b64encode(img_data).decode('utf-8')
            
        return f"data:{mime_type};base64,{base64_data}"
    except Exception as e:
        print(f"转换图片失败: {e}")
        return None

def save_to_markdown(image_path, base64_str, image_info):
    """保存Base64编码到Markdown文件"""
    try:
        # 生成输出文件名
        filename = os.path.basename(image_path)
        name_without_ext = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1].lower().replace('.', '')
        output_file = f"{name_without_ext}_{ext}.md"
        
        # 写入Markdown文件
        with open(output_file, 'w', encoding='utf-8') as f:
            # 写入标题
            f.write(f"# 图片信息: {filename}\n\n")
            
            # 写入图片信息
            f.write(f"- **文件名**: {image_info['filename']}\n")
            f.write(f"- **格式**: {image_info['format']}\n")
            f.write(f"- **尺寸**: {image_info['width']} × {image_info['height']} 像素\n")
            f.write(f"- **颜色模式**: {image_info['mode']}\n")
            
            # 写入Base64编码的图片
            f.write("图片预览:\n\n")
            f.write(f"![{filename}]({base64_str})\n\n")
            
            # 写入纯Base64数据（不含data URI前缀）
            # 移除data URI前缀
            if base64_str.startswith('data:'):
                pure_base64 = base64_str.split(',', 1)[1]
            else:
                pure_base64 = base64_str
            
            f.write(f"\n*完整Base64数据长度: {len(pure_base64)} 字符*\n")
        
        print(f"已保存到: {output_file}")
        return output_file
    except Exception as e:
        print(f"保存Markdown文件失败: {e}")
        return None

def display_image_info(image_info):
    """显示图片信息"""
    print(f"图片信息:")
    print(f"  文件名: {image_info['filename']}")
    print(f"  格式: {image_info['format']}")
    print(f"  尺寸: {image_info['width']} × {image_info['height']} 像素")
    print(f"  颜色模式: {image_info['mode']}")
    print("-" * 40)

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='将图片转换为Base64编码并保存为Markdown文件')
    parser.add_argument('images', nargs='+', help='要转换的图片文件路径')
    parser.add_argument('--output-dir', '-o', help='输出目录（默认为当前目录）')
    
    args = parser.parse_args()
    
    # 设置输出目录
    output_dir = args.output_dir or os.getcwd()
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 处理每个图片文件
    for image_path in args.images:
        if not os.path.exists(image_path):
            print(f"错误: 文件不存在 - {image_path}")
            continue
        
        print(f"\n处理图片: {image_path}")
        
        # 获取图片信息
        image_info = get_image_info(image_path)
        if not image_info:
            print(f"跳过: 无法读取图片信息 - {image_path}")
            continue
        
        # 显示图片信息
        display_image_info(image_info)
        
        # 转换为Base64
        base64_str = image_to_base64(image_path)
        if not base64_str:
            print(f"跳过: 无法转换图片 - {image_path}")
            continue
        
        # 保存到Markdown文件
        original_dir = os.getcwd()
        try:
            if output_dir:
                os.chdir(output_dir)
            save_to_markdown(image_path, base64_str, image_info)
        finally:
            os.chdir(original_dir)
    
    print("\n处理完成!")

if __name__ == "__main__":
    # 如果没有命令行参数，显示用法
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n示例:")
        print("  python image2base64.py yu.png feature.jpg")
        print("  python image2base64.py --output-dir ./output image1.jpg image2.png")
    else:
        main()
