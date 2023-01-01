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

st.write('Stablesford scoring system is as follows:'
        '<ul><li> 0 Points - Double Bogey or higher</li>'
        '<li> 1 Point - Bogey</li>'
        '<li> 2 Points - Par</li>'
        '<li> 3 Points - Birdie</li>'
        '<li> 4 Points - Eagle or higher</li></ul>')
