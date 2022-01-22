# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:24:40 2022

@author: MC
"""

import pandas as pd
import ELO_Functions as elo
import streamlit as st
import altair as alt

header = st.container()
inputs = st.container()
graph = st.container()
footer = st.container()



with header:
    st.title('The Vaz Brothers Fifa Rankings!')
    st.text('')
    st.text('This project uses a custom ELO formula that takes into account team ratings')
    st.text('This custom formula uses a different k-factor depending on team ratings')
    st.text('The purpose is to determine which brother is the best at FIFA')
    st.text('')
    st.text('Instructions:')
    st.text('1. Select the Winner')
    st.text('2. Select the Loser')
    st.text('3. Team Rankings (stars)')
    st.text('4. Hit the "Calculate" button')
    
with inputs:
    
    st.title('Inputs for calculation')
    col1, col2, col3, col4 = st.columns((3,1,3,1))
    
    Players_List = ['MC','Austin','Liam','Donovan']
    Ratings_List = [5,4.5,4,3.5,3,2.5,2,1.5,1,0.5]
    
    with col1:
        Won = st.selectbox('Winner', Players_List)
        WTR = st.selectbox('Winner Team Rating',Ratings_List)
    with col3:
        Lost = st.selectbox('Loser', Players_List)
        LTR = st.selectbox('Loser Team Rating',Ratings_List)
    
    
    calculate = st.button('Calculate')
    
    Player_Data = pd.read_csv('ELO_Rankings')
    
    melted_df = Player_Data.melt(id_vars = ['Date'],
                                 value_vars = ['Austin','MC','Donovan','Liam'],
                                 var_name = 'Player',
                                 value_name = 'ELO')
    
    Chart = (alt.Chart(melted_df, width =700, height = 600)
             .mark_line()
             .configure_title(fontSize = 24)
             .configure_axis(titleFontSize = 20)
             .encode(x=alt.X("Date:T", title = 'Date'),
                     y= alt.Y("ELO:Q",title = 'ELO Rating',scale = alt.Scale(domain=(1200, 1700))),
                     color = 'Player')
             .properties(title = "Ranking over Time"))
    
    
if calculate:
    
    result = elo.play_a_game(Won, Lost, WTR, LTR, Player_Data)
    
    result.to_csv('ELO_Rankings')
    
    
    

    with graph:
    
        st.dataframe(result.drop(columns = 'Date').tail(1))
        
        #st.text('This graph shows our ELO scores over time!')
        
        #st.altair_chart(Chart)
        

    
    
    