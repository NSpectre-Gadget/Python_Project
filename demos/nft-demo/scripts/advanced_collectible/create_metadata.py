from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

# breed_to_iimage_uri={"upload_image_uris here if you want to speed up getting images"}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"Youhave created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"  # returns string with number
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite.")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            # image_uri=image_uri if image_uri else breed_to_image_uri[breed]
            # remember to include the above line if using above image_uri and bypassing IPFS
            collectible_metadata["image"] = image_uri
            # We need our image already uploaded to IPFS so we can assign it to our metadata.
            # We accomplish this by
            # image_uri = upload to ipfs(image_path)
            # collectible_metadata["image_url"]. Using def upload_to_ipfs()
            # dump the collectible_metadata["image"] to its own filename and then upload to IPFS by doing the following:
            with open(metadata_file_name), "w" as file:
                json.dump(collectible_metadata, file)
            # if os.getenv("UPLOAD_IPFS") == "true":
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # start upload stuff
        # to start download command linefor IPFS by searching on Google
        ipfs_url = "http://127.0.0.1:5001/webui"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["hash"]
        filename = filepath.split("/")[-1:][0]  # "./img/PUG.png" becomes "0-PUG.png"
        image_uri = f"http://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        # "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
        print(image_uri)
        return image_uri


# curl-X POST -F file-@metadata/rinkeby/0-SHIBA_INU.json http:///localhost:5001/api
