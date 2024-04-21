import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# 定义源文件夹和目标文件夹
source_folder = 'vowel'
output_folder = 'output_vowel'

# 创建输出文件夹如果它不存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历源文件夹中的所有文件
for file_name in os.listdir(source_folder):
    # 检查文件是否是.ogg格式
    if file_name.lower().endswith('.ogg'):
        # 构建完整的文件路径
        file_path = os.path.join(source_folder, file_name)
        
        # 加载音频文件
        audio = AudioSegment.from_ogg(file_path)
        
        # 使用detect_nonsilent找到非静音部分
        nonsilent_intervals = detect_nonsilent(audio, silence_thresh=-40, min_silence_len=50)
        
        # 如果找到非静音部分，截取去掉静音部分后的音频
        if nonsilent_intervals:
            start_pos = nonsilent_intervals[0][0]
            chunk = audio[start_pos:]
            
            # 确定输出文件路径
            output_file_path = os.path.join(output_folder, file_name)
            
            # 保存截取后的音频到输出文件夹
            chunk.export(output_file_path, format='ogg')
            print(f"Processed {file_name} and saved to {output_file_path}")
        else:
            print(f"No non-silent parts found in {file_name}")

print("Processing complete.")
