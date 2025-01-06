
class TerminalScreen:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.color_mode = 0
        self.screen_data = []
        self.cursor_x = 0
        self.cursor_y = 0
        self.is_screen_initialized = False

    def setup_screen(self, width, height, color_mode):
        #initializing the screen with the given width, height and color
        self.width = width
        self.height = height
        self.color_mode = color_mode
        self.screen_data= [[' ' for  _ in range(width)] for _ in range(height)]
        self.is_screen_initialized = True
        print(f"Screen initialized: {width}x{height}, color mode: {color_mode}")

    def draw_character(self, x, y, color, char):
        #draws a character at a specific position
        if not self.is_screen_initialized:
            print("screen not initialized. the command is ignored")
            return

        if 0<= x < self.width and 0 <= y < self.height:
            self.screen_data[y][x] = chr(char)
            print(f"Character '{chr(char)}' drawn at ({x}, {y}) with color {color}.")
        else:
            print(f"Invalid coordinates ({x}, {y}). command ignored")

    def draw_line(self, x1, y1, x2, y2, color, char):
        # drawing a line between two pints using a specific character"
        if not self.is_screen_initialized:
            print("screen not initialized. command ignores!!!")
            return

        # bresenham's line algorithm for drawing
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 < self.width and 0 <= y1 < self.height:
                self.screen_data[y1][x1] = chr(char)

            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        print(f"line drawn from({x1},{y1} to {x2},{y2}) with color {color} and character '{chr(char)}'.")
