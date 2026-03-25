@echo off
echo Downloading anatomical images from Wikimedia Commons...
echo.

REM Create images directory if not exists
if not exist "images" mkdir images

echo [1/5] Downloading Coronary Arteries...
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0" ^
  -o "coronary_arteries.png" ^
  "https://upload.wikimedia.org/wikipedia/commons/5/57/Blausen_0256_CoronaryArteries.png"

echo [2/5] Downloading Aorta Branches (SVG to PNG)...
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0" ^
  -o "aorta_branches.svg" ^
  "https://upload.wikimedia.org/wikipedia/commons/2/22/Arterial_System_en.svg"

echo [3/5] Downloading Lower Limb Arteries...
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0" ^
  -o "lower_limb_arteries.png" ^
  "https://upload.wikimedia.org/wikipedia/commons/9/94/Blausen_0607_LegArteries.png"

echo [4/5] Downloading Carotid Arteries...
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0" ^
  -o "carotid_arteries.png" ^
  "https://upload.wikimedia.org/wikipedia/commons/a/a5/Blausen_0170_CarotidArteries.png"

echo [5/5] Downloading Circle of Willis (SVG to PNG)...
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0" ^
  -o "circle_of_willis.svg" ^
  "https://upload.wikimedia.org/wikipedia/commons/2/2e/Circle_of_Willis_en.svg"

echo.
echo Download complete! Files saved in current directory.
echo.
echo Image Licenses:
echo - coronary_arteries.png: CC BY 3.0 - Blausen Medical
echo - aorta_branches.svg: CC BY-SA 3.0 - Wikimedia Commons
echo - lower_limb_arteries.png: CC BY 3.0 - Blausen Medical
echo - carotid_arteries.png: CC BY 3.0 - Blausen Medical
echo - circle_of_willis.svg: CC BY-SA 3.0 - Wikimedia Commons
echo.
pause
