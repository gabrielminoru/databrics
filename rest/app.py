from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from typing import Union

app = FastAPI(title="databrics")
data = Path("data/countries.txt").read_text().split("\n")[:-1]

def alternate_case(text: str) -> str:
    res = ""
    for idx, l in enumerate(text):
        if idx % 2 == 0:
            res += l.lower()
        else:
            res += l.upper()
    return res

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    text = "<h1>Welcome to BRICS</h1>"
    for c in data:
        text += f"\n<li>{c}</li>"
    return text

@app.get("/list")
def list(case: Union[str, None] = None):
    if not case:
        return data
    if case == "upper":
        return [d.upper() for d in data]
    if case == "lower":
        return [d.lower() for d in data]
    if case == "alternate":
        return [alternate_case(d) for d in data]

@app.get("/check/")
def read_item(country: str):
    return {"is_brics": country in data}
