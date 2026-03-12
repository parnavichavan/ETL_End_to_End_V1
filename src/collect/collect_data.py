import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name, save_path):
    api = KaggleApi()
    api.authenticate()   # This will now use KAGGLE_USERNAME and KAGGLE_KEY from Jenkins

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print(f"Downloading {dataset_name} to {save_path} ...")
    api.dataset_download_files(dataset_name, path=save_path, unzip=True)
    print("✅ Download complete!")

if __name__ == "__main__":
    dataset = "ranitsarkar01/porter-delivery-time-estimation-dataset"
    save_dir = "data/raw"
    download_dataset(dataset, save_dir)
