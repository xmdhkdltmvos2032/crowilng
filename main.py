import os
from fastapi import FastAPI, Query
import subprocess

app = FastAPI()

# 🚀 서버 시작 시 쿠키 파일 생성
cookies_content = os.getenv("INSTAGRAM_COOKIES")

if cookies_content:
    with open("cookies.txt", "w") as f:
        f.write(cookies_content)

@app.get("/get_video")
def get_video(url: str = Query(...)):
    try:
        cmd = [
            "yt-dlp",
            "--cookies", "cookies.txt",
            "--no-playlist",
            "--quiet",
            "-f", "best",
            "-g",
            url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            return {"success": False, "error": result.stderr.strip()}

        return {
            "success": True,
            "direct_urls": result.stdout.strip().split("\n")
        }

    except Exception as e:
        return {"success": False, "error": str(e)}
