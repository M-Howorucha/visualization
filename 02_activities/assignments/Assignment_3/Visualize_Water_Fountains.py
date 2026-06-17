import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import json
import matplotlib.patches as mpatches

# load the dataset
filename = 'Parks Drinking Fountains - 4326.csv'
direc = 'C:\\Users\\micha\\Documents\\DSI\\visualization\\02_activities\\assignments\\'

df = pd.read_csv(direc + filename)


# print(header_list)
# print(df['location'][0:5])
# print(df['type'][0:5])
# print(df['Status'][0:5]) # 0 = closed * 1 = open * 2 = service alert 
# print(df['geometry'][0])


# lat and lon are stored as json strings in the 'geometry' column. 
# We need to parse them out to create separate lat and lon arrays for plotting. 
# We also want to keep track of the status of each fountain for coloring the 
# points later.

lat = np.zeros(len(df['geometry']))
lon = np.zeros(len(df['geometry']))
status = np.zeros(len(df['geometry']))
address = np.empty(len(df['geometry']), dtype=object)
location_details = np.empty(len(df['geometry']), dtype=object)

for i in range(len(df['geometry'])):
    numbers = json.loads(df['geometry'][i])["coordinates"][0]
    lon[i] , lat[i] = numbers
    status[i] = df['Status'][i]
    address[i] = df['address'][i]
    location_details[i] = df['location_details'][i]

# Check the first few values to make sure we parsed them correctly.
print(lat[0:5])
print(lon[0:5])
print(status[0:5])
print(address[0:5])
print(location_details[0:5])

# Create dataframe for plotting
data = {
    'status': status,
    'lat': lat,
    'lon': lon,
    'address': address,
    'location_details': location_details
}

df_plot = pd.DataFrame(data)

# Create geopandas from pandas dataframe
gdf = gpd.GeoDataFrame(
    df_plot, 
    geometry=gpd.points_from_xy(x=df_plot.lon, y=df_plot.lat),
    crs="EPSG:4326" 
)

# Convert coords to Web Mercator (3857) for plotting with contextily 
# (recommended from online sources)
# This made the plot not show the right coordinates so I got rid of it, but copied
# the old gdf variable into the gdf_projected since I already wrote some 
#  of the code using that variable name.
gdf_projected = gdf.copy()#gdf.to_crs(epsg=3857) 

# create colour map for the status of the fountains
# use red and green for standard readable of "good and bad" 
# but use the "tab" color palette for colour blind purposes
color_rules = {0: 'tab:red', 1: 'tab:green', 2: 'tab:orange'}

# Map them to a new column
gdf_projected['color'] = gdf_projected['status'].map(color_rules)

# make the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the data
gdf_projected.plot(
    ax=ax, 
    color=gdf_projected['color'], # Use your mapped colors
    markersize=50, 
    edgecolor='black'
)

'''
add the hover over to see details option. 
'''

# ax.set_xlim([-79.43, -79.33]) # West to East
ax.set_xlim([-79.5, -79.3]) # West to East

ax.set_ylim([43.61, 43.68])   # South to Northn

# add  city street map background
cx.add_basemap(ax, crs=gdf.crs,source=cx.providers.CartoDB.Positron)


plt.title("Locations of Public Water Fountains in Downtown Toronto", 
          fontsize=18, 
          wrap=True)

ax.set_xlabel("Longitude", fontsize=12)
ax.set_ylabel("Latitude", fontsize=12)

# To add a legend for the colours we use the patches function from matplotlib.
open_patch = mpatches.Patch(color='tab:green', label='Open')
closed_patch = mpatches.Patch(color='tab:red', label='Closed')
service_patch = mpatches.Patch(color='tab:orange', label='Service Alert')

ax.legend(
    handles=[open_patch, closed_patch, service_patch], 
    title="Location Status",
    loc="upper left"
)
plt.tight_layout()
plt.show()