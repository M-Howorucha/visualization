'''
The following code is the code from the learning session on June 1, 2026
Everything until the next multiline comment is the code from this session.

I'm sorry for using a standard python file instead of a juypter notebook... 
I just prefer using a .py file. 
To make this a little easier, you can uncomment the lines for each session, and 
run them instead of the whole file? 
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import PIL
import scipy
import requests

np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0,100,50)

fig,ax = plt.subplots(figsize = (5,3))
ax.scatter(x,y)
plt.show()

fig,ax = plt.subplots(figsize = (5,3))
ax.bar(x,y)

fig,ax = plt.subplots(figsize = (5,3))
ax.plot(x,y)


fig,ax = plt.subplots(figsize = (5,3))
ax.plot(x,y)

font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

ax.set_title('Total growth over time', fontdict=font1)
ax.set_xlabel('Years since start', fontdict=font2)
ax.set_ylabel('Total growth', fontdict=font2)

fig.tight_layout()
plt.show()



fig,ax = plt.subplots(figsize = (5,3))

font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

ax.plot(x,
        y,
        marker='*',
        color='indigo', 
        linestyle='--',
        linewidth=2)

ax.set_title('Total growth over time')
ax.set_xlabel('Years since start')
ax.set_ylabel('Total growth')

fig.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,
        y,
        marker = '*',
        color = 'indigo',
        linestyle = '--', 
        linewidth = 2,
        markersize = 14, # size of the data point
        markeredgecolor = '#fa9359', # edge of the data point marker
        markerfacecolor = '#000000') # fill of the marker
fig.show()

'''
Below is the code for the learning session on June 3, 2026
'''

# libraries and data
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
df=pd.DataFrame({'x_values': range(1,101), 'y_values': np.random.randn(100)*15+range(1,101), 'z_values': (np.random.randn(100)*15+range(1,101))*2 })

# Plot 1
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1)
ax1.plot( 'x_values', 'y_values', data=df, marker='o', alpha=0.4)

# Plot 2
ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1)
ax2.plot( 'x_values','z_values', data=df, marker='o', color="grey", alpha=0.3)

# Plot 3
ax3 = plt.subplot2grid((2, 2), (0, 1), rowspan=2)
ax3.plot( 'x_values','z_values', data=df, marker='o', color="orange", alpha=0.3)

# Show the graph
plt.show()

# Comments:
# I think this visualization satisfies most qualities of a good visualization. 
# It is clear, concise, The use of different colors on the different plots helps
# to differentiate them. The layout is also well-organized, with the three plots 
# arranged in a clean way. The different axes for the left plots are a little 
# misleading with roughly twice the growth in the bottom plot compared to the top, 
# while they visually appear to be similar. 
# Overall, I think this is a good visualization.

'''
This is the code for the learning session on June 8, 2026
'''

np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y, label='y')
ax.plot(x,y2, label='y2')
ax.legend(loc='lower right',
          bbox_to_anchor = (1, 1),
          frameon=True,
          fontsize=12,
          ncol =2,
          shadow=True,
          facecolor='white',
          edgecolor='black'
          )
plt.show()


fig, ax = plt.subplots()
ax.axis([0,10,0,10])
ax.text(1,5,".Data:(1,5)", transform=ax.transData)
ax.text(0.5,0.1,".Data:(0.5,0.1)", transform=ax.transAxes)
ax.text(0.2,0.2,".Data:(0.2,0.2)", transform=fig.transFigure)

plt.show()


np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y, label='y')
ax.scatter(x,y2, label='y2')
ax.legend(loc='lower right')
ax.annotate('This is important!', 
            xy=(10,95),
            xytext=(20,94), 
            arrowprops=dict(facecolor='black'))

# ax.yaxis.set_major_locator(plt.NullLocator())
# ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.xticks(rotation=45, ha='right')

plt.show()

np.random.seed(613)
font1 = {'family'  : 'sans-serif',
         'color'   : 'blue'}
x = np.arange(50)
y = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y, label='Person 1')
ax.scatter(x,y2, label='Person 2')
ax.legend(loc='lower right')

plt.xlabel('Shiny new X Axis', fontsize = 18, fontdict=font1)

plt.show()


np.random.seed(613)
font1 = {'family'  : 'sans-serif',
         'color'   : 'blue'}
x = np.arange(50)
y = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y, label='Person 1')

plt.show()

'''
Below is the code from the learning session on June 10, 2026
'''

np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0,75,50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110,180,240,99,220])

fig, ax = plt.subplots(figsize=(5,3))

fig,(ax1,ax2) = plt.subplots(ncols=2,
                             nrows=1,
                             figsize=(7,3))

ax1.scatter(x1,y1, color='tab:blue')
ax2.bar(x2,y2, color='tab:orange')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_title('Scatter Plot')
ax2.set_xlabel('Characters')
ax2.set_ylabel('Power Level')
ax2.set_title('Bar Plot')

fig.tight_layout()
plt.show()



fig,(ax1,ax2) = plt.subplots(ncols=2,
                             nrows=1,
                             figsize=(7,3))
ax1.scatter(x1,y1)
ax1.annotate("This is some text", 
             xy=(10,40), 
             xytext=(20,50), 
             arrowprops=dict(facecolor='black'))

ax2.bar(x2,y2, color='tab:orange')

fig.tight_layout()
plt.show()


fig, someaxes = plt.subplot_mosaic([['ax1','ax3'], ['ax2', 'ax3']], figsize=(7,4))

someaxes['ax1'].scatter(x1,y1)
someaxes['ax1'].set_title('Scatter Plot')
someaxes['ax2'].bar(x2,y2, color='tab:orange')
someaxes['ax2'].set_title('Bar Plot')
someaxes['ax3'].plot(x1,y1, color='tab:blue')


fig.tight_layout()
plt.show()

x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110,180,240,99,220])
y2 = np.array([170,100, 90, 120, 50])

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(x,y1, color = 'indigo')

ax.plot(x,y2, color='red')
fig.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(7,3))
y2_std = np.std(y2)
ax.plot(x,y2,color='red')
ax.errorbar(x,y2, yerr=y2_std, fmt='none', ecolor='indigo',elinewidth=4, capsize=5)
fig.tight_layout()
plt.show()


from PIL import Image
import requests
from io import BytesIO

url = "https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "image/*,*/*;q=0.8",
    "Referer": "https://en.wikipedia.org/"
}

response=requests.get(url,headers=headers)
image_file=BytesIO(response.content)
image=Image.open(image_file)


x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110,180,240,99,220])
y2 = np.array([170,100, 90, 120, 50])


fig, ax = plt.subplots(figsize=(7,3))
ax.plot(x,y2,color='red')
ax_image = fig.add_axes([0.1,0.11,0.15,0.35])
ax_image.imshow(image)
ax_image.axis('off')
fig.tight_layout()
plt.show()
 
'''
This is the code for the learning session on June 15, 2026
'''

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import PIL
import requests
import os
tips = sns.load_dataset('tips')

print(tips)

sns.lineplot(data=tips, 
             x='total_bill',
               y='tip')

sns.set_style('whitegrid')
tipgraph = sns.lineplot(data=tips,
                x='total_bill',
                y='tip')
tipgraph.set(title='Tips vs. Total Bill ',
                   xlabel = 'Total Bill ($)',
                   ylabel = 'Tip Amount ($)')

plt.show()

fig = plt.subplots(figsize=(10,3))
tipgraph = sns.lineplot(data=tips,
                x='total_bill',
                y='tip', 
                color='hotpink',
                linestyle='--',
                linewidth=3,
                marker='o',
                markerfacecolor='indigo')

plt.show()


tipgraph = sns.scatterplot(data=tips,
                           x='total_bill',
                           y='tip',
                           style='time', hue='day',
                           palette = ['purple','hotpink','deepskyblue','yellowgreen'])

tipgraph.set(title='Tips vs. Total Bill ',
             xlabel = 'Total Bill ($)',
             ylabel = 'Tip Amount ($)')

plt.show()



sns.pairplot(data=tips,
                hue='day')

plt.show()



daysplot = sns.relplot(data=tips,
                x='total_bill',
                y='tip',
                hue='sex',
                col='day',
                kind='scatter',
                col_wrap=2)


plt.show()


import plotly.graph_objects as go

x1 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110,180,240,99,220])


graph = go.Figure()
graph.add_trace(go.Bar(x=x1, y=y1))

graph.update_layout(title="Pirate Scores",
                    xaxis_title="Pirates",
                    yaxis_title="Scores")

graph.show()

graph = go.Figure()
graph.add_trace(go.Scatter(x=x1,y=y1,mode='markers', marker = dict(size=15, color='hotpink')))
graph.update_layout(title='Pirate Scores',
             xaxis_title='Pirates',
             yaxis_title='Scores',
             width=500,
             height=500)

graph.show()

from wordcloud import WordCloud
direc = 'C:\\Users\\micha\\Documents\\DSI\\visualization\\02_activities\\assignments'
df = pd.read_csv(direc + "\\movie_quotes.csv")
# print(df)

text = " ".join(each for each in df.quote)

wordcloud = WordCloud(background_color='white',colormap='inferno').generate(text)


fig, ax = plt.subplots(figsize=(7,3))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')


from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
A = set(["apple","banana", "watermelon"])
B = set(["pumkin", "blueberry", "apple", 'key lime'])

diagram = venn2_unweighted([A,B], 
                           set_labels=('Fruits', 'Pies'),
                           set_colors=("blue", "red"),
                           alpha=0.5)

diagram.get_label_by_id("10").set_text("\n".join(A - B))
diagram.get_label_by_id("11").set_text("\n".join(A & B))
diagram.get_label_by_id("01").set_text("\n".join(B - A))

plt.show()






