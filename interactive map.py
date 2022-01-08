import folium as f
import pandas as pd
loc = pd.read_excel('file.xlsx')    
my_map = f.Map(location=[34.06961775193662, 72.6445797253496], tiles="Stamen Toner", zoom_start=15)
f.Marker(location=[34.069238079003156, 72.64002352470665],  popup="HOSTEL 1", tooltip="HOSTEL 1").add_to(my_map)
f.Marker(location=[34.069988284144216, 72.6403391313031], popup="HOSTEL 3", tooltip="HOSTEL 3").add_to(my_map)
f.Marker(location=[34.07101128044904, 72.64084684626256], popup="HOSTEL 11", tooltip="HOSTEL 11").add_to(my_map)
f.Marker(location=[34.070488417214335, 72.64125850704052], popup="HOSTEL 8", tooltip="HOSTEL 8").add_to(my_map)
f.Marker(location=[34.06876067227285, 72.63948836569531], popup="HOSTEL 10", tooltip="HOSTEL 10").add_to(my_map)
f.Marker(location=[34.06839693200607, 72.64158783566288], popup="GIKI CRICKET GROUND", tooltip="CRICKET GROUND").add_to(my_map)
f.Marker(location=[34.071215878227676, 72.64143689337763], popup="HOSTEL 12", tooltip="HOSTEL 12").add_to(my_map)
f.Marker(location=[34.07310270111758, 72.64220532682981], popup="FACULTY CLUB", tooltip="FACULTY CLUB").add_to(my_map)
f.Marker(location=[34.07060208340641, 72.64304237054814], popup="NEW ACADAMIC BLOCK", tooltip="ACADAMIC BLOCK").add_to(my_map)
f.Marker(location=[34.069649624581146, 72.64704224845387], popup="HBL ATM", tooltip="ATM").add_to(my_map)
f.Marker(location=[34.070685479001895, 72.64723463307139], popup="RAJU HOTEL", tooltip="RAJU").add_to(my_map)
f.Marker(location=[34.07164164111208, 72.64690757925894], popup="MEDICAL CENTER", tooltip="MC").add_to(my_map)
f.Marker(location=[34.07345831935395, 72.64888914083238], popup="C TYPE RESIDENTIAL AREA", tooltip="C TYPE").add_to(my_map)
my_map

'''for _, l in loc.iterrows():
    f.Marker(
    location=[l["latitude"], l["longitude"]], 
        popup=l['name'], 
        tooltip=l['name']
    ).add_to(my_map)
    '''