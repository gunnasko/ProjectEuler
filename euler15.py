import numpy
import random
import copy
from pprint import pprint

num_of_hor_cells = 3
num_of_ver_cells = 3

point_array = numpy.zeros((num_of_hor_cells+1, num_of_ver_cells+1))
crawler = [[0 for x in range(2)] for x in range(1)]
crawler[0][0] = 0
crawler[0][1] = 0
print crawler
no_route_left = False

def go_right(current_point, array):
    (num_of_rows, num_of_columns) = array.shape
    x = current_point[0][0]
    y = current_point[0][1]
    if y + 1 < num_of_columns:
        array[x][y] = 1
        current_point[0][1] = y + 1
        array[x][y+1] = 2
        return True
    else:
        return False

def go_down(current_point, array):
    (num_of_rows, num_of_columns) = array.shape
    x = current_point[0][0]
    y = current_point[0][1]
    if x + 1 < num_of_rows:
        array[x][y] = 1
        current_point[0][0] = x + 1
        array[x+1][y] = 2
        return True
    else:
        return False


def print_array(array):
    print numpy.array_str(array)

def last_point(current_point):
    x = current_point[0][0]
    y = current_point[0][1]
    if x >= num_of_hor_cells and y >= num_of_ver_cells:
        return True
    else:
        return False


route = []
unique_routes = []
traversed = True

while no_route_left == False:
    assert not route or type(route[0]) == list
    if traversed == True:
        route.append(copy.deepcopy(crawler))

    turn = random.randint(0,1)
    #print_array(point_array)
    traversed = False
    if turn == 0:
        traversed = go_right(crawler, point_array)
    else:
        traversed = go_down(crawler, point_array)

    #print_array(crawler)
    if last_point(crawler):
        route.append(copy.deepcopy(crawler))

        new_route = True
        if route not in unique_routes:
            unique_routes.append(route)
            #print_array(point_array)
            print len(unique_routes)

        route = []
        point_array = numpy.zeros((num_of_hor_cells+1, num_of_ver_cells+1))
        point_array[0][0] = 2;
        crawler[0][0] = 0
        crawler[0][1] = 0
