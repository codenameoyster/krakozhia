import asyncio
import os

from anthropic import AsyncAnthropic
from anthropic.types import ContentBlock, Message, TextBlock
from dotenv import load_dotenv

evals = [
    "What is Underwhelming Spatula?",
    "Who wrote 'Dubious Parenting Tips'?",
    "How long is Almost-Perfect Investment Guidle?",
]
eval_answers = [
    "Underwhelming Spatula is a kitchen tool that redefines expectations by fusing whimsy with functionality.",
    "Lisa Melton wrote Dubious Parenting Tips.",
    "The Almost-Perfect Investment Guide is 210 pages long.",
]

load_dotenv()
client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)


async def main() -> None:
    message: Message = await client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        model="claude-haiku-4-5",
    )
    print(message.content)


async def send_eval(msg: str) -> list[ContentBlock]:
    message: Message = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
    )

    return message.content


async def evaluate_answers(expected_answer: str, actual_answer: str) -> str:
    prompt = f"""Please evaluate the generated answer. If the generated answer provides the same information as the expected answer, then return PASS. Otherwise, return FAIL. Expected answer: {expected_answer} Generated answer: {actual_answer}"""
    resp = await send_eval(prompt)
    r = resp[0]
    match r:
        case TextBlock(text=text):
            return text.strip()
        case _:
            raise ValueError("Expected a TextBlock in the response content.")

    if isinstance(r, TextBlock):
        return r.text.strip()
    raise ValueError("Expected a TextBlock in the response content.")


asyncio.run(main())
