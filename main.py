from arquivos import maio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
mes = maio

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def PaginaHtml(request : Request):
    dados = mes.LerArquivo()
    preçoDoKg = mes.PreçoDoKG()
    frangosAbatidos = mes.FrangosAbatidos()
    PreçoDeRetorno = mes.PreçoDeRetorno()
    FrangosVendidos = mes.FrangosVendidos()
    return templates.TemplateResponse("item.html",
    {"request": request, "dados": dados, "preçokg": preçoDoKg, "frangosAbatidos": frangosAbatidos,
     "retorno": PreçoDeRetorno, "frangosVendidos": FrangosVendidos})

@app.get("/Frangos")
async def Frangos():
    return mes.LerArquivo()

@app.get("/PreçoDoKg")
async def PreçoDoKg():
    return mes.PreçoDoKG()

@app.get("/FrangosAbatidos")
async def FrangosAbatidos():
    return mes.FrangosAbatidos()

@app.get("/FrangosVendidos")
async def FrangosVendidos():
    return mes.FrangosVendidos()

@app.get("/PreçoDeRetorno")
async def PreçoDeRetorno():
    return mes.PreçoDeRetorno()