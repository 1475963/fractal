# module to draw things with tkinter

from tkinter import *
import sys
import consts
import random

def getInstance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()

def sierpinski_triangle(data):
    triangles = []

    for triangle in data:
        triangles.append([triangle[0],
                          (triangle[0][0] + ((triangle[1][0] - triangle[0][0]) / 2), triangle[1][1]),
                          (triangle[0][0] + ((triangle[2][0] - triangle[0][0]) / 2), triangle[0][1] + ((triangle[2][1] - triangle[0][1]) / 2))])
        triangles.append([(triangle[0][0] + ((triangle[1][0] - triangle[0][0]) / 2), triangle[1][1]),
                          triangle[1],
                          (triangle[1][0] - ((triangle[1][0] - triangle[2][0]) / 2), triangle[1][1] + ((triangle[2][1] - triangle[1][1]) / 2))])
        triangles.append([(triangle[0][0] + ((triangle[2][0] - triangle[0][0]) / 2), triangle[0][1] + ((triangle[2][1] - triangle[0][1]) / 2)),
                          (triangle[1][0] - ((triangle[1][0] - triangle[2][0]) / 2), triangle[1][1] + ((triangle[2][1] - triangle[1][1]) / 2)),
                          triangle[2]])

    return triangles

def updateHandler(pInstance, window, data):
    print("data to process: ", data);
    for triangle in data:
        for i, point in enumerate(triangle):
            target = triangle[(i + 1) % len(triangle)]
            window.create_line(point[0], point[1], target[0], target[1], width=2, fill=random.choice(consts.TK_RDM_COLORS))
    attachUpdater(pInstance, window, sierpinski_triangle(data))


def getWindow(pInstance):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(pInstance, width=consts.TK_WIN_WIDTH, height=consts.TK_WIN_HEIGHT)
    canvas.focus_set()
    canvas.pack()
    return canvas


def attachUpdater(pInstance, pWindow, data):
    pInstance.after(consts.TK_UPDATE_TIMER, updateHandler,
                    pInstance, pWindow, data)


def attachMainloop(pInstance):
    ''' Calls Tkinter mainloop() function '''
    pInstance.mainloop()

def resetBackground(window, color):
    window.create_rectangle(0, 0, consts.TK_WIN_WIDTH, consts.TK_WIN_HEIGHT, fill=color)

def drawPoint(window, x, y, xvector, yvector, color):
    window.create_rectangle(x, y, x + xvector, y + yvector, fill=color)

# audio visualiser
def drawData(window, data):
    '''Draws the data in the canvas on the window'''
    window.create_rectangle(0, 0,
                        consts.TK_WIN_WIDTH, consts.TK_WIN_HEIGHT,
                        fill=TK_BG_COLOR)
    for sample in data:
        rescaled_sample = sample * (consts.TK_WIN_HEIGHT / 2)
        drawPoint(window, consts.TK_WIN_WIDTH / 2, consts.TK_WIN_HEIGHT / 2, 10, -rescaled_sample, consts.TK_COLOR_SKYBLUE)
