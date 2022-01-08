'''
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
data = pd.read_csv("graph.xlsx", index_col=0)
G = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,3)
nx.draw(G, with_labels=False)
plt.show()

print(data)
'''
import pandas as pd
import networkx as nx
import pylab as plt

df = pd.read_excel (r'graph.xlsx', index_col=False, header=0) #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df_s = df.set_index('place')
print (df_s)



A=df_s.to_numpy()
H=nx.from_numpy_matrix(A)
nx.draw(H)
plt.show()