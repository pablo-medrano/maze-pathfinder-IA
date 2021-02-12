import maze
import pytest

@pytest.mark.parametrize('laberinto, meta',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('maze4.txt',(1, 6)),
                          ('maze5.txt',(3, 6))
                          ])

def test_prueba(laberinto, meta):
    m = maze.Maze(laberinto)
    m.solve
    assert m.goal == meta