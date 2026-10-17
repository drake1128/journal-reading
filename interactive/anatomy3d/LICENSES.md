# 授權說明

## 3D 模型（models/*.glb）

本站的模型是改作物，依 **CC BY-SA 4.0** 釋出：
<https://creativecommons.org/licenses/by-sa/4.0/>

來源：

- **Z-Anatomy**（Gauthier Kervyn、Lluís Vinent Juanico 等），CC BY-SA 4.0。
  <https://github.com/LluisV/Z-Anatomy>
  使用的檔案：CardioVascular41、SkeletalSystem100、MuscularSystem100、VisceralSystem100。
- **BodyParts3D** © The Database Center for Life Science（DBCLS），CC BY-SA 2.1 Japan。
  <https://lifesciencedb.jp/bp3d/>
  使用的元件：FJ2420（二尖瓣前葉）、FJ2421（三尖瓣前葉）、FJ2418（左心室前外側乳頭肌）、
  FJ2633–FJ2648（對角支）、FJ2692–FJ2700（後降支）。

改作內容：

- 擷取心臟、下肢、頭頸部相關構造，部分構造合併成單一物件。
- 以 meshoptimizer 減面，並重新置中、量化與壓縮。
- BodyParts3D 的元件以相似轉換對齊到 Z-Anatomy 心臟（以 10 個瓣膜與乳頭肌中心點擬合，均方根誤差約 2.8 mm）。

## 程式

- Three.js 與其範例模組（OrbitControls、GLTFLoader、CSS2DRenderer、meshopt decoder），MIT License，見 `assets/vendor/three-LICENSE.txt`。
- 檢視器程式（assets/viewer.js、viewer.css）與建置腳本為謝慕揚撰寫。

## 教學說明文字

各構造的臨床重點由謝慕揚醫師撰寫，供教學使用。
