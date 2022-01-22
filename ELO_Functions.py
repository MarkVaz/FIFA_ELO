# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:51:07 2022

@author: MC
"""
import pandas as pd
import numpy as np

def prob_win(PlayerA,PlayerB):
    #ELO probability of winning formula
    probA = (1/(1+(10**((PlayerB-PlayerA)/400))))
    
    return probA

def new_rating(current,k,result,expected):
    #ELO new rating formula
    new_rating = current + k*(result - expected)
    
    return new_rating

def play_a_game(Winner,Loser,WinnerTR,LoserTR, dataframe):
    
    
    #assign the Winners pre-match elo to a variable
    Winners_Elo = dataframe[Winner].iloc[-1]
    #assign the Losers pre-match elo to a variable
    Losers_Elo = dataframe[Loser].iloc[-1]
    
    #calculate the winners probability to win the played match based on ELOs
    Winners_Prob = prob_win(Winners_Elo, Losers_Elo)
    #calculate the losers probability to win the played match based on ELOs
    Losers_Prob = prob_win(Losers_Elo, Winners_Elo)
    
    #A dicionary of k values to be used based on the team ratings that played.
    K_factor_dict = {'4.5':16,
                     '4':19,
                     '3.5':22,
                     '3':25,
                     '2.5':28,
                     '2':31,
                     '1.5':34,
                     '1':37,
                     '0.5':40,
                     '0':40,
                     '-0.5':40,
                     '-1':43,
                     '-1.5':46,
                     '-2':49,
                     '-2.5':52,
                     '-3':55,
                     '-3.5':58,
                     '-4':61,
                     '-4.5':64}
    #assign a variable to hold the proper k-factor based on team ratings
    k_factor = K_factor_dict[str(WinnerTR-LoserTR)]    
    
    #calculate the winner's new post match elo rating
    Winners_New_Elo = new_rating(Winners_Elo, k_factor, 1, Winners_Prob)
    
    #calulate the loser's new post match elo rating
    Losers_New_Elo = new_rating(Losers_Elo, k_factor, 0, Losers_Prob)
    
    time = pd.to_datetime('today')
    
    if Winner == 'Austin':
        if Loser == 'MC':
            new_row = {'Date':time,
                       'Austin':Winners_New_Elo,
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':Losers_New_Elo,
                       'Donovan':(dataframe['Donovan'].iloc[-1])}                        
        
        elif Loser =='Donovan':
            new_row = {'Date':time,
                       'Austin':Winners_New_Elo,
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':Losers_New_Elo}
            
        elif Loser == 'Liam':
            new_row = {'Date':time,
                       'Austin':Winners_New_Elo,
                       'Liam':Losers_New_Elo,
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':(dataframe['Donovan'].iloc[-1])}
            
        elif Loser == 'Austin':
            raise TypeError('You cannot have both selections be the same')
            
        
    elif Winner == 'MC':        
        if Loser == 'Austin':
            new_row = {'Date':time,
                       'Austin':Losers_New_Elo,
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':Winners_New_Elo,
                       'Donovan':(dataframe['Donovan'].iloc[-1])}
            
        elif Loser == 'Donovan':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':Winners_New_Elo,
                       'Donovan':Losers_New_Elo}
            
        elif Loser == 'Liam':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':Losers_New_Elo,
                       'MC':Winners_New_Elo,
                       'Donovan':(dataframe['Donovan'].iloc[-1])}

        elif Loser == 'MC':
            raise TypeError('You cannot have both selections be the same')
            
            
        
    elif Winner == 'Donovan':
        
        if Loser == 'Austin':
            new_row = {'Date':time,
                       'Austin':Losers_New_Elo,
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':Winners_New_Elo}
            
            
        elif Loser == 'MC':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':(dataframe['Liam'].iloc[-1]),
                       'MC':Losers_New_Elo,
                       'Donovan':Winners_New_Elo}
            
        elif Loser == 'Liam':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':Losers_New_Elo,
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':Winners_New_Elo}
            
        elif Loser == 'Donovan':
            raise TypeError('You cannot have both selections be the same')
        
    elif Winner == 'Liam':
        
        if Loser == 'Austin':
            new_row = {'Date':time,
                       'Austin':Losers_New_Elo,
                       'Liam':Winners_New_Elo,
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':(dataframe['Donovan'].iloc[-1])}
            
        elif Loser == 'MC':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':Winners_New_Elo,
                       'MC':Losers_New_Elo,
                       'Donovan':(dataframe['Donovan'].iloc[-1])}
            
        elif Loser == 'Donovan':
            new_row = {'Date':time,
                       'Austin':(dataframe['Austin'].iloc[-1]),
                       'Liam':Winners_New_Elo,
                       'MC':(dataframe['MC'].iloc[-1]),
                       'Donovan':Losers_New_Elo}
            
            
        elif Loser == 'Liam':
            raise TypeError('You cannot have both selections be the same')
            
    new_dataframe = dataframe.append(new_row, ignore_index = True)
    
    new_dataframe = new_dataframe.iloc[: , 1:]
    
    
    return new_dataframe

