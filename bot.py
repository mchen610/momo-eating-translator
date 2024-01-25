import os
import json
from discord import Intents, Bot, Message
from file_reading import read_file_to_string
from openai_util import get_completion_to_prompt
from dotenv import load_dotenv

load_dotenv()


DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
DISCORD_USER_ID = os.environ["DISCORD_USER_ID"] 

bot = Bot(intents=Intents.all())


def get_nlp_data(text: str) -> dict:
    prompt = read_file_to_string("prompt.md")
    response = get_completion_to_prompt(f"{prompt}\nText: {text}")
    try:
        return json.loads(response)
    except json.decoder.JSONDecodeError:
        return {"is_gibberish": False, "translation": ""}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message: Message):
    if message.author.id == DISCORD_USER_ID:
        data = get_nlp_data(message.content)
        if (
            "is_gibberish" in data
            and data["is_gibberish"]
            and data["translation"] != ""
        ):
            await message.channel.send(data["translation"])


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
