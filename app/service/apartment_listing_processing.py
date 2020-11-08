from model.samtrygg_filter_options import SamtryggFilterOptions
from model.samtrygg_rank_options import SamtryggRankOptions


class ApartmentListingProcessing():
    
    
    @staticmethod
    def filter_samtrygg_listings(listings, filter_options):
        # TODO: filtering NOT currently implemented:
            # washer_dryer_included
            # dishwasher_included
        filtered_listings = []
        for listing in listings:
            if (
                listing.get_price() >= filter_options.price_range[0] and 
                listing.get_price() <= filter_options.price_range[1] and 
                listing.get_rooms() >= filter_options.rooms_range[0] and
                listing.get_rooms() <= filter_options.rooms_range[1] and
                listing.get_sq_meters() >= filter_options.square_meters_range[0] and
                listing.get_sq_meters() <= filter_options.square_meters_range[1] and
                listing.get_pets_allowed() == filter_options.pets_allowed and
                listing.get_city() in filter_options.city_whitelist
            ):
                filtered_listings.append(listing)
        return filtered_listings

    
    @staticmethod
    def rank_samtrygg_listings(listings, rank_options):
        # stub
        return listings

    
    @staticmethod
    def get_processed_listings(listings, processing_config):
        pc = processing_config
        # instantiate filter options struct
        filter_options = SamtryggFilterOptions(
            price_range=(pc.price_min, pc.price_max),
            rooms_range=(pc.rooms_min, pc.rooms_max),
            square_meters_range=(pc.sq_meters_min, pc.sq_meters_max),
            city_whitelist=pc.city_whitelist,
            pets_allowed=pc.pets_allowed,
            washer_dryer_included=pc.washer_dryer_included,
            dishwasher_included=pc.dishwasher_included
        )
        # filter the listings
        filtered_listings = ApartmentListingProcessing.filter_samtrygg_listings(
            listings,
            filter_options
        )
        # instantiate rank options struct
        rank_options = SamtryggRankOptions(
            listing_freshness_weight=pc.listing_freshness_weight,
            price_per_square_meter_weight=pc.price_per_square_meter_weight,
            optimal_room_amount_and_weight=pc.optimal_room_amount_and_weight,
            favorite_locations_and_weight=pc.favorite_locations_and_weight,
            is_furninshed_and_weight=pc.is_furninshed_and_weight
        )
        # rank the listings
        ranked_listings = ApartmentListingProcessing.rank_samtrygg_listings(
            filtered_listings,
            rank_options
        )
        return ranked_listings
