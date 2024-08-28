from fastapi import FastAPI

#recrea el comportamiento de nuestro servidor
app = FastAPI()

@app.get("/")
async def root():
    return "alo aqui dani"