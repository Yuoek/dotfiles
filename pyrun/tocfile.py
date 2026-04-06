import os
import re
import datetime
from pathlib import Path

def process_md_files(root_dir=".", output_dir="tocFile"):
    """
    遍历根目录下的所有md文件，按tab标签拆分并创建新的md文件
    
    Args:
        root_dir: 根目录路径
        output_dir: 输出目录
    """
    
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # 遍历根目录下的所有md文件
    for md_file in Path(root_dir).glob("*.md"):
        print(f"处理文件: {md_file}")
        
        # 读取文件内容
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取tab标签内容
        tabs_pattern = r'{{% tab "([^"]+)" %}}(.*?){{% /tab %}}'
        matches = re.findall(tabs_pattern, content, re.DOTALL)
        
        if not matches:
            print(f"在文件 {md_file} 中未找到tab标签")
            continue
        
        # 创建与md文件同名的文件夹
        folder_name = md_file.stem  # 去掉扩展名的文件名
        folder_path = output_path / folder_name
        folder_path.mkdir(exist_ok=True)
        
        # 获取当前日期
        current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
        
        # 处理每个tab标签
        for i, (tab_title, tab_content) in enumerate(matches, 1):
            # 清理tab标题中的特殊字符
            clean_title = re.sub(r'[/()（）]', '_', tab_title)
            
            # 生成新文件名
            new_filename = f"{i}_{clean_title}.md"
            new_file_path = folder_path / new_filename
            
            # 创建头文件信息
            header = f"""---
title: "{tab_title}"
date: {current_date}
weight: {i}
---

"""
            
            # 写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(header + tab_content.strip())
            
            print(f"创建文件: {new_file_path}")

def main():
    """主函数"""
    print("开始处理md文件...")
    
    try:
        process_md_files()
        print("处理完成！")
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

if __name__ == "__main__":
    main()
