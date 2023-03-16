import discord
from discord.ext import commands
import speech_recognition as sr
import openai
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
Discord_token = os.getenv("Discord_token")
OPEN_AI_API = os.getenv("OPEN_AI_API")


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


openai.api_key = OPEN_AI_API
listening = False

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def hello(ctx):
    text_channel = ctx.channel
    await text_channel.send('I am a Voice ChatGPT')

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()
    await listen_to_question_and_answer(voice_client)


async def listen_to_question_and_answer(voice_client):
    global listening
    while True:
        if not listening:
            audio_task = asyncio.create_task(record_audio())
            listening = True
            audio = await audio_task
            listening = False
            try:
                question = transcribe_audio(audio)
                print('Question:', question)
                await send_question(voice_client, question)
                answer = generate_answer(question)
                print('Answer:', answer)
                await send_answer(voice_client, answer)
            except sr.UnknownValueError:
                print('Unknown Value Error')
            except sr.RequestError as e:
                print('Request Error:', e)

async def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = await asyncio.get_event_loop().run_in_executor(None, r.listen, source)
    return audio

def transcribe_audio(audio):
    r = sr.Recognizer()
    return r.recognize_google(audio)

def generate_answer(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.7,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text.strip()

async def send_answer(voice_client, answer):
    text_channel = voice_client.channel.guild.text_channels[0]
    await text_channel.send(f"Answer : {answer}")

async def send_question(voice_client, question):
    text_channel = voice_client.channel.guild.text_channels[0]
    await text_channel.send(f"Question : {question}" )

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

bot.run(Discord_token)