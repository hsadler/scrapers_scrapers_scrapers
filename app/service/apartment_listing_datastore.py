import config.scrape_config as scrape_config


class ApartmentListingDatastore():


    # SAMTRYGG
    
    @staticmethod
    def set_samtrygg_data(id_to_listing):
        # store to json file
        with open(scrape_config.SAMTRYGG_DATASTORE_FILEPATH, "w") as f:
            json_string = json.dumps(id_to_listing, indent=2, sort_keys=True)
            f.write(json_string)

    @staticmethod
    def get_samtrygg_data():
        # stub
        pass

    