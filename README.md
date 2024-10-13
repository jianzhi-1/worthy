# Worthy
Pear VC Hack 2024 🍐

A visually appealing OpenAI-powered (Realtime, DALL-E, GPT) companion, capable of real-time conversations and emotional reactions. See [Demo](https://www.youtube.com/watch?v=XSTgHln8Upg)!

![Edgeworth Image](./app_image.png)

### Set up

#### Installation
First, download Edgeworth sprites by running
```shell
python3 download_gifs.py
python3 gifs_to_frames.py
```

Search for occurrences of `<API_KEY>` in the codebase and replace with your OpenAI API key. Then, run the following shell commands to install the necessary Python and JavaScript libraries.
```shell
pip install openai pygame Flask
cd realtime-backend
npm i
npm start
```
Go to `http://localhost:3000/`, where you will be prompted to enter your `<API_KEY>` for OpenAI's Realtime API access.

#### Running
In three different terminals, start the Realtime API backend (JavaScript), then the emotion state backend (Flask), then the game frontend (pygame).
```shell
cd realtime-backend
npm start
```
You can check the successful running of the backend by going to: `http://localhost:3000`

```shell
python3 emotion_state_backend.py
```
You can check the status of the Flask app by going to: `http://localhost:5000/getEmotion`

```shell
python3 game_frontend.py
```
Note that `game_frontend.py` must be run after `emotion_state_backend.py`. It takes typically around 10 seconds for the game UI to appear.

### Basic Description of Idea
Create a virtual bot that has naturalistic conversation abilities (e.g. talking to it should feel more natural than Alexa). For one, the audio stream will keep going (like Zoom), and the bot should have interrupt mechanisms to shorten the response time. There should be minimal waiting for the user. This is the speech aspect.

The other aspects involve making this conversation environment nicer:

(1) it would be nice to have a transcript documenting what has been spoken

(2) From the transcript and speech, can use OpenAI's text-to-image to visualise what the bot is thinking as the user is speaking (or when it is generating its outputs)

(3) Graphics-wise, should have an avatar as the face of the bot. Hopefully can find some pre-existing online animations to render, with the avatar displaying some basic emotions.

(4) Another very cool feature is if we show the Bot the user's webcam, the Bot can use the webcam background to update its own background. (This can be done with OpenAI's image-to-image)

### Features

1. 🎨 Amazing graphics and visuals 
You have Edgeworth himself, with his variety of prosecutorial poses. The background is DALL-E generated depending on the context of the conversation (not fully implemented yet). There may be some flickering of the image due to interweaved API calls, but it is minimal.

2. 🗣️ Speech agent (with transcript)
Automatically fulfilled by RealTime API. Guarantees robust performance - allows interruption of the speech agent. The voice is chosen as a variant of `echo`. For best effect, interact with it in a silent room. Sometimes, the latency for response is a bit longer than naturalistic conversations. 

3. 🤨 Emotion states and transitions
Edgeworth usually appears reserved, but there are times where he might be "shocked"! Can you find those scenarios? Emotion inference is done through GPT text completion and the transition is done via an API call to the Flask backend. 

### Resources
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [Edgeworth Sprites](https://aceattorney.fandom.com/wiki/Miles_Edgeworth_-_Sprite_Gallery#Chief_Prosecutor_(SoJ))

### Attributions
We thank the [Ace Attorney](https://www.ace-attorney.com/) [fandom wiki](https://aceattorney.fandom.com/wiki/Ace_Attorney_Wiki) for their collection of [Edgeworth 3D Sprites](https://aceattorney.fandom.com/wiki/Miles_Edgeworth_-_Sprite_Gallery#Chief_Prosecutor_(SoJ)), which made for fantastic visuals.