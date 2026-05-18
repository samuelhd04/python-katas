from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.kata1_dictionary import Dictionary
from src.kata2_spending import get_total
from src.kata3_nth_letter import nth_letter

app = FastAPI()
dictionary = Dictionary()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return FileResponse("static/index.html")


@app.get("/dictionary/{word}")
def look(word: str):
    return {"result": dictionary.look(word)}


@app.post("/dictionary/{word}")
def newentry(word: str, definition: str):
    dictionary.newentry(word, definition)
    return {"message": f"Entry added for {word}"}


@app.get("/spending")
def spending(items: str, costs: str, tax: float):
    costs_dict = {}
    for pair in costs.split(","):
        name, price = pair.split(":")
        costs_dict[name] = float(price)
    items_list = items.split(",")
    return {"result": get_total(costs_dict, items_list, tax)}


@app.get("/nth-letter")
def nth(words: str):
    words_list = words.split(",")
    return {"result": nth_letter(words_list)}
