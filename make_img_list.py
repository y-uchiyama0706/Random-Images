import os
import json

img_dir = 'img'
img_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

with open('imgList.json', 'w', encoding='utf-8') as f:
    json.dump(img_files, f, indent=2)

print("imgList.json を作成しました！")
