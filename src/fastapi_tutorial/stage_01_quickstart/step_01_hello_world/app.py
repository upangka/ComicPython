from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Tutorial",
    summary="FastAPI Tutorial",
    description="A sample project for learning FastAPI.",
    version="0.1.0",
    contact={
        "name": "Pkmer",
        "url": "https://juejin.cn/user/3112047871800540"
    }
)

@app.get("/", summary="root path")
async def read_root():
    return ("Hello","World")
