#pip install windows-curses
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "O"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr((i+1)*2, (j+1)*3, "X", RED)
            else:
                stdscr.addstr((i+1)*2, (j+1)*3, value, BLUE)
                
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = 'O'
    end = "X"
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    
    visited = set()
    
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            rn, cn = neighbor
            if maze[rn][cn] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
            
                    
def find_neighbors(maze, row, col):
    neighbors = []
    
    if row > 0: #ARRIBA
        neighbors.append((row - 1, col))
    
    if row + 1 < len(maze): #ABAJO
        neighbors.append((row + 1, col))
        
    if col > 0: #IZQUIERDA
        neighbors.append((row, col - 1))
        
    if col + 1 < len(maze[0]): #DERECHA
        neighbors.append((row, col + 1))
        
    return neighbors


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    find_path(maze, stdscr)
    stdscr.getch()
    
wrapper(main)