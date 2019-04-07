from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(['RED', 'BLUE', 'GREEN', 'YELLOW']),
                choice(['#4CAF50', '#FFD600', '#C62828', '#3F51B5']),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        for i in shapes:
            if i['text'] == text.lower():
                shape_index = shapes.index(i)
    else:
        for i in shapes:
            if i['color'] == color:
                shape_index = shapes.index(i)
    return is_inside([x, y],shapes[shape_index]['rect'])

def is_inside(point, rect):
    return (point[0] in range(rect[0], rect[0] + rect[2] + 1)) and \
        (point[1] in range(rect[1], rect[1] + rect[3] + 1))
