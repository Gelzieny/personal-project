from fastapi import FastAPI
from starlette.responses import HTMLResponse
from App.controller.category_controller import category_controller
from App.dependencias.database import ConexaoPostgres
from fastapi.responses import JSONResponse

app = FastAPI(
  title="Projeto Pessoal de Finanças",
  description=""
)

######################### ROUTERS #####################
app.include_router(category_controller)

@app.get("/apiname", include_in_schema=False, response_class=HTMLResponse)
async def apiname() -> str:
  return "Projeto Pessoal de Finanças"


@app.get("/healthz", include_in_schema=False, response_class=JSONResponse)
async def test_conexao():
  resultado = ConexaoPostgres().teste() 
  return JSONResponse(content={"status": resultado['status'], "result": resultado['resultado']})


import uvicorn
if __name__ == "__main__":
  uvicorn.run("manage:app", port=5499, host="localhost",  log_level="info", reload=True)