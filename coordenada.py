class Coordenada:

    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitutude = longitude

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitutude

    def __str__(self):
        return f'{self._latitude} {self._longitutude}'
