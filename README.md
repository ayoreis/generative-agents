```mermaid
flowchart LR
    p(Perceive)
    m[["`**Memory Stream**`"]]
    r(Retrieve)
    rm[["`**Retrieved Memories**`"]]
    pl(Plan)
    re(Reflect)
    a(Act)

    p --> m
    subgraph Generative Agent Memory
    m --> r
    r --> rm
    end
    rm --> pl
    rm --> re
    pl --> m
    re --> m
    rm --> a
```

# Generative Agents:<br/>Interactive Simulacra<br/>of Human Behavior

<https://arxiv.org/abs/2304.03442>

Join us on Discord: <https://discord.gg/5dkM59gsDY>

## TODO

- [x] Read the [paper](https://arxiv.org/abs/2304.03442)
- [x] Memories
- [x] Memory stream
- [x] ChatGPT
- [ ] Observations
- [ ] Memory retrival
- [ ] Reflection
- [ ] Planing
- [ ] Reacting
- [ ] Enviroment
- [ ] Inner voice
- [ ] User agent
- [ ] Licence
- [ ] Alternative cheaper/local models
- [ ] GUI

## Usage

```sh
pip install openai
```

### Authentication

Create a `openai_api.py` file and set your key there.

> **Note** https://platform.openai.com/docs/api-reference/authentication

```py
import openai

openai.api_key = 'OpenAI API key'
```

<!-- Tip: Use https://github.com/PawanOsman/ChatGPT -->

## Helpful links

- <https://reverie.herokuapp.com/arXiv_Demo/#>
- <https://platform.openai.com/docs/guides/chat/introduction>
- <https://platform.openai.com/docs/api-reference/chat>

## Updates

### May 19

- Created Discord server <https://discord.gg/5dkM59gsDY>
- Indexed by Google <cache:https://github.com/ayoreis/generative-agents>
