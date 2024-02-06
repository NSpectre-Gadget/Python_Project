import os
from pathlib import Path
import requests

PINTATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath possibly using  for loop to grab all images in img folder
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.env("PINATA_API_KEY"),
    "pinata_secret_api_key": os.env("PINATA_SECRET_API_KEY"),
}


def main():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINTATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
        )
        print(response.json())
