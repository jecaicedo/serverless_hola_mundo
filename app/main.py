from fastapi import FastAPI, Response
from mangum import Mangum

app = FastAPI()

@app.get("/", response_class=Response)
def hola_mundo():
    
    hola_mundo = "hola mundo"
    return Response(content=hola_mundo)

handler = Mangum(app)