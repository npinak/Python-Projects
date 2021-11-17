import arcade


WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10
SCREEN_HEIGHT = (HEIGHT * ROW_COUNT) + (MARGIN * (ROW_COUNT + 1))
SCREEN_WIDTH = (WIDTH * COLUMN_COUNT) + (MARGIN * (COLUMN_COUNT + 1))

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        # Setting the background color
        arcade.set_background_color(arcade.color.BLACK)

        # --- Creating grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)


    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Creating the squares and logic for color selection
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.ALIZARIN_CRIMSON
                else:
                    color = arcade.color.WHITE

                # creating x_center for the rectangles
                x = (MARGIN + WIDTH) * column + MARGIN + (WIDTH/2)
                # creating y_center for the rectangles
                y = (MARGIN + WIDTH) * row + MARGIN + (WIDTH/2)

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT,
                                                 color)



    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)


        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":

    main()
