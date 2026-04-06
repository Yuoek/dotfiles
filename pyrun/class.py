import os
import sys
from datetime import datetime

def create_markdown_files(num_files, folder_name, bilibili_code):
    # 获取当前时间
    now = datetime.now()
    date_format = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    # 创建目标文件夹
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 批量创建 markdown 文件
    for i in range(1, num_files + 1):
        file_name = f"lecture-{i:03d}.md"
        file_path = os.path.join(folder_name, file_name)
        
        # 定义文件内容
        content = f"""---
title: "Lecture-{i}"
date: {date_format}
categories: ""
tags: ""
series: ""
series_order: ""
type: ""
weight: {i}
---

## {folder_name} {i:03d}

{{{{< bilibili {bilibili_code} {i} >}}}}
"""
        # 写入文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    # 创建 _index.md 文件
    index_file_path = os.path.join(folder_name, "_index.md")
    index_content = f"""---
title: "{folder_name}"
date: {date_format}
categories: ""
tags: ""
series: ""
series_order: ""
type: ""
bookCollapseSection: true
---
"""
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"Successfully created {num_files} markdown files and _index.md in '{folder_name}' folder.")

if __name__ == "__main__":
    # 从命令行参数获取输入
    if len(sys.argv) != 4:
        print("Usage: python script.py <num_files> <folder_name> <bilibili_code>")
        sys.exit(1)
    
    try:
        num_files = int(sys.argv[1])
        folder_name = sys.argv[2]
        bilibili_code = sys.argv[3]
        
        create_markdown_files(num_files, folder_name, bilibili_code)
    except ValueError:
        print("The first argument (num_files) must be an integer.")
        sys.exit(1)
