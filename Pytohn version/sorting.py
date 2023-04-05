import PySimpleGUI as sg
import random
import time 

NUM_ELEMENTS = 800
GRAPH_X = 1600
GRAPH_Y = 800
BAR_WIDTH = GRAPH_X/NUM_ELEMENTS
BAR_SPACING = BAR_WIDTH
EDGE_OFFSET = 3     # offset from the left edge for first bar
GRAPH_SIZE = DATA_SIZE = (GRAPH_X, GRAPH_Y)       # size in pixels
GRAPH_ARRAY = []

sg.theme('Black')

layout = [[sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, k='-GRAPH-')],
          [sg.Button('Randomize'), sg.Button('Bubble_sort'),
           sg.Button('Insertion_sort'), sg.Button('Selection_sort'),
           sg.Button('Radix_sort')],
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
    sorted = 0
    i = 0
    while i < NUM_ELEMENTS:
        graph.erase()
        if i != NUM_ELEMENTS-1:
            if array[i]>array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                sorted = 0
            else:
                sorted += 1

        for j in range(len(array)):
            graph_value = array[j]
            if graph_value == array[i]:
                graph.draw_rectangle(top_left=(j * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(j * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='Red')
            else:
                graph.draw_rectangle(top_left=(j * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(j * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='White')

        if i == NUM_ELEMENTS-1 and sorted < NUM_ELEMENTS-1:
            sorted = 0
            i = 0
        else:
            i += 1

        window.read(timeout=0)
    
    return array.copy()

def insertion_sort(graph, array):
    for i in range(NUM_ELEMENTS+1):
        for j in reversed(range(i)):
            graph.erase()
            if j > 0:
                if array[j]<array[j-1]:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp

            for k in range(len(array)):
                graph_value = array[k]
                if graph_value == array[j]:
                    graph.draw_rectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                        bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                        fill_color='Red')
                else:
                    graph.draw_rectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                        bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                        fill_color='White')

            window.read(timeout=0)
    
    return array.copy()

def selection_sort(graph, array):
    for i in range(NUM_ELEMENTS):
        graph.erase()
        min_index = i
        for j in range(i+1, NUM_ELEMENTS):
            if array[j] < array[min_index]:
                min_index = j
        
        (array[i], array[min_index]) = (array[min_index], array[i])

        for k in range(len(array)):
            graph_value = array[k]
            if graph_value == array[i]:
                graph.draw_rectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='Red')
            else:
                graph.draw_rectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                    bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                    fill_color='White')

        window.read(timeout=1)
                

    return array.copy()

def radix_sort(graph, array):
    biggest_num = max(array)
    digits = len(str(biggest_num))

    for i in reversed(range(digits)):
        temp_array = []
        for j in range(NUM_ELEMENTS):
            string = str(array[j])
            string = string.zfill(digits)
            temp_array.append(string)
        
        zeroes = []
        ones = []
        twos = []
        threes = []
        fours = []
        fives = []
        sixes = []
        sevens = []
        eights = []
        nines = []
        misc = []

        for j in range(NUM_ELEMENTS):
            current_element = temp_array[j]
            cur_digit = current_element[i]

            if cur_digit == '0':
                zeroes.append(current_element)
            elif cur_digit == '1':
                ones.append(current_element)
            elif cur_digit == '2':
                twos.append(current_element)
            elif cur_digit == '3':
                threes.append(current_element)
            elif cur_digit == '4':
                fours.append(current_element)
            elif cur_digit == '5':
                fives.append(current_element)
            elif cur_digit == '6':
                sixes.append(current_element)
            elif cur_digit == '7':
                sevens.append(current_element)
            elif cur_digit == '8':
                eights.append(current_element)
            elif cur_digit == '9':
                nines.append(current_element)
            else:
                misc.append(current_element)

        temp_array = zeroes + ones + twos + threes + fours + fives + sixes + sevens + eights + nines + misc

        array = []
        for j in range(NUM_ELEMENTS):
            array.append(float(temp_array[j]))

        graph.erase()
        for k in range(NUM_ELEMENTS):
            graph_value = array[k]
            graph.draw_rectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                                fill_color='White')

        window.read(timeout=300)
    return array.copy()

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
        GRAPH_ARRAY = bubble_sort(graph, GRAPH_ARRAY)

    if event == "Insertion_sort":
        graph.erase()
        GRAPH_ARRAY = insertion_sort(graph, GRAPH_ARRAY)

    if event == "Selection_sort":
        graph.erase()
        GRAPH_ARRAY = selection_sort(graph, GRAPH_ARRAY)

    if event == "Radix_sort":
        graph.erase()
        GRAPH_ARRAY = radix_sort(graph, GRAPH_ARRAY)

window.close()