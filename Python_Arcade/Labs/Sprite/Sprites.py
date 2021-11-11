'''Creating a game where the player collects stars and avoids red orbs'''
'''Art work from kenney.nl'''

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.35
SPRITE_SCALING_STAR = 0.2
STAR_COUNT = 50
ORB_COUNT = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Star(arcade.Sprite):

    def reset_pos(self):
        # Reset the orb to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT - 400,
                                         SCREEN_HEIGHT - 20)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the stars
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Orb(arcade.Sprite):

    '''Creating the movement for the Orbs'''

    def reset_pos(self):
        # Reset the orb to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        ''' Code to make orb stars move downwards'''

        self.center_y -= 1

        # See if the orb went off-screen
        if self.top < 0:
            # Resetting the orb to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.star_list = None
        self.orb_list = None

        # Setting up the player info
        self.player_sprite = None
        self.score = 0

        # Hiding the mouse cursor
        self.set_mouse_visible(False)

        # Variable to freeze game in the beginning if the player hasn't gotten a star yet
        self.movement = 0

        # Setting the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Setting up the game and initializing the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.orb_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player character sprite
        self.player_sprite = arcade.Sprite("character_robot_side.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Creating the stars
        for i in range(STAR_COUNT):
            # Create the stars
            star = Star("star.png", SPRITE_SCALING_STAR)

            # Position the stars
            star.center_x = random.randrange(SCREEN_WIDTH-400, SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)
            star.change_x = random.randrange(-3, 4)
            star.change_y = random.randrange(-3, 4)

            # Add the stars to the lists
            self.star_list.append(star)

        # Creating the orbs
        for i in range(ORB_COUNT):
            # Create the orb instance
            # Star image from kenney.nl
            orb = Orb('ball_red_small.png', SPRITE_SCALING_STAR)

            # Position the orbs
            orb.center_x = random.randrange(SCREEN_WIDTH)
            orb.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the orbs to the orb list
            self.orb_list.append(orb)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Mouse Motion for the Sprite """

        # Moving the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Detecting Collisions and Scoring """

        # Generating a list of star sprites that collided with the player.
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.star_list)

        # Makes the sprites freeze if a player hasn't collected at least one star
        if len(star_hit_list) > 0:
            self.movement = 1

        if self.movement == 1:
            self.orb_list.update()
            self.star_list.update()

        # Looping through each colliding star sprite, resetting it, and add to the score.
        for star in star_hit_list:
            star.reset_pos()
            self.score += 1

        # Checking for orb sprites that collided with the player sprite
        orb_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.orb_list)

        # Looping through each colliding orb sprite, resetting it, and subtracting the score.
        for orb in orb_hit_list:
            orb.reset_pos()
            self.score += -1

    def on_draw(self):
        '''Drawing all the sprites on the screen'''
        arcade.start_render()

        self.star_list.draw()
        self.player_list.draw()
        self.orb_list.draw()

        # Score text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()