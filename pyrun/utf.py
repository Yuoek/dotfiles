import os
import codecs
import chardet

def convert_to_utf8(file_path):
    """
    将单个文件转换为UTF-8编码
    """
    try:
        # 检测文件原始编码
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            if not raw_data:  # 空文件
                return
            
            # 检测编码
            detected = chardet.detect(raw_data)
            original_encoding = detected['encoding']
            confidence = detected['confidence']
            
            # 如果检测置信度较低或无法检测编码，跳过该文件
            if not original_encoding or confidence < 0.6:
                print(f"跳过 {file_path}: 无法确定编码 (置信度: {confidence})")
                return
            
            # 如果已经是UTF-8，跳过
            if original_encoding.lower() in ['utf-8', 'utf-8-sig']:
                print(f"跳过 {file_path}: 已经是UTF-8编码")
                return
            
            # 读取原始内容
            try:
                with codecs.open(file_path, 'r', encoding=original_encoding) as f:
                    content = f.read()
            except (UnicodeDecodeError, LookupError) as e:
                print(f"解码失败 {file_path}: {e}")
                return
            
            # 写入UTF-8编码
            with codecs.open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"转换成功 {file_path}: {original_encoding} -> UTF-8")
            
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

def convert_directory_to_utf8(directory='.'):
    """
    递归转换目录及其子目录中的所有文件为UTF-8编码
    """
    # 支持的文件扩展名（可根据需要修改）
    text_extensions = {
        '.txt', '.py', '.java', '.cpp', '.c', '.h', '.html', '.css', '.js',
        '.xml', '.json', '.csv', '.md', '.rst', '.ini', '.cfg', '.conf',
        '.php', '.rb', '.pl', '.sh', '.bat', '.ps1', '.sql', '.yaml', '.yml'
    }
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 只处理文本文件（可根据需要修改条件）
            if any(file.lower().endswith(ext) for ext in text_extensions):
                convert_to_utf8(file_path)
            else:
                print(f"跳过 {file_path}: 非文本文件")

if __name__ == "__main__":
    # 使用当前目录
    current_directory = '.'
    
    print("开始转换文件编码为UTF-8...")
    print("=" * 50)
    
    convert_directory_to_utf8(current_directory)
    
    print("=" * 50)
    print("转换完成！")
