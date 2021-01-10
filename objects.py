import random
from api import *

class Tetromino:
    
    def __init__(self, name, data):
        '''
            volume_shape : pixel number in one shape
        '''
        self.name = name
        self.color = data['color']
        self.shape = self.prepare_shape_data_as_one_tuple(data['shape'])
        self.max_rotations = len(data['shape'])
        self.current_rotation = 0 #get a random current rotation at object creation with max rotation
        self.current_top_left_position = (0,0)
        self.bottom_check = 0
        self.right_check = 0
        self.volume_shape = 16

    def prepare_shape_data_as_one_tuple(self, data):
        '''
            prepare a single tupple with the shape data and return it
        '''
        shapelist = []
        for shape in data:
            for line in range(4):
                for pixel in range(4):
                    try:
                        if shape[line][pixel] == 1:
                            shapelist.append(1)
                        else:
                            shapelist.append(0)
                    except IndexError:
                        shapelist.append(0)

        shapetuple = tuple(shapelist)
        return shapetuple

    def draw_all_position(self):
        '''
            draw all shapes in text from the tuple
        '''
        print(self.name)
        print(self.color)
        for rotation in range(self.max_rotations):
            self.start = rotation*self.volume_shape
            for pixel in range(self.volume_shape):
                print(self.shape[self.start+pixel], end='')
                if pixel%4 == 3:
                    print('')
            print('****')

    def draw(self):
        '''
            draw the shape of the current rotation
        '''
        print(self.name)
        print(self.color)
        print('position : ' + str(self.current_rotation))
        self.start = self.current_rotation*self.volume_shape
        for pixel in range(self.volume_shape):
            print(self.shape[self.start+pixel], end='')
            if pixel%4 == 3:
                print('')

    def move(self, key):
        '''
            movement
            play movement sound
        '''
        pass

    def rotate(self, rotation):
        '''
            rotation clockwise(cw) or anticlockwise(acw), get the correct
            play rotating sound
        '''
        if rotation == 'cw':
            self.current_rotation = (self.current_rotation + 1)%self.max_rotations
        elif rotation == 'acw':
            self.current_rotation = (self.current_rotation - 1)%self.max_rotations
        else:
            print('can only be clockwise(cw) or anticlockwise(acw).')

class Board:
    def __init__(self, data):
        self.width = data['size'][0]
        self.height = data['size'][1]
        self.update_surface = True

    def draw(self, surface, grid, debug):
        print('draw board')
        # draw borders
        color = 'grey'
        rectangle(surface, (0,0,grid,self.height),color)
        rectangle(surface, (grid,self.height-grid,self.width-grid,grid),color)
        rectangle(surface, (self.width-grid,0,grid,self.height-grid),color)

        if debug == True:
            self.draw_grid(surface,grid)

    def draw_grid(self, surface, grid):
        color = 'red'
        for x in range(0, self.width, grid):
            for y in range(0, self.height, grid):
                line(surface,(0,y), (self.width, y), color)
                line(surface,(x,0), (x, self.height), color)
        

class Stats:
    def __init__(self):
        self.name = 'stats'
        print('stats class')