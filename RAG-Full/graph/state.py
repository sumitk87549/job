from typing import TypedDict

class GraphState(TypedDict):
    query:str
    answer:str
    intent:str

    def __init__ (self, query:str, answer:str, intent:str):
        self.query = query
        self.answer = answer
        self.intent = intent
