# Generative Agents:<br/>Interactive Simulacra<br/>of Human Behavior

[![Stars](https://img.shields.io/github/stars/ayoreis/generative-agents?logo=github&label=Stars&style=social&prefix=S)](https://github.com/ayoreis/generative-agents/stargazers)
[![](https://img.shields.io/discord/1109062117937659986?label=Discord&logo=discord&style=social)](https://discord.gg/97kcgMNN)

Generative agents proposed by this [paper](https://arxiv.org/abs/2304.03442) extend LLMs (like ChatGPT) with memory, reflection, planing and a sandbox environment.

We're building our Python implementation that allows you to add Generative Agents to your own worlds.

<!-- Join us on [Discord](https://discord.gg/5dkM59gsDY) to get updates, ask questions, help or just chat about generative agents. -->

## TODO and contributing

We have a `#dev` chanel on Discord.

Answer [questions](/questions.md).

Check out the issues and projects tabs, there are also `# TODO`s scatered around the code.

- Python 3.10+
- Black
- isort

### Parts

- 4.1 [`Memory`](/blob/main/memory.py) represents the most basic type of memory, an observation. Importance calculation is done here.
- 4.2 [`Reflection`](/blob/main/reflection.py) a reflection.
- 4.3 [`Plan`](/blob/main/plan.py) a plan.
- 4.1 [`MemoryStream`](/blob/main/memory_stream.py) a stream of memories. Memory retrival is done here.
- 4 [`Agent`](/blob/main/agent.py)
- 5 [`Sandbox`](/blob/main/sandbox.py) tick, time,
- Figure 2 [`World`](/blob/main/nodes.py)
- Figure 2 [`Area`](/blob/main/nodes.py)
- Figure 2 [`Object`](/blob/main/nodes.py)

## Usage

```sh
pip install openai
```

### Authentication

Create a `openai_secrets.py` file and set your key there.

> **Note** https://platform.openai.com/docs/api-reference/authentication

```py
import openai

openai.api_key = 'Your OpenAI API key'
```

<!-- Tip: Use https://github.com/PawanOsman/ChatGPT -->
