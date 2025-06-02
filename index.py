import os
from enum import Enum

import pandas as pd

DATASET_PATH = "dataset.xlsx"

df = pd.read_excel(DATASET_PATH)


class Columns(Enum):
    DISTRICT = "District"
    SOIL_DENSITY = "Soil Bulk Density"
    LONGITUDE = "Longitude"
    LATITUDE = "Latitude"
    SOIL = "Soil"
    COLOR = "Color"
    TEXTURE = "Texture"


def get_column(column: str) -> list:
    lst = df.get(f"{column}").to_list()

    return lst


def filter_by_column(column: str, value: str) -> pd.DataFrame:
    condition = f"{column} == '{value}'"
    record = df.query(condition)

    return record
