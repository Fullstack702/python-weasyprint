import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
%matplotlib notebook




site_A=[68.0, 81.3, 91.0, 98.0]
site_B=[100.0, 100.0, 100.0, 100.0]
site_C=[100.0, 96.0, 80.0, 64.0]
site_D=[70.0, 85.0, 85.0, 85.0]

site_names=['Site A','Site B','Site C','Site D']



y=[site_A,site_B,site_C,site_D]
x_label=site_names
x=np.arange(0,len(site_names)*2,2)

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 10),sharey=True)

fig.suptitle("Audit Score Summary (across all sites)", fontsize=16,weight='bold')
for i in range(len(y)):
    h=y[i]
    for j in range(len(y[i])):
        axes[i].bar(x[j], h[j],width=1.25)
for i in range(4):
    axes[i].yaxis.grid(True)
    axes[i].set_axisbelow(True)
    axes[i].set_xticks(np.arange(0,8,2))
    axes[i].set_xticks(np.arange(0,8,2))
    axes[i].set_xticklabels(x_label, rotation=45)
    axes[i].set_title(site_names[i],fontsize=13)
    if i==0:
        axes[i].set_ylabel('Scores',fontsize=13)
for j in range(4):    
    for i in range(len(y)):
        h=y[j]
        axes[j].annotate(str(h[i]), (x[i]-0.2, h[i] * 1.01))
        
        
fig.savefig('Bar(Audit score summary).png')