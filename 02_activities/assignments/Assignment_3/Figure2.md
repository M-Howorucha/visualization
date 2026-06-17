This visualization utilized Excel to create two small plots as part of one 
visualization. It shows the number of public water sources in Toronto sorted by 
type in a "donut" plot, as well as a bar graph of the percentage of each source
type that is currently operating (as of downloading the dataset). This 
visualization is intending for a more niche audience perhaps city planners, 
maintenance personnel, or other employees of the city which have a stake in 
the type abundance, and operation of these amenities. Again, I chose simple and 
clean as my primary design choices to frame my visualization. There are only 
two variables shown in this visualization which are both related, but distinctly 
different. I also chose the same colour scheme for the two plots so that the 
same type of variable is consistent across the two. As before, I made sure that 
the colours were chosen to be legible for colourblind individuals using the 
online tool at, https://www.color-blindness.com/coblis-color-blindness-simulator/.
I also chose to limit the x-axes ticks on the right plot to 0,25,50,and 100 in 
order to reduce the amount of information on the plot. In this case, the 
visualization is not reproducible by others, since I worked directly in the 
.csv file within excel that I downloaded from the City of Toronto's Open Data 
Portal. If someone wanted to reproduce this visualization, they would need the 
specific functions and methods that I used in my local copy of the file. 
However, for me, the visualization is reproducible since I have the csv file 
and the process to generate the visualizations was static (ie. no random 
variables or processes which change with time). I think the only communities 
impacted by this visualization would be those working in sectors which are 
responsible for these amenities. Since this visualization is not particularly 
useful to the general public, only those with a technical stake would likely be 
impacted. For this visualization I went through several iterations with 
different features missing. I felt that the "numeric" variables in this dataset 
where the most suitable for a visualization so I chose to create several 
variables that represent the dataset as a whole; this required a fair amount 
of "underwater labour." SInce the dataset is simply a series of rows containing 
information about individual sources, I needed to create "metadata" summarizing 
aspects of the overall dataset. In this case, I had to find all the unique 
"types" of water sources, and then use several Excel functions to count the 
number of sources matching every unique type, and well as filtering by if they 
were operating or not. An annoying bit of additional time was spent trying to 
figure out how to wrap text in the axes labels for the percentage plot on the 
right. Excel does not have a wrapping feature in their plots, you have to insert 
a newline character into the labels which I found through a stackexchange post. 
However the way I had the spreadsheet setup, this broke the unique counting 
since the dataset did not contain any labels that including newline characters. 

The datasource can be found here: https://open.toronto.ca/dataset/parks-drinking-fountains/