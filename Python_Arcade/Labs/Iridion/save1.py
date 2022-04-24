import random
import arcade
import math
import os


SPRITE_SCALING = 0.5
SPRITE_SCALING_LASER = 0.3
SPRITE_SCALING_ENEMY = 0.5

BULLET_SPEED = 10
ANGLE_SPEED = 5
MOVEMENT_SPEED = 5
REG_ENEMY_SPEED = 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Iridion Remake"

ENEMY_COUNT = 10


class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Reg_Enemy(arcade.Sprite):

    def __init__(self, name_folder, name_file):
        super().__init__()

        # Creating bullet list for reg_aim method
        self.reg_enemy_bullet_list = arcade.SpriteList()

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """


        if self.center_y > SCREEN_HEIGHT:
            self.change_y = -2

        if self.center_y < 0:
            self.change_y = +2

        if self.center_x > SCREEN_WIDTH:
            self.change_x = -2

        if self.center_x < 0:
            self.change_x = 2

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * REG_ENEMY_SPEED
            self.change_y = math.sin(angle) * REG_ENEMY_SPEED

    '''def reg_aim(self, player_sprite):

        #for enemy in enemy_list:  # we won't be needing this line later. Just for context

        start_x = self.center_x
        start_y = self.center_y

        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)

        reg_enemy_bullet = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                         "Iridion/Game_Assets/Active_use/Lasers/spaceMissiles_038.png",
                                         SPRITE_SCALING_LASER)
        reg_enemy_bullet.angle = angle
        reg_enemy_bullet.change_y = -math.cos(math.radians(player_sprite.angle)) * BULLET_SPEED
        reg_enemy_bullet.change_x = math.sin(math.radians(player_sprite.angle)) * BULLET_SPEED
        # Add the bullet to the appropriate list
        self.reg_enemy_bullet_list.append(reg_enemy_bullet)'''



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.bullet_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/Iridion/"
                                    "Game_Assets/Active_use/Player/spaceShips_001.png",
                                    SPRITE_SCALING, angle = 180)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Adding enemies to the screen

        for i in range(ENEMY_COUNT):
            enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/Iridion/"
                              "Game_Assets/Active_use/Enemies/Turrent_01.png", SPRITE_SCALING_ENEMY) # @@ angle = 180) - Saving this to see why angle doesn't work when added to the code.
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 50)
            self.enemy_list.append(enemy)


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen
        self.clear()

        # Draw all the sprites.
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()

    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update to move the sprites
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()

        for enemy in self.enemy_list:
            enemy.follow_sprite(self.player_sprite)
            #enemy.reg_aim(self.player_sprite)

        # Checking for collisions with enemies
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()

            # Removing bullets if they leave the screen
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            elif bullet.center_y < 0:
                bullet.remove_from_sprite_lists()

            elif bullet.center_x < 0:
                bullet.remove_from_sprite_lists()
            elif bullet.center_x > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

        # Calling respawn method
        #self.respawn()

        # Change Angle when Z and X are pressed. See on_key_press and on_key_release for more details.
        self.player_sprite.angle += self.player_sprite.change_angle

    '''def respawn(self):
        # This respawns regular enemies
        # Respawn
        if (len(self.enemy_list) < 6) and random.randrange(0,200) == 1:
            print("hello")
            for i in range(ENEMY_COUNT):
                enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/Iridion/"
                                  "Game_Assets/Active_use/Enemies/Turrent_01.png", SPRITE_SCALING_ENEMY, angle=180)
                enemy.center_x = random.randrange(SCREEN_WIDTH)
                enemy.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 50)
                self.enemy_list.append(enemy)'''


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Controls player movement
        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

        # Creating a bullet when the user presses the spacebar
        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/Iridion/"
                                   "Game_Assets/Active_use/Lasers/Laser_01.png", SPRITE_SCALING_LASER)

            bullet.change_y = -math.cos(math.radians(self.player_sprite.angle)) * BULLET_SPEED
            bullet.change_x = math.sin(math.radians(self.player_sprite.angle)) * BULLET_SPEED
            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.center_y
            bullet.angle = self.player_sprite.angle

            # Add the bullet to the appropriate list
            self.bullet_list.append(bullet)

        # Change angle if Z or X are pressed.
        if key == arcade.key.Z:
            self.player_sprite.change_angle = 5
        elif key == arcade.key.X:
            self.player_sprite.change_angle = -5


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

        # Stop changing angle if Z or X are released.
        if key == arcade.key.Z:
            self.player_sprite.change_angle = 0
        if key == arcade.key.X:
            self.player_sprite.change_angle = 0


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()