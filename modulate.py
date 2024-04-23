import os
import librosa
import soundfile as sf

def pitch_shift_audio(input_file, output_file, semitone_shift):
    """
    对音频文件进行变调并保存结果。
    
    参数:
    input_file (str): 输入音频文件的路径。
    output_file (str): 输出音频文件的路径。
    semitone_shift (float): 变调的半音数（正数为提高音调，负数为降低音调）。
    """
    
    # 加载音频文件并使用soundfile作为加载器
    y, sr = librosa.load(input_file, sr=None, res_type='kaiser_fast')

    # 变调
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitone_shift)

    # 确保输出文件夹存在
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 保存变调后的音频文件
    sf.write(output_file, y_shifted, sr)

# 示例调用
if __name__ == "__main__":
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建完整的文件路径
    audio_file = os.path.join(script_dir, 'output_vowel', 'a.ogg')
    output_file = os.path.join(script_dir, 'output_modulate', 'a_lowered.ogg')

    # 设置变调半音数（正数为提高音调，负数为降低音调）
    semitone_shift = -2  # 例如：降低两个半音

    # 调用函数进行变调
    pitch_shift_audio(audio_file, output_file, semitone_shift)
