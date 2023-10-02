#!/usr/bin/env python3
import logging
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    llm = Ollama(
        base_url="http://localhost:11434",
        model="llama2",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )

    llm("Tell me about the history of AI")


if __name__ == "__main__":
    main()
