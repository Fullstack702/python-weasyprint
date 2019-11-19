import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
%matplotlib notebook


data=[91.0, 90.0, 91.0, 96.0, 84.0, 68.0, 78.0, 85.0, 85.0, 86.0]
questions=['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10']

key=[]
for i in questions:
    l=i
    k='Question'+str(i.replace('#',''))
    if len(i)==3:
        key.append(l+' : '+k)
    else:
        key.append(l+'   : '+k)
        
        
plt.figure(figsize=(15,10))
textstr = '\n'.join(key)
bar=plt.bar(x=questions,height=data,color="red")
plt.yticks(np.arange(0,max(data)+5,5))
plt.title('Failure for All Locations (Last 12 Months)',fontsize=15,weight='bold')
plt.xlabel('Question',fontsize=13)
plt.ylabel('Failures',fontsize=13)
plt.text(11, 12, textstr, fontsize=14)
plt.gca().yaxis.grid(True)
plt.gca().set_axisbelow(True)
plt.savefig('Bar(Questions).png', bbox_inches='tight')