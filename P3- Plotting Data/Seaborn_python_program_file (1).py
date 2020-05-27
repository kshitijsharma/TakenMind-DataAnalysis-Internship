import pandas as pd

import seaborn as sns

dframe = pd.read_csv('f2m_ratios.csv')
Table_1 = pd.pivot_table(dframe, values="Ratio", index="Age", columns="Year")
Image = sns.heatmap(Table_1).get_figure().savefig("Ratio_study.png", cmap="YlGnBu")
