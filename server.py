from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import aiohttp

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

@app.get("/api/data")
async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            data = await response.json()
            return JSONResponse(content=data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
