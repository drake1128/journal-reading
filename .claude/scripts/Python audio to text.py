# 下載最佳音質的音訊（自動轉成 mp3）
# yt-dlp -x --audio-format mp3 "影片網址"

import whisper
import os
from pathlib import Path

# 取得程式所在的目錄
script_dir = Path(__file__).parent

# 尋找所有 MP3 檔案
mp3_files = list(script_dir.glob("*.mp3"))

if not mp3_files:
    print("工作目錄中沒有找到 MP3 檔案")
    exit()

print(f"找到 {len(mp3_files)} 個 MP3 檔案")
for i, file in enumerate(mp3_files, 1):
    print(f"{i}. {file.name}")

# 載入模型（只需載入一次）
print("\n載入 Whisper 模型...")
model = whisper.load_model("base")

# 處理每個檔案
for mp3_file in mp3_files:
    print(f"\n開始轉錄: {mp3_file.name}")
    
    result = model.transcribe(str(mp3_file), language="en")
    
    # 輸出帶時間軸的文字
    print("\n=== 轉錄結果 ===")
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        print(f"[{start:.2f}s - {end:.2f}s] {text}")
    
    # 儲存成 SRT
    def save_as_srt(segments, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments, 1):
                start = format_time(segment["start"])
                end = format_time(segment["end"])
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{segment['text'].strip()}\n\n")
    
    def format_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    
    output_file = mp3_file.with_suffix(".srt")
    save_as_srt(result["segments"], output_file)
    
    print(f"字幕已儲存到: {output_file.name}")

print("\n全部完成！")