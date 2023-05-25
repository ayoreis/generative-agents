from tkinter import *
from tkinter import ttk

from agent import Agent

AGENTS = (Agent('Ayo is a 15 years old; Ayo is learning about AI'),)

root = Tk()
root.title('Generative Agents')
root.geometry('600x400')

paned_window = PanedWindow(orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=1)

left_pane = Frame(paned_window)
paned_window.add(left_pane)

Label(left_pane, text="Select agent").pack()

tabs = ttk.Notebook(paned_window)
paned_window.add(tabs)

agents_tab = Frame(tabs)
tabs.add(agents_tab, text='Agents')

for index, agent in enumerate(AGENTS):
    agent_frame = Frame(left_pane)
    memories = LabelFrame(agent_frame, text="Memories")

    for memory in agent.memory_stream.stream:
        memory = Label(memories, text=memory.natural_language_description)
        memory.pack()

    memories.pack()

    def refresh():
        for child in list(left_pane.children.values()):
            child.forget()

        agent_frame.pack()

    button = Button(agents_tab, text=f'Agent {index + 1}', command=refresh)
    button.pack()

locations_tab = Frame(tabs)
tabs.add(locations_tab, text='Locations')

root.mainloop()
