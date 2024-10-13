import argparse
import io
import json
import os
import openai
from PIL import Image, ImageFilter
import requests
import time
API_KEY = "<API_KEY>"
openai.api_key = API_KEY


def save_image_from_prompt(fname, response):
    if response.status_code == 200:
        save_directory = "generated_image/"  # Change this to your target directory
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        data = response.content.decode("utf-8")
        data_dict = json.loads(data)
        image_response = requests.get(data_dict['data'][0]['url'])
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


def generate_similar_backgroud(image_url, max_tokens=1000, fname="sample_image"):
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
    image_path = generate_image(f"{description} Remove all the humans, I just want the pure background", fname=fname)
    return image_path


def combine_image_with_background(background_path, over_path):
    background =Image.open(background_path)
    background = background.resize((800, 800))
    overlay = Image.open(over_path)
    blurred_background = background.filter(ImageFilter.GaussianBlur(10)) 
    background_width, background_height = blurred_background.size
    overlay_width, overlay_height = overlay.size
    center_x = (background_width - overlay_width) // 2
    blurred_background.paste(overlay, (center_x, 150), overlay.convert("RGBA")) 
    blurred_image_path = os.path.join("generated_image", "blurred_output_image.jpg")
    blurred_background.save(blurred_background)
    Image.open(blurred_image_path)
    print(f"Saved blurred background with character image to {blurred_image_path}")
   
   
def main():
    parser = argparse.ArgumentParser(description="A simple argument parser example.")
    parser.add_argument('--orig_background', type=str, help='The URL of the original image') 
    parser.add_argument('--overlay_image', type=str, help='The animated character')
    args = parser.parse_args()
    background_path = generate_similar_backgroud(args.orig_background)
    combine_image_with_background(background_path, args.overlay_image)

    
if __name__ == '__main__':
    main()