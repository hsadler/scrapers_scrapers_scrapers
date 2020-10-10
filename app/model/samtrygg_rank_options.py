

class SamtryggRankOptions():
    """
    Samtrygg rank options struct
    """


    def __init__(
        self,
        listing_freshness_weight,
        price_per_square_meter_weight,
        optimal_room_amount_and_weight,
        favorite_locations_and_weight,
        is_furninshed_and_weight
    ):
        self.listing_freshness_weight = listing_freshness_weight
        self.price_per_square_meter_weight = price_per_square_meter_weight
        self.optimal_room_amount_and_weight = optimal_room_amount_and_weight
        self.favorite_locations_and_weight = favorite_locations_and_weight
        self.is_furninshed_and_weight = is_furninshed_and_weight
