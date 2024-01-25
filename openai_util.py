from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_completion_to_messages(
    messages: list, model: str = "gpt-4-1106-preview", temperature: int = 0
) -> str:
    """
    Gets the completion of a list of messages using OpenAI's API.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content


def get_stream_to_messages(
    messages: list, model: str = "gpt-4-1106-preview", temperature: int = 0
) -> str:
    """
    Gets the completion of a list of messages using OpenAI's API.
    """
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True,
    )
    return stream


def get_completion_to_prompt(
    prompt: str,
    model: str = "gpt-4-1106-preview",
    temperature: int = 0,
    role: str = "user",
) -> str:
    """Gets the response to a prompt using OpenAI's API."""
    messages = [{"role": "user", "content": prompt}]
    return get_completion_to_messages(messages, model, temperature)
