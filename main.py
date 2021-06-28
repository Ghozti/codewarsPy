from KYU6.kyu6 import Highest_Rank
from KYU6.kyu6 import MazeRunner

x = MazeRunner()

print(x.maze_run(
        [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E","W","W"]))

