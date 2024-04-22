import os
import librosa
import soundfile as sf

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建完整的文件路径
audio_file = os.path.join(script_dir, 'output_vowel', 'au.ogg')

# 加载音频文件并使用soundfile作为加载器
y, sr = librosa.load(audio_file, sr=None, res_type='kaiser_fast')

# 设置变调半音数（正数为提高音调，负数为降低音调）
semitone_shift = -2  # 例如：降低两个半音

# 变调
y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitone_shift)

# 确保输出文件夹存在
output_dir = os.path.join(script_dir, 'output_modulate')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 保存变调后的音频文件
output_file = os.path.join(output_dir, 'au_lowered.ogg')
sf.write(output_file, y_shifted, sr)
