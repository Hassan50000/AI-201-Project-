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
          print("Error {} : ".format(e) )
            
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
    'S':('A','D'),
    'A':('B','C'),
    'D':('B','E'),
    'B':('C','E'),
    'E':('G'),
    'C':('G')
}

print(Graph)

Cost = {
    ('S','A'):3,
    ('S','D'):2,
    ('A','B'):5,
    ('A','C'):10,
    ('B','C'):2,
    ('B','E'):1,
    ('D','E'):4,
    ('D','B'):1,
    ('C','G'):4,
    ('E','G'):3
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
                
print(list(dfs_paths(Graph, 'S','G')))



print("The individual / possible paths of Depth first Search from start node to goal are : \n ")

paths_dfs = list(dfs_paths(Graph, 'S', 'G'))
for i in paths_dfs:
    temp=0
    
    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp=temp + Cost[(i[j],i[j+1])]

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
                
                
                
print(list(bfs_paths(Graph, 'S','G')))

print("The individual / possible paths of Breadth first Search from start node to goal are : \n ")

paths_bfs = list(bfs_paths(Graph, 'S', 'G'))


for i in paths_bfs:
    temp=0
    
    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp=temp + Cost[(i[j],i[j+1])]

    print(temp)
    print("\n")
    
print("Expanded nodes are : ",dfs_expended(Gp, 'A', 'G'))     

print("Expanded nodes are : ",bfs_expended(Gp, 'A', 'G'))   

print("The path using breadth first search is : ")

y=list(dfs_paths(Gp, 'F', 'G'))

print(y)

# FINDING Cost of possible paths 

def ucs_path(graph,cost,start,goal):
    queue = []
    solution_cost=[]
    queue.append([0, start])
 
    visited = {}
 
    while (len(queue) > 0):
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] =p[0]*-1
 
        if (p[1] == goal):
            visited[p[1]]=[k for k,v in graph.items() if p[1] in v]
            solution_cost=p[0]
            break
        queue = sorted(queue)
 
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                if graph[p[1]][i] not in visited:
                    queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
                    path=[k for k,v in graph.items() if p[1] in v]
        visited[p[1]] = path
    solution = set([v[0] for v in visited.values() if len(v)>0]) | set('G')
    return solution, solution_cost



print(ucs_path(Graph,Cost,'S','G'))
print("PATH WITH ITS COST: ", ucs_path(graph,Hurestics,'S','G'))

    
def ucs(graph, start,goal):
     visited, pqueue = [], [(0,start)]
     while pqueue:
         vertex = pqueue.pop(0)
         if vertex[1] not in visited:
               visited.append(vertex[1])
               temp=[l[0] for l in graph[vertex[1]] if l[0] not in visited]
               cost=[l[1]+vertex[0] for l in graph[vertex[1]] if l[0] not in visited]
               pqueue.extend(zip(cost,temp))
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

def is_seperator(dataList):
    for i in range(len(dataList)-1):
        if dataList[i] == 'is':
            return dataList[i+1]
''' file handlin code data retrieval thu voice commaands returning specific words ..... '''
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
''' FURTHER CODE ..... '''
