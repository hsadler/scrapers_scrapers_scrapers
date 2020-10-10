import config.scrape_config as scrape_config


class ApartmentListingProcessing():
    
    @staticmethod
    def filter_samtrygg_listings(listings, filter_options):
        filtered_listings = []
        for listing in listings:
            if (
                listing.get_price() >= filter_options.price_range[0] and 
                listing.get_price() <= filter_options.price_range[1]
            ):
                filtered_listings.append(listing)
        return filtered_listings

    @staticmethod
    def rank_samtrygg_listings(listings, rank_options):
        # stub
        return listings
