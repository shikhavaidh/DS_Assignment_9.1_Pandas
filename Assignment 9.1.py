
# coding: utf-8

# In[36]:

#Assignment 9.1
#Consider a DataFrame df where there is an integer column 'X':
#df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer).
#These values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.

#Approach 1 using Pandas
import pandas as pd
s = pd.Series([7, 2, 0, 3, 4, 2, 5, 0, 3, 4])
#print(s)
df = pd.DataFrame({'Series':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#print(df)
df['Output']=(s.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()
#lst1 = (s.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()
print("Result Approach 1: ")
df   


# In[38]:

#Approach 2 using for loop
import pandas as pd
lst=[7,2,0,3,4,2,5,0,3,4]
ctr=0
index=0
df = pd.DataFrame(columns=('Series', 'Output'))
for j in lst:   
    
    if j==0:
        ctr=0
    else:    
        ctr+=1
   
    #lstdisp.append(ctr)
    df.loc[index] = [j,ctr]
    index+=1 
df


# In[ ]:



