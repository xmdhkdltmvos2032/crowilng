from fastapi import FastAPI, Query
import subprocess

app = FastAPI()

@app.get("/get_video")
def get_video(url: str = Query(...)):
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "-f", "best",
                "--no-warnings",
                "--no-playlist",
                "-g",
                url
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        direct_url = result.stdout.strip().split("\n")[0]

        return {"direct_url": direct_url}

    except Exception as e:
        return {"error": str(e)}
