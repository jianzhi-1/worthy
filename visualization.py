import pygame
from PIL import Image
import os

def main():
    media_path = 'media/gifs'
    frames_path = 'media/frames'
    gif_names = [os.path.splitext(file)[0] for file in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, file))]
    gif_frames = {}
    for gif_name in gif_names:
        gif_frames[gif_name] = []
        frames_dir = os.path.join(frames_path, gif_name)
        frames = os.listdir(frames_dir)
        for frame in sorted(os.listdir(frames_dir), key=lambda x: int(x[6:-4])):
            frame_path = os.path.join(frames_dir, frame)
            gif_frames[gif_name].append(pygame.image.load(frame_path))
    
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

    pygame.init()
    screen = pygame.display.set_mode((1000, 667))
    pygame.display.set_caption('GIF Player')

    running = True
    clock = pygame.time.Clock()
    frame_index = 0
    current_gif = 'normal'
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    number_pressed = event.key - pygame.K_0
                    current_gif = key_to_gif_mapping[str(number_pressed)]
                    frame_index = 0

        screen.blit(gif_frames[current_gif][frame_index], (0, 0))
        pygame.display.flip()
        frame_index = (frame_index + 1) % len(gif_frames[current_gif])
        clock.tick(30)  # Control FPS
    pygame.quit()

if __name__ == '__main__':
    main()