from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import storage

app = FastAPI()

# Configura bucket
client = storage.Client.from_service_account_json('credentials.json')
bucket = client.bucket('pcloud20204_test2025')

# Modello dati
class SensorData(BaseModel):
    client: str
    type: str
    data: dict

@app.post("/data/")
async def receive_data(sensor: SensorData):
    file_name = f"{sensor.client}/{sensor.type}.txt"
    blob = bucket.blob(file_name)
    blob.upload_from_string(str(sensor.data))
    return {"status": "ok"}

@app.get("/")
async def dashboard():
    return {"message": "Server operativo"}
