import json
import re
import sys

def md_to_json(md_file, json_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割内容为不同的部分
    sections = re.split(r'\n##\s+', content)
    
    result = {}
    
    for section in sections:
        if not section.strip():
            continue
            
        # 提取主标题（第二级标题）
        lines = section.strip().split('\n')
        main_title = lines[0].strip()
        
        # 跳过不符合要求的标题
        if not main_title:
            continue
            
        # 初始化变量
        description = ""
        body_lines = []
        in_code_block = False
        code_block_language = ""
        
        # 处理剩余行
        for i in range(1, len(lines)):
            line = lines[i]
            
            # 检查是否是第三级标题
            if line.startswith('### '):
                # 提取描述，将空格替换为\n
                description = line[4:].strip().replace(' ', '\n')
            
            # 检查是否是代码块开始
            elif line.startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_block_language = line[3:].strip()
                    body_lines.append(f"```{code_block_language}")
                else:
                    in_code_block = False
                    body_lines.append("```")
            
            # 如果是代码块内的内容
            elif in_code_block:
                body_lines.append(line)
            
            # 其他内容（非标题，非代码块标记）
            elif line.strip() and not line.startswith('#') and not line.startswith('```'):
                body_lines.append(line)
        
        # 如果有描述和内容，则添加到结果中
        if description and body_lines:
            result[main_title] = {
                "prefix": main_title,
                "description": description,
                "body": body_lines
            }
    
    # 写入JSON文件
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python md2json.py input.md output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        md_to_json(input_file, output_file)
        print(f"转换完成: {input_file} -> {output_file}")
    except Exception as e:
        print(f"转换失败: {e}")
