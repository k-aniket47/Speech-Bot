# Speech-Bot

SpeechBot is a Discord bot that utilizes the OpenAI API and speech recognition to interact with users in voice channels. The bot can listen to user questions, 
transcribe them, generate answers using the OpenAI GPT-3.5 model, and then respond with the generated answers in the text channel.

## Setup and Configuration

To use SpeechBot, you need to follow these steps:

Clone this repository to your local machine.

Install the required dependencies listed in the requirements.txt file.

Obtain your Discord bot token and OpenAI API key.

Create a .env file in the root directory of the project and store your keys in it as follows:

Discord_token=YOUR_DISCORD_BOT_TOKEN
OPEN_AI_API=YOUR_OPENAI_API_KEY

Invite the bot to your Discord server, making sure to grant it the necessary permissions to join voice channels and send messages in text channels.

## How to Use

Once the bot is set up and invited to your server, use the !join command in any text channel to make the bot join the voice channel you are currently in.

Ask questions aloud while the bot is in the voice channel. The bot will transcribe your question, generate an answer using the GPT-3.5 model, and then respond in the text channel.

Use the !leave command in any text channel to make the bot leave the voice channel.

## Available Commands

!join: Tells the bot to join the voice channel you are currently in.

!leave: Makes the bot leave the voice channel.

!hello: Sends a simple greeting message in the text channel.

!ping: Sends a "pong!" message in response to check if the bot is responsive.

## How It Works
When you use the !join command, the bot will join the voice channel you are connected to.

The bot will continuously listen for any questions you ask in the voice channel.

Once it detects a question, it will transcribe the audio to text using speech recognition.

The transcribed question will be sent to OpenAI's GPT-3.5 model as a prompt.

The GPT-3.5 model will generate an answer based on the provided question.

The generated answer will be sent back to the text channel for everyone to see.

### Important Note
The bot requires access to the internet and access to the OpenAI API to work correctly.

The accuracy and quality of the answers depend on the capabilities of the GPT-3.5 model and the clarity of the questions asked.

![image](https://github.com/k-aniket47/Speech-Bot/assets/79148315/bc852858-70bb-49ac-a717-ae6a4bf07731)
![image](https://github.com/k-aniket47/Speech-Bot/assets/79148315/eec604ba-d486-44d0-8863-0dbcee52b637)

## Text Response:

![image](https://github.com/k-aniket47/Speech-Bot/assets/79148315/a77d209d-5d03-4875-b03a-6ca76c0f2c09)
![image](https://github.com/k-aniket47/Speech-Bot/assets/79148315/a163643b-eff3-40fe-ba9b-f9ff7c1f47a9)



