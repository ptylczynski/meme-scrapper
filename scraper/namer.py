import datetime
import os
from datetime import date


class SimpleNamer:
    def __init__(self, store_location: str):
        self.store_location = store_location

    def create_name(self, input_file_name: str) -> str:
        extension = input_file_name.split('.')[-1]
        return f'{os.getcwd()}/{self.store_location}/{str(datetime.datetime.now())}.{extension}'