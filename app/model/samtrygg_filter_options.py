

class SamtryggFilterOptions():
    """
    Samtrygg filter options struct
    """

    

    def __init__(
        self,
        price_range,
        rooms_range,
        square_meters_range,
        location_blacklist,
        pets_allowed,
        washer_dryer_included,
        dishwasher_included
    ):
        self.price_range = price_range
        self.rooms_range = rooms_range
        self.square_meters_range = square_meters_range
        self.location_blacklist = location_blacklist
        self.pets_allowed = pets_allowed
        self.washer_dryer_included = washer_dryer_included
        self.dishwasher_include = dishwasher_included
