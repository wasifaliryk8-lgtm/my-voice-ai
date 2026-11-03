from fastapi import FastAPI

app = FastAPI(title="My Voice AI")

@app.get("/")
def home():
    return {
        "message": "Welcome to My Voice AI!",
        "status": "App is running"
    }
