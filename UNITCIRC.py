from math import pi, cos, sin, radians
from ti_system import escape, wait_key
import ti_plotlib as plt

idx = 0

angles = [
    [0, "0 rad", "1", "0"],
    [30, "pi/6 rad", "sqrt(3)/2", "1/2"],
    [45, "pi/4 rad", "1/sqrt(2)", "1/sqrt(2)"],
    [60, "pi/3 rad", "1/2", "sqrt(3)/2"],
    [90, "pi/2 rad", "0", "1"],
    [120, "2pi/3 rad", "-1/2", "sqrt(3)/2"],
    [135, "3pi/4 rad", "-1/sqrt(2)", "1/sqrt(2)"],
    [150, "5pi/6 rad", "-sqrt(3)/2", "1/2"],
    [180, "pi rad", "-1", "0"],
    [210, "7pi/6 rad", "-sqrt(3)/2", "-1/2"],
    [225, "5pi/4 rad", "-1/sqrt(2)", "-1/sqrt(2)"],
    [240, "4pi/3 rad", "-1/2", "-sqrt(3)/2"],
    [270, "3pi/2 rad", "0", "-1"],
    [300, "5pi/3 rad", "1/2", "-sqrt(3)/2"],
    [315, "7pi/4 rad", "1/sqrt(2)", "-1/sqrt(2)"],
    [330, "11pi/6 rad", "sqrt(3)/2", "-1/2"],
]

def draw_unit_circle():
    points = []
    for i in range(31):
        angle = 2 * pi * i / 30
        x = cos(angle)
        y = sin(angle)
        points.append((x, y))
    for i in range(30):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        plt.line(x1, y1, x2, y2)

def update():
    a = angles[idx]
    plt.color(0, 0, 0)
    plt.text_at(11, "[" + str(idx + 1) + "/16] " + str(a[1]) + " (" + str(a[0]) + "°)", "center")
    plt.text_at(12, "(" + str(a[2]) + ", " + str(a[3]) + ")", "center")
    plt.color(255, 0, 0)
    plt.line(0, 0, cos(radians(a[0])) * 0.9, sin(radians(a[0])) * 0.9, "arrow")

def main():
    plt.cls()
    plt.color(0, 0, 0)
    plt.pen("thick", "solid")
    plt.window(-2.8, 2.8, -1.8, 1.8)
    plt.grid(1, 1, "dot")
    global idx
    draw_unit_circle()
    update()
    while not escape():
        k = wait_key()
        if k in (9, 64):
            return
        o = idx
        if k == 1:
            idx += 1
        elif k == 2:
            idx -= 1
        elif k == 143:
            idx = 10
        elif k == 144:
            idx = 12
        elif k == 145:
            idx = 14
        elif k == 146:
            idx = 8
        elif k == 148:
            idx = 0
        elif k == 149:
            idx = 6
        elif k == 150:
            idx = 4
        elif k == 151:
            idx = 2
        else:
            continue
        idx %= 16
        plt.color(255, 255, 255)
        plt.line(0, 0, cos(radians(angles[o][0])) * 0.9, sin(radians(angles[o][0])) * 0.9, "arrow")
        update()

main()
