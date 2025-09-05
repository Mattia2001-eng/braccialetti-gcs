from google.cloud import storage
import os

# Cartella dei CSV
csv_folder = "client/data"
bucket_name = "pcloud20204_test2025"

# Autenticazione con il file JSON
client = storage.Client.from_service_account_json('credentials.json')
bucket = client.bucket(bucket_name)

# Carica tutti i CSV presenti nella cartella
for fname in os.listdir(csv_folder):
    source_file = os.path.join(csv_folder, fname)
    destination_blob_name = f"data/{fname}"
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file)
    print(f"File {source_file} uploaded to {destination_blob_name}.")
