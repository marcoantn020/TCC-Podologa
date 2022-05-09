from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.application.api.routes import user_route
from src.application.api.routes import login_route

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_route.router)
app.include_router(login_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)