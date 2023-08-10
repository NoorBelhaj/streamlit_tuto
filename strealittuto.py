import streamlit as st
import time
st.write("Hello ,let's learn how to build a streamlit app together")

# st.title ("this is the app title")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# st.checkbox('yes')
# st.button('Click')
# st.radio('Pick your gender',['Male','Female'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)

# st.number_input('Pick a number', 0,10)
# st.text_input('Email address')
# st.date_input('Travelling date')
# st.time_input('School time')
# st.text_area('Description')
# st.file_uploader('Upload a photo')
# st.color_picker('Choose your favo rite color')


# This code uses the Streamlit library to create some interactive elements in a web application.
# • The first line st.balloons() displays a fun animation of balloons on the screen.
# • The second line st.progress(10) creates a progress bar that is 10% complete.
# • The third line with st.spinner('Wait for it...'): time.sleep(10) creates a spinner animation with the message "Wait for it..." and then pauses the program for 10 seconds using the time.sleep() function.
# • The with statement is used to ensure that the spinner animation is displayed during the entire 10-second pause.
st.balloons() 
st.progress(10) 
with st.spinner('Wait for it...'):
    time.sleep(5)

# st.success("You did it !")
# st.error("Error")
# st.warnig("Warning")
# st.info("It's easy to build a streamlit app")
# st.exception(RuntimeError("RuntimeError exception"))  


# Add content to the main area
st.title('Main Area Content')
st.write('This is the main content of the web application.')

# Add content to the sidebar
st.sidebar.title('Sidebar Content')
st.sidebar.write('This is the sidebar content.')


# • It then generates an array of 20 random numbers using NumPy's random.normal() function with a mean of 1 and a standard deviation of 2.
# • Next, it creates a histogram of the random numbers using Matplotlib's hist() function with 15 bins.
# • The resulting histogram is stored in a fig object and the ax object is used to manipulate the plot.
# • Finally, the st.pyplot() function from Streamlit is used to display the histogram in the Streamlit app.
import matplotlib.pyplot as plt
import numpy as np 
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


# • It then creates a Pandas DataFrame df with 10 rows and 2 columns, where the values are randomly generated using np.random.randn().
# • The columns are labeled 'x' and 'y'.
# • Finally, the code uses st.line_chart() from the streamlit library to display a line chart of the DataFrame df.
# • The line chart shows the relationship between the 'x' and 'y' columns.
import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)

import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)

import pandas as pd
import numpy as np
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)

#  it creates a DataFrame called df using pandas.
# • The DataFrame has 500 rows and 3 columns, with random values generated using numpy.
# • The columns are named 'x', 'y', and 'z'.
# • Next, it creates an altair chart called c using the df DataFrame.
# • The chart is a scatter plot with circles (mark_circle()) and the x-axis is the 'x' column, the y-axis is the 'y' column, the size of the circles is determined by the 'z' column, and the color of the circles is also determined by the 'z' column.
# • The tooltip shows the values of 'x', 'y', and 'z' for each circle.
# • Finally, the altair chart is displayed using streamlit with the st.altair_chart() function.
# • The use_container_width=True argument ensures that the chart is displayed at the full width of the container.
import numpy as np
import pandas as pd 
import altair as alt
df = pd.DataFrame(   np.random.randn(500, 3),   columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)


#  The code then uses the graphviz_chart function from the Streamlit library to create a directed graph using the Graphviz syntax.
# • The graph has four nodes: "Big_shark", "Tuna", "Mackerel", and "Small_fishes", with arrows indicating the direction of the relationships between them.
# • The code then displays the graph in the Streamlit app.
import streamlit as st
import graphviz as graphviz
import graphviz as graphviz
st.graphviz_chart('''    digraph {        
                  Big_shark -> Tuna        
                  Tuna -> Mackerel        
                  Mackerel -> Small_fishes        
                  Small_fishes -> Shrimp    }''')


# It then creates a pandas DataFrame called df with 500 rows and 2 columns, where the values are randomly generated using numpy's randn function.
# • The values are then divided by [50, 50] and added to the coordinates [37.76, -122.4] to create a set of latitude and longitude coordinates for San Francisco.
# • The columns are labeled 'lat' and 'lon'.
# • Finally, the st.map function from the streamlit library is used to display the coordinates on a map.
import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)



