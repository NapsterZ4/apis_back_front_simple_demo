from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/v1/get_names", tags=["GET"])
async def get_names():
    return {
        "nombre": "Jorge",
        "apellido": "Godoy"
    }


@app.post("/v1/upload_names", tags=["POST"])
async def post_names(data: dict):
    return {"message": data.get("nombre")}


@app.post("/v1/suma_numeros", tags=["SUMAS"])
async def post_suma(number: int):
    if isinstance(number, int):
        value = 2 + number
        return {"message": value}
    else:
        return JSONResponse(
            status_code=400,
            content={"message": f"Error! you need an integer"}
        )
