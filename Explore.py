import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title='Streamlit Title', page_icon=None, menu_items={'Get help': None, 'Report a Bug': None})

# LOAD DATA
def load_data():
    data = pd.read_csv(
        "trulia_2020.csv",
        usecols=["Longitude", "Latitude"]
    )

    return data

# FUNCTION FOR AIRPORT MAPS
def map(data, lat, lon, zoom):
    st.write(
        pdk.Deck(
            # map_style='light',
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=data,
                    get_position=['Longitude', 'Latitude'],
                    auto_highlight=True,
                    get_radius=1000,
                    get_fill_color=[180, 0, 200, 140],
                    pickable=True,
                ),
            ],
        )
    )

# CALCULATE MIDPOINT FOR GIVEN SET OF DATA
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))

# STREAMLIT APP LAYOUT
data = load_data()

# Lay out middle section of the app with maps
row2_1, row2_2 = st.columns((2,1))

zoom_level = 12
midpoint = mpoint(data["Latitude"], data["Longitude"])

map(data, midpoint[0], midpoint[1], 11)