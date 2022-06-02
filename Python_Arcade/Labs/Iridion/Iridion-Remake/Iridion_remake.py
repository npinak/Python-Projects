from dataclasses import asdict
import random
import arcade
import math

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.4
ENEMY_SCALING_LASER = 0.4

COIN_COUNT = 50
ENEMY_COUNT = 10

MOVEMENT_SPEED = 5
TURN_SPEED  = 5
BULLET_SPEED = 8
REG_ENEMY_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

REG_ENEMY_RESPAWN = 5

OFFSCREEN_SPACE = 300


class Reg_Enemy(arcade.Sprite, arcade.View):

    def __init__(self, image_file, scale, enemy_bullet_list, time_between_firing):
        """ Set up the enemy """
        super().__init__(image_file, scale)
        arcade.View.__init__(self)
        # Time since last firing
        self.time_since_last_firing = 0.0

        # Time Between Firing
        self.time_between_firing = time_between_firing

        # Keep Track of Bullets
        self.enemy_bullet_list = enemy_bullet_list
        self.game = GameView()

    def setup(self):
        
        self.enemy_bullet_list = arcade.SpriteList()

    def follow_player(self, player_sprite):

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that the enemy will change from its old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Calculate how to get the bullet to the destination.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            self.change_x = math.cos(angle) * REG_ENEMY_SPEED
            self.change_y = math.sin(angle) * REG_ENEMY_SPEED

    def on_update(self, player_sprite, player_list, delta_time: float = 1 / 60): 
        """ Update this sprite. """ 

    
        # Get Enemy's position
        start_x = self.center_x
        start_y = self.center_y

        # Get the Player's position
        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        # Get differences between enemy and player position
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # Calculate angle between enemy and player
        angle = math.atan2(y_diff, x_diff)

        # Track time since we last fired
        self.time_since_last_firing += delta_time

        # If it is past the firing time, then fire
        if self.time_since_last_firing >= self.time_between_firing:

            # Reset timer
            self.time_since_last_firing = 0

            # Fire the bullet
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png",
            scale = ENEMY_SCALING_LASER) 
            bullet.center_x = self.center_x
            bullet.angle = math.degrees(angle)
            bullet.top = self.bottom
            bullet.change_x = math.cos(angle) * REG_ENEMY_SPEED
            bullet.change_y = math.sin(angle) * REG_ENEMY_SPEED
            self.enemy_bullet_list.append(bullet)
    
        # Bullet Collision Detection. Need to add health and subtract 
        for bullet in self.enemy_bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, player_list)


            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                view = GameOverView()
                self.window.show_view(view)

        # Get Enemy's position
        start_x = self.center_x
        start_y = self.center_y

        # Get the Player's position
        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        # Get differences between enemy and player position
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # Calculate angle between enemy and player
        angle = math.atan2(y_diff, x_diff)

        # Making the enemy face the player
        self.angle = math.degrees(angle) - 90



class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
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

class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.coin_list = None
        self.bullet_list = None
        self.enemy_bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.health = 100


        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.background = None


        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList() ####
        # Set up the player
        self.score = 0
        self.health = 100 ####

        # Setting background Image
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")


        # Setting up the Player Sprite. Image from kenney.nl
        self.player_sprite = arcade.Sprite("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                           "Iridion/Game_Assets/Active_use/Player/spaceShips_001.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite.angle = 180
        self.player_list.append(self.player_sprite)

        # Setting up the enemies and adding them to a list
        for enemy in range(ENEMY_COUNT):
            time_between_firing = random.uniform(3,8)
            enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                  "Iridion/Game_Assets/Active_use/Enemies/Turrent_01.png",SPRITE_SCALING_PLAYER,
                                  enemy_bullet_list = self.enemy_bullet_list,
                                  time_between_firing = time_between_firing) 
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 10, SCREEN_HEIGHT + 100)
            self.enemy_list.append(enemy)

        # Background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)


        # Draw all the sprites.
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.enemy_bullet_list.draw() ####

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def reg_enemy_respawn(self):

        # Creates more enemies if it's too low
        for enemy in range(REG_ENEMY_RESPAWN):
            enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                  "Iridion/Game_Assets/Active_use/Enemies/Turrent_01.png", SPRITE_SCALING_PLAYER,
                                  enemy_bullet_list = self.enemy_bullet_list,####
                                  time_between_firing = random.uniform(3,8)) ####
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 30, SCREEN_HEIGHT + 200)
            self.enemy_list.append(enemy)


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # Moving the Player Ship
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

        # Change the angle that the player faces
        if key == arcade.key.X:
            self.player_sprite.change_angle = -TURN_SPEED
        elif key == arcade.key.Z:
            self.player_sprite.change_angle = TURN_SPEED

        # Player Shooting
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

        if key == arcade.key.X or key == arcade.key.Z:
            self.player_sprite.change_angle = 0

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


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_bullet_list.update()

        for enemy in self.enemy_list:
            enemy.on_update(self.player_sprite, self.player_list, delta_time)


        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                self.score += 1 
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        # Calling follow player for regular enemy
        for enemy in self.enemy_list:
            enemy.follow_player(self.player_sprite)
    
        # Respawn more regular enemies if number falls below 6
        if (len(self.enemy_list) < 6):
            self.reg_enemy_respawn()

        # Moving the player to the otherside of the screen if they go out-of-bounds
        # Check for out-of-bounds
        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_x = 0

        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT:
            self.player_sprite.center_y = 0


class MenuView(arcade.View):
    # Starting Menu

    def on_show_view(self):
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100,
                         arcade.color.GRAY, font_size=50, anchor_x="center")

        arcade.draw_text("Up-Arrow = Forward",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
         arcade.color.DUTCH_WHITE,font_size=20, anchor_x="center")
        arcade.draw_text("Down-Arrow = Backward", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Left-Arrow = Left", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Right-Arrow = Right", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Z = Turn Counter-Clockwise", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 -  50,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("X = Turn Clockwise", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Space = Shoot", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.DUTCH_WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("Click to advance.", SCREEN_WIDTH / 2, 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        self.window.show_view(game)
        game.setup()


class GameOverView(arcade.View):
    # Game Over View
   
    def on_show_view(self):
        arcade.set_background_color(arcade.color.NAVAJO_WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("You got Hit! Game over :(", SCREEN_WIDTH / 2, SCREEN_HEIGHT/2,
                         arcade.color.GRAY, font_size=50, anchor_x="center")

        arcade.draw_text("Click to Replay", SCREEN_WIDTH / 2, SCREEN_HEIGHT/2 - 100,
                    arcade.color.GRAY, font_size=50, anchor_x="center")

        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        self.window.show_view(game)
        game.setup()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Iridion Remake")
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()