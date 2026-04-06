##TODO 
## 对合并后的文件 details 的解法没有内容，修改使得正解匹配到内容, 内容为原文件二级标题 ## 解法到文件末尾
## 合并后的文件正文标题获取出错如示Definition for singly-linked list.， 修改使得正确获取一级标题
import os
import re
import glob
from datetime import datetime
from typing import List, Dict, Set

class MDFileMerger:
    def __init__(self):
        self.current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    def parse_md_file(self, file_path: str) -> Dict:
        """解析单个md文件，提取各部分内容"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取文件名中的序号
        filename = os.path.basename(file_path)
        file_number = int(re.search(r'solution_(\d+)', filename).group(1))
        
        # 解析front matter
        front_matter_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if front_matter_match:
            front_matter = front_matter_match.group(1)
            title_match = re.search(r'title:\s*"([^"]+)"', front_matter)
            tags_match = re.search(r'tags:\s*\[([^\]]+)\]', front_matter)
            
            title = title_match.group(1) if title_match else ""
            tags = [tag.strip() for tag in tags_match.group(1).split(',')] if tags_match else []
        else:
            title = ""
            tags = []
        
        # 提取tabs部分
        tabs_match = re.search(r'{{<\s*tabs[^>]*>}}(.*?){{<\s*/tabs\s*>}}', content, re.DOTALL)
        tabs_content = tabs_match.group(1) if tabs_match else ""
        
        # 修复：提取一级标题（改进的正则表达式）
        # 移除front matter后的内容
        content_after_frontmatter = content[front_matter_match.end() + 1:] if front_matter_match else content
        
        # 查找第一个一级标题
        h1_match = re.search(r'^#\s+(\[.+)$', content_after_frontmatter, re.MULTILINE)
        if not h1_match:
            # 如果没有找到标准格式，尝试其他可能的格式
            h1_match = re.search(r'^#(\[.+)$', content_after_frontmatter, re.MULTILINE)
        
        h1_content = h1_match.group(1).strip() if h1_match else title  # 如果没有一级标题，使用front matter中的title
        
        # 提取题目描述和解法
        # 找到一级标题后的内容
        after_h1 = content[h1_match.end():] if h1_match else content_after_frontmatter
        
        # 分割题目描述和解法
        description_match = re.search(r'(##\s*题目描述.*?)(?=##\s*解法|$)', after_h1, re.DOTALL)
        
        # 修改解法提取逻辑：从"## 解法"开始到文件末尾
        solution_match = re.search(r'(##\s*解法.*)', after_h1, re.DOTALL)
        
        description_content = description_match.group(1).strip() if description_match else ""
        solution_content = solution_match.group(1).strip() if solution_match else ""
        
        return {
            'file_number': file_number,
            'title': title,
            'tags': tags,
            'tabs_content': tabs_content,
            'h1_content': h1_content,
            'description_content': description_content,
            'solution_content': solution_content
        }
    
    def generate_markmap(self, files_data: List[Dict], batch_num: int) -> str:
        """生成markmap内容"""
        markmap_lines = ['{{< markmap >}}']
        
        for file_data in files_data:
            title = file_data['title']
            file_num = file_data['file_number']
            tags = file_data['tags']
            
            # 三级标题带超链接
            markmap_lines.append(f'### [{title}](#{file_num})')
            
            # 四级标题（tags）
            for tag in tags:
                markmap_lines.append(f'#### [{tag}](#{file_num})')
        
        markmap_lines.append('{{< /markmap >}}')
        return '\n'.join(markmap_lines)
    
    def generate_revealjs(self, files_data: List[Dict]) -> str:
        """生成revealjs内容"""
        revealjs_lines = [
            '{{< revealjs theme="white" transition="slide" progress="true" controls="true" history="true" >}}'
        ]
        
        for i, file_data in enumerate(files_data):
            title = file_data['title']
            tags = file_data['tags']
            
            # 三级标题
            revealjs_lines.append(f'### {title}')
            
            # 四级标题（tags）
            for tag in tags:
                revealjs_lines.append('___')
                revealjs_lines.append(f'#### {tag}')
            
            # 文件间分隔符
            if i < len(files_data) - 1:
                revealjs_lines.append('---')
        
        revealjs_lines.append('{{< /revealjs >}}')
        return '\n'.join(revealjs_lines)
    
    def generate_tags_table(self, all_tags: Set[str]) -> str:
        """生成tags表格"""
        tags_list = sorted(list(all_tags))
        
        # 将tags分成3列
        table_lines = [
            '',
            '{{< katex />}}',
            '',
            '| Tag1 | Tag2 | Tag3 |',
            '| --------------- | --------------- | --------------- |'
        ]
        
        # 每3个tags一行
        for i in range(0, len(tags_list), 3):
            row_tags = tags_list[i:i+3]
            # 补全到3个
            while len(row_tags) < 3:
                row_tags.append('')
            table_lines.append(f'| {row_tags[0]} | {row_tags[1]} | {row_tags[2]} |')
        
        return '\n'.join(table_lines)
    
    def merge_files(self, file_paths: List[str], batch_num: int) -> str:
        """合并多个文件"""
        files_data = []
        all_tags = set()
        
        # 解析所有文件
        for file_path in file_paths:
            file_data = self.parse_md_file(file_path)
            files_data.append(file_data)
            all_tags.update(file_data['tags'])
        
        # 生成合并内容
        merged_content = []
        
        # Front matter
        first_file = files_data[0]
        merged_content.extend([
            '---',
            f'title: "{first_file["title"]}"',
            f'date: {self.current_time}',
            f'weight: {batch_num}',
            f'tags: [{", ".join(sorted(all_tags))}]',
            '---',
            ''
        ])
        
        # Markmap
        merged_content.append(self.generate_markmap(files_data, batch_num))
        merged_content.append('')
        
        # Revealjs
        merged_content.append(self.generate_revealjs(files_data))
        merged_content.append('')
        
        # Tags表格
        merged_content.append(self.generate_tags_table(all_tags))
        merged_content.append('')
        
        # 各个文件的内容
        for file_data in files_data:
            file_num = file_data['file_number']
            
            # 一级标题（带锚点）
            if file_data['h1_content']:
                merged_content.append(f'# {file_data["h1_content"]}{{#{file_num}}}')
                merged_content.append('')
            
            # Tabs内容
            if file_data['tabs_content']:
                merged_content.append(f'{{{{< tabs "{file_num}" >}}}}')
                merged_content.append(file_data['tabs_content'])
                merged_content.append('{{< /tabs >}}')
                merged_content.append('')
            
            # 题目描述（用hint和details包裹）
            if file_data['description_content']:
                merged_content.extend([
                    '{{% hint info %}}',
                    '{{% details "题目描述" %}}',
                    file_data['description_content'],
                    '{{% /details %}}',
                    '{{% /hint %}}',
                    ''
                ])
            
            # 解法（用hint和details包裹）
            if file_data['solution_content']:
                merged_content.extend([
                    '{{% hint info %}}',
                    '{{% details "解法" %}}',
                    file_data['solution_content'],
                    '{{% /details %}}',
                    '{{% /hint %}}',
                    ''
                ])
        
        return '\n'.join(merged_content)
    
    def process_directory(self, directory: str = ".", batch_size: int = 10):
        """处理当前目录下的所有md文件"""
        # 获取所有solution_*.md文件
        pattern = os.path.join(directory, "solution_*.md")
        md_files = glob.glob(pattern)
        
        # 按文件名排序
        md_files.sort(key=lambda x: int(re.search(r'solution_(\d+)', x).group(1)))
        
        # 分批处理
        for i in range(0, len(md_files), batch_size):
            batch_files = md_files[i:i+batch_size]
            batch_num = i // batch_size + 1
            
            if batch_files:
                merged_content = self.merge_files(batch_files, batch_num)
                
                # 保存合并后的文件
                output_filename = f"Pre_solution_{batch_num:04d}.md"
                output_path = os.path.join(directory, output_filename)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(merged_content)
                
                print(f"已生成: {output_path} (包含 {len(batch_files)} 个文件)")

def main():
    merger = MDFileMerger()
    merger.process_directory()

if __name__ == "__main__":
    main()
