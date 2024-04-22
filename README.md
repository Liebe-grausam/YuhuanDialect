# YuhuanDialect
Dictionary of Yuhuan Dialect for personal use.

---

## preprocessing.py
### m4a_to_ogg
预处理脚本，将raw文件夹中的所有m4a格式音频转化为可以在vscode中预览的ogg格式，保存至convert_to_ogg文件夹中。
### divide_consonant
遍历consonant文件夹中的所有文件，获取非静音部分的前50毫秒，保存至output_consonant文件夹中。
### vowel_silence_removal
遍历vowel文件夹中的所有文件，截取去掉静音部分的音频，保存至output_vowel文件夹中。

---

## combine.py
使用交叉淡入淡出平滑连接元音和辅音。

---

## modulate.py
暂未实现连续变调，但已可以实现整体变调。
