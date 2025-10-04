import asyncio
from langgraph_sdk import get_client

async def main():
    client = get_client(url="http://127.0.0.1:2024")

    thread = await client.threads.create()
    input_question = {"question": "How were Nvidia Q2 2024 earnings?"}

    async for event in client.runs.stream(
        thread["thread_id"],
        assistant_id="parallelization",
        input=input_question,
        stream_mode="values",
    ):
        if event.data is not None:
            answer = event.data.get("answer", None)
            if answer:
                print(answer["content"])

if __name__ == "__main__":
    asyncio.run(main())