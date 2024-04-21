import os
from pydub import AudioSegment

# 定义源文件夹和目标文件夹
source_folder = 'raw'
output_folder = 'converted_to_ogg'

# 创建输出文件夹如果它不存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历源文件夹中的所有文件
for file_name in os.listdir(source_folder):
    # 构建完整的文件路径
    file_path = os.path.join(source_folder, file_name)
    
    # 仅处理音频文件，这里我们假设文件有扩展名
    if file_path.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg')):
        # 确定输出文件名和路径
        output_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.ogg')

        try:
            # 加载音频文件（pydub自动猜测格式）
            audio = AudioSegment.from_file(file_path)

            # 导出为OGG格式
            audio.export(output_file_path, format='ogg')
            print(f"Converted {file_name} to {output_file_path}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

print("Conversion complete.")
