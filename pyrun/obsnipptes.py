import os
import re
import json

def convert_md_to_js(md_content):
    """
    将markdown内容转换为JavaScript代码片段格式
    """
    # 匹配三级标题和对应的代码块
    pattern = r'###\s*(.+?)\n```(\w+)\s*\n(.*?)\n```'
    matches = re.findall(pattern, md_content, re.DOTALL)
    
    snippets = []
    for match in matches:
        trigger = match[0].strip()
        language = match[1].strip()
        code_content = match[2].strip()
        
        # 处理代码内容中的特殊字符
        code_content = code_content.replace('"', '\\"').replace('\n', '\\n')
        
        snippet = {
            "trigger": trigger,
            "replacement": code_content,
            "options": "cA"
        }
        snippets.append(snippet)
    
    return snippets

def process_md_files():
    """
    处理当前目录下的所有md文件
    """
    current_dir = os.getcwd()
    
    # 创建snippets目录（如果不存在）
    snippets_dir = os.path.join(current_dir, 'snippets')
    if not os.path.exists(snippets_dir):
        os.makedirs(snippets_dir)
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        if filename.endswith('.md'):
            md_file_path = os.path.join(current_dir, filename)
            
            # 读取md文件内容
            with open(md_file_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # 转换为代码片段
            snippets = convert_md_to_js(md_content)
            
            if snippets:
                # 生成对应的js文件名
                js_filename = filename.replace('.md', '.md')
                js_file_path = os.path.join(snippets_dir, js_filename)
                
                # 写入js文件
                with open(js_file_path, 'w', encoding='utf-8') as f:
                    f.write('[\n')
                    for i, snippet in enumerate(snippets):
                        # 构建JavaScript对象字符串
                        snippet_str = f'\t{{trigger: "{snippet["trigger"]}", replacement: "{snippet["replacement"]}", options: "{snippet["options"]}"}}'
                        if i < len(snippets) - 1:
                            snippet_str += ','
                        f.write(snippet_str + '\n')
                    f.write(']\n')
                
                print(f'成功转换: {filename} -> snippets/{js_filename}')
            else:
                print(f'警告: {filename} 中没有找到有效的代码片段')

if __name__ == '__main__':
    process_md_files()
    print('转换完成！')
