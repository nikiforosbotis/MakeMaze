#A program that implements the Make Maze algorithm.
#Author: Nikiforos Botis
#Date: March 2015

import sys
import random
sys.setrecursionlimit(10000)
n = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]
input_seed = sys.argv[4]
output_file = sys.argv[5]
n = int(n)
x = int(x)
y = int(y)
visited = []
random.seed(input_seed)

def DFS(x,y):
    if((x,y)) not in visited:
        visited.append((x,y))
    #t1, t2, t3, t4 are tuples which declare the possible neighbours
    #in order to facilitate the creation of neighbouring_list.
    t1 = ((x + 1), y)
    t2 = (x, (y + 1))
    t3 = ((x - 1), y)
    t4 = (x, (y - 1))
    #This loop creates the neighbouring_list based on the position of the node (x,y)
    if((x == 0) and (y == 0)):
        neighbouring_list = [t1, t2]
    elif (x == (n - 1) and y == 0):
        neighbouring_list = [t3, t2]
    elif (y == 0):
        neighbouring_list = [t1, t3, t2]
    elif (y == (n - 1) and x == 0):
        neighbouring_list = [t4, t1]
    elif (x == 0):
        neighbouring_list = [t2, t4, t1]
    elif (x == (n - 1) and y == (n - 1)):
        neighbouring_list = [t4, t3]
    elif (x == (n - 1)):
        neighbouring_list = [t3, t2, t4]
    elif (y == (n - 1)):
        neighbouring_list = [t4, t3, t1]
    else:
        neighbouring_list = [t3, t1, t2, t4]
    #The mixed neigbouring_list is called random_neighbours
    random_neighbours = random.sample(neighbouring_list, len(neighbouring_list))
    i = 0
    #While the neighbour that is examined belongs to the visited list (i.e. we have not visited it yet)
    #and we do not the list's capaciy, then proceed to the next neighbour.
    while((random_neighbours[i] in visited) and (i < (len(random_neighbours) - 1 ))):
        i = i + 1
    x, y = random_neighbours[i]
    #The recursive call of DFS
    if(len(visited) < (n * n)):
        DFS(x,y)

#The first call of DFS with the user's input for (x,y)
DFS(x,y)
print(visited)

with open(output_file, 'w') as f:
    i = 0
    total = 1
    while(total < (len(visited))):
        while(i < 2):
            if(i == 0):
                f.write(str(visited[total - 1]))
            if(i == 1):
                f.write(', ')
                f.write(str(visited[total]))
            i = i + 1
        total = total + 1
        i = 0
        f.write('\n')
f.close()
