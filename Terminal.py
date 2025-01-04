
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

