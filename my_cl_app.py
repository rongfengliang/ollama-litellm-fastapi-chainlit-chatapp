import chainlit as cl
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="sk-ZTp5zuetNQoJNgG4xHgGzw",
    base_url="http://localhost:4000"
)

settings = {
    "model": "dalongdemov3",
    "temperature": 0,
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        stream= True,
        messages=[
            {
                "content": "You are a helpful bot, you always reply in chinese.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    ) 
    msg = cl.Message(content="")
    await msg.send()
    async for token in  response:
        await msg.stream_token(token.choices[0].delta.content or "")
    await msg.update()

@cl.on_chat_start
async def main():
    await cl.Message(content="你好").send()
