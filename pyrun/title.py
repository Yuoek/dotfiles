import sys
import re
import os

def sanitize_filename(title):
    """将标题转换为安全的文件名，用下划线替换空格和特殊字符"""
    # 移除markdown标题标记
    title = title.replace('##', '').strip()
    # 替换空格和特殊字符为下划线
    sanitized = re.sub(r'[\s\/\&\?\.]', '_', title)
    return sanitized

def create_files_from_headings(markdown_file):
    """从markdown文件读取二级标题并创建对应文件"""
    
    if not os.path.exists(markdown_file):
        print(f"错误：文件 {markdown_file} 不存在")
        return
    
    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 使用正则表达式匹配所有二级标题
        headings = re.findall(r'##\s+(.+)$', content, re.MULTILINE)
        
        if not headings:
            print("未找到二级标题")
            return
        
        print(f"找到 {len(headings)} 个二级标题：")
        
        # 存储创建的文件信息
        created_files = []
        
        # 为每个标题创建文件
        for i, heading in enumerate(headings, 1):
            # 清理文件名
            filename = sanitize_filename(heading)
            # 添加编号
            numbered_filename = f"{i:03d}_{filename}.md"
            
            print(f"创建文件: {numbered_filename}")
            
            # 创建markdown文件
            with open(numbered_filename, 'w', encoding='utf-8') as new_file:
                new_file.write(f"## {i:03d} {heading}\n\n")
            
            # 保存文件信息用于生成链接
            created_files.append({
                'original_heading': heading,
                'filename': numbered_filename
            })
        
        # 在原始markdown文件中添加超链接
        add_links_to_original_file(markdown_file, created_files)
                
    except Exception as e:
        print(f"处理文件时出错: {e}")

def add_links_to_original_file(markdown_file, created_files):
    """在原始markdown文件中添加文件超链接"""
    
    # 读取原始文件内容
    with open(markdown_file, 'r', encoding='utf-8') as file:
        original_content = file.read()
    
    # 构建链接部分
    links_section = "\n\n## 文件链接\n\n"
    for file_info in created_files:
        links_section += f"- [{file_info['original_heading']}]({file_info['filename']})\n"
    
    # 将链接添加到文件末尾
    new_content = original_content + links_section
    
    # 写回文件
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"\n已在 {markdown_file} 中添加 {len(created_files)} 个文件链接")

def main():
    if len(sys.argv) != 2:
        print("使用方法: python title.py <markdown文件>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    create_files_from_headings(markdown_file)

if __name__ == "__main__":
    main()
