"""
Part-2 of Array backed grids lab.
https://learn.arcade.academy/en/latest/labs/lab_11_array_backed_grids/array_backed_grids.html

"""
import arcade
import numpy as np

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        #print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        ''' Counts the number of cells selected in each row and column '''

        total_count = 0
        row_count_list = []
        column_count = np.zeros(10)

        for row in range(10):
            row_count = 0
            for column in range(10):
                if self.grid[row][column] == 1:
                    total_count += 1
                    row_count += 1
                    column_count[column] = column_count[column] + 1
            row_count_list.append(f"Row {row} has {row_count} cells selected")

        ''' Counts the number of continous cells selected '''
        continous_count_list = np.zeros(10)

        for row in range(ROW_COUNT):
          continous_count = 0
          for column in range(COLUMN_COUNT):
            if self.grid[row][column] == 1:
              continous_count += 1
            elif self.grid[row][column] == 0:
              if continous_count > 1:
                continous_count_list[row] = continous_count_list[row] + continous_count
                print(continous_count_list[row])
                continous_count = 0
              else:
                continous_count = 0


        '''Printing all the different outputs'''

        print(f"There are a total of {total_count} cells selected in the entire grid")

        for row in range(len(row_count_list)):
            if continous_count_list[row] > 0:
                print(f"There are {int(continous_count_list[row])} cells selected continously in row {row}.")
            print(row_count_list[row])

        for column in range(len(column_count)):
            print(f"Column {column} has {int(column_count[column])} cells selected")




def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()