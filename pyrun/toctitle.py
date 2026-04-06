import os
import re
import glob

def process_md_files():
    # 创建tocTabs文件夹（如果不存在）
    output_dir = "tocTabs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建文件夹: {output_dir}")
    
    # 获取当前目录所有md文件
    md_files = glob.glob("*.md")
    
    for file_path in md_files:
        print(f"处理文件: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 处理内容
        processed_content = process_content(content, file_path)
        
        # 保存到tocTabs文件夹
        output_path = os.path.join(output_dir, file_path)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        
        print(f"已保存: {output_path}")

def process_content(content, file_path):
    # 获取文件名（不含扩展名）作为标题
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    lines = content.split('\n')
    processed_lines = []
    in_third_level = False
    current_tab_content = []
    tab_titles = []
    tab_contents = []
    
    # 在文件开头添加一级标题
    processed_lines.append(f"# {file_name}")
    processed_lines.append("")  # 添加空行
    
    for line in lines:
        # 检测三级标题
        if line.startswith('### '):
            if current_tab_content and in_third_level:
                # 保存前一个标签的内容
                tab_contents.append('\n'.join(current_tab_content))
                current_tab_content = []
            
            in_third_level = True
            # 提取并清理标题
            title = line[4:].strip()  # 去掉"### "
            # 去掉序号和第几节第几章
            clean_title = re.sub(r'^\d+\.\d+\s*', '', title)  # 去掉"1.1 "这样的序号
            clean_title = re.sub(r'^第[一二三四五六七八九十]+[章节]\s*', '', clean_title)  # 去掉"第一章 "这样的
            clean_title = clean_title.strip()
            
            if clean_title:  # 如果清理后标题不为空
                tab_titles.append(clean_title)
                current_tab_content.append(f"## {clean_title}")
        
        # 如果是三级标题下的内容
        # elif in_third_level and line.strip() and not line.startswith('#') and not line.startswith('{{'):
            # current_tab_content.append(line)
        
        # 遇到其他级别的标题或空行，结束当前三级标题块
        elif (line.startswith('#') and not line.startswith('###')) or (not line.strip() and current_tab_content):
            if current_tab_content and in_third_level:
                tab_contents.append('\n'.join(current_tab_content))
                current_tab_content = []
                in_third_level = False
    
    # 处理最后一个标签
    if current_tab_content and in_third_level:
        tab_contents.append('\n'.join(current_tab_content))
    
    # 生成tabs结构
    if tab_titles and tab_contents:
        processed_lines.append('{{< tabs "1" >}}')
        
        for title, content in zip(tab_titles, tab_contents):
            processed_lines.append(f'{{{{% tab "{title}" %}}}}')
            processed_lines.append(f'{file_name} {title}')
            processed_lines.append('{{% /tab %}}')
        
        processed_lines.append('{{< /tabs >}}')
    
    return '\n'.join(processed_lines)

if __name__ == "__main__":
    process_md_files()
    print("处理完成！所有文件已保存到 tocTabs 文件夹中")
