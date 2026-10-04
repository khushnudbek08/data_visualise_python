from pathlib import Path
import json
import plotly.express as px

# read data as string an change to python object
path = Path("eq_data/readable_eq_data.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)


# Examine all earthquicks in the dataset
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


title = "Global Earthquakes"
fig = px.scatter_map(lat=lats, lon=lons, size=mags, title=title)
fig.show()
