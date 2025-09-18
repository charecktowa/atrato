from fastapi import FastAPI
from app.routes import hello, student

import uvicorn

app = FastAPI()

# Registrar los routers
app.include_router(hello.router)
app.include_router(student.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
