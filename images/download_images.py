#!/usr/bin/env python3
"""
解剖圖片下載腳本 / Anatomical Images Download Script

本腳本用於下載 Creative Commons 授權的解剖圖片
這些圖片用於 HoloLens VR 心血管解剖教學投影片

使用方式 / Usage:
    python download_images.py

圖片來源 / Image Sources:
    - Wikimedia Commons (CC BY-SA 3.0, CC BY 4.0)
    - Blausen Medical (CC BY 3.0)
    - Gray's Anatomy (Public Domain)

作者 / Author: 新竹台大分院心血管中心
"""

import urllib.request
import os
import time
import sys

def download_image(url, filename, description):
    """Download an image with retry logic."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://commons.wikimedia.org/',
    }

    print(f"\n下載中 / Downloading: {description}")
    print(f"URL: {url}")

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                # Check if it's actually an image (not an error page)
                if len(data) < 1000 or data[:5] == b'<!DOC' or data[:5] == b'<html':
                    print(f"  警告: 可能下載到錯誤頁面，請手動下載")
                    return False

                with open(filename, 'wb') as f:
                    f.write(data)

                print(f"  成功! 檔案大小: {len(data):,} bytes")
                return True

        except Exception as e:
            print(f"  嘗試 {attempt + 1}/3 失敗: {e}")
            time.sleep(2)

    return False

def main():
    print("=" * 60)
    print("HoloLens VR 心血管解剖教學 - 圖片下載工具")
    print("Cardiovascular Anatomy Teaching - Image Downloader")
    print("=" * 60)

    # Define images to download with their sources and licenses
    images = [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Blausen_0256_CoronaryArteries.png/640px-Blausen_0256_CoronaryArteries.png',
            'filename': 'coronary_arteries.png',
            'description': '冠狀動脈解剖 / Coronary Arteries',
            'license': 'CC BY 3.0 - Blausen Medical',
            'manual_url': 'https://commons.wikimedia.org/wiki/File:Blausen_0256_CoronaryArteries.png'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Arterial_System_en.svg/400px-Arterial_System_en.svg.png',
            'filename': 'aorta_branches.png',
            'description': '主動脈與分支 / Aorta and Branches',
            'license': 'CC BY-SA 3.0 - Wikimedia Commons',
            'manual_url': 'https://commons.wikimedia.org/wiki/File:Arterial_System_en.svg'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Blausen_0607_LegArteries.png/400px-Blausen_0607_LegArteries.png',
            'filename': 'lower_limb_arteries.png',
            'description': '下肢動脈 / Lower Limb Arteries',
            'license': 'CC BY 3.0 - Blausen Medical',
            'manual_url': 'https://commons.wikimedia.org/wiki/File:Blausen_0607_LegArteries.png'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Blausen_0170_CarotidArteries.png/500px-Blausen_0170_CarotidArteries.png',
            'filename': 'carotid_arteries.png',
            'description': '頸動脈 / Carotid Arteries',
            'license': 'CC BY 3.0 - Blausen Medical',
            'manual_url': 'https://commons.wikimedia.org/wiki/File:Blausen_0170_CarotidArteries.png'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Circle_of_Willis_en.svg/500px-Circle_of_Willis_en.svg.png',
            'filename': 'circle_of_willis.png',
            'description': '威利氏環 / Circle of Willis',
            'license': 'CC BY-SA 3.0 - Wikimedia Commons',
            'manual_url': 'https://commons.wikimedia.org/wiki/File:Circle_of_Willis_en.svg'
        },
    ]

    success_count = 0
    failed_images = []

    for img in images:
        if download_image(img['url'], img['filename'], img['description']):
            success_count += 1
        else:
            failed_images.append(img)
        time.sleep(1)  # Be polite to the server

    print("\n" + "=" * 60)
    print(f"下載完成! 成功: {success_count}/{len(images)}")

    if failed_images:
        print("\n以下圖片需要手動下載 / Please download manually:")
        print("-" * 60)
        for img in failed_images:
            print(f"\n{img['description']}")
            print(f"  手動下載連結: {img['manual_url']}")
            print(f"  儲存為: {img['filename']}")
            print(f"  授權: {img['license']}")

    print("\n" + "=" * 60)
    print("圖片授權聲明 / Image Licenses:")
    print("-" * 60)
    for img in images:
        print(f"  {img['filename']}: {img['license']}")

    print("\n完成! 圖片已儲存在當前目錄。")
    print("Done! Images saved in current directory.")

if __name__ == '__main__':
    main()
