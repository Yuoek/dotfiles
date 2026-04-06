import os
import re
import json
from glob import glob

def extract_md_content(file_path):
    """从markdown文件中提取三级标题和对应的代码块"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配三级标题和后续的代码块
    pattern = r'### (.*?)\n\n```(?:cpp|c|python|java|markdown|mermaid)\s*\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    result = {}
    for title, code_block in matches:
        # 清理标题中的空格和特殊字符
        clean_title = title.strip()
        key = "" + clean_title.replace(" ", "")
        
        # 将代码块按行分割
        code_lines = [line for line in code_block.split('\n') if line.strip()]
        
        result[key] = {
            "prefix": key,
            "body": code_lines
        }
    
    return result

def process_all_md_files():
    """处理当前目录下所有md文件"""
    all_data = {}
    
    # 获取当前目录下所有.md文件
    md_files = glob("*.md")
    
    for md_file in md_files:
        print(f"处理文件: {md_file}")
        try:
            file_data = extract_md_content(md_file)
            all_data.update(file_data)
        except Exception as e:
            print(f"处理文件 {md_file} 时出错: {e}")
    
    return all_data

def save_to_json(data, output_file="output.json"):
    """将数据保存为JSON文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"JSON文件已生成: {output_file}")

if __name__ == "__main__":
    # 处理所有md文件
    extracted_data = process_all_md_files()
    
    if extracted_data:
        # 保存为JSON文件
        save_to_json(extracted_data)
        
        # 同时打印到控制台
        print("\n生成的JSON内容:")
        print(json.dumps(extracted_data, ensure_ascii=False, indent=2))
    else:
        print("未找到任何三级标题和代码块")

