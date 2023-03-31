# import module
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# Title
st.title("Hello Irohackers!!!")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a text")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

# Display Images

img = "https://ml.globenewswire.com/Resource/Download/739a0114-4c0d-4a18-b85e-b53982324cbc?size=3"


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi select box
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')

# Button
# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if (st.button("About")):
    st.text("Welcome To the creative IT system")

# Text Input
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if (st.button('Submit')):
    result = name.title()
    st.success(result)
    print(result)



# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

date = st.date_input("Pick a date")
st.text('Date: {}'.format(date))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

data = pd.DataFrame({'a': np.random.randint(0,3,100)})

st.markdown('## Streamlit plots')
st.bar_chart(data['a'].value_counts())

st.markdown('## Seaborn plots')

sns.countplot(x=data['a'])
st.pyplot(plt.gcf())

st.markdown('## Altair plots')
import altair as alt

c = alt.Chart(data).mark_bar().encode(x='a', y='count()')

st.altair_chart(c, use_container_width=True)

st.markdown('## Maps')

@st.cache_data
def mapa():
    df = pd.read_csv('https://analisi.transparenciacatalunya.cat/api/views/9aju-tpwc/rows.csv')

    return df.rename(columns={'Latitud':'lat', 'Longitud':'lon'}).drop([501,318])

st.map(mapa())
