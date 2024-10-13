from flask import Flask, request, jsonify
import pygame
from PIL import Image, ImageFilter
import threading
import os
import requests
import io
import json
import openai
import requests
import time
import shutil
API_KEY = "<API_KEY>"
openai.api_key = API_KEY

background_url = "https://karenapp.io/books/zoom/images/gettingstartedwithzoom/virtualbackground/vbackground.jpg"

state = None

def main():
    global state
    media_path = 'media/gifs'
    frames_path = 'media/frames'
    gif_names = [os.path.splitext(file)[0] for file in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, file))]
    gif_frames = {}
    # for gif_name in gif_names:
    #     gif_frames[gif_name] = []
    #     frames_dir = os.path.join(frames_path, gif_name)
    #     frames = os.listdir(frames_dir)
    #     for frame in sorted(os.listdir(frames_dir), key=lambda x: int(x[6:-4])):
    #         frame_path = os.path.join(frames_dir, frame)
    #         gif_frames[gif_name].append(pygame.image.load(frame_path))

    new_frames_path = "media/new_frames"
    if not os.path.exists(new_frames_path):
        os.makedirs(new_frames_path)
        for gif_name in gif_names:
            gif_frames[gif_name] = []
            new_frames_gifs_path = os.path.join(new_frames_path, gif_name)
            os.makedirs(new_frames_gifs_path)
            frames_dir = os.path.join(frames_path, gif_name)
            for frame in sorted(os.listdir(frames_dir), key=lambda x: int(x[6:-4])):
                frame_path = os.path.join(frames_dir, frame)
                new_frame_path = os.path.join(new_frames_gifs_path, frame)
                end_to_end(background_url, frame_path, new_frame_path)
                gif_frames[gif_name].append(pygame.image.load(new_frame_path))
    else:
        for gif_name in gif_names:
            gif_frames[gif_name] = []
            new_frames_gifs_path = os.path.join(new_frames_path, gif_name)
            for frame in sorted(os.listdir(new_frames_gifs_path), key=lambda x: int(x[6:-4])):
                new_frame_path = os.path.join(new_frames_gifs_path, frame)
                gif_frames[gif_name].append(pygame.image.load(new_frame_path))
    
    key_to_gif_mapping = {
        '1': 'normal',
        '2': 'normal-talking',
        '3': 'determined',
        '4': 'determined-talking',
        '5': 'thinking',
        '6': 'thinking-talking',
        '7': 'pointing',
        '8': 'making-point',
        '9': 'shocked',
        '0': 'bowing'
    }

    emotion_mapping = {
        "SHOCKED":'9', 
        "THANKFUL":'0', 
        "NORMAL":'2',
        "THINKING":'6', 
        "DETERMINED":'4'
    }

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('GIF Player')

    running = True
    counter = 0
    clock = pygame.time.Clock()
    frame_index = 0
    current_gif = 'normal'
    same_as_prev_counter = 0
    prev_state = None
    frozen = 0
    while running:
        counter += 1
        frozen = max(frozen - 1, 0)
        if counter % 10 == 0 and frozen == 0:
            r = requests.get('http://127.0.0.1:5000/getEmotion')
            state = r.json()['emotion']
            if state != prev_state:
                frozen = 30
                current_gif = key_to_gif_mapping['1' if state is None else emotion_mapping[state]]
                frame_index = 0
                prev_state = state
        
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if state is None:
            #     current_gif = key_to_gif_mapping['1']
            #     same_as_prev_counter = 0
            #     frame_index = 0
            #     prev_state = state
            # else:
            #     if prev_state is None or prev_state != state:
            #         same_as_prev_counter = 20
            #         prev_state = state
            #     current_gif = key_to_gif_mapping[emotion_mapping[state]]
            #     same_as_prev_counter -= 1
            #     if same_as_prev_counter == 0:
            #         state = None
            #         prev_state = None
            #     frame_index = 0

        screen.blit(gif_frames[current_gif][frame_index], (0, 0))
        pygame.display.flip()
        frame_index = (frame_index + 1) % len(gif_frames[current_gif])
        clock.tick(30)  # Control FPS
    pygame.quit()

def save_image_from_prompt(fname, response):
    if response.status_code == 200:
        save_directory = "generated_image/"  # Change this to your target directory
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        image_response = requests.get(response.json()['data'][0]['url'])
        image_data = io.BytesIO(image_response.content)
        image = Image.open(image_data)
        png_output = io.BytesIO()
        image.save(png_output, format="PNG")
        png_output.seek(0)
        image_path = os.path.join(save_directory, f"{fname}.png")
        with open(image_path, "wb") as f:
            f.write(png_output.getvalue())
        print(f"Image successfully saved to {image_path}")
        return image_path
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def generate_image(prompt, url="https://api.openai.com/v1/images/generations", model="dall-e-3", n=1, size="1024x1024", fname="sample_image"):
    start_time = time.time()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "OpenAI-Organization": "org-JTROgcNqsT3nmIykBTWAWqQf",
        "OpenAI-Project": "proj_VfrQaUHCOOTqNxwQXri4ekiz"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "n": n,
        "size": size
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    print(f"Generation took {time.time() - start_time} seconds") 
    image_path = save_image_from_prompt(fname, response)
    return image_path


def generate_similar_background(image_url, max_tokens=1000):
    img_path = os.path.join("generated_image", f"{image_url.replace('/', '_')}.png")
    if os.path.exists(img_path):
        return img_path
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the background image in great details."},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                },
                },
            ],
            }
        ],
        max_tokens=700,
    )
    description = response.choices[0]
    image_path = generate_image(f"{description} Remove all the humans, I just want the pure background", fname=image_url.replace('/', '_'))
    return image_path


def combine_image_with_background(background_path, over_path, save_path):
    background = Image.open(background_path)
    background = background.resize((800, 800))
    overlay = Image.open(over_path)
    blurred_background = background.filter(ImageFilter.GaussianBlur(10)) 
    background_width, background_height = blurred_background.size
    overlay_width, overlay_height = overlay.size
    center_x = (background_width - overlay_width) // 2
    blurred_background.paste(overlay, (center_x, 150), overlay.convert("RGBA")) 
    blurred_background.save(save_path)
    return
   

def end_to_end(background_url, frame, new_frame):
    background_path = generate_similar_background(background_url)
    combine_image_with_background(background_path, frame, new_frame)

if __name__ == '__main__':
    main()
    