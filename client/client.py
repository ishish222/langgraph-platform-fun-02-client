import pdb
import os
import asyncio
from langgraph_sdk import get_client
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

ENDPOINT_ADDR = os.getenv("ENDPOINT_ADDR")
API_KEY = os.getenv("LANGCHAIN_API_KEY")


async def main():
    client = get_client(url=ENDPOINT_ADDR, api_key=API_KEY)

    assistant_id = "agent"
    new_thread = await client.threads.create()
    print(new_thread)

    input = {"messages": [{"role": "user", "content": "what's the weather in la"}]}

    async for chunk in client.runs.stream(
        new_thread["thread_id"],
        assistant_id,
        input=input,
        stream_mode="values"
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")


if __name__ == "__main__":
    asyncio.run(main())
