from PIL import Image
import os
import shutil
from tqdm import tqdm

def extract_frames_and_get_dimensions(gif_path):
    frames = []
    with Image.open(gif_path) as img:
        for frame in range(img.n_frames):
            img.seek(frame)
            frame_img = img.copy().convert("RGBA")
            frames.append(frame_img)
    return frames

def save_frames(frames, temp_dir):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    for i, frame in enumerate(frames):
        frame_path = os.path.join(temp_dir, f"frame_{i}.png")
        frame.save(frame_path)

def main():
    media_path = 'media/gifs'
    frames_path = 'media/frames'
    if os.path.exists(frames_path):
        shutil.rmtree(frames_path)
    os.makedirs(frames_path)
    gif_names = [os.path.splitext(file)[0] for file in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, file))]
    for gif_name in tqdm(gif_names):
        gif_path = os.path.join(media_path, f'{gif_name}.gif')
        frames = extract_frames_and_get_dimensions(gif_path)
        save_path = os.path.join(frames_path, gif_name)
        save_frames(frames, save_path)

if __name__ == '__main__':
    main()