import uvicorn
from fastapi import FastAPI
from service import equation, Equation, color_hint

app = FastAPI()


@app.post('/')
def index(item: Equation):
    return equation(item)


@app.get('/')
def check_color(item: int):
    return color_hint(item)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
