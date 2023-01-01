#####################
# Sadomasochism Cup #
#####################

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt


#App basic config
st.set_page_config(page_title="Sadomasochism Golf Cup",
                    page_icon=":bar_chart:",
                    )

st.header('Sadomasochism Cup')
st.write('Welcome to the stats page for the Sadomasochism Cup.'
        ' Here you will find stats and statistics for each player, which will be updated throughout the tournament.'
        ' We will be using a more lenient variation of the stableford scoring system to determine the tournament winner '
        'however this page will also be displaying stroke score stats for each participating player. This is for information only.')


st.subheader('Scoring')
scoring = ('Stableford scoring system is as follows:<br>'
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
#st.write(full_stats)
#st.write(full_with_stableford)

player_scores = full_with_stableford.loc[:,['player_id','score','stableford_score']].groupby(by=['player_id'],as_index=False).sum()
player_scores = player_scores.sort_values(by=['stableford_score'], ascending=False)
player_scores.set_axis(['Player ID','Stroke Score', 'Stableford Score'], axis='columns', inplace=True)
ps2 = player_scores.set_index('Player ID', append=False)
st.subheader('Tournament Table')
st.dataframe(ps2, use_container_width=True)

#Select box for the course names
course_names = pd.DataFrame(full_stats.loc[:,['course_name']].sort_values(by=['course_name'],ascending=True)).drop_duplicates().reset_index(drop=True)
course_names = course_names['course_name'].values.tolist()
course_var = st.selectbox('Select a course to for hole specific averages:',course_names[:])

#Select box for the round dates
round_dates = pd.DataFrame(full_stats.loc[full_stats['course_name'] == course_var, ['round_date']]).drop_duplicates().reset_index(drop=True)
round_dates = round_dates['round_date'].values.tolist()
datebox=st.selectbox('Which date would you like scores from?', round_dates[:])

#Select box for player id
player_select = pd.DataFrame(full_stats.loc[:,['player_id']]).drop_duplicates().reset_index(drop=True)
player_select = player_select['player_id'].values.tolist()
player_box=st.selectbox('Which date would you like scores from?', player_select[:])

#Fig 2 - Stableford and stroke score for each player for each hole on specified course and date.
st.subheader('Individual Round Stats')
round_par = pd.DataFrame(full_with_stableford.loc[(full_with_stableford['course_name'] == course_var) & (full_stats['round_date'] == datebox) & (full_stats['player_id'] == player_box), ['player_id','course_name','par','score','stableford_score','hole_number']])
#st.write(round_par)
fig5_par = alt.Chart(round_par).mark_bar(size=10,color='grey').encode(
    x = 'hole_number', y = 'par'
)
fig5_score = alt.Chart(round_par).mark_line(size=5,color='pink').encode(
    x = 'hole_number', y=alt.Y('score',title='score')
)
fig5_stableford = alt.Chart(round_par).mark_bar(size=5,color='orange').encode(
    x = 'hole_number', y =alt.Y('stableford_score',title='score')
)
fig_5_layer = alt.layer(fig5_par, fig5_score, fig5_stableford).resolve_axis(
    y = 'independent'
).configure(autosize=alt.AutoSizeParams(resize=True))
st.altair_chart(fig_5_layer, use_container_width=True)
