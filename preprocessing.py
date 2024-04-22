import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent


def m4a_to_ogg(source_folder, output_folder):
    """
    将源文件夹中的音频文件转换为OGG格式并保存到目标文件夹。
    
    参数:
    source_folder (str): 源文件夹路径。
    output_folder (str): 目标文件夹路径。
    """
    
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


def divide_consonant(input_folder, output_folder, silence_thresh=-40, min_silence_len=50, chunk_len=50):
    """
    从输入文件夹中的音频文件中提取非静音部分，并保存为新的OGG文件。
    
    参数:
    input_folder (str): 输入文件夹路径。
    output_folder (str): 输出文件夹路径。
    silence_thresh (float): 静音阈值（默认为-40dB）。
    min_silence_len (int): 最小静音长度（默认为50毫秒）。
    chunk_len (int): 要提取的音频片段长度（默认为50毫秒）。
    """
    
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        audio = AudioSegment.from_ogg(file_path)
       
        # 使用detect_nonsilent找到非静音部分
        nonsilent_intervals = detect_nonsilent(audio, silence_thresh=silence_thresh, min_silence_len=min_silence_len)

        # 获取第一个非静音部分的开始位置并截取音频
        if nonsilent_intervals:
            start_pos = nonsilent_intervals[0][0]
            # 截取去掉静音部分后的音频片段
            chunk = audio[start_pos:start_pos + chunk_len]

            # 保存截取出的音频
            output_file = os.path.join(output_folder, filename)
            chunk.export(output_file, format="ogg")

            print(f"Successfully extracted the audio segment after removing the silent part from {filename}.")
        else:
            print(f"No non-silent parts were found in {filename}.")


def vowel_silence_removal(source_folder, output_folder, silence_thresh=-40, min_silence_len=50):
    """
    从给定的音频文件夹中提取非静音部分，并保存为新的OGG文件。
    
    参数:
    source_folder (str): 输入音频文件夹路径。
    output_folder (str): 输出音频文件夹路径。
    silence_thresh (float, 可选): 静音阈值，默认为-40dB。
    min_silence_len (int, 可选): 最小静音长度，默认为50毫秒。
    """
    
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
            nonsilent_intervals = detect_nonsilent(audio, silence_thresh=silence_thresh, min_silence_len=min_silence_len)
            
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


# 示例调用
if __name__ == "__main__":
    # 1. m4a_to_ogg 示例调用
    source_folder = 'raw'
    output_folder = 'converted_to_ogg'
    
    m4a_to_ogg(source_folder, output_folder)
    # 2. divide_consonant 示例调用
    input_folder = "consonant"
    output_folder = "output_consonant"
    
    divide_consonant(input_folder, output_folder)

    # 3. vowel_silence_removal 示例调用
    source_folder = 'vowel'
    output_folder = 'output_vowel'
    
    vowel_silence_removal(source_folder, output_folder)


