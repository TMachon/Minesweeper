
# PySweeper, a python minesweeper

## Description

Yet another Minesweeper terminal game, made with python, currently in 1.0

## Sources

* [magmax](https://github.com/magmax) / **[python-inquirer](https://github.com/magmax/python-inquirer)**
* [voronind](https://github.com/voronind) / **[range-regex](https://github.com/voronind/range-regex)**

## Todo

 * [ ] TUI with selectable individual cases
 * [ ] Mouse implementation in TUI
 * [ ] Bomb generation after the first click

## Exemple

    $ py minesweeper.py 
    [?] Select difficulty: Novice
     > Novice
       Easy
       Medium
       Hard
       Impossible
    
    [?] Select width (between 5 and 50): 5
    [?] Select height (between 5 and 50): 5
    
        1   2   3   4   5  
      ┼───┼───┼───┼───┼───┤
     1│ □ │ □ │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     2│ □ │ □ │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     3│ □ │ □ │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     4│ □ │ □ │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     5│ □ │ □ │ □ │ □ │ □ │
      ┴───┴───┴───┴───┴───┘
    
    [?] Select a row for your next move: 1
    [?] Select a column for your next move: 1
    
        1   2   3   4   5  
      ┼───┼───┼───┼───┼───┤
     1│   │ 1 │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     2│   │ 1 │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     3│ 2 │ 2 │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     4│ □ │ □ │ □ │ □ │ □ │
      ┼───┼───┼───┼───┼───┤
     5│ □ │ □ │ □ │ □ │ □ │
      ┴───┴───┴───┴───┴───┘
    [?] Select a row for your next move: 
    
*Théo Machon 2020*
