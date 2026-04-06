import re
import os
from pathlib import Path

class MarkdownProcessor:
    def __init__(self):
        self.current_section = [0, 0, 0, 0, 0, 0]  # 用于跟踪各级标题编号
        self.column_counter = 0  # 用于跟踪columns计数
    
    def reset_counters(self):
        """重置计数器"""
        self.current_section = [0, 0, 0, 0, 0, 0]
        self.column_counter = 0
    
    def get_next_number(self, level):
        """获取下一级编号"""
        level_index = level - 1
        
        # 增加当前级别的计数器
        self.current_section[level_index] += 1
        
        # 重置所有更低级别的计数器
        for i in range(level_index + 1, len(self.current_section)):
            self.current_section[i] = 0
        
        # 生成编号字符串
        numbers = []
        for i in range(level_index + 1):
            if self.current_section[i] > 0:
                numbers.append(str(self.current_section[i]))
        
        return '.'.join(numbers)
    
    def extract_title_text(self, title_line):
        """提取标题文本，去除原有编号"""
        # 匹配标题标记和文本
        match = re.match(r'(#{1,6})\s+(.*)', title_line)
        if not match:
            return None, None
        
        level = len(match.group(1))
        text = match.group(2).strip()
        
        # 去除原有编号（匹配各种可能的编号格式）
        # 如 "第一章、", "1. ", "1.1. " 等
        text = re.sub(r'^第[一二三四五六七八九十]+章[、.]?\s*', '', text)
        text = re.sub(r'^[一二三四五六七八九十]+[、.]?\s*', '', text)
        text = re.sub(r'^\d+(\.\d+)*[、.]?\s*', '', text)
        text = re.sub(r'^\d+(\.\d+)*[、.]?\s*', '', text)
        text = re.sub(r'[()（）]', ' ', text)
        
        return level, text.strip()

    def generate_anchor(self, number):
        """生成锚点ID，只取数字前两位"""
        return number.split('.')[0][:2]
    
    def process_revealjs_section(self, lines):
        """处理revealjs部分"""
        revealjs_lines = []
        other_lines = []
        in_revealjs = False
        
        for line in lines:
            if line.strip() == '{{< revealjs theme="white" transition="slide" progress="true" controls="true" history="true" >}}':
                in_revealjs = True
                revealjs_lines.append(line)
            elif line.strip() == '{{< /revealjs >}}':
                in_revealjs = False
                revealjs_lines.append(line)
            elif in_revealjs:
                revealjs_lines.append(line)
            else:
                other_lines.append(line)
        
        return revealjs_lines, other_lines
    
    def generate_revealjs_content(self, lines):
        """生成revealjs内容"""
        self.reset_counters()
        revealjs_lines = ['{{< revealjs theme="white" transition="slide" progress="true" controls="true" history="true"  >}}']
        
        current_third_level = None
        third_level_content = []
        
        for line in lines:
            level, text = self.extract_title_text(line)
            if level and text:
                number = self.get_next_number(level)
                
                # 构建revealjs行
                hashes = '#' * level
                revealjs_line = f'{hashes} {number} {text}'
                
                # 处理三级标题
                if level == 3:
                    # 如果之前有三级标题内容，先处理它
                    if current_third_level and third_level_content:
                        revealjs_lines.extend(self.process_revealjs_third_level(current_third_level, third_level_content))
                        third_level_content = []
                    
                    current_third_level = {
                        'number': number,
                        'text': text,
                        'line': revealjs_line
                    }
                    revealjs_lines.append(revealjs_line)
                elif level > 3 and current_third_level:
                    # 四级及以下标题添加到当前三级标题的内容中
                    third_level_content.append({
                        'level': level,
                        'number': number,
                        'text': text,
                        'line': revealjs_line
                    })
                else:
                    revealjs_lines.append(revealjs_line)
            else:
                revealjs_lines.append(line)
        
        # 处理最后一个三级标题
        if current_third_level and third_level_content:
            revealjs_lines.extend(self.process_revealjs_third_level(current_third_level, third_level_content))
        
        revealjs_lines.append('{{< /revealjs >}}')
        return revealjs_lines
    
    def process_revealjs_third_level(self, third_level, sub_content):
        """处理revealjs中的三级标题及其子内容"""
        result = []
        
        # 添加三级标题之间的分隔符
        result.append('---')
        
        # 添加三级标题行
        result.append(third_level['line'])
        
        # 添加四级及以下标题，用___分隔
        for item in sub_content:
            result.append('___')
            result.append(item['line'])
        
        return result
    
    def process_markmap_section(self, lines):
        """处理markmap部分"""
        markmap_lines = []
        in_markmap = False
        other_lines = []
        
        for line in lines:
            if line.strip() == '{{< markmap >}}':
                in_markmap = True
                markmap_lines.append(line)
            elif line.strip() == '{{< /markmap >}}':
                in_markmap = False
                markmap_lines.append(line)
            elif in_markmap:
                markmap_lines.append(line)
            else:
                other_lines.append(line)
        
        return markmap_lines, other_lines
    
    def generate_markmap_content(self, lines):
        """生成markmap内容"""
        self.reset_counters()
        markmap_lines = ['{{< markmap >}}']
        
        for line in lines:
            level, text = self.extract_title_text(line)
            if level and text:
                number = self.get_next_number(level)
                anchor = self.generate_anchor(number)
                
                # 构建markmap行
                hashes = '#' * level
                markmap_line = f'{hashes} {number} [{text}](#{anchor})'
                markmap_lines.append(markmap_line)
        
        markmap_lines.append('{{< /markmap >}}')
        return markmap_lines
    
    def generate_content_sections(self, lines):
        """生成内容部分"""
        self.reset_counters()
        content_lines = []
        current_third_level = None
        third_level_content = []
        
        for line in lines:
            level, text = self.extract_title_text(line)
            if level and text:
                number = self.get_next_number(level)
                anchor = self.generate_anchor(number)
                
                # 构建内容行
                hashes = '#' * level
                content_line = f'{hashes} {number} {text}{{#{anchor}}}'
                
                # 处理三级标题
                if level == 3:
                    # 如果之前有三级标题内容，先处理它
                    if current_third_level and third_level_content:
                        content_lines.extend(self.process_third_level_section(current_third_level, third_level_content))
                        third_level_content = []
                    
                    current_third_level = {
                        'number': number,
                        'text': text,
                        'anchor': anchor,
                        'line': content_line
                    }
                    content_lines.append(content_line)
                elif level > 3 and current_third_level:
                    # 四级及以下标题添加到当前三级标题的内容中
                    third_level_content.append({
                        'level': level,
                        'number': number,
                        'text': text,
                        'anchor': anchor,
                        'line': content_line
                    })
                else:
                    content_lines.append(content_line)
            else:
                content_lines.append(line)
        
        # 处理最后一个三级标题
        if current_third_level and third_level_content:
            content_lines.extend(self.process_third_level_section(current_third_level, third_level_content))
        
        return content_lines
    
    def process_third_level_section(self, third_level, sub_content):
        """处理三级标题及其子内容"""
        result = []
        
        # 添加columns和mermaid
        result.extend(self.generate_columns_section(third_level, sub_content))
        
        return result

    def generate_columns_section(self, third_level, sub_content):
        """生成columns部分，包含mermaid和details"""
        columns_lines = []
        
        # 开始columns
        columns_lines.append('{{% columns ratio="1:1" %}}')
        
        # 生成mermaid流程图
        mermaid_lines = self.generate_mermaid_for_third_level(third_level, sub_content)
        
        # 生成details标签
        details_lines = self.generate_details_for_subcontent(sub_content)
        
        # 根据column_counter决定显示顺序
        if self.column_counter % 2 == 0:  # 偶数columns：mermaid在前，details在后
            columns_lines.extend(mermaid_lines)
            columns_lines.append('<--->')
            columns_lines.extend(details_lines)
        else:  # 奇数columns：details在前，mermaid在后
            columns_lines.extend(details_lines)
            columns_lines.append('<--->')
            columns_lines.extend(mermaid_lines)
        
        # 结束columns
        columns_lines.append('{{% /columns %}}')
        columns_lines.append('')  # 空行分隔
        
        # 增加column计数器
        self.column_counter += 1
        
        return columns_lines
    
    def generate_mermaid_for_third_level(self, third_level, sub_content):
        """为三级标题生成mermaid流程图"""
        mermaid_lines = [
            '```mermaid',
            'mindmap'
        ]
        
        # 添加根节点
        root_id = third_level['number'].replace('.', '-')
        mermaid_lines.append(f'    id{root_id}[{third_level["text"]}]')
        
        # 添加子节点
        for item in sub_content:
            item_id = item['number'].replace('.', '-')
            indent = '    ' * (item['level'] - 2)  # 根据级别调整缩进
            mermaid_lines.append(f'{indent}id{item_id}[{item["text"]}]')
        
        mermaid_lines.append('```')
        mermaid_lines.append('')  # 空行
        
        return mermaid_lines
    
    def generate_details_for_subcontent(self, sub_content):
        """为子内容生成details标签"""
        details_lines = []
        
        for item in sub_content:
            details_lines.append(f'{{{{% details "{item["text"]}" %}}}}')
            details_lines.append('{{% /details %}}')
        
        return details_lines

# 修改，将修改好的output_file 内容追加到原有 input_file
    def process_file(self, input_file, output_file):
        """处理单个文件"""
        print(f"处理文件: {input_file}")
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            lines = original_content.split('\n')
            
            # 分离revealjs部分和其他内容
            revealjs_lines, other_lines = self.process_revealjs_section(lines)
            
            # 如果原文件没有revealjs部分，则生成新的
            if len(revealjs_lines) <= 2:  # 只有开始和结束标签
                revealjs_lines = self.generate_revealjs_content(other_lines)
            
            # 分离markmap部分和其他内容
            markmap_lines, content_lines = self.process_markmap_section(other_lines)
            
            # 如果原文件没有markmap部分，则生成新的
            if len(markmap_lines) <= 2:  # 只有开始和结束标签
                markmap_lines = self.generate_markmap_content(content_lines)
            
            # 生成内容部分
            content_lines = self.generate_content_sections(content_lines)
            
            # 合并结果：revealjs + markmap + 内容
            result_lines = markmap_lines + [''] + revealjs_lines + [''] + content_lines
            
            with open(input_file, 'a', encoding='utf-8') as f:
                f.write('\n\n')  # 添加空行分隔
                f.write('\n'.join(result_lines))

            print(f"成功将处理内容追加到: {input_file}")

            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            start_line = 5  # 第六行（索引从0开始）
            end_marker = "{{< markmap >}}"

            end_line = None
            for i, line in enumerate(lines):
                if end_marker in line:
                    end_line = i
                    break

            if end_line is not None and end_line > start_line:
                del lines[start_line:end_line - 1]  # +1 包含结束标记行
                
                # 重新写入文件
                with open(input_file, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                print(f"已删除第6行到{{< markmap >}}之间的内容")
            else:
                print("未找到{{< markmap >}}标记或标记位置无效")

            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 从第10行开始处理（索引从0开始，所以第10行是索引9）
            content_from_line_10 = ''.join(lines[9:])

            # 修改正则表达式，匹配从---\ntitle:开始到下一个---之间的内容
            pattern = r'(---\ntitle:.*?\n---)'

            # 删除所有匹配的yaml块
            cleaned_content_from_line_10 = re.sub(pattern, '', content_from_line_10, flags=re.DOTALL)
            print("已经清除多余的 title")

            # 重新组合文件内容（保留前9行，加上清理后的内容）
            cleaned_content = ''.join(lines[:9]) + cleaned_content_from_line_10
            print("重新组合完毕")

            # 写入清理后的内容
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
                        
        except Exception as e:
            print(f"处理文件 {input_file} 时出错: {e}")
    
    def process_all_files(self):
        """处理当前目录下所有的md文件"""
        current_dir = Path('.')
        md_files = list(current_dir.glob('*.md'))
        
        for md_file in md_files:
            if md_file.name.startswith('pre_'):
                continue  # 跳过已处理的文件
            
            # 直接修改原文件，不再创建新文件
            self.process_file(md_file, md_file)

def main():
    """主函数"""
    processor = MarkdownProcessor()
    processor.process_all_files()
    print("所有文件处理完成！")

if __name__ == "__main__":
    main();
