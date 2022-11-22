import pandas as pd 
import numpy as np 

data = pd.read_csv("data.csv")
data.head()

  Gender   height  weight  Index
0   male      174      96      4
1   male      189      87      2
2 female      185     110      4
3 female      195     104      3
4    ale      145      61      3

data['obese'] = (data.Index >=4).astype('int').astype('str')
data.drop('Index',axis = 1, inplace = True)

print(
  " Mal clasificados al cortar en 100kg:",
  data.loc[(data['Weight']>=100) & (data['obese']==0),:].shape[0], "\n",
  "Mal clasificados al cortar en 80kg:",
  data.loc[(data['Weight']>=80) & (data['obese']==0),:].shape[0]
)
f