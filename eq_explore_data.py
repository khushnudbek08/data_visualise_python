from pathlib import Path
import json

# read data as string an change to python object
path = Path("eq_data/eq_1_day_m1.geojson")
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

print(mags)
print(lons)
print(lats)
# # Creat a more readable version of the data file.
# path = Path("eq_data/readable_eq_data.geojson")
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)
