import numpy as np
import pandas as pd

import streamlit as st
from index import Columns, filter_by_column, get_column


@st.cache_data
def main():
    st.markdown("# _Soil Identification and Geolocation_")
    """
    Automated System for :blue[_**Soil type Identification and Geolocation**_] using atmospheric data, python based software framework and libraries.
    """


main()

st.markdown("## 🔥 Get Records below")
district: str = st.selectbox(
    "Select District?",
    get_column(Columns.DISTRICT.value),
    index=None,
    placeholder="Select district name ...",
)

if district is not None:
    st.markdown(f"## 🚀 You selected :rainbow[{district.capitalize()}]")
    record = filter_by_column(Columns.DISTRICT.value, district)

    record

if st.checkbox("Filter By Soil Bulk Density"):
    density = st.selectbox(
        "Select Soil Bulk Density?",
        get_column(Columns.SOIL_DENSITY.value),
        index=None,
        placeholder="Select Soil Bulk Density ...",
    )

    "You selected: ", density
