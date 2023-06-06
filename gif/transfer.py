from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx
from PIL import Image
import os

# 定義輸入MP4文件路徑、輸出GIF文件路徑和壓縮比率
input_file = '4.mp4'
output_file = '4.gif'
compression_ratio = 20  # 壓縮比率，越小則壓縮後的GIF文件越小
speed_factor = 3  # 加速倍率

# 加載視頻
video = VideoFileClip(input_file)

# 調整大小和加速影片
resized_video = video.resize((640, 360))
accelerated_video = vfx.speedx(resized_video, speed_factor)

# 創建一個臨時文件夾來保存影格圖像
temp_folder = 'temp_frames'
os.makedirs(temp_folder, exist_ok=True)

# 提取每一幀圖像並保存為臨時文件
frame_count = int(accelerated_video.duration * accelerated_video.fps)
print(frame_count)
for i in range(30, frame_count-90):
    t = i / accelerated_video.fps
    frame = accelerated_video.get_frame(t)
    image = Image.fromarray(frame)
    image.save(os.path.join(temp_folder, f'frame_{i:05d}.png'))
    print(i)

# 使用PIL將圖像文件轉換為GIF
frames = sorted(os.listdir(temp_folder))
images = [Image.open(os.path.join(temp_folder, frame)) for frame in frames]
images[0].save(output_file, save_all=True, append_images=images[1:], optimize=True, duration=1000/accelerated_video.fps, loop=0, disposal=2)

# 刪除臨時文件夾
for frame in frames:
    os.remove(os.path.join(temp_folder, frame))
os.rmdir(temp_folder)
