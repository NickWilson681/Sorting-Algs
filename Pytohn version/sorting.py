import PySimpleGUI as sg
import random
import time 

NUM_ELEMENTS = 100
GRAPH_X = 1600
GRAPH_Y = 800
BAR_WIDTH = GRAPH_X/NUM_ELEMENTS
BAR_SPACING = BAR_WIDTH
EDGE_OFFSET = 3     # offset from the left edge for first bar
GRAPH_SIZE = DATA_SIZE = (GRAPH_X, GRAPH_Y)       # size in pixels
GRAPH_ARRAY = []

sg.theme('Black')

layout = [[sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, k='-GRAPH-')],
          [sg.Button('Randomize'), sg.Button('Bubble_sort')],
        ]

window = sg.Window('Bar Graph', layout, finalize=True)

graph = window['-GRAPH-'] #type: sg.Graph

def initalize(graph, array):
    for i in range(NUM_ELEMENTS):
        graph_value = i * (GRAPH_Y/NUM_ELEMENTS)
        array.append(graph_value)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='White')
        window.read(timeout=0)

def randomize(graph, array):
    temp = []
    for i in range(NUM_ELEMENTS):
        random_i = random.randint(0, len(array) - 1)
        temp.append(array[random_i])
        graph_value = array[random_i]
        array.remove(graph_value)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='White')
        window.read(timeout=0)
    return temp.copy()
        
def bubble_sort(graph, array):
    for i in range(0, NUM_ELEMENTS):
        array.pop()
        graph.erase()
        for j in range(len(array)):
            graph_value = array[j]
            if graph_value == array[-1]:
                graph.draw_rectangle(top_left=(j * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(j * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='Red')
            else:
                graph.draw_rectangle(top_left=(j * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(j * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='White')
        
        window.read(timeout=1)

while True:
    if len(GRAPH_ARRAY) == 0:
        graph.erase()
        initalize(graph, GRAPH_ARRAY)

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Randomize":
        graph.erase()
        GRAPH_ARRAY = randomize(graph, GRAPH_ARRAY)

    if event == "Bubble_sort":
        graph.erase()
        temp = GRAPH_ARRAY.copy()
        bubble_sort(graph, GRAPH_ARRAY)
        GRAPH_ARRAY = temp.copy()

window.close()