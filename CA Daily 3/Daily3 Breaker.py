import requests
import json 
import numpy as np
import pandas as pd

import statistics
from statistics import mode

from bs4 import BeautifulSoup


#Daily 3 Breaker Project by JK
def showmethemoney():
    """Calculate a probability of the 'California Daily 3 Lottery' most drawn numbers in percentage"""

    x = range(21) 

    dn_list =[] # List of Draw Number
    dd_list =[] # List of Draw Date
    w1_list = [] # List of 1st Spot Winning Numbers
    w2_list = [] # List of 2nd Spot Winning Numbers
    w3_list = [] # List of 3rd Spot Winning Numbers

    for i in x:
        i += 1
        api = "https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/9/" + str(i) + "/20" # Collecting JSON data of the past drawn numbers
        r = requests.get(api)

        soup = BeautifulSoup(r.content, 'html.parser')

        json_data = soup.prettify()
        json_object = json.loads(json_data) # <class 'dict'>

        for content in json_object.get('PreviousDraws'): # Collecting the values from json_object (JSON)

            c1 = np.array([content.get('DrawNumber')])
            c2 = np.array([content.get('DrawDate')])
            c3 = np.array([content.get('WinningNumbers')['1']['Number']])
            c4 = np.array([content.get('WinningNumbers')['2']['Number']])
            c5 = np.array([content.get('WinningNumbers')['3']['Number']])
            cc = np.hstack((c3, c4, c5))

            s = pd.Series([c1, c2, c3, c4, c5])

            dn = s[0]
            dd = s[1]
            w1 = s[2]
            w2 = s[3]
            w3 = s[4]

            for one in w1:
                w1_list.append(one)
            
            for two in w2:
                w2_list.append(two)
            
            for three in w3:
                w3_list.append(three)

            w1_numbers_count = len(w1_list)
            w2_numbers_count = len(w2_list)
            w3_numbers_count = len(w3_list)

            most_w1 = statistics.mode(w1_list)
            most_w2 = statistics.mode(w2_list)
            most_w3 = statistics.mode(w3_list)

            count_most_w1 = w1_list.count(most_w1)
            count_most_w2 = w2_list.count(most_w2)
            count_most_w3 = w3_list.count(most_w3)

    print(f"Winning Number 1 List:\n{w1_list}", "\n" * 2,
          f"Winning Number 2 List:\n{w2_list}", "\n" * 2,
          f"Winning Number 3 List:\n{w3_list}", "\n" * 2,

          "The Most Frequent Drawn Numbers:"

          f"\n1st Spot: [{most_w1}] counted: {count_most_w1}/{w1_numbers_count} Probability: {round(count_most_w1/w1_numbers_count * 100)}%", 
          f"\n2nd Spot: [{most_w2}] counted: {count_most_w2}/{w2_numbers_count} Probability: {round(count_most_w2/w2_numbers_count * 100)}%",
          f"\n3rd Spot: [{most_w3}] counted: {count_most_w3}/{w3_numbers_count} Probability: {round(count_most_w3/w3_numbers_count * 100)}%",)
    
showmethemoney()   
