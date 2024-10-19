""" 
The Rock-Paper-Scissors Game powered by Streamlit
"""

import streamlit as st
import random

results=["You win!", "You lose!", "It's a draw!"]
rps_choice_list = ["Rock", "Paper", "Scissors"]
images = ['rock.jpg', 'paper.jpg', 'scissors.jpg']

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    st.write("## Welcome to the Rock Paper Scissors Game.")
    name = st.text_input('What is your name?', on_change=set_state, args=[2])


if st.session_state.stage >=2:
    st.write(f'Hello {name.capitalize()}!')
    computer_choice = random.randint(0, 2)
    user_choice = st.text_input(
            "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n",
            on_change=set_state, args=[3]
            )

    if user_choice is None:
        set_state(2)

if st.session_state.stage >=3:
    try:
        st.markdown(f"You chose {rps_choice_list[int(user_choice)]}:")
        #st.image(images[int(user_choice)])

        st.markdown(f"Computer chose {rps_choice_list[computer_choice]}:")
        #st.image(images[computer_choice])

        
        if int(user_choice) == 0:
            if computer_choice == 0:
                st.markdown(f"##### :orange[{results[2]}]")
            elif computer_choice == 1:
                st.markdown(f"##### :orange[{results[1]}]")
            else:
                st.markdown(f"##### :orange[{results[0]}]")
        elif int(user_choice) == 1:
            if computer_choice == 0:
                st.markdown(f"##### :orange[{results[0]}]")
            elif computer_choice == 1:
                st.markdown(f"##### :orange[{results[2]}]")
            else:
                st.markdown(f"##### :orange[{results[1]}]")
        elif int(user_choice) == 2:
            if computer_choice == 0:
                st.markdown(f"##### :orange[{results[1]}]")
            elif computer_choice == 1:
                st.markdown(f"##### :orange[{results[0]}]")
            else:
                st.markdown(f"##### :orange[{results[2]}]")

        st.button("Start Over", on_click=set_state, args=[0])

    except:
        st.markdown("#### :orange[You typed an invalid number; you lose!]")
        st.button("Start Over", on_click=set_state, args=[0])
