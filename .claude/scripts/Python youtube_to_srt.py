#!/usr/bin/env python3
"""
YouTube 影片轉 SRT 字幕工具
1. 貼上 YouTube 網址
2. 自動下載 MP3 音訊
3. 選擇輸出語言（英文或繁體中文）
4. 使用 Whisper 轉錄成 SRT 字幕檔
"""

import whisper
import subprocess
import sys
from pathlib import Path


def download_audio(url: str, output_dir: Path) -> Path | None:
    """使用 yt-dlp 下載 YouTube 影片的音訊並轉成 MP3"""
    print(f"\n正在下載音訊...")
    
    # 設定輸出模板（下載到程式所在目錄）
    output_template = str(output_dir / "%(title)s.%(ext)s")
    
    cmd = [
        "yt-dlp",
        "-x",                      # 只擷取音訊
        "--audio-format", "mp3",   # 轉成 MP3 格式
        "-o", output_template,     # 輸出路徑
        "--print", "after_move:filepath",  # 印出最終檔案路徑
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # 取得下載後的檔案路徑
        filepath = result.stdout.strip().split('\n')[-1]
        mp3_path = Path(filepath)
        
        if mp3_path.exists():
            print(f"✓ 下載完成: {mp3_path.name}")
            return mp3_path
        else:
            print(f"✗ 找不到下載的檔案")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"✗ 下載失敗: {e.stderr}")
        return None
    except FileNotFoundError:
        print("✗ 找不到 yt-dlp，請先安裝: pip install yt-dlp")
        return None


def format_time(seconds: float) -> str:
    """將秒數轉換成 SRT 時間格式 (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def save_as_srt(segments: list, filename: Path) -> None:
    """將轉錄結果儲存為 SRT 字幕檔"""
    with open(filename, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, 1):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{segment['text'].strip()}\n\n")


def transcribe_audio(mp3_path: Path, language: str, model) -> Path:
    """使用 Whisper 轉錄音訊並儲存為 SRT"""
    print(f"\n開始轉錄: {mp3_path.name}")
    print(f"使用語言: {'英文 (English)' if language == 'en' else '繁體中文 (Traditional Chinese)'}")
    
    result = model.transcribe(str(mp3_path), language=language)
    
    # 輸出帶時間軸的文字（預覽前5段）
    print("\n=== 轉錄結果預覽（前5段）===")
    for segment in result["segments"][:5]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        print(f"[{start:.2f}s - {end:.2f}s] {text}")
    
    if len(result["segments"]) > 5:
        print(f"... 共 {len(result['segments'])} 段")
    
    # 儲存成 SRT
    output_file = mp3_path.with_suffix(".srt")
    save_as_srt(result["segments"], output_file)
    
    print(f"\n✓ 字幕已儲存到: {output_file.name}")
    return output_file


def get_language_choice() -> str:
    """讓使用者選擇輸出語言"""
    print("\n請選擇轉錄語言:")
    print("1. English (英文)")
    print("2. 繁體中文 (Traditional Chinese)")
    
    while True:
        choice = input("\n請輸入選項 (1 或 2): ").strip()
        if choice == "1":
            return "en"
        elif choice == "2":
            return "zh"
        else:
            print("無效選項，請重新輸入")


def main():
    # 取得程式所在的目錄
    script_dir = Path(__file__).parent
    
    print("=" * 50)
    print("  YouTube 影片轉 SRT 字幕工具")
    print("=" * 50)
    
    # 輸入 YouTube 網址
    url = input("\n請貼上 YouTube 網址: ").strip()
    
    if not url:
        print("✗ 未輸入網址")
        sys.exit(1)
    
    # 選擇語言
    language = get_language_choice()
    
    # 下載音訊
    mp3_path = download_audio(url, script_dir)
    
    if mp3_path is None:
        print("\n✗ 無法下載音訊，程式結束")
        sys.exit(1)
    
    # 載入 Whisper 模型
    print("\n載入 Whisper 模型...")
    model = whisper.load_model("base")
    print("✓ 模型載入完成")
    
    # 轉錄音訊
    srt_path = transcribe_audio(mp3_path, language, model)
    
    print("\n" + "=" * 50)
    print("  全部完成！")
    print("=" * 50)
    print(f"MP3 檔案: {mp3_path}")
    print(f"SRT 字幕: {srt_path}")
    
    # 詢問是否刪除 MP3
    delete_mp3 = input("\n是否刪除 MP3 檔案？(y/n): ").strip().lower()
    if delete_mp3 == 'y':
        mp3_path.unlink()
        print("✓ MP3 檔案已刪除")


if __name__ == "__main__":
    main()
