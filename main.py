import pygame
import Screen
import Button
import Chip
import Chip_data
import Enemy
import Player
import image_settings
from Dice import Dice

pygame.init()

# window size settings
screen_width = image_settings.WIDTH
screen_height = image_settings.HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))

# game elements initialization
player = Player.Player("white")
bg_image = pygame.image.load("Assets/background.jpg")
img_data = image_settings.images_data
background = pygame.transform.scale(bg_image,
                                    (img_data["background"]["width"],
                                     img_data["background"]["height"]))

dice_table_image = pygame.image.load("Assets/dice_table.png")
dice_table = pygame.transform.scale(dice_table_image,
                                    (img_data["dice_table"]["width"],
                                     img_data["dice_table"]["height"]))

field_image = pygame.image.load("Assets/field.png")
field = pygame.transform.scale(field_image,
                               (img_data["field"]["width"],
                                img_data["field"]["height"]))

score_desk_image = pygame.image.load("Assets/score_desk.png")
score_desk = pygame.transform.scale(score_desk_image,
                                    (img_data["score_desk"]["width"],
                                     img_data["score_desk"]["height"]))

dice_button_image = pygame.image.load("Assets/dice_button.png")
dice_button = Button.Button(dice_button_image, "dice_button")

white_chips = Chip_data.white_chips
black_chips = Chip_data.black_chips
help_chips = []

is_game_start = False
running = True
selected_chip = None
is_player_move = True
is_player_move_throw_dices = False

enemy = Enemy.Enemy()

# Function to spawn chips only once
def spawn_chips():
    Chip_data.spawn_chips(field)

previous_coord = (0, 0)
while running:
    if enemy.is_enemy_move and not enemy.is_enemy_move_throw_dices:
        enemy.throw_dices()
        dice_table.blit(enemy.dice_1[0], (Dice.x_pos_1, Dice.y_pos_1))
        dice_table.blit(enemy.dice_2[0], (Dice.x_pos_2, Dice.y_pos_2))

        enemy.is_enemy_move_throw_dices = True

    if enemy.is_enemy_move and enemy.is_enemy_move_throw_dices:
        enemy.make_move(black_chips, white_chips)
        
        print(Chip.count_of_occupied)
        is_player_move_throw_dices = False
        is_player_move = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка, нажата ли кнопка
            if dice_button.rect.collidepoint(event.pos) and is_player_move and not is_player_move_throw_dices:
                dice_1, dice_2 = Dice.throw(), Dice.throw()
                player.dice_values[0] = dice_1[1]
                player.dice_values[1] = dice_2[1]
                dice_table.blit(dice_1[0], (Dice.x_pos_1, Dice.y_pos_1))
                dice_table.blit(dice_2[0], (Dice.x_pos_2, Dice.y_pos_2))
                is_player_move_throw_dices = True

            # Проверка, выбрана ли фишка
            if is_player_move and is_player_move_throw_dices:
                for chip in black_chips:
                    if chip.can_move:
                        if chip.rect.collidepoint(event.pos):
                            previous_coord = chip.rect.copy()
                            selected_chip = chip

                            help_chips = chip.create_help_chips(player.dice_values, black_chips, white_chips)

                            # ВЫБРАСЫВАНИЕ ЗА ПРЕДЕЛЫ ДОСКИ
                            for value in player.dice_values:
                                print("sadasdasdds", value + chip.count_moves)

                                if (value + 1 + chip.count_moves) == 24:

                                    throw_chip = Chip.Chip(440, 500, "help")
                                    throw_chip.is_throw = True
                                    help_chips.append(throw_chip)




                            print("МЫ", len(help_chips))
                            offset_x = chip.rect.x - event.pos[0]
                            offset_y = chip.rect.y - event.pos[1]
                            break

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_chip != None:
                is_good = False
                for help_chip in help_chips:
                    if selected_chip.rect.colliderect(help_chip):
                        if help_chip.is_throw:
                            black_chips.remove(selected_chip)
                            player.count_of_thrown += 1
                        for c in black_chips:
                            if c.y == selected_chip.y - 15 and c.x == selected_chip.x:
                                c.can_move = True
                        print(abs(help_chip.position_number - selected_chip.position_number), "ляляля")

                        selected_chip.count_moves += help_chip.current_dice_value
                        print("теперь фиша", selected_chip.count_moves)
                        selected_chip.rect = help_chip.rect
                        selected_chip.x = help_chip.x
                        selected_chip.y = help_chip.y

                        Chip.count_of_occupied[
                            selected_chip.position_number] -= 1
                        if Chip.count_of_occupied[
                            selected_chip.position_number] == 0:
                            Chip.owner_of_occupied[
                                selected_chip.position_number] = "black"
                        selected_chip.position_number = help_chip.position_number
                        for c in black_chips:
                            if c.y + 15 == selected_chip.y and  c.x == selected_chip.x:
                                c.can_move = False
                        is_good = True
                        is_player_move = False
                        print(selected_chip.x, selected_chip.y)

                        Chip.count_of_occupied[selected_chip.position_number] += 1
                        Chip.owner_of_occupied[selected_chip.position_number] = "black"

                        enemy.is_enemy_move = True
                        enemy.is_enemy_move_throw_dices = False
                        break
                if not is_good:
                    selected_chip.rect = previous_coord

            selected_chip = None
            help_chips = []


        elif event.type == pygame.MOUSEMOTION:
            if selected_chip and is_player_move:
                selected_chip.rect.x = event.pos[0] + offset_x
                selected_chip.rect.y = event.pos[1] + offset_y



    screen.fill((0, 0, 0))

    # adding game elements to screen
    screen.blit(background, img_data["background"]["pos"])
    screen.blit(field, img_data["field"]["pos"])
    screen.blit(dice_table, img_data["dice_table"]["pos"])
    screen.blit(score_desk, img_data["score_desk"]["pos"])
    screen.blit(dice_button.texture, dice_button.pos)

    # spawn chips only once
    if not is_game_start:
        spawn_chips()
        is_game_start = True


    # draw chips
    for chip in white_chips + black_chips + help_chips:
        screen.blit(chip.texture, chip.rect)

    pygame.display.flip()

pygame.quit()
