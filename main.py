from fastapi import FastAPI, Query
import subprocess

app = FastAPI()

@app.get("/get_video")
def get_video(url: str = Query(...)):
    try:
        result = subprocess.run(
            ["yt-dlp", "-g", url],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        return {"direct_url": result.stdout.strip()}

    except Exception as e:
        return {"error": str(e)}
