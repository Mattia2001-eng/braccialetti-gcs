from google.cloud import storage

client = storage.Client.from_service_account_json('credentials.json')
bucket = client.bucket('pcloud20204_test2025')

files = ["gcp1/prev.pdf",
         "client/data/wrist_acc.csv",
         "client/data/wrist_bvp.csv",
         "client/data/wrist_eda.csv",
         "client/data/wrist_hr.csv",
         "client/data/wrist_ibi.csv",
         "client/data/wrist_skin_temperature.csv"]

for f in files:
    blob = bucket.blob(f)
    blob.upload_from_filename(f)
    print(f"File {f} uploaded to {f}.")
