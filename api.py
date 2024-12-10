from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar carpeta de plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/python", response_class=HTMLResponse)
def Python(request: Request):
    return templates.TemplateResponse("Python.html", {"request": request, "title": "Graficos Python"})

@app.get("/R", response_class=HTMLResponse)
def R(request: Request):
    return templates.TemplateResponse("R.html", {"request": request, "title": "Graficos R"})

@app.get("/datawriper", response_class=HTMLResponse)
def R(request: Request):
    return templates.TemplateResponse("datawriper.html", {"request": request, "title": "Graficos DataWriper"})

@app.get("/documento", response_class=HTMLResponse)
def R(request: Request):
    return templates.TemplateResponse("documento.html", {"request": request, "title": "Documento completo"})