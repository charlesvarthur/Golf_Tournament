#####################
# Sadomasochism Cup #
#####################

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt


st.header('Sadomasochism Cup')
st.write('Welcome to the stats page for the Sadomasochism Cup.'
        ' Here you will find stats and statistics for head player, which will be updated throughout the tournament.')


scoring = ('Stablesford scoring system is as follows:<br>'
        '<ul><li><strong>0 Points</strong> - Double Bogey or higher</li>'
        '<li><strong>1 Point</strong> - Bogey</li>'
        '<li><strong>2 Points</strong> - Par</li>'
        '<li><strong>3 Points</strong> - Birdie</li>'
        '<li><strong>4 Points</strong> - Eagle or higher</li></ul>')

st.markdown(scoring,unsafe_allow_html=True) 

#Main data source
full_stats = pd.DataFrame('https://raw.githubusercontent.com/charlesvarthur/Golf_Tournament/main/cup_full_stats.csv')
st.write(full_stats.head(5))

#Figure 1 - Leaderboard Table
