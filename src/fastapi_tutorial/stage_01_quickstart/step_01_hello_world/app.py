from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Tutorial",
    description="一个用于学习 FastAPI 的示例项目",
    version="0.1.0",
)

@app.get("/", summary="根路径")
async def read_root():
    return ("Hello","World")
