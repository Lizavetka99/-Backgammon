import pygame
import Screen
import Button
import Chip
import Chip_data
import Enemy
import Player
import image_settings
import save_load
from Dice import Dice

pygame.init()

# window size settings
screen_width = image_settings.WIDTH
screen_height = image_settings.HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))

# game elements initialization
player_dict, enemy_dict, white_chips_dict, black_chips_dict = save_load.load_game()
print(1, player_dict)
print(enemy_dict)
print(white_chips_dict)
print(black_chips_dict)
player = Player.Player("white")
enemy = Enemy.Enemy()
white_chips = Chip_data.white_chips
black_chips = Chip_data.black_chips
help_chips = []

if player_dict:
    player.count_of_thrown = player_dict['count_of_thrown']
    player.dice_values = player_dict['player_dice_values']

if enemy_dict:
    enemy.is_enemy_move = enemy_dict['is_enemy_move']
    enemy.is_enemy_move_throw_dices = enemy_dict['is_enemy_move_throw_dices']
    enemy.throw_count = enemy_dict['throw_count']
    # enemy.dice_1 = enemy_dict['dice_1']
    # enemy.dice_2 = enemy_dict['dice_2']
    enemy.dice_values = enemy_dict['enemy_dice_values']
if white_chips_dict:
    white_chips = white_chips_dict
if black_chips_dict:
    black_chips = black_chips_dict

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

is_game_start = False
running = True
selected_chip = None
is_player_move = True
is_player_move_throw_dices = False
player_moves = 0


# Function to spawn chips only once
def spawn_chips():
    Chip_data.spawn_chips(field)


def get_data(array):
    array_data = {}
    for i in range(len(array)):
        array_data[i] = array[i].get_data()
    return array_data


previous_coord = (0, 0)
while running:
    if player.count_of_thrown == 15 or enemy.throw_count == 15:
        break

    if enemy.is_enemy_move and not enemy.is_enemy_move_throw_dices:
        dice_1_en, dice_2_en = Dice.throw(), Dice.throw()

        enemy.dice_values[0] = dice_1_en[1]
        enemy.dice_values[1] = dice_2_en[1]

        dice_table.blit(dice_1_en[0], (Dice.x_pos_1, Dice.y_pos_1))
        dice_table.blit(dice_2_en[0], (Dice.x_pos_2, Dice.y_pos_2))

        enemy.is_enemy_move_throw_dices = True

    if enemy.is_enemy_move and enemy.is_enemy_move_throw_dices:
        enemy.make_move(black_chips, white_chips)
        is_player_move_throw_dices = False
        is_player_move = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # save_load.save(player, enemy, get_data(white_chips), get_data(black_chips))
            save_load.save(player, enemy, get_data(white_chips), get_data(black_chips), Chip.get_data_list())
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка, нажата ли кнопка
            if dice_button.rect.collidepoint(event.pos) and is_player_move and not is_player_move_throw_dices:
                dice_1, dice_2 = Dice.throw(), Dice.throw()
                if dice_1[1] != dice_2[1]:
                    player_moves = 2
                else:
                    player_moves = 4

                player.dice_values[0] = dice_1[1]
                player.dice_values[1] = dice_2[1]
                dice_table.blit(dice_1[0], (Dice.x_pos_1, Dice.y_pos_1))
                dice_table.blit(dice_2[0], (Dice.x_pos_2, Dice.y_pos_2))
                is_player_move_throw_dices = True

            # Проверка, выбрана ли фишка

            if is_player_move and is_player_move_throw_dices:
                can_any_move = False
                for chip in black_chips:

                    if chip.can_move and len(
                            chip.create_help_chips(player.dice_values, black_chips, white_chips, player)) != 0:
                        can_any_move = True
                        if chip.rect.collidepoint(event.pos):
                            previous_coord = chip.rect.copy()
                            selected_chip = chip

                            help_chips = chip.create_help_chips(player.dice_values, black_chips, white_chips, player)

                            # ВЫБРАСЫВАНИЕ ЗА ПРЕДЕЛЫ ДОСКИ

                            offset_x = chip.rect.x - event.pos[0]
                            offset_y = chip.rect.y - event.pos[1]
                            break
                if not can_any_move:
                    is_player_move = False
                    enemy.is_enemy_move = True
                    enemy.is_enemy_move_throw_dices = False

        elif event.type == pygame.MOUSEBUTTONUP:

            if selected_chip != None:
                is_good = False
                is_moves_added = False
                if len(help_chips) == 0:
                    is_player_move = False
                    enemy.is_enemy_move = True
                    enemy.is_enemy_move_throw_dices = True

                for help_chip in help_chips:

                    if selected_chip.rect.colliderect(help_chip):
                        if help_chip.is_throw:
                            # black_chips.remove(selected_chip)
                            player.count_of_thrown += 1
                        if player.dice_values[0] != player.dice_values[1]:
                            if (sum(player.dice_values) == help_chip.current_dice_value - 2):
                                player_moves = 0
                                player.dice_values = [-1, -1]
                            else:
                                player_moves -= 1

                                if (help_chip.current_dice_value - 1 in player.dice_values):
                                    player.dice_values.remove(
                                        help_chip.current_dice_value - 1)
                                    player.dice_values.append(-1)
                        else:
                            player_moves -= 1

                        for c in black_chips:
                            if c.y == selected_chip.y - 15 and c.x == selected_chip.x:
                                c.can_move = True
                        if not (is_moves_added):
                            selected_chip.count_moves += help_chip.current_dice_value
                            is_moves_added = True

                        selected_chip.rect = help_chip.rect
                        selected_chip.x = help_chip.x
                        selected_chip.y = help_chip.y

                        Chip.count_of_occupied[selected_chip.position_number] -= 1
                        if Chip.count_of_occupied[
                            selected_chip.position_number] == 0:
                            Chip.owner_of_occupied[
                                selected_chip.position_number] = "black"
                        selected_chip.position_number = help_chip.position_number
                        for c in black_chips:
                            if c.y + 15 == selected_chip.y and c.x == selected_chip.x:
                                c.can_move = False
                        is_good = True

                        Chip.count_of_occupied[selected_chip.position_number] += 1
                        Chip.owner_of_occupied[selected_chip.position_number] = "black"
                        if (player_moves == 0):
                            is_player_move = False
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

    f1 = pygame.font.SysFont('arial', 50)
    text1 = f1.render(str(player.count_of_thrown), 1, (255, 255, 255))
    f2 = pygame.font.SysFont('arial', 50)
    text2 = f2.render(str(enemy.throw_count), 1, (255, 255, 255))

    # adding game elements to screen
    screen.blit(background, img_data["background"]["pos"])
    screen.blit(field, img_data["field"]["pos"])
    screen.blit(dice_table, img_data["dice_table"]["pos"])
    screen.blit(score_desk, img_data["score_desk"]["pos"])
    screen.blit(dice_button.texture, dice_button.pos)
    screen.blit(text1, (850, 70))
    screen.blit(text2, (850, 500))

    # spawn chips only once
    if not is_game_start:
        spawn_chips()
        is_game_start = True

    # draw chips
    for chip in white_chips + black_chips + help_chips:
        screen.blit(chip.texture, chip.rect)

    pygame.display.flip()

pygame.quit()
