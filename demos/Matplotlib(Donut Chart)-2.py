import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
import random
%matplotlib notebook





plt.figure(figsize=(15,10))
sections=[
'Red Lights',
'Layout, constructions, equipment, and utensils',
'Housekeeping, cleaning, and waste practices',
'Food storage condition and practices, temperature control practices',
'People, personal hygiene practice, good hygienic practices, knowledge and competence',
'Pest prevention and control',
'HACCP based food safety manegement system and controls, supplier assurance, allergen information, traceability, incidents & complaints'
]
failures = [random.randint(1, 14) for _ in range(len(sections))]


wedges, texts,val= plt.pie(failures, wedgeprops=dict(width=0.5), autopct='%1.0f%%',pctdistance=1.1,startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")
plt.title("Audit Fails By section (this location)",fontsize=15,weight='bold')
plt.legend(wedges, sections,
          loc="upper center",
           bbox_to_anchor=(0.5, -0.00),
          fancybox=True)
plt.savefig('Donut.png', bbox_inches='tight')