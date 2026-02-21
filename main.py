from fastapi import FastAPI
from googlenewsdecoder import gnewsdecoder

app = FastAPI()

@app.get("/decode")
def decode(url: str):
    try:
        real_url = gnewsdecoder(url)
        return {"real_url": real_url}
    except Exception as e:
        return {"error": str(e)}
