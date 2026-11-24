from fastapi import FastAPI

app = FastAPI(title="Clinic Booking API")


@app.get("/health")
def health_check():
    return {"status":"ok"}