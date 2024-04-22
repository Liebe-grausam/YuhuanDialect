from pydub import AudioSegment
import os

def combine_audio_files(consonant_path, vowel_path, output_path, output_dir="./output_combine"):
    """
    合并给定的辅音和元音音频文件，并保存为新的OGG文件。
    
    参数:
    consonant_path (str): 辅音音频文件的路径。
    vowel_path (str): 元音音频文件的路径。
    output_path (str): 输出音频文件的路径。
    output_dir (str, 可选): 输出目录的路径，默认为"./output_combine"。
    """
    
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 加载第一个音频文件（辅音）
    audio1 = AudioSegment.from_file(consonant_path, format="ogg")
    # 增加十分贝音量
    audio1 = audio1 + 15
    # 添加静音并进行淡入处理
    silence = AudioSegment.silent(duration=20)  # 100毫秒的静音
    audio1_with_silence = silence + audio1.fade_in(3)  # 在静音后添加第一个音频片段，并进行100毫秒的淡入

    # 加载第二个音频文件（元音）
    audio2 = AudioSegment.from_file(vowel_path, format="ogg")

    # 计算交叉淡入淡出的时长（取两个音频长度的四分之一作为交叉淡入淡出的时长）
    crossfade_duration = min(len(audio1), len(audio2)) // 6

    # 使用交叉淡入淡出平滑地合成两个音频片段
    combined_audio = audio1[-crossfade_duration:].append(audio2.fade_in(crossfade_duration), crossfade_duration)

    # 保存合成后的音频到新文件
    combined_audio.export(output_path, format="ogg")

    print("Audio files combined with crossfade successfully!")

# 示例调用
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    consonant_path = os.path.join(script_dir, "./output_consonant/t.ogg")
    vowel_path = os.path.join(script_dir, "./output_vowel/ei.ogg")
    output_dir = os.path.join(script_dir, "./output_combine")
    output_path = os.path.join(output_dir, "tei.ogg")
    
    combine_audio_files(consonant_path, vowel_path, output_path, output_dir)
