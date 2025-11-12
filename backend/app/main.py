from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 1. Import
from app.api.endpoints import checker

app = FastAPI(title="News Checker API")

# 2. Define your frontend's origin
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# 3. Add the middleware (BEFORE the router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Include your router AFTER the middleware
app.include_router(checker.router)

@app.get("/")
def read_root():
    return {"status": "API is running"}