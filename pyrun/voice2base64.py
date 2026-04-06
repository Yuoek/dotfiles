# 用python voice2base64.py yu.mp3，python 将音频转为base64, 其中音频格式支持ma3,ogg,wav等,并保存为yu_mp3.md,并可以在md文档打开音频 写出voice2base64.py 代码
import base64
import sys
import os

def audio_to_base64(audio_file_path, output_md_path):
    """
    将音频文件转换为base64编码并保存到markdown文件
    
    Args:
        audio_file_path: 音频文件路径
        output_md_path: 输出的markdown文件路径
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(audio_file_path):
            print(f"错误: 文件 '{audio_file_path}' 不存在")
            return False
        
        # 获取文件扩展名
        file_extension = os.path.splitext(audio_file_path)[1].lower()
        
        # 支持的音频格式
        supported_formats = ['.mp3', '.wav', '.ogg', '.m4a', '.flac', '.aac']
        
        if file_extension not in supported_formats:
            print(f"警告: 文件格式 '{file_extension}' 可能不被所有浏览器支持")
            print(f"支持的格式: {', '.join(supported_formats)}")
        
        # 读取音频文件
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = audio_file.read()
        
        # 转换为base64
        base64_encoded = base64.b64encode(audio_data).decode('utf-8')
        
        # 根据文件类型确定MIME类型
        mime_types = {
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
            '.ogg': 'audio/ogg',
            '.m4a': 'audio/mp4',
            '.flac': 'audio/flac',
            '.aac': 'audio/aac'
        }
        
        mime_type = mime_types.get(file_extension, 'audio/mpeg')
        
        # 创建markdown内容
        md_content = f"""# 音频文件 Base64 编码

## 文件信息
- 原始文件: `{os.path.basename(audio_file_path)}`
- 文件大小: {os.path.getsize(audio_file_path)} 字节
- MIME类型: {mime_type}
- 格式: {file_extension[1:] if file_extension else '未知'}

<audio controls>
    <source src="data:{mime_type};base64,{base64_encoded}" type="{mime_type}">
    您的浏览器不支持音频元素。
</audio>
"""
        
        # 保存到markdown文件
        with open(output_md_path, 'w', encoding='utf-8') as md_file:
            md_file.write(md_content)
        
        print(f"成功: 已将 '{audio_file_path}' 转换为base64并保存到 '{output_md_path}'")
        print(f"文件大小: {len(base64_encoded)} 字符")
        
        # 显示预览信息
        preview_length = min(100, len(base64_encoded))
        print(f"\nBase64预览 (前{preview_length}个字符):")
        print(base64_encoded[:preview_length] + "...")
        
        return True
        
    except Exception as e:
        print(f"错误: 处理文件时发生错误 - {str(e)}")
        return False

def main():
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python voice2base64.py <音频文件路径>")
        print("示例: python voice2base64.py yu.mp3")
        print("示例: python voice2base64.py audio.wav")
        print("示例: python voice2base64.py sound.ogg")
        return
    
    audio_file = sys.argv[1]
    
    # 生成输出文件名
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_file = f"{base_name}_base64.md"
    
    # 转换并保存
    audio_to_base64(audio_file, output_file)

if __name__ == "__main__":
    main()
