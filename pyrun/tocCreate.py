import sys
import os
from datetime import datetime

def create_toc_file(filename):
    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    # 提取文件名（去掉扩展名）
    base_name = os.path.splitext(filename)[0]
    
    # 构建文件内容
    content = f'''---
title: "{base_name}"
date: {current_date}
weight:
categories: ""
tags: ""
series: ""
series_order: ""
type: ""
---

{{< katex />}}

{base_name}
'''
    
    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"文件 {filename} 创建成功！")

def main():
    if len(sys.argv) < 2:
        print("用法: python tocCreate.py <filename1> [filename2] [filename3] ...")
        print("例如: python tocCreate.py html css javascript")
        print("例如: python tocCreate.py chapter1.md chapter2.md")
        sys.exit(1)
    
    # 获取所有命令行参数（从第二个开始）
    filenames = sys.argv[1:]
    
    for input_filename in filenames:
        # 确保文件扩展名为 .md
        if not input_filename.endswith('.md'):
            filename = input_filename + '.md'
        else:
            filename = input_filename
        
        create_toc_file(filename)

if __name__ == "__main__":
    main()
