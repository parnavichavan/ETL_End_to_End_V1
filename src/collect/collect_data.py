import os
from kaggle.api.kaggle_api_extended import KaggleApi

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name, save_path):
    """
    Download dataset from Kaggle using API.
    dataset_name: str -> format: "owner/dataset-name"
    save_path: str -> folder path to save dataset
    """
    # Create an instance of the Kaggle API
    api = KaggleApi()
    
    # Authenticate using the kaggle.json file
    api.authenticate()

    # Create the target directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print(f"Downloading {dataset_name} to {save_path} ...")
    
    # Download and unzip the files
    api.dataset_download_files(dataset_name, path=save_path, unzip=True)
    
    print("✅ Download complete!")

if __name__ == "__main__":
    dataset = "ranitsarkar01/porter-delivery-time-estimation-dataset"
    save_dir = "data/raw"

    download_dataset(dataset, save_dir)
