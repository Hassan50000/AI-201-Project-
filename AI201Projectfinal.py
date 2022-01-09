# OUR AI 201 PROJECT

import pyttsx3
import gtts
from gtts import gTTS

import webbrowser as wb

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please speak anything:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("YOU HAVE SPOKEN THE TEXT  :: {}".format(text))
    except:
        print("Sorry we could not recognize what you just said speak again")

    sound = "recorded.wav"
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
          r.adjust_for_ambient_noise(source)
          print("Converting Audio To Text : ")
          audio = r.listen(source)

    try:
          print("Your Converted Audio Is : \n" + r.recognize_google(audio))

    except Exception as e:
          print("Error {} : ".format(e))

'''If you receive errors such as No module named win32com.client, No module
named win32, or No module named win32api, you will need to additionally install pypiwin32.
 pip install pyttsx3'''

    engine = pyttsx3.init()

    engine.say("welcome to MAP of GIKI... ")
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.5)
    engine.runAndWait()

    tts = gTTS(text="  TRAVELLING WITH US... ", lang='en')
    tts.save("audiofile.mp3")
    print("Your text has been converted  .. congratulations ")

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print(" Where do you want to travel..")
        audio = r.listen(source)
        print(" Pleease waitt...")

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")

        except Exception as e:
            print("Error :  " + str(e))

    with open("fileaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())


# Implementing basic bffs andd dfs through random map as an example andd testing

Graph = {
    'S': ('A', 'D'),
    'A': ('B', 'C'),
    'D': ('B', 'E'),
    'B': ('C', 'E'),
    'E': ('G'),
    'C': ('G')
}

print(Graph)

Cost = {
    ('S', 'A'): 3,
    ('S', 'D'): 2,
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('B', 'C'): 2,
    ('B', 'E'): 1,
    ('D', 'E'): 4,
    ('D', 'B'): 1,
    ('C', 'G'): 4,
    ('E', 'G'): 3
}

print(Cost)


def dfs_paths(Graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(Graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


print(list(dfs_paths(Graph, 'S', 'G')))


print("The individual / possible paths of Depth first Search from start node to goal are : \n ")

paths_dfs = list(dfs_paths(Graph, 'S', 'G'))
for i in paths_dfs:
    temp = 0

    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp = temp + Cost[(i[j], i[j+1])]

    print(temp)
    print("\n")


def bfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


print(list(bfs_paths(Graph, 'S', 'G')))

print("The individual / possible paths of Breadth first Search from start node to goal are : \n ")

paths_bfs = list(bfs_paths(Graph, 'S', 'G'))


for i in paths_bfs:
    temp = 0

    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp = temp + Cost[(i[j], i[j+1])]

    print(temp)
    print("\n")

print("Expanded nodes are : ", dfs_expended(Gp, 'A', 'G'))

print("Expanded nodes are : ", bfs_expended(Gp, 'A', 'G'))

print("The path using breadth first search is : ")

y = list(dfs_paths(Gp, 'F', 'G'))

print(y)

# FINDING Cost of possible paths


def ucs_path(graph, cost, start, goal):
    queue = []
    solution_cost = []
    queue.append([0, start])

    visited = {}

    while (len(queue) > 0):
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] = p[0]*-1

        if (p[1] == goal):
            visited[p[1]] = [k for k, v in graph.items() if p[1] in v]
            solution_cost = p[0]
            break
        queue = sorted(queue)

        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                if graph[p[1]][i] not in visited:
                    queue.append(
                        [(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])
                    path = [k for k, v in graph.items() if p[1] in v]
        visited[p[1]] = path
    solution = set([v[0] for v in visited.values() if len(v) > 0]) | set('G')
    return solution, solution_cost


print(ucs_path(Graph, Cost, 'S', 'G'))
print("PATH WITH ITS COST: ", ucs_path(graph, Hurestics, 'S', 'G'))


def ucs(graph, start, goal):
     visited, pqueue = [], [(0, start)]
     while pqueue:
         vertex = pqueue.pop(0)
         if vertex[1] not in visited:
               visited.append(vertex[1])
               temp = [l[0] for l in graph[vertex[1]] if l[0] not in visited]
               cost = [l[1]+vertex[0]
                   for l in graph[vertex[1]] if l[0] not in visited]
               pqueue.extend(zip(cost, temp))
               pqueue.sort()

        if vertex[1]==goal:
        break
    return visited
Let’s run this for the graph that we defined earlier.
ucs(graph, ‘A’, ‘G’)

# above and below code of UCS have difference, in lower one we are communicating and handling the cost as well...

def ucs(graph, COST, start, goal):
    visited, pqueue = [], [(0,start)]
    while pqueue:
        vertex = pqueue.pop(0)
        if vertex[1] not in visited:
            visited.append(vertex[1])
            if vertex[1]==goal:
                break
            temp=[l for l in graph[vertex[1]] if l not in visited]
            cost=[COST[(vertex[1],l)]+ vertex[0] for l in temp]
            pqueue.extend(zip(cost,temp))
            pqueue.sort()
    return visited
ucs(graph,cost ‘A’, ‘G’)
print(ucs(graph, Hurestics, 'S', 'G'))
    
# Trying to search things and connect with our Internet Interface .. Search queries    


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[ALEXA: searching someting or connecting to a builtin ur or map  ON google or YOUTUBE]')
    print("Please Speak Anything :")
    audio = r3.listen(source)
    
if 'ALEXA' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.google.com/'
    
    with sr.Microphone() as source:
        print("What do u want to search...:")
        audio = r2.listen(source)
    try:
        get = r2.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error generated please try again .. Thankyou")
    except sr.RequestError as e:
        print('error generated'.format(e))
        
if 'video' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.google.com/'
    
    with sr.Microphone() as source:
        print("Speak Anything and  search your problem.. TRY Again:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error generated please try again .. Thankyou")
    except sr.RequestError as e:
        print('error generated'.format(e))
''' file handlin code data retrieval thu voice commaands returning specific words ..... '''


 # In text file it is printed : 
 # Hello I wanna travel from Hostel9 to Tuc
 # Command i.e. the above line is given through audio from microphone
 # The program saves that audio in a text file and then returns only our source and destination 

 # According to my program the AI smart machine would itself automatically detect the source and destination

 # AI Assistant voice would return something like this : 
 # Your Source is Hostel9 and your destination is Tuc Thankyou for travelling with us 

def is_seperator(dataList):
    for i in range(len(dataList)-1):
        if dataList[i] == 'from':
            return dataList[i+1]
def is_seperator1(dataList):
    for i in range(len(dataList)-1):
        if dataList[i] == 'to':
            return dataList[i+1]

myFile = open('input.txt')
sentenceList = []
afterIs = []

data = myFile.readlines()
print(data)
sentenceList = []
for i in data:
    sentenceList.append(i.split(' '))
print(sentenceList)

for i in range(len(sentenceList)):
    afterIs.append(is_seperator(sentenceList[i]))


for i in afterIs:
    print(i)

# ********************************************************************

myFile = open('input.txt')
sentenceList1 = []
afterIs1 = []

data1 = myFile.readlines()
print(data1)
sentenceList1 = []
for i in data1:
    sentenceList1.append(i.split(' '))
print(sentenceList1)

for i in range(len(sentenceList1)):
    afterIs1.append(is_seperator1(sentenceList1[i]))


for i in afterIs1:
    print(i)

''' FURTHER CODE ..... '''
Hostel_9_to_tuc = [(34.068611, 72.640354),
                    (34.068138, 72.643522),
                    (34.068576, 72.645982), 
                    (34.070269, 72.647414) 
                    ]
SportComplex_to_hostel_11 = [
                    (34.067887, 72.639636),
                    (34.069456, 72.641095),
                    (34.07101128044904, 72.64084684626256)
]
Hostel_6_to_MC = [
                    (34.070220, 72.639359),
                    (34.070389, 72.641103),
                    (34.071613, 72.645029),
                    (34.071701, 72.645716),
                    (34.071411, 72.646636)
]

HOSTEL_9_TO_BRABERS = [
                    (34.068611, 72.640354),
                    (34.069616, 72.642323),
                    (34.07060208340641, 72.64304237054814),
                    (34.071211, 72.643594),
                    (34.071613, 72.645029)
    ]

INCUBATION_TO_ MOSQUE[
                    (34.071701, 72.645716),
                    (34.071613, 72.645029),
                    (34.071211, 72.643594),
                    (34.07060208340641, 72.64304237054814),
                    ([34.069616, 72.642323),
                    (34.069456, 72.641095)
]

HOSTEL_2_TO_FCSE = [
                (34.069069, 72.639464),
                (34.069145, 72.640309),
                (34.069456, 72.641095),
                (34.069616, 72.642323),
                (34.069029, 72.643294)
]
HOSTEL_2_TO_RAJU = [
                (34.069069, 72.639464),
                (34.070273, 72.640196),
                (34.07101128044904, 72.64084684626256),
                (34.071215878227676, 72.64143689337763),
                (34.072437, 72.642489),
                (34.07345831935395, 72.64888914083238),
                (34.072655, 72.644072),
                (34.070269, 72.647414)
]

import folium as f
from folium import plugins

my_map = f.Map(location=[34.06961775193662, 72.6445797253496], zoom_start=15)

f.Marker(location=[34.06839693200607, 72.64158783566288], popup="GIKI CRICKET GROUND", tooltip="CRICKET GROUND").add_to(my_map)
f.Marker(location=[34.071411, 72.646636], popup="MEDICAL CENTER", tooltip="MC").add_to(my_map)
f.Marker(location=[34.07060208340641, 72.64304237054814], popup="NEW ACADAMIC BLOCK", tooltip="ACADAMIC BLOCK").add_to(my_map)
f.Marker(location=[34.069649624581146, 72.64704224845387], popup="HBL ATM", tooltip="ATM").add_to(my_map)
f.Marker(location=[34.070685479001895, 72.64723463307139], popup="RAJU HOTEL", tooltip="RAJU").add_to(my_map)
f.Marker(location=[34.07345831935395, 72.64888914083238], popup="C TYPE RESIDENTIAL AREA", tooltip="C TYPE").add_to(my_map)

f.Marker(location=[34.072437, 72.642489], popup="FACULTY CLUB", tooltip="FACULTY CLUB").add_to(my_map)
f.Marker(location=[34.069005, 72.647229], icon=f.Icon(color="orange", icon="cloud"),popup="TUC MOSQUE", tooltip="TUC MOSQUE").add_to(my_map)
f.Marker(location=[34.071211, 72.643594], icon=f.Icon(color="red", icon="cloud"),popup="LIBRARY", tooltip="LIBRARY").add_to(my_map)
f.Marker(location=[34.072655, 72.644072], icon=f.Icon(color="red", icon="cloud"),popup="Helipad", tooltip="Giki helipad").add_to(my_map)
f.Marker(location=[34.069296, 72.644957], icon=f.Icon(color="black", icon="cloud"),popup="FME", tooltip="FME").add_to(my_map)
f.Marker(location=[34.069882, 72.643959], icon=f.Icon(color="red", icon="cloud"),popup="Audi", tooltip="Audi").add_to(my_map)
f.Marker(location=[34.069616, 72.642323], icon=f.Icon(color="black", icon="cloud"),popup="FES", tooltip="FES").add_to(my_map)
f.Marker(location=[34.070118, 72.645633], icon=f.Icon(color="black", icon="cloud"),popup="FCME", tooltip="FCME").add_to(my_map)
f.Marker(location=[34.068576, 72.645982], icon=f.Icon(color="red", icon="cloud"),popup="Guest House", tooltip="Guest House").add_to(my_map)
f.Marker(location=[34.070269, 72.647414], icon=f.Icon(color="red", icon="cloud"),popup="TuckShop", tooltip="TuckShop").add_to(my_map)
f.Marker(location=[34.069029, 72.643294], icon=f.Icon(color="black", icon="cloud"),popup="FCSE", tooltip="FCSE").add_to(my_map)
f.Marker(location=[34.069456, 72.641095], icon=f.Icon(color="red", icon="cloud"),popup="StudentMasjid", tooltip="StudentMasjid").add_to(my_map)
f.Marker(location=[34.068300, 72.641663], icon=f.Icon(color="red", icon="cloud"),popup="Sports Ground", tooltip="Sports Ground").add_to(my_map)
f.Marker(location=[34.067887, 72.639636], icon=f.Icon(color="red", icon="cloud"),popup="Sports Complex", tooltip="Sports Complex").add_to(my_map)
f.Marker(location=[34.068491, 72.639453], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 10", tooltip="Hostel 10").add_to(my_map)
f.Marker(location=[34.068611, 72.640354], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 9", tooltip="Hostel 9").add_to(my_map)
f.Marker(location=[34.069069, 72.639464], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 2", tooltip="Hostel 2").add_to(my_map)
f.Marker(location=[34.069145, 72.640309], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 1", tooltip="Hostel 1").add_to(my_map)
f.Marker(location=[34.070273, 72.640196], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 5", tooltip="Hostel 5").add_to(my_map)
f.Marker(location=[34.070220, 72.639359], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 6", tooltip="Hostel 6").add_to(my_map)
f.Marker(location=[34.069638, 72.639418], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 4", tooltip="Hostel 4").add_to(my_map)
f.Marker(location=[34.069678, 72.640319], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 3", tooltip="Hostel 3").add_to(my_map)
f.Marker(location=[34.071215878227676, 72.64143689337763],icon=f.Icon(color="purple"), popup="HOSTEL 12", tooltip="HOSTEL 12").add_to(my_map)
f.Marker(location=[34.07101128044904, 72.64084684626256],icon=f.Icon(color="purple"), popup="HOSTEL 11", tooltip="HOSTEL 11").add_to(my_map)
f.Marker(location=[34.070389, 72.641103],icon=f.Icon(color="purple"), popup="HOSTEL 8", tooltip="HOSTEL 8").add_to(my_map)
f.Marker(location=[34.068138, 72.643522], icon=f.Icon(color="red", icon="cloud"),popup="Admin Block", tooltip="Admin Block").add_to(my_map)
f.Marker(location=[34.071033, 72.653838], icon=f.Icon(color="red", icon="cloud"),popup="Market", tooltip="Market").add_to(my_map)
f.Marker(location=[34.065350, 72.660956], icon=f.Icon(color="red", icon="cloud"),popup="RVC Jamia Masjid", tooltip="RVC Jamia Masjid").add_to(my_map)
f.Marker(location=[34.071613, 72.645029], icon=f.Icon(color="black", icon="cloud"),popup="Brabers", tooltip="Brabers").add_to(my_map)
f.Marker(location=[34.071701, 72.645716], icon=f.Icon(color="orange", icon="cloud"),popup="Incubator", tooltip="Incubator").add_to(my_map)

# f.Marker(location=[],icon=f.Icon(color="orange", icon="cloud"), popup=" Clock Tower", tooltip="C TYPE").add_to(my_map)

my_map
