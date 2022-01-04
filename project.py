import pandas as pd
import folium as f
from pandas.core import indexing
graph = pd.read_excel("graph.xlsx")
# print(graph)
g = pd.DataFrame(graph)
print(g[:2])
m = f.Map(location=[40.06, -105.30],
               tiles='Stamen Terrain', 
               zoom_start = 13)