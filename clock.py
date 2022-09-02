from datetime import datetime
from math import sin, cos, pi
from time import sleep
import os

class Time:

    """
        This is a component for handling time
    """

    def __init__(self,hour=0,minute=0,second=0):

        if hour > 23 or minute > 59 or second > 59:
            raise ValueError("Invalid time, Out of range")

        self._hour = hour
        self._minute = minute
        self._second = second

    def seconds(self,degree=True):
        angle = self._second

        if degree:
            angle = int((angle/60)*360)

        return angle

    def minutes(self,degree=True):
        angle = self._minute + (self._second/60)

        if degree:
            angle = int((angle/60)*360)

        return angle


    def hours(self, degree=True):

        minutes = self.minutes(degree=False)
        angle = self._hour + (minutes/60)

        if degree:
            angle = int((angle/12)*360)%360

        return angle

    def __str__(self):
        hour, morning = (self._hour - 12, False) if self._hour > 12 else (self._hour, True)
        return f"{hour}:{self._minute}:{self._second} {'AM' if morning else 'PM'}"


class Grid:

    """
    This is for four quadrants in a graph to plot the clock in terminal

    Here x,y represent the 4 qudrant of the graph.
        x = True and y = True 1st quadrant    [A -> All]
        x = True and y = False 2nd quadrant   [S -> Sin]
        x = False and y = False 3rd quadrant  [T -> Tan]
        x = False and y = True 4th quadrant   [C -> Cosec]
    """

    def __init__(self,x,y,size):
        self._x_quadrant = x
        self._y_quadrant = y

        if x:
            self._quadrant = 'A' if y else 'S'
        else:
            self._quadrant = 'C' if y else 'T'

        self._grid = [[' ' for _ in range(size)] for _ in range(size)]


    def __str__(self):
        grid = ''
        for row in self._grid:
                grid = grid + ''.join(row) + '\n'

        return grid


class Clock:

    """
    The main widget to render the clock
    It creates 4 grids to create a graph where it later plots the clock needles.

    def __init__(self,radius):  -> radius is the size of the clock
    """

    def __init__(self,time=None,radius=10,padding=0):

        if not time:
            now = datetime.now()
            time = Time(now.hour, now.minute, now.second)

        self.time = time
        self.radius = radius
        self.A = Grid(x=True,y=True,size=radius+padding)
        self.S = Grid(x=True,y=False,size=radius+padding)
        self.C = Grid(x=False,y=True,size=radius+padding)
        self.T = Grid(x=False,y=False,size=radius+padding)

    @staticmethod
    def degree_to_radians(degree):
        return degree * (pi/180)

    @staticmethod
    def transpose_matrix(matrix,turns=1):
        for _ in range(turns):
            matrix = [[matrix[col][row] for col in range(len(matrix))][::-1] for row in range(len(matrix))]
        return matrix

    def _plot_hour(self):
        hour_angle = self.time.hours()
        grid,transpose_times = (self.A,3) if hour_angle < 91 else (self.S,4) if hour_angle <181 \
                else (self.T,1) if hour_angle < 271 else (self.C,2)
        for radii in range(self.radius):
            radian = Clock.degree_to_radians(hour_angle%90)
            x, y = round(radii*sin(radian)),round(radii*cos(radian))
            grid._grid[x][y] = '█'

        return grid,grid._quadrant,transpose_times

    def _plot_minute(self):
        minute_angle = self.time.minutes()
        grid,transpose_times = (self.A,3) if minute_angle < 90 else (self.S,4) if minute_angle <180 \
                else (self.T,1) if minute_angle < 270 else (self.C,2)

        for radii in range(self.radius):
            radian = Clock.degree_to_radians(minute_angle%90)
            x, y = round(radii*sin(radian)),round(radii*cos(radian))
            grid._grid[x][y] = '■'

        return grid,grid._quadrant,transpose_times

    def _plot_seconds(self):
        second_angle = self.time.seconds()
        grid,transpose_times = (self.A,3) if second_angle < 90 else (self.S,4) if second_angle <180 \
                else (self.T,1) if second_angle < 270 else (self.C,2)

        for radii in range(self.radius):
            radian = Clock.degree_to_radians(second_angle%90)
            x, y = round(radii*sin(radian)),round(radii*cos(radian))
            grid._grid[x][y] = '.'

        return grid,grid._quadrant,transpose_times

    def __str__(self):

        s_grid,s_name,st= self._plot_seconds()
        m_grid,m_name,mt= self._plot_minute()
        h_grid,h_name,ht = self._plot_hour()

        rotation = dict()
        rotation[s_name] = s_grid,st
        rotation[m_name] = m_grid,mt
        rotation[h_name] = h_grid,ht

        for grid,turns in rotation.values():
            grid._grid = Clock.transpose_matrix(grid._grid,turns)


        matrix = ''
        for row_C,row_A in zip(self.C._grid,self.A._grid):
            matrix += ' '.join(row_C) + ''.join(row_A) + '\n'

        for row_T,row_S in zip(self.T._grid,self.S._grid):
            matrix += ' '.join(row_T) + ''.join(row_S) + '\n'

        return matrix


if __name__ == "__main__":
    while(True):
        os.system('clear')
        c = Clock()
        print(c)
        sleep(1)
