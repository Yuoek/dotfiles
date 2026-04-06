
import os
import re
import glob

def create_toc_folder():
    """创建tocText文件夹"""
    if not os.path.exists('tocText'):
        os.makedirs('tocText')

def detect_format(content):
    """检测文件格式"""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('- '):
            return 2
    return 1

def clean_title(title):
    """清理标题，去掉第几节、第几章、大写数字和标点符号"""
    # 去掉第几节、第几章等前缀
    title = re.sub(r'^第[一二三四五六七八九十]+[章节条]\s*', '', title)
    
    # 去掉开头的大写数字和标点
    title = re.sub(r'^[一二三四五六七八九十]+[、\.\s]*', '', title)
    # title = re.sub(r'^[0-9].*?[、\.\s]*', '', title)
    
    # 去掉其他标点符号（保留字母、数字、下划线、汉字）
    title = re.sub(r'\((.*?)\)', r'（\1）', title)
    # 修改 正则表达式将英文()改为中文（）
    # title = re.sub(r'[^\w\u4e00-\u9fff\s]', '-', title)
    
    return title.strip()

def process_format1(content):
    """处理格式1的文件"""
    lines = content.split('\n')
    result = []
    in_header = False
    
    for line in lines:
        if line.startswith('---'):
            in_header = not in_header
            result.append(line)
            continue
            
        if not in_header and line.startswith('#'):
            # 计算标题级别
            level = len(re.match(r'#+', line).group())
            
            if level >= 2:  # 二级及以下标题降一级
                # 提取标题内容
                title_content = line[level:].strip()
                cleaned_title = clean_title(title_content)
                
                # 构建新的标题行
                new_level = level + 1
                new_line = '#' * new_level + ' ' + cleaned_title
                result.append(new_line)
            else:
                # 一级标题保持不变
                result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)

def process_format2(content):
    """处理格式2的文件"""
    lines = content.split('\n')
    result = []
    in_header = False
    
    for i, line in enumerate(lines):
        if line.startswith('---'):
            in_header = not in_header
            result.append(line)
            continue
            
        if not in_header:
            if line.startswith('- '):
                # 将 - 开头的内容改为四级标题
                title_content = line[2:].strip()
                cleaned_title = clean_title(title_content)
                result.append('#### ' + cleaned_title)
            elif line.startswith('#'):
                # 计算标题级别
                level = len(re.match(r'#+', line).group())
                
                if level >= 2:  # 二级及以下标题降一级
                    title_content = line[level:].strip()
                    cleaned_title = clean_title(title_content)
                    new_level = level + 1
                    new_line = '#' * new_level + ' ' + cleaned_title
                    result.append(new_line)
                else:
                    # 一级标题保持不变
                    result.append(line)
            else:
                result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)

def process_md_files():
    """处理所有md文件"""
    create_toc_folder()
    
    # 获取当前目录所有md文件
    md_files = glob.glob('*.md')
    
    for md_file in md_files:
        print(f"处理文件: {md_file}")
        
        try:
            # 读取文件内容
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检测文件格式
            file_format = detect_format(content)
            print(f"  检测到格式: {file_format}")
            
            # 根据格式处理内容
            if file_format == 1:
                processed_content = process_format1(content)
            else:
                processed_content = process_format2(content)
            
            # 保存处理后的文件
            output_file = os.path.join('tocText', md_file)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            print(f"  处理完成: {output_file}")
            
        except Exception as e:
            print(f"  处理文件 {md_file} 时出错: {str(e)}")

if __name__ == "__main__":
    process_md_files()
 
