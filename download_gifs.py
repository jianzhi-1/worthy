import requests
import os
import shutil

def download_gif(gif_url, save_path):
    try:
        # Send a GET request to the GIF URL
        response = requests.get(gif_url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Open a local file with write-binary mode
            with open(save_path, 'wb') as file:
                # Write the content of the response to a local file
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"GIF downloaded successfully and saved to {save_path}")
        else:
            print(f"Failed to retrieve GIF. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

media_path = 'media'
if os.path.exists(media_path):
    shutil.rmtree(media_path)
os.makedirs(media_path)

gif_path = 'media/gifs'
if os.path.exists(gif_path):
    shutil.rmtree(gif_path)
os.makedirs(gif_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/f/f8/SoJ_Miles_Bowing.gif/revision/latest/scale-to-width-down/1000?cb=20210920052914'
save_path = 'media/gifs/bowing.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/4/40/SoJ_Miles_Determined_T.gif/revision/latest/scale-to-width-down/1000?cb=20210920044150'
save_path = 'media/gifs/determined-talking.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/b/bb/SoJ_Miles_Determined.gif/revision/latest/scale-to-width-down/1000?cb=20210920053039'
save_path = 'media/gifs/determined.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/c/c1/SoJ_Miles_Pointing.gif/revision/latest/scale-to-width-down/1000?cb=20210920052912'
save_path = 'media/gifs/making-point.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/a/ac/SoJ_Miles_Normal_T.gif/revision/latest/scale-to-width-down/1000?cb=20210920044149'
save_path = 'media/gifs/normal-talking.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/4/43/SoJ_Miles_Normal.gif/revision/latest/scale-to-width-down/1000?cb=20210920053101'
save_path = 'media/gifs/normal.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/1/19/SoJ_Miles_Point.gif/revision/latest/scale-to-width-down/1000?cb=20210920053102'
save_path = 'media/gifs/pointing.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/3/35/SoJ_Miles_Shock.gif/revision/latest/scale-to-width-down/1000?cb=20220317034613'
save_path = 'media/gifs/shocked.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/d/d0/SoJ_Miles_Think_T.gif/revision/latest/scale-to-width-down/1000?cb=20210920044233'
save_path = 'media/gifs/thinking-talking.gif'
download_gif(gif_url, save_path)

gif_url = 'https://static.wikia.nocookie.net/aceattorney/images/d/d1/SoJ_Miles_Think.gif/revision/latest/scale-to-width-down/1000?cb=20210920053101'
save_path = 'media/gifs/thinking.gif'
download_gif(gif_url, save_path)