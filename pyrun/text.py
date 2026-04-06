```python
import os
import re
import datetime
from pathlib import Path

def process_md_file(file_path):
    """处理单个md文件，提取tab标签并创建对应的md文件"""
        
        # 读取原文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
        # 使用正则表达式提取所有tab标签内容
        pattern = r'{{%\s*tab\s*"([^"]+)"\s*%}}([\s\S]*?){{%\s*/tab\s*%}}'
        matches = re.findall(pattern, content)
        
        if not matches:
                print(f"在文件 {file_path} 中未找到tab标签")
                return
            
        # 获取当前日期
        current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
        
        # 处理每个tab标签
        for index, (tab_name, tab_content) in enumerate(matches, 1):
                # 清理tab名称，替换特殊字符为下划线
                clean_name = re.sub(r'[/()（）]', '_', tab_name.strip())
                
                # 生成文件名
                filename = f"{index}_{clean_name}.md"
                
                # 生成文件内容
                file_content = f"""---
            title: "{tab_name}"
            date: {current_date}
            weight: {index}
        ---

             {tab_content.strip()}
        """
            
            # 写入文件
            with open(filename, 'w', encoding='utf-8') as f:
                    f.write(file_content)
                
            print(f"已创建文件: {filename}")

    def main():
        """主函数：遍历当前目录所有md文件并处理"""
            
            # 获取当前目录
            current_dir = Path('.')
            
            # 查找所有md文件
            md_files = list(current_dir.glob('*.md'))
            
            if not md_files:
                    print("当前目录下未找到md文件")
                    return
                
            print(f"找到 {len(md_files)} 个md文件")
            
            # 处理每个md文件
            for md_file in md_files:
                    print(f"\n处理文件: {md_file}")
                    process_md_file(md_file)

        if __name__ == "__main__":
            main()
            ```

    这个Python脚本的功能：

        1. **遍历当前目录**：查找所有的`.md`文件
            2. **提取tab内容**：使用正则表达式匹配`{{% tab "标签名" %}}内容{{% /tab %}}`格式
            3. **清理文件名**：将`/`、`()`、`（）`等特殊字符替换为下划线`_`
            4. **生成文件头**：包含title、date、weight信息
            5. **批量创建文件**：按顺序生成带序号的md文件

            使用方法：
            1. 将脚本保存为`process_md_files.py`
        2. 放在包含原始md文件的目录中
    3. 运行 `python process_md_files.py`

    生成的md文件格式示例：
    ```markdown
---
    title: "操作系统概述"
date: 2025-10-12T09:23:06+08:00
weight: 1
---

    ## 操作系统概述(into)
    ```

    注意：脚本会使用当前系统时间作为date字段的值。



