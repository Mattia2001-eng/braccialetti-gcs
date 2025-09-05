import os
import time
import pandas as pd
import requests

SERVER_URL = "https://TUO-SERVER-CLOUD-RUN/data/"
CLIENT_NAME = "client1"
DATA_DIR = f"client/{CLIENT_NAME}/data/"
INTERVAL = 1  # secondi tra una riga e l'altra

csv_files = {
    "wrist_acc.csv": ["timestamp", "ax", "ay", "az"],
    "wrist_skin_temperature.csv": ["timestamp", "temp"],
    "wrist_ibi.csv": ["timestamp", "duration"],
    "wrist_hr.csv": ["timestamp", "hr"],
    "wrist_eda.csv": ["timestamp", "eda"],
    "wrist_bvp.csv": ["timestamp", "bvp"]
    
}

for file_name, cols in csv_files.items():
    file_path = os.path.join(DATA_DIR, file_name)
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        payload = {
            "client": CLIENT_NAME,
            "type": file_name,
            "data": row.to_dict()
        }
        try:
            requests.post(SERVER_URL, json=payload)
        except Exception as e:
            print(f"Errore invio dati: {e}")
        time.sleep(INTERVAL)
