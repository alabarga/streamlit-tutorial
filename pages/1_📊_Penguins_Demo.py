import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go


# st.title()- to set the title
# st.text() to write the description for the particular graph
# st.markdown() to display text as markdown
# st.latex() to display the mathematical expressions in the dashboard.
# st.write() helps to display everything such as plotly graph, dataframe, functions, model, etc.
# st.sidebar() is used for displaying data on the sidebar.
# st.pyplot() show the visualization
# st.dataframe() to display the data frame
# st.map() to display the map in just a single line code etc


st.set_page_config(page_title="Palmer's penguins EDA", page_icon=":penguin:", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title('Penguins')
st.markdown('Explore the penguins dataset')

st.sidebar.title('Visualization Selector')
st.sidebar.markdown('Select the Charts/Plots accordingly:')

@st.cache_data
def load_data():
    """ Utility function for loading the penguins dataset as a dataframe."""
    df = sns.load_dataset('penguins')

    return df

# load dataset
data = load_data()

# checkbox widget
checkbox = st.sidebar.checkbox("Reveal data.")

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

# create scatterplots
st.sidebar.subheader("Scatter plot setup")

numeric_columns = data.select_dtypes(['number']).columns

# add select widget
select_x = st.sidebar.selectbox(label='X axis', options=numeric_columns)
select_y = st.sidebar.selectbox(label="Y axis", options=numeric_columns)

# add select widget
color = st.sidebar.radio(
     "Color by",
     data.select_dtypes(['object']).columns)


col1, col2 = st.columns(2)

with col1:
    sns.relplot(data=data, x=select_x, y=select_y, hue=color)
    st.pyplot(plt.gcf())

with col2:
    sns.catplot(data=data, x=color, y=select_x, kind='box')
    st.pyplot(plt.gcf())
    
c = alt.Chart(data).mark_circle().encode(
    x=select_x, y=select_y, size='body_mass_g', color=color)

st.altair_chart(c, use_container_width=True)
