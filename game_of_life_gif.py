from game_of_life import GameOfLife
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class GameOfLifeFrameGenerator:
    def __init__(self, input_grid, num_frames, num_rows=10, num_cols=10):
        self.curr_frame = 0
        self.num_frames = num_frames
        self.gameboard = GameOfLife(input_grid)
        self.num_rows = num_rows
        self.num_cols = num_cols

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_frame += 1
        if self.curr_frame < self.num_frames:
            self.gameboard.advance_state()
            return self.gameboard.output_grid(self.num_rows, self.num_cols)
        raise StopIteration

    def advance_frame(self):
        self.gameboard.advance_state()

    def get_grid(self):
        # print(self.gameboard.output_grid(self.num_rows, self.num_cols))
        return self.gameboard.output_grid(self.num_rows, self.num_cols)


def frame_test(grid):
    from helper import game_of_life_colormap as cmap

    num_minutes = 10
    rotten = GameOfLifeFrameGenerator(grid, num_minutes)
    for idx, img in enumerate(rotten):
        plt.imshow(img, cmap=cmap)
        plt.title(f"{idx} ticks")
        plt.axis('off')
        plt.show()


def RottenGIF(grid, file_name, num_rows, num_cols):
    from helper import game_of_life_colormap as cmap

    num_minutes = 600
    rotten = GameOfLifeFrameGenerator(grid, num_minutes, num_rows, num_cols)

    fig = plt.figure()
    # plt.xlim([0, 10])
    # plt.ylim([0, 10])
    ax = plt.axes()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    im = plt.imshow(rotten.get_grid(), interpolation='none', cmap=cmap)

    def animate(idx):
        if idx == 0:
            fig.suptitle(f'Day Zero')
            im.set_array(rotten.get_grid())
            return [im]
        else:
            fig.suptitle(f'Day {idx}')
            rotten.advance_frame()
            im.set_array(rotten.get_grid())
            return [im]

    anim = FuncAnimation(fig, animate, frames=num_minutes, interval=100)
    anim.save(file_name, dpi=100, writer='ffmpeg')
    # plt.show()


def random_grid(x_dim, y_dim):
    import random
    p_alive = .99
    grid = [[0 for _ in range(x_dim)] for _ in range(y_dim)]
    for j in range(x_dim):
        for i in range(y_dim):
            rand_float = random.uniform(0, 1)
            if rand_float < p_alive:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # frame_test(test_grid)
    import os
    path = os.getcwd() + "\\output"

    num_rows = 125
    num_cols = 125
    grid = random_grid(num_rows, num_cols)
    print("Generating MP4")
    RottenGIF(grid, path + "\\rotteno.mp4", num_rows, num_cols)
    print("Generating GIF")
    os.system(f"ffmpeg -y -i {path}\\rotteno.mp4 {path}\\rotteno.gif")

