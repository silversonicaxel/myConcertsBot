class Concert:
    def __init__(
            self,
            artists,
            date,
            venue,
            latitude,
            longitude,
            city,
            country):
        self.artists = artists
        self.date = date
        self.venue = venue
        self.latitude = str(latitude)
        self.longitude = str(longitude)
        self.city = city
        self.country = country
