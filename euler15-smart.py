from pprint import pprint


num_of_hor_cells = 20
num_of_ver_cells = 20

array = [[0 for x in range(num_of_hor_cells+1)] for x in range(num_of_ver_cells+1)]

def initalize_array(array):
    for x in range (0, num_of_ver_cells):
        array[x][num_of_hor_cells] = 1
    for y in range(0, num_of_hor_cells):
        array[num_of_hor_cells][y] = 1

def print_array(array):
    for x in range (0, num_of_ver_cells):
        for y in range(0, num_of_hor_cells):
            pprint(array[x][y])

initalize_array(array)

for x in range (num_of_ver_cells - 1 , -1, -1):
    for y in range(num_of_hor_cells - 1, -1, -1):
        print x, y
        array[x][y] = array[x+1][y] + array[x][y+1]


print(array[0][0])
