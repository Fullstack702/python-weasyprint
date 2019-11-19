import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
%matplotlib notebook

date=['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08','2019-01-09', '2019-01-10', '2019-01-11', '2019-01-12']
data=[91.0, 90.0, 91.0, 96.0, 84.0, 68.0, 78.0, 85.0, 85.0, 86.0, 99.9, 100.0]


check=[i for i in range(len(data)) if data[i]<80]
x=np.arange(0,len(date)*2,2)


plt.figure(figsize=(15,5))
bar=plt.bar(x=x,height=data,color="orange",width=1.5)
for i in check:
    bar[i].set_color('r')
    
    
    
plt.yticks(np.arange(0,110,10))
plt.xticks(np.arange(0,24,2))
plt.title('Audit Scores Summary (Rolling last 12 audits)',fontsize=15,weight='bold',y=1.08)
plt.xlabel('Date',fontsize=13)
plt.ylabel('Audit Score',fontsize=13)
plt.gca().yaxis.grid(True)
plt.gca().set_axisbelow(True)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().set_xticklabels(date)
for i in range(len(data)):
    plt.annotate(str(data[i])+'.00%', (x[i]-0.5, data[i] * 1.02))
    
plt.savefig('Bar(Audit).png',bbox_inches='tight')

