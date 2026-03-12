import os, json
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name, save_path):
    # Load kaggle.json from config folder
    with open("config/kaggle.json") as f:
        creds = json.load(f)

    os.environ["KAGGLE_USERNAME"] = creds["username"]
    os.environ["KAGGLE_KEY"] = creds["key"]

    api = KaggleApi()
    api.authenticate()

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print(f"Downloading {dataset_name} to {save_path} ...")
    api.dataset_download_files(dataset_name, path=save_path, unzip=True)
    print("✅ Download complete!")

if __name__ == "__main__":
    dataset = "ranitsarkar01/porter-delivery-time-estimation-dataset"
    save_dir = "data/raw"
    download_dataset(dataset, save_dir)
