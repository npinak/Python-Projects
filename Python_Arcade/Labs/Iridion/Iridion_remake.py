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


# Todo List

# - Remove Ship turning capability 
#̶ - A̶d̶d̶ b̶e̶t̶t̶e̶r̶ m̶o̶v̶e̶ b̶y̶ k̶e̶y̶b̶o̶a̶r̶d̶ (̶h̶t̶t̶p̶s̶:̶/̶/̶a̶p̶i̶.̶a̶r̶c̶a̶d̶e̶.̶a̶c̶a̶d̶e̶m̶y̶/̶e̶n̶/̶l̶a̶t̶e̶s̶t̶/̶e̶x̶a̶m̶p̶l̶e̶s̶/̶s̶p̶r̶i̶t̶e̶_̶m̶o̶v̶e̶_̶k̶e̶y̶b̶o̶a̶r̶d̶_̶b̶e̶t̶t̶e̶r̶.̶h̶t̶m̶l̶?̶h̶i̶g̶h̶l̶i̶g̶h̶t̶=̶k̶e̶y̶b̶o̶a̶r̶d̶)̶
# - M̶a̶k̶e̶ e̶n̶e̶m̶i̶e̶s̶ s̶p̶a̶w̶n̶ a̶n̶d̶ f̶o̶l̶l̶o̶w̶ t̶h̶e̶ p̶l̶a̶y̶e̶r̶
    # - M̶a̶k̶e̶ e̶n̶e̶m̶i̶e̶s̶ s̶p̶a̶w̶n̶ a̶b̶o̶v̶e̶ t̶h̶e̶ s̶c̶r̶e̶e̶n̶ b̶o̶r̶d̶e̶r̶
    # - A̶d̶d̶ r̶e̶s̶p̶a̶w̶n̶i̶n̶g̶ c̶a̶p̶a̶b̶i̶l̶i̶t̶y̶
    # - M̶a̶k̶e̶ E̶n̶e̶m̶i̶e̶s̶ S̶h̶o̶o̶t̶
    #̶   -̶ M̶a̶k̶e̶ e̶n̶e̶m̶i̶e̶s̶ a̶i̶m̶ a̶t̶ t̶h̶e̶ p̶l̶a̶y̶e̶r̶
    #̶   -̶ M̶a̶k̶e̶ e̶n̶e̶m̶i̶e̶s̶ s̶h̶o̶o̶t̶ i̶n̶d̶e̶p̶e̶n̶d̶e̶n̶t̶l̶y̶ o̶f̶ e̶a̶c̶h̶ o̶t̶h̶e̶r̶ 
    # -̶ M̶a̶k̶e̶ E̶n̶e̶m̶y̶ t̶u̶r̶n̶ t̶o̶ f̶a̶c̶e̶ t̶h̶e̶ p̶l̶a̶y̶e̶r̶ a̶t̶ a̶ c̶e̶r̶t̶a̶i̶n̶ s̶p̶e̶e̶d̶ 
    # - Make enemies crossover at screen border
    # - If enemy touches player it gets destroyed and the player loses health
    # - Add Pro Enemy
# - Add a moving background
# - Make power-up 
# - M̶a̶k̶e̶ p̶l̶a̶y̶e̶r̶ s̶h̶i̶p̶ c̶r̶o̶s̶s̶o̶v̶e̶r̶ a̶t̶ s̶c̶r̶e̶e̶n̶b̶o̶r̶d̶e̶r̶ 
# - Give player healthbar 
    # - Subtract player health when bullet hits 
# - Make a menu screen 

class Reg_Enemy(arcade.Sprite):

    def __init__(self, image_file, scale, enemy_bullet_list, time_between_firing): #### This entire method is a test
        """ Set up the enemy """
        super().__init__(image_file, scale)

        # How long has it been since we last fired?
        self.time_since_last_firing = 0.0

        # How often do we fire?
        self.time_between_firing = time_between_firing

        # When we fire, what list tracks the bullets?
        self.enemy_bullet_list = enemy_bullet_list

    def setup(self):
        
        self.enemy_bullet_list = arcade.SpriteList()

    def follow_player(self, player_sprite):

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

    def on_update(self, player_sprite, player_list, delta_time: float = 1 / 60): #### Added player_list 
        """ Update this sprite. """ # What does delta_time: float = 1 / 60 mean? Ask Prof. Craven ####

        # Getting Enemy's position
        start_x = self.center_x
        start_y = self.center_y

        # Getting the Player's position
        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        # Get differences between enemy and player position
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # Calculate angle between enemy and player
        angle = math.atan2(y_diff, x_diff)

        # Track time since we last fired
        self.time_since_last_firing += delta_time

        # If we are past the firing time, then fire
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


        # Getting Enemy's position
        start_x = self.center_x
        start_y = self.center_y

        # Getting the Player's position
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

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Iridion Remake")

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.coin_list = None
        self.bullet_list = None
        self.enemy_bullet_list = None ####

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


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
            time_between_firing = random.uniform(5,10)
            enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                  "Iridion/Game_Assets/Active_use/Enemies/Turrent_01.png",SPRITE_SCALING_PLAYER,
                                  enemy_bullet_list = self.enemy_bullet_list,####
                                  time_between_firing = time_between_firing) ####
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 10, SCREEN_HEIGHT + 100)
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
        self.enemy_bullet_list.draw() ####

        # Render the text
        arcade.draw_text(f"Health: | Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def reg_enemy_respawn(self):

        for enemy in range(REG_ENEMY_RESPAWN):
            enemy = Reg_Enemy("/Users/pinaknayak/Documents/Github/Python-Projects/Python_Arcade/Labs/"
                                  "Iridion/Game_Assets/Active_use/Enemies/Turrent_01.png", SPRITE_SCALING_PLAYER,
                                  enemy_bullet_list = self.enemy_bullet_list,####
                                  time_between_firing = random.uniform(5,10)) ####
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT + 30, SCREEN_HEIGHT + 200)
            self.enemy_list.append(enemy)


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # Create command to move ship
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
        self.coin_list.update()
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_bullet_list.update() #### Update Enemy_bullet_list to move the enemy bullets 

        for enemy in self.enemy_list:
            enemy.on_update(self.player_sprite, self.player_list, delta_time)


        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
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



def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()