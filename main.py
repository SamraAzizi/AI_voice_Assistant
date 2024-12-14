import asyncio

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

from dotenv import load_dotenv

load_dotenv()


async def entrypoint(ctx: JobContext):

    intital_ctx = llm.chat_context().append(
        role="system",
        text=("you are a voice assistant created by livekit, your interface with user will be voice"
             "you should short and concise responses and avoid using a unpronoucable pubtualities"
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=intital_ctx
    )

    assistant.start(ctx.room)

    await asyncio.sleep(1)

    await assistant.say("hey! how can I assist you today!", allow_interruptions=True)





if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))