from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import aiohttp
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

API_URL = "https://miniapp-liard.vercel.app/"

@app.get("/api/data")
async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            data = await response.json()
            return JSONResponse(content=data)

# @app.get("/")
# async def serve_index():
#    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
