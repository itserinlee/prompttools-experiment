from prompttools.experiment import OpenAIChatExperiment
from dotenv import load_dotenv, find_dotenv
# import os

load_dotenv(find_dotenv())


# Input messages
prompts = [
    "Tell me a joke.",
    "Is 17077 a prime number?"
]

messages = [
    [{"role": "user", "content": prompts[0]},],
    [{"role": "user", "content": prompts[1]},],
]

models = ["gpt-3.5-turbo", "gpt-4"]
temperatures = [0.0]
outputTokenLimit=[60]

exp = OpenAIChatExperiment(
    model=models,
    messages=messages,
    temperature=temperatures,
    max_tokens=outputTokenLimit
    )

exp.run()
exp.visualize()