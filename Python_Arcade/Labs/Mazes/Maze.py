"""

Artwork from https://kenney.nl
"""

import random
import arcade

SPRITE_SCALING = 0.5
GEM_SCALING = 0.5

NUMBER_OF_GEMS = 40
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# Setting how fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# Setting how fast the character moves
PLAYER_MOVEMENT_SPEED = 5.5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Setting up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Creating the cameras. One for the GUI, one for the sprites.
        # 'camera_sprites' scrolls but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Score variable
        self.score = 0 # player score
        self.gem_number = NUMBER_OF_GEMS # number of gems left

    def setup(self):
        """ Setting up the game and initializing the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.25)
        self.player_sprite.center_x = 210
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # Creating the bottom perimeter
        for x in range(0, 1600, 32):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        # Creating the left wall
        for y in range(0, 1600, 32):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = -32
            wall.center_y = y
            self.wall_list.append(wall)

        # Creating the top wall
        for x in range(0, 1600, 32):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1600 - 32
            self.wall_list.append(wall)

        # Creating the right wall
        for y in range(0, 1600, 32):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = 1568
            wall.center_y = y
            self.wall_list.append(wall)

        # Creating the inside maze walls
        for x in range(-32, 1600, 64):
            for y in range(0, 1600, 32):
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Adding the gems so that they don't overlap with the walls or with each other.
        for i in range(NUMBER_OF_GEMS):

            # Create the gem instance
            # Gem image from kenney.nl
            gem = arcade.Sprite("platformPack_item010.png", GEM_SCALING)

            # Boolean variable if we successfully placed the gem
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the coin
                gem.center_x = random.randrange(0, 1600, 32)  # from 0 to 1600 in steps of 32
                gem.center_y = random.randrange(0, 1600, 32)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                # See if the coin is hitting another coin
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Adding the coin to the lists
            self.gem_list.append(gem)

        # Physics Engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Setting the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Selecting the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        # Selecting the (un-scrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        text = f'Score: {self.score} | Gems left: {self.gem_number}'
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        # Collision checking with player and gems

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.gem_list)
        for gem in gem_hit_list:
            self.score += 1
            self.gem_number -= 1
            gem.remove_from_sprite_lists()

    def scroll_to_player(self):
        """ Scroll the window to the player. """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
