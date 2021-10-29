""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Rectangle_Sun:
    def __init__(self,position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """Code to draw the Rectangle Sun"""
        arcade.draw_line(self.position_x ,self.position_y, self.position_x+75, self.position_y,  self.color, 3)  # Ray going to the right
        arcade.draw_line(self.position_x-75, self.position_y, self.position_x, self.position_y, self.color, 3)  # Ray going to the left
        arcade.draw_line(self.position_x, self.position_y, self.position_x, self.position_y+75, self.color, 3)  # Ray going up
        arcade.draw_line(self.position_x, self.position_y-75, self.position_x, self.position_y, self.color, 3)  # Ray going down
        arcade.draw_lrtb_rectangle_filled(self.position_x-50, self.position_x+50,self.position_y+50, self.position_y-50,self.color)

        #arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) # core of the sun

    def update(self):
        '''Checking to see where the sun is located'''
        if self.position_x > 0:
            print("Move the other way!")

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Creating a Rectangle_Sun Object
        self.sun = Rectangle_Sun(300,300,3,arcade.csscolor.ORANGE)

        # Making sure that the mouse is not visible
        self.set_mouse_visible(False)

        # Setting Background Color
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        # Loading Sound
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.explosion_sound_player = None

    def on_draw(self):

        # Starting Render
        arcade.start_render()

        # Drawing the grass
        arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.csscolor.GREEN)

        # Drawing the Tree
        arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

        # Draw the Sun
        self.sun.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.sun.position_x = x
        self.sun.position_y = y

        '''Play an explosion noise if the mouse goes beyond the window'''
        if x == 0:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


        if x == 799:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

        if y == 0:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

        if y == 599:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


def main():
    window = MyGame()
    arcade.run()


main()
