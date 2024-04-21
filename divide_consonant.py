from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os

# 指定输入和输出文件夹
input_folder = "consonant"
output_folder = "output_consonant"

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    audio = AudioSegment.from_ogg(file_path)
   
    # 使用detect_nonsilent找到非静音部分
    nonsilent_intervals = detect_nonsilent(audio, silence_thresh=-40, min_silence_len=50)

    # 获取第一个非静音部分的开始位置并截取音频
    if nonsilent_intervals:
        start_pos = nonsilent_intervals[0][0]
        # 截取去掉静音部分后的前20毫秒音频
        chunk = audio[start_pos:start_pos + 50]

        # 保存截取出的音频
        output_file = os.path.join(output_folder, filename)
        chunk.export(output_file, format="ogg")

        print(f"Successfully extracted the first 20 milliseconds of audio after removing the silent part from {filename}.")
    else:
        print(f"No non-silent parts were found in {filename}.")
