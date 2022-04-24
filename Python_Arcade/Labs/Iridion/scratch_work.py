import random
import arcade
import math

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8

COIN_COUNT = 50
ENEMY_COUNT = 10

MOVEMENT_SPEED = 5
TURN_SPEED  = 5
BULLET_SPEED = 5
REG_ENEMY_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Extras to add

# 1) Make the bullet appear in front of the ship accounting for the angle.


class Reg_Enemy(arcade.Sprite):

    def follow_player(self, player_sprite):

        start_x = self.center_x
        start_y = self.center_y

        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        x_diff = start_x - dest_x
        y_diff = start_y - dest_y

        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.sin(math.radians(angle)) * REG_ENEMY_SPEED
        self.change_y = math.cos(math.radians(angle)) * REG_ENEMY_SPEED





class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                           "Iridion/Game_Assets/Active_use/Player/spaceShips_001.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite.angle = 180
        self.player_list.append(self.player_sprite)

        for enemy in range(ENEMY_COUNT):
            enemy = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                  "Iridion/Game_Assets/Active_use/Enemies/Turrent_01.png",SPRITE_SCALING_PLAYER)
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)
            self.enemy_list.append(enemy)



        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # Create command to move ship
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        # Create command for angle change using z and x
        if key == arcade.key.X:
            self.player_sprite.change_angle = -TURN_SPEED
        elif key == arcade.key.Z:
            self.player_sprite.change_angle = TURN_SPEED

        # Create command for shooting
        if key == arcade.key.SPACE:
            bullet_sprite = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/"
                                          "Python_Arcade/Labs/Iridion/Game_Assets/Active_use/Lasers/Laser_01.png",
                                          SPRITE_SCALING_PLAYER)
            bullet_sprite.center_x = self.player_sprite.center_x
            bullet_sprite.center_y = self.player_sprite.center_y
            bullet_sprite.change_y = -math.cos(math.radians(self.player_sprite.angle)) * BULLET_SPEED
            bullet_sprite.change_x = math.sin(math.radians(self.player_sprite.angle)) * BULLET_SPEED
            bullet_sprite.angle = self.player_sprite.angle
            self.bullet_list.append(bullet_sprite)


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

        if key == arcade.key.X or key == arcade.key.Z:
            self.player_sprite.change_angle = 0


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()
        self.player_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                print(hit_list[0])
                bullet.remove_from_sprite_lists()
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        # Calling follow player for regular enemy

        for enemy in self.enemy_list:
            enemy.follow_player(self.player_sprite)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()