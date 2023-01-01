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
        '<ul><li><strong>0 Points</strong> - Triple Bogey or higher</li>'
        '<li><strong>1 Point</strong> - Double Bogey</li>'
        '<li><strong>2 Points</strong> - Bogey</li>'
        '<li><strong>3 Points</strong> - Par </li>'
        '<li><strong>4 Points</strong> - Birdie or higher</li></ul>')

st.markdown(scoring,unsafe_allow_html=True) 

#Main data source
full_stats = pd.read_csv('https://raw.githubusercontent.com/charlesvarthur/Golf_Tournament/main/cup_full_stats.csv')
#st.write(full_stats.head(5))

#Figure 1 - Leaderboard Table
stableford = []
for rows in full_stats['score_vs_par']:
    if rows >= 3:
        stableford.append(0)
    elif rows == 2:
        stableford.append(1)
    elif rows == 1:
        stableford.append(2)
    elif rows == 0:
        stableford.append(3)
    elif rows <= int('-1'):
        stableford.append(4) 


full_with_stableford = pd.DataFrame(full_stats)
full_with_stableford['stableford_score'] = stableford
#st.write(full_with_stableford)


player_scores = full_with_stableford.loc[:,['player_id','score','stableford_score']].groupby(by=['player_id']).sum()
player_scores.rename(columns = {'stableford_score':'Stableford Score','score':'Score'}, inplace = True)
player_scores = player_scores.sort_values(by=['stableford_score'], ascending=False)


st.subheader('League Table')
st.write(player_scores)
