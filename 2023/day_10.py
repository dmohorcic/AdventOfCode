from dataclasses import dataclass

import numpy as np


def check_above(row, col, arr):
    return row-1 < 0 or arr[row-1, col] not in {"F","7","S","|"}

def check_below(row, col, arr):
    return row+1 >= arr.shape[0] or arr[row+1, col] not in {"J","L","S","|"}

def check_left(row, col, arr):
    return col-1 < 0 or arr[row, col-1] not in {"F","L","S","-"}

def check_right(row, col, arr):
    return col+1 >= arr.shape[1] or arr[row, col+1] not in {"J","7","S","-"}


def remove_unconnected_pipes(arr: np.ndarray) -> int:
    changed_pipes = 0
    for j in range(arr.shape[0]):
        for i in range(arr.shape[1]):
            pipe = arr[j, i]
            if pipe == ".":
                continue
            elif pipe == "|":
                if check_above(j, i, arr) or check_below(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
            elif pipe == "-":
                if check_right(j, i, arr) or check_left(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
            elif pipe == "J":
                if check_above(j, i, arr) or check_left(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
            elif pipe == "F":
                if check_right(j, i, arr) or check_below(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
            elif pipe == "7":
                if check_left(j, i, arr) or check_below(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
            elif pipe == "L":
                if check_right(j, i, arr) or check_above(j, i, arr):
                    arr[j, i] = "."
                    changed_pipes += 1
    return changed_pipes


@dataclass
class PipePart:
    x: int
    y: int
    pipe_type: str
    distance: int
    prev_x: int = None
    prev_y: int = None

    def __repr__(self):
        return f"<PipePart x={self.x}, y={self.y}, type={self.pipe_type}, dist={self.distance}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.pipe_type == other.pipe_type

    def __hash__(self):
        return hash(str(self.x)+"-"+str(self.y)+self.pipe_type)


def trace_pipes(pipe_grid: np.ndarray):
    pipe_path: list[PipePart] = list()
    queue: list[PipePart] = list()

    (y, x) = np.where(pipe_grid == "S"); y = y[0]; x = x[0]
    start_pipe = PipePart(x, y, "S", 0)
    pipe_path.append(start_pipe)

    # check where next
    if x+1 < pipe_grid.shape[1] and pipe_grid[y, x+1] in {"J", "-", "7"}: # right
        queue.append(PipePart(x+1, y, pipe_grid[y, x+1], 1, start_pipe.x, start_pipe.y))
    if x-1 >= 0 and pipe_grid[y, x-1] in {"L", "-", "F"}: # left
        queue.append(PipePart(x-1, y, pipe_grid[y, x-1], 1, start_pipe.x, start_pipe.y))
    if y-1 >= 0 and pipe_grid[y-1, x] in {"F", "|", "7"}: # up
        queue.append(PipePart(x, y-1, pipe_grid[y-1, x], 1, start_pipe.x, start_pipe.y))
    if y+1 < pipe_grid.shape[0] and pipe_grid[y+1, x] in {"J", "|", "L"}: # down
        queue.append(PipePart(x, y+1, pipe_grid[y+1, x], 1, start_pipe.x, start_pipe.y))
    
    assert len(queue) == 2

    while len(queue):
        cpipe = queue.pop(0)
        if cpipe in pipe_path:
            continue
        pipe_path.append(cpipe)
        
        pipe_type = cpipe.pipe_type
        dir_x = cpipe.x - cpipe.prev_x
        dir_y = cpipe.y - cpipe.prev_y

        nx, ny = 0, 0
        if pipe_type == "|":
            if dir_y > 0: # down
                nx = cpipe.x
                ny = cpipe.y+1
            else: # up
                nx = cpipe.x
                ny = cpipe.y-1
        elif pipe_type == "-":
            if dir_x > 0: # right
                nx = cpipe.x+1
                ny = cpipe.y
            else: # left
                nx = cpipe.x-1
                ny = cpipe.y
        elif pipe_type == "F":
            if dir_x: # down
                nx = cpipe.x
                ny = cpipe.y+1
            else: # right
                nx = cpipe.x+1
                ny = cpipe.y
        elif pipe_type == "J":
            if dir_x: # up
                nx = cpipe.x
                ny = cpipe.y-1
            else: # left
                nx = cpipe.x-1
                ny = cpipe.y
        elif pipe_type == "L":
            if dir_x: # up
                nx = cpipe.x
                ny = cpipe.y-1
            else: # right
                nx = cpipe.x+1
                ny = cpipe.y
        elif pipe_type == "7":
            if dir_x: # down
                nx = cpipe.x
                ny = cpipe.y+1
            else: # left
                nx = cpipe.x-1
                ny = cpipe.y

        npipe = PipePart(nx, ny, pipe_grid[ny, nx], cpipe.distance+1, cpipe.x, cpipe.y)
        queue.append(npipe)

    return pipe_path


def check_enclosed_area(pipe_grid: np.ndarray):
    area = 0
    for j, row in enumerate(pipe_grid):
        inside = False
        prev_pipe = ""
        for elem in row:
            if elem == "." and inside:
                area += 1
                prev_pipe = ""
            # we directly go in/out
            elif elem == "|":
                inside = not inside
                prev_pipe = ""
            # potential in/out with F-- and L--
            elif elem == "F":
                prev_pipe = "F"
            elif elem == "L":
                prev_pipe = "L"
            # in/out with F--J
            elif elem == "J":
                if prev_pipe == "F":
                    inside = not inside
                prev_pipe = ""
            # in/out with L--7
            elif elem == "7":
                if prev_pipe == "L":
                    inside = not inside
                prev_pipe = ""
            # - can be ignored
        if inside:
            print(j, "problem")
    return area

def main():
    
    pipe_grid = list()
    with open("2023/day_10.in", "r") as file:
        pipe_grid = [[x for x in line.strip()] for line in file]
    pipe_grid = np.array(pipe_grid)

    """ # remove all pipes that are not connected
    num_of_removed = remove_unconnected_pipes(pipe_grid)
    while num_of_removed:
        num_of_removed = remove_unconnected_pipes(pipe_grid)
    
    with open("2023/day_10.debug", "w", encoding="utf8") as file:
        for line in pipe_grid:
            string = "".join(line)+"\n"
            string = string.replace("|", "║").replace("-", "═")\
                           .replace("F", "╔").replace("7", "╗")\
                           .replace("L", "╚").replace("J", "╝")
            file.write(string) """
    pipe_path = trace_pipes(pipe_grid)

    # task 1
    print(pipe_path[-1].distance)

    # task 2
    # keep only path pipes
    new_pipe_grid = np.full(pipe_grid.shape, ".", dtype=np.dtype('<U1'))
    for pipe in pipe_path:
        new_pipe_grid[pipe.y, pipe.x] = pipe_grid[pipe.y, pipe.x]
    pipe_grid = new_pipe_grid

    # check area
    area = check_enclosed_area(pipe_grid)
    print(area)

if __name__ == "__main__":
    main()
