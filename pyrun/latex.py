
import os
import re

def convert_latex_delimiters(text):
    """
    将文本中的 \( \) 转换为 $ $，将 \[ \] 转换为 $$ $$
    """
    # 将 \[ \] 转换为 $$ $$
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text, flags=re.DOTALL)
    
    # 将 \( \) 转换为 $ $
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text, flags=re.DOTALL)
    
    return text

def process_files():
    """
    处理当前目录下的所有文件
    """
    current_dir = os.getcwd()
    
    for filename in os.listdir(current_dir):
        # 跳过目录和Python脚本本身
        if os.path.isdir(filename) or filename.endswith('.py'):
            continue
            
        try:
            # 读取文件内容
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 转换LaTeX分隔符
            new_content = convert_latex_delimiters(content)
            
            # 如果内容有变化，则写入文件
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"已转换文件: {filename}")
            else:
                print(f"无需转换: {filename}")
                
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")

if __name__ == "__main__":
    print("开始转换LaTeX分隔符...")
    process_files()
    print("转换完成！")
