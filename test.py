import plotly

# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np

py.sign_in('untitled_3212', '8v2pyr7o5x')

#stream_ids = tls.get_credentials_file()['stream_ids']
#stream_id = stream_ids[0]

# Make instance of stream id object 
"""
stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

trace1 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream         # (!) embed stream id, 1 per trace
)

data = Data([trace1])

# Add title to layout object
layout = Layout(title='Time Series')

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='s7_first-stream')


# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
s = py.Stream(stream_id)

# (@) Open the stream
s.open()
"""

# (*) Import module keep track and format current time
import datetime
import time
import random

i = 0    # a counter
k = 5    # some shape parameter
N = 200  # number of points to be plotted

# Delay start of stream by 5 sec (time to switch tabs)
#time.sleep(5)


import plotly.plotly as py
import plotly.graph_objs as go

arr=['7:00', '8:00', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W']

base = datetime.datetime.today()
hoursOpen=24
date_list = [base - datetime.timedelta(hours=x) for x in range(0, hoursOpen)]
for idx, val in enumerate(date_list):
	date_list[idx]=date_list[idx].replace(hour=(idx+7)%24, minute=0, second=0)
pairArr=map(lambda t: t.hour,date_list)

import pprint

pprint.pprint(pairArr)

values=[[random.uniform(10, 33) for x in range(hoursOpen)]]
for _ in xrange(2):
	orig=values[-1] #get the previous numbers
	new_list=[values[-1][x]+random.uniform(10, 30) for x in range(hoursOpen)]
	values.append(new_list)

sumsSoFar=[100 for j in xrange(hoursOpen)]
values.append(sumsSoFar)
values=values[::-1]

amounts=[]
data=[]
colours=['rgb(255,255,255)','rgb(0,100,0)','rgb(139,26,26)', 'rgb(139,69,19)']
names=['Not In Use',"Free Weights","Cardio", "Bench"]
for i in xrange(4):
	data.append(go.Area(
				    r=values[i],
				    t=date_list,
				    name=names[i],
				    marker=dict(
				        color=colours[i]
				    )
				    ))

layout = go.Layout(
    title='Wind Speed Distribution in Laurel, NE',
    font=dict(
        size=10
    ),
    radialaxis=dict(
        ticksuffix='%'
    ),
    orientation=270
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='polar-area-chart')


"""
while True:
    i += 1   # add to counter

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

    # (-) Both x and y are numbers (i.e. not lists nor arrays)

    # (@) write to Plotly stream!
    s.write(dict(x=x, y=y))

    # (!) Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot (more in 7.2).

    time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting

# (@) Close the stream when done plotting

"""
#s.close()