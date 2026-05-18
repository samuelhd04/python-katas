from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.kata1_dictionary import Dictionary
from src.kata2_spending import get_total
from src.kata3_nth_letter import nth_letter

app = FastAPI()
dictionary = Dictionary()


@app.get("/dictionary/{word}")
def look(word: str):
    return {"result": dictionary.look(word)}


@app.post("/dictionary/{word}")
def newentry(word: str, definition: str):
    dictionary.newentry(word, definition)
    return {"message": f"Entry added for {word}"}


@app.get("/spending")
def spending(items: str, tax: float):
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    items_list = items.split(",")
    return {"result": get_total(costs, items_list, tax)}


@app.get("/nth-letter")
def nth(words: str):
    words_list = words.split(",")
    return {"result": nth_letter(words_list)}
