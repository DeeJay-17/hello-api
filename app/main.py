from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from my HomeLab!",
        "server": "DJ-Ubuntu"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}