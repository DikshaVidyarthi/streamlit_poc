import streamlit as st
import random

# Title and intro
st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    Just click on the buttons below and discover what you can do 
    with Streamlit. 
    """
)

# Balloons button
if st.button("Send balloons! 🎈"):
    st.balloons()

# Confetti / snow button
if st.button("Celebrate with snowflake! ❄️"):
    st.snow()

# Text input greeting
name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}! 🎉")

# Slider for mood
mood = st.slider("How's your mood today? 🤔", 0, 10, 5)
st.write(f"Your mood level is: {mood}/10")

# Checkbox to show an image
# if st.checkbox("Show a cute puppy 🐶"):
#     st.image("https://placedog.net/500/300", caption="Here's a doggo for you!")

# Selectbox for ice cream flavor
flavor = st.selectbox(
    "Pick your favorite ice cream 🍦", 
    ["Vanilla", "Chocolate", "Strawberry", "Mango"]
)
st.write(f"You chose: {flavor}")

# Random joke button
jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I’m reading a book on anti-gravity. It’s impossible to put down!"
]
if st.button("Tell me a joke 😂"):
    st.info(random.choice(jokes))

        


