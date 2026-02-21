from fastapi import FastAPI
from googlenewsdecoder import gnewsdecoder

app = FastAPI()

@app.get("/decode")
def decode(url: str, title: str):
    try:
        result = gnewsdecoder(url)

        if not result.get("status"):
            return {"error": "Decoding failed"}

        return {
            "title": title,
            "decoded_url": result["decoded_url"]
        }

    except Exception as e:
        return {"error": str(e)}
