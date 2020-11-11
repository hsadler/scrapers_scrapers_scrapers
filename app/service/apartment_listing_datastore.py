import json
from pathlib import Path
import config.scrape_config as scrape_config


class ApartmentListingDatastore():


    # SAMTRYGG
    
    @staticmethod
    def save_samtrygg_data(id_to_listing, filepath):
        # store to json file
        with open(filepath, "w") as f:
            json_string = json.dumps(id_to_listing, indent=2, sort_keys=True)
            f.write(json_string)

    @staticmethod
    def load_samtrygg_data(filepath):
        file = Path(filepath)
        if file.is_file():
            # load from json file
            with open(filepath) as f:
                return json.load(f)
        else:
            return {}

