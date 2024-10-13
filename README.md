# Maya
Pear VC Hack 2024 🍐

### Resources
[OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
[Maya Fey Sprites](https://aceattorney.fandom.com/wiki/Maya_Fey_-_Sprite_Gallery)
[Maya Fey Sprites](https://aceattorney.fandom.com/wiki/Maya_Fey_-_Sprite_Gallery#Without_Hood_)
[Edgeworth Sprites](https://aceattorney.fandom.com/wiki/Miles_Edgeworth_-_Sprite_Gallery#Chief_Prosecutor_(SoJ))

### Basic Description of Idea
Create a virtual bot that has naturalistic conversation abilities (e.g. talking to it should feel more natural than Alexa). For one, the audio stream will keep going (like Zoom), and the bot should have interrupt mechanisms to shorten the response time. There should be minimal waiting for the user. This is the speech aspect.

The other aspects involve making this conversation environment nicer:

(1) it would be nice to have a transcript documenting what has been spoken

(2) From the transcript and speech, can use OpenAI's text-to-image to visualise what the bot is thinking as the user is speaking (or when it is generating its outputs)

(3) Graphics-wise, should have an avatar as the face of the bot. Hopefully can find some pre-existing online animations to render, with the avatar displaying some basic emotions.

(4) Another very cool feature is if we show the Bot the user's webcam, the Bot can use the webcam background to update its own background. (This can be done with OpenAI's image-to-image)

### Breakdown of Idea

1. Voice (Jianzhi) + Chat Integration (Jianzhi)
Mainly use RealTime API
- seems quite comprehensive, receive input audio, commit
- Should interrupt? If yes, interrupt, emit. If receive some more, pause, push emit back into stack for next emission
- Speech update
This part may take at least **8** hours.

2. Thought-Image Generation
This part may take ~2 hours hours.
Given AI bot's speech (in text), generate an image that most closely match what the bot is thinking.

4. Background-Image Generation
This part might take at least 4 hours.
Given user's background / back ground suggestion, match the background for the application.

5. Chat
This part should take maximally 1 hour if everything else is done correctly. Just display a UI for chat. Don't need do this if no time. Not exciting.

6. Avatar (Hopefully Jin Wei, since he has graphics knowledge)
This part may take ~3-4 hours. Ask ChatGPT to generate the website (maybe this will work)

- https://www.reddit.com/r/vndevs/comments/esyt4e/emotional_ranges_of_sprites_referencechecklist/
- https://sketchfab.com/

8. Demo
??
