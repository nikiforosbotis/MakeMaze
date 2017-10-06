# MakeMaze

Script in Python which implements the [Depth-first search algorithm](https://en.wikipedia.org/wiki/Depth-first_search).

The script can be ran by typing the following on the command line:

```
python make_maze.py <n> <start_x> <start_y> <seed> <output_file>
```

Where:

* `n` is the number of lines and of columns of the graph's grid. It can be up to 30.
*  `start_x` is the x coordinate of the starting node,
`0 <= start_x < n`.
*  `start_y` is the y coordinate of the starting node,
`0 <= start_y < n`.
*  `seed` is a number or string which will be imported to the engine of random numbers.
*  `output_file` is the file in which the labyrinth will be stored.

For example, if the user gives:

```
python make_maze.py 10 5 5 20150206 maze_10x10.txt
```

The file in which the labyrinth will be saved will have the following form:

```
(5, 2), (6, 2)
(6, 2), (6, 1)
(6, 1), (7, 1)
(7, 1), (8, 1)
(8, 1), (8, 0)
(8, 0), (9, 0)
(9, 0), (9, 1)
(9, 1), (9, 2)
(9, 2), (9, 3)
(9, 3), (8, 3)
(8, 3), (8, 2)
...
```

Full program's description (Greek) can be found [here](https://github.com/dmst-algorithms-course/assignment-2015-1).
