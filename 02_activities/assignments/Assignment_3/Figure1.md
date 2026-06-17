For this visualization I utilized Python with several libraries, most uniquely
the geopandas, and contextily in order to plot geospatial data on a map. This 
visualization shows the locations of all publicly accessible water sources 
maintain by the city of Toronto, within the downtown region. The intention of 
this visualization is to have the general population use it (particularly 
tourists) which may require water and don't know where to go. Additionally, any 
unhoused individuals or people who do not have consistent access to clean water 
could use this visualization to help them source it. For this visualization I 
wanted to be intentional with colours such that it was obvious which sources 
were operational. Since green is generally seen as "good" while red is "bad" I 
wanted to utilize those colours. Since red-green colourblindness is fairly 
common, I used the "tableau" colours in Python which have better readability for 
colourblind individuals. I checked this using the online tool available at,  
https://www.color-blindness.com/coblis-color-blindness-simulator/. The 
visualization is entirely reproducible from the available dataset used, provided
the format of the .csv file containing the information does not change. I think 
several communities could be affected by this visualization, particularly those 
who live in areas with a high density of public water sources, such as along 
the lake shore or on the Toronto islands, could see an influx of people in the 
area, looking for these water sources. As mentioned previously, individuals 
who do not have access to clena water could also be positively impacted by the 
ability to locate and source clean water. There is also the possibility that 
city officials could use this visualization in order to chose where to locate 
future water sources, by identifying areas with low density such as along the 
lakeshore to the west by Ontario Place. I chose to include only a few of the 
available data types for this visualization to keep it clean and simple. Instead 
of flooding the figure with data, I chose to make it easy to interpret, while 
still conveying the message. A future iteration of this visualization 
(something I didn't have time to do but wanted to) could have a pop-up text 
box appear when the cursor hovers over a point which displays additional 
information about the source such as it's address, and the "location details" 
which contains a short but detailed description of where to find the source; 
both of which are available data types in the dataset. Many aspects of the work 
could be defined as "underwater labour". For instance the initial dataset 
contained numerous unused variables which I both needed to understand and parse 
before decided to omit them. Also, the locations in latitude and longitude 
coordinates where stored in json format, which I needed to parse into separate 
lat, and lon variables in order to input it them into the plotting feature. 

The datasource can be found here: https://open.toronto.ca/dataset/parks-drinking-fountains/
