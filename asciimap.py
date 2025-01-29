import numpy as np

class MapExplorer:
    def __init__(self, size=100):
        self.size = size
        self.map = np.full((size, size), ' ')
        # Start in the middle of the map
        self.current_pos = [size // 2, size // 2]
        self.mark_position()
        
    def mark_position(self):
        self.map[self.current_pos[0], self.current_pos[1]] = '@'
        
    def draw_path(self, direction):
        pathsMove = {
            'n': {'move': (-2, 0)},
            's': {'move': (2, 0)},
            'e': {'move': (0, 2)},
            'w': {'move': (0, -2)},
            'ne': {'move': (-2, 2)},
            'sw': {'move': (2, -2)},
            'nw': {'move': (-2, -2)},
            'se': {'move': (2, 2)}
        }
        pathsSymbol = {
            'n': {'symbol': '|', 'move': (-1, 0)},
            's': {'symbol': '|', 'move': (1, 0)},
            'e': {'symbol': '-', 'move': (0, 1)},
            'w': {'symbol': '-', 'move': (0, -1)},
            'ne': {'symbol': '/', 'move': (-1, 1)},
            'sw': {'symbol': '/', 'move': (1, -1)},
            'nw': {'symbol': '\\', 'move': (-1, -1)},
            'se': {'symbol': '\\', 'move': (1, 1)}
        }
        
        if direction in pathsMove:
            pathMove = pathsMove[direction]
            pathSymbol = pathsSymbol[direction]
            new_pos_symbol = [
                self.current_pos[0] + pathSymbol['move'][0],
                self.current_pos[1] + pathSymbol['move'][1]
            ]
            new_pos_move = [
                self.current_pos[0] + pathMove['move'][0],
                self.current_pos[1] + pathMove['move'][1]
            ]
            
            # Check if the new position is within bounds
            if (0 <= new_pos_move[0] < self.size and 
                0 <= new_pos_move[1] < self.size):
                # Draw the path
                self.map[self.current_pos[0], self.current_pos[1]] = 'o'
                
                currentSymbol = self.map[
                    self.current_pos[0] + pathSymbol['move'][0],
                    self.current_pos[1] + pathSymbol['move'][1]
                    ]
                if currentSymbol == currentSymbol == 'X':
                    self.map[
                        self.current_pos[0] + pathSymbol['move'][0],
                        self.current_pos[1] + pathSymbol['move'][1]
                        ] = 'X'
                elif currentSymbol == '\\' and pathSymbol['symbol'] == '/':
                    self.map[
                        self.current_pos[0] + pathSymbol['move'][0],
                        self.current_pos[1] + pathSymbol['move'][1]
                        ] = 'X'
                elif currentSymbol == '/' and pathSymbol['symbol'] == '\\':
                    self.map[
                        self.current_pos[0] + pathSymbol['move'][0],
                        self.current_pos[1] + pathSymbol['move'][1]
                        ] = 'X'
                else:
                    self.map[
                        self.current_pos[0] + pathSymbol['move'][0],
                        self.current_pos[1] + pathSymbol['move'][1]
                        ] = pathSymbol['symbol']
                self.current_pos = new_pos_move
                self.mark_position()
                return True
        return False
    
    def display_map(self):
        # Find the bounds of the explored area
        explored_rows = np.where(self.map != ' ')[0]
        explored_cols = np.where(self.map != ' ')[1]
        
        if len(explored_rows) == 0 or len(explored_cols) == 0:
            return
        
        # Add padding of 1 around the explored area
        min_row = max(0, explored_rows.min() - 1)
        max_row = min(self.size, explored_rows.max() + 2)
        min_col = max(0, explored_cols.min() - 1)
        max_col = min(self.size, explored_cols.max() + 2)
        
        # Print only the explored area with padding
        for row in range(min_row, max_row):
            print(''.join(self.map[row, min_col:max_col]))

# Example usage
def explore_map():
    explorer = MapExplorer()
    
    while True:
        explorer.display_map()
        direction = input("\nEnter direction (n/ne/e/se/s/sw/w/nw) or 'q' to quit: ").lower()
        
        if direction == 'q':
            break
            
        if not explorer.draw_path(direction):
            print("Invalid move! Stay within bounds and use valid directions.")

if __name__ == "__main__":
    explore_map()
