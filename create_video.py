#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw
import sys
import struct
import zlib

# الحصول على المجلد الحالي
current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'tmp_frames')
os.makedirs(output_dir, exist_ok=True)

# إعدادات الفيديو
width, height = 1280, 720
fps = 30
duration = 8
frame_count = fps * duration

# الألوان (RGB)
bg_color = (25, 25, 112)  # Midnight Blue
gold = (255, 215, 0)  # Gold
white = (255, 255, 255)

texts_timeline = [
    (0, 2, "مرحباً بكم في", "Welcome to", "System Pro"),
    (2, 4, "مركز الأكواد الرسمي", "Official Codes Center", ""),
    (4, 6, "أكواد Suno و Stunning.so", "Suno & Stunning.so Codes", ""),
    (6, 8, "متوفر في جميع الدول العربية", "Available in all Arab Countries", "")
]

print("📝 جاري إنشاء الإطارات...")
for frame_num in range(frame_count):
    # إنشاء صورة جديدة
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    current_time = frame_num / fps
    
    # إضافة النصوص حسب الوقت
    for start, end, ar_text, en_text, extra in texts_timeline:
        if start <= current_time <= end:
            # النص الرئيسي
            if ar_text:
                draw.text((width // 2 - 200, height // 2 - 100), ar_text, 
                         fill=gold, anchor="lm")
            if en_text:
                draw.text((width // 2 - 220, height // 2), en_text,
                         fill=white, anchor="lm")
            if extra:
                draw.text((width // 2 - 150, height // 2 + 80), extra,
                         fill=gold, anchor="lm")
    
    # رسم إطار متحرك
    import math
    rect_offset = int(20 * math.sin(frame_num * 0.1))
    draw.rectangle([150 + rect_offset, 150, width - 150 - rect_offset, height - 150],
                  outline=gold, width=3)
    
    # رسم نقاط متحركة
    for i in range(3):
        angle = math.radians((frame_num + i * 120) * 0.05)
        x = int(width // 2 + 300 * math.cos(angle))
        y = int(height // 2 + 300 * math.sin(angle))
        draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=gold)
    
    # حفظ الصورة
    img.save(f'{output_dir}/frame_{frame_num:05d}.png')
    
    if frame_num % 30 == 0:
        print(f"✓ تم إنشاء {frame_num}/{frame_count} إطار")

print("✅ تم إنشاء جميع الإطارات")
print(f"📁 الإطارات محفوظة في: {output_dir}")

# إنشاء ملف فيديو بسيط باستخدام imageio
try:
    import imageio
    print("📹 جاري إنشاء الفيديو باستخدام imageio...")
    
    frames = []
    for i in range(frame_count):
        img_path = f'{output_dir}/frame_{i:05d}.png'
        img = Image.open(img_path)
        frames.append(img)
    
    output_file = os.path.join(current_dir, 'promo_with_voice.mp4')
    imageio.mimwrite(output_file, frames, fps=fps, codec='libx264')
    print(f"✅ تم إنشاء الفيديو: {output_file}")
    
except ImportError:
    print("⚠️ تثبيت imageio...")
    os.system(f'{sys.executable} -m pip install imageio imageio-ffmpeg -q')
    
    import imageio
    frames = []
    for i in range(frame_count):
        img_path = f'{output_dir}/frame_{i:05d}.png'
        img = Image.open(img_path)
        frames.append(img)
    
    output_file = os.path.join(current_dir, 'promo_with_voice.mp4')
    imageio.mimwrite(output_file, frames, fps=fps)
    print(f"✅ تم إنشاء الفيديو: {output_file}")

# تنظيف الملفات المؤقتة
import shutil
shutil.rmtree(output_dir, ignore_errors=True)
print("✓ تم تنظيف الملفات المؤقتة")

# إعدادات الفيديو
width, height = 1280, 720
fps = 30
duration = 8
frame_count = fps * duration

# الألوان (RGB)
bg_color = (25, 25, 112)  # Midnight Blue
gold = (255, 215, 0)  # Gold
white = (255, 255, 255)

# خط النص
font_size_title = 80
font_size_text = 50

texts_timeline = [
    (0, 2, "مرحباً بكم في", "Welcome to", "System Pro"),
    (2, 4, "مركز الأكواد الرسمي", "Official Codes Center", ""),
    (4, 6, "أكواد Suno و Stunning.so", "Suno & Stunning.so Codes", ""),
    (6, 8, "متوفر في جميع الدول العربية", "Available in all Arab Countries", "")
]

print("📝 جاري إنشاء الإطارات...")
for frame_num in range(frame_count):
    # إنشاء صورة جديدة
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    current_time = frame_num / fps
    
    # إضافة النصوص حسب الوقت
    for start, end, ar_text, en_text, extra in texts_timeline:
        if start <= current_time <= end:
            # حساب تأثير الشفافية
            progress = (current_time - start) / (end - start)
            
            # النص الرئيسي
            if ar_text:
                draw.text((width // 2 - 200, height // 2 - 100), ar_text, 
                         fill=gold, anchor="lm")
            if en_text:
                draw.text((width // 2 - 220, height // 2), en_text,
                         fill=white, anchor="lm")
            if extra:
                draw.text((width // 2 - 150, height // 2 + 80), extra,
                         fill=gold, anchor="lm")
    
    # رسم إطار متحرك
    import math
    rect_offset = int(20 * math.sin(frame_num * 0.1))
    draw.rectangle([150 + rect_offset, 150, width - 150 - rect_offset, height - 150],
                  outline=gold, width=3)
    
    # رسم نقاط متحركة
    for i in range(3):
        angle = math.radians((frame_num + i * 120) * 0.05)
        x = int(width // 2 + 300 * math.cos(angle))
        y = int(height // 2 + 300 * math.sin(angle))
        draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=gold)
    
    # حفظ الصورة
    img.save(f'{output_dir}/frame_{frame_num:05d}.png')
    
    if frame_num % 30 == 0:
        print(f"✓ تم إنشاء {frame_num}/{frame_count} إطار")

print("✅ تم إنشاء جميع الإطارات")

# إنشاء الفيديو من الإطارات باستخدام ffmpeg
output_file = 'promo_with_voice.mp4'
cmd = f'ffmpeg -framerate {fps} -i {output_dir}/frame_%05d.png -c:v libx264 -pix_fmt yuv420p -y {output_file} 2>/dev/null'
os.system(cmd)

print(f"✅ تم إنشاء الفيديو: {output_file}")

# تنظيف الملفات المؤقتة
import shutil
shutil.rmtree(output_dir, ignore_errors=True)
print("✓ تم تنظيف الملفات المؤقتة")
