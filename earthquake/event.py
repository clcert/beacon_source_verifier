import datetime
import hashlib


class Event:

    def __init__(self, id: str, date: str, lat: str, long: str, depth: str, magnitude: str):
        self.id = id
        self.datestr = date
        self.lat = lat
        self.long = long
        self.depth = depth
        self.magnitude = magnitude

    def get_raw_data(self) -> bytes:
        return ";".join(self.get_tuple()).encode()

    def get_tuple(self):
        return self.id, self.datestr, self.lat, self.long, self.depth, self.magnitude

    def __eq__(self, other):
        return self.get_tuple() == other.get_tuple()

    def get_marker(self) -> str:
        return hashlib.sha3_512(self.get_raw_data()).hexdigest()
