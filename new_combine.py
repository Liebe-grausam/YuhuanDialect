from pydub import AudioSegment
import os

def generate_silent_audio(duration=30, output_path="./output_consonant/#.ogg"):
    """
    生成指定时长的静音音频文件。
    
    参数:
    duration (int, 可选): 静音时长，单位为毫秒，默认为30ms。
    output_path (str, 可选): 输出音频文件的路径，默认为"./output_consonant/#.ogg"。
    """
    
    # 生成指定时长的静音音频
    silent_audio = AudioSegment.silent(duration=duration)
    
    # 保存音频到指定路径
    silent_audio.export(output_path, format="ogg")
    
    print(f"Silent audio with duration {duration}ms saved successfully!")



def combine_audio_files(files_with_pitch, output_path, output_dir="./output_combine"):
    """
    合并给定的音频文件列表，并保存为新的OGG文件。
    
    参数:
    files_with_pitch (list): 包含音频文件名和升降半音数的列表。
    output_path (str): 输出音频文件的路径。
    output_dir (str, 可选): 输出目录的路径，默认为"./output_combine"。
    """
    
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    combined_audio = None

    for file, pitch in files_with_pitch:
        # 加载音频文件
        audio = AudioSegment.from_file(file, format="ogg")

        # 根据升降半音数调整音频音调
        audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * (2 ** (pitch / 12.0)))
        }).set_frame_rate(audio.frame_rate)

        if combined_audio is None:
            combined_audio = audio
        else:
            # 添加交叉淡入淡出和静音
            crossfade_duration = min(len(combined_audio), len(audio)) // 6
            combined_audio = combined_audio.append(
                AudioSegment.silent(duration=20), 20
            ).append(audio.fade_in(crossfade_duration), 20)

    # 保存合成后的音频到新文件
    combined_audio.export(output_path, format="ogg")

    print("Audio files combined with crossfade successfully!")

# 示例调用
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    
    silent_path = os.path.join(script_dir, "./output_consonant/#.ogg")
    
    generate_silent_audio(output_path=silent_path)
    files_with_pitch = [
        (os.path.join(script_dir, "./output_consonant/f.ogg"), 0),
        (os.path.join(script_dir, "./output_vowel/a.ogg"), -2),
        (os.path.join(script_dir, "./output_consonant/#.ogg"), 0),
        (os.path.join(script_dir, "./output_consonant/t.ogg"), 0),
        (os.path.join(script_dir, "./output_vowel/ei.ogg"), 0)
    ]

    output_dir = os.path.join(script_dir, "./output_combine")
    output_path = os.path.join(output_dir, "tei.ogg")
    
    combine_audio_files(files_with_pitch, output_path, output_dir)
