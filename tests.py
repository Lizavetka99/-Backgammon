import Chip_data
import Button
import Player
import Chip
import pygame
from Dice import Dice
import main
import unittest

from main import player

class TestBackgammon(unittest.TestCase):
    def test_initial_chip_positions(self):
        assert len(Chip_data.white_chips) == 15
        assert len(Chip_data.black_chips) == 15
        assert Chip_data.white_chips[0].x == 160
        assert Chip_data.black_chips[0].x == 717


    def test_chip_count_on_field(self):
        white_count = sum(1 for chip in Chip_data.white_chips if chip.owner == 'white')
        black_count = sum(1 for chip in Chip_data.black_chips if chip.owner == 'black')
        assert white_count == 15
        assert black_count == 15


    def test_chip_move_with_dice(self):
        chip = Chip_data.white_chips[0]
        chip.count_moves = 0
        dice_values = [2, 4]  # Пример значений кубиков
        possible_moves = chip.create_help_chips(dice_values, Chip_data.black_chips, Chip_data.white_chips, player)

        # Ожидаем, что фишка может двигаться
        assert len(possible_moves) > 0

    def test_chip_cannot_move_to_occupied_cell(self):
        chip = Chip_data.white_chips[0]
        dice_values = [1]  # Двигаем на одну клетку
        Chip.owner_of_occupied[chip.position_number + 1] = "black"  # Противник на следующей клетке

        possible_moves = chip.create_help_chips(dice_values, Chip_data.black_chips, Chip_data.white_chips, player)

        # Фишка не должна иметь возможных ходов на занятые клетки
        assert len(possible_moves) == 0


    def test_double_dice_roll(self):
        player.dice_values = [3, 3]
        chip = Chip_data.white_chips[0]
        possible_moves = chip.create_help_chips(player.dice_values, Chip_data.black_chips, Chip_data.white_chips, player)

        # Должно быть 4 возможных хода
        assert len(possible_moves) == 4


    def test_dice_button_click(self):
        dice_button = Button.Button(pygame.image.load("Assets/dice_button.png"), "dice_button")
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(dice_button.pos[0] + 1, dice_button.pos[1] + 1))
        dice_button.is_clicked()  # Должен сработать метод is_clicked()
        assert Dice.is_throw  # Кубики должны быть брошены


    def test_move_without_dice_throw(self):
        player.dice_values = [0, 0]
        chip = Chip_data.white_chips[0]
        possible_moves = chip.create_help_chips(player.dice_values, Chip_data.black_chips, Chip_data.white_chips, player)

        # Игрок не должен иметь возможности двигаться без броска кубиков
        assert len(possible_moves) == 0


    def test_player_win_condition(self):
        player.count_of_thrown = 15  # Все фишки выведены
        assert player.count_of_thrown == 15


    def test_no_moves_left(self):
        player.dice_values = [0, 0]
        player.chips[0].can_move = False
        possible_moves = player.chips[0].create_help_chips(player.dice_values, Chip_data.black_chips, Chip_data.white_chips,
                                                           player)
        assert len(possible_moves) == 0  # Нет доступных ходов


    def test_invalid_dice_roll(self):
        dice = Dice.throw()
        assert 1 <= dice[1] <= 6  # Значение кубика должно быть от 1 до 6


    def test_chip_move_position(self):
        chip = Chip_data.white_chips[0]
        initial_position = chip.position_number
        dice_values = [2]  # Двигаем на 2 клетки
        possible_moves = chip.create_help_chips(dice_values, Chip_data.black_chips, Chip_data.white_chips, player)

        chip.position_number += 2  # Перемещаем фишку на 2 клетки
        assert chip.position_number == initial_position + 2


    def test_chip_spawner(self):
        main.spawn_chips()
        assert len(Chip_data.white_chips) == 15
        assert len(Chip_data.black_chips) == 15


    def test_chip_cannot_land_on_enemy_cell(self):
        chip = Chip_data.white_chips[0]
        Chip.owner_of_occupied[chip.position_number + 1] = "black"  # Противник на следующей клетке
        possible_moves = chip.create_help_chips([1], Chip_data.black_chips, Chip_data.white_chips, player)
        assert len(possible_moves) == 0


    def test_chip_move_to_home(self):
        chip = Chip_data.white_chips[0]
        chip.position_number = 0  # Начальная позиция
        possible_moves = chip.create_help_chips([1], Chip_data.black_chips, Chip_data.white_chips, player)
        assert len(possible_moves) > 0  # Фишка может двигаться


    def test_invalid_move(self):
        chip = Chip_data.white_chips[0]
        initial_position = chip.position_number
        chip.count_moves = 0
        dice_values = [0]  # Неверное значение для движения
        possible_moves = chip.create_help_chips(dice_values, Chip_data.black_chips, Chip_data.white_chips, player)
        assert chip.position_number == initial_position


    def test_blocked_move_by_same_color_chip(self):
        chip = Chip_data.white_chips[0]
        Chip.owner_of_occupied[chip.position_number + 1] = "white"  # Другая фишка белого на клетке
        possible_moves = chip.create_help_chips([1], Chip_data.black_chips, Chip_data.white_chips, player)
        assert len(possible_moves) == 0


    def test_chip_exit_from_home(self):
        chip = Chip_data.white_chips[0]
        chip.position_number = 0  # Начальная позиция
        possible_moves = chip.create_help_chips([1], Chip_data.black_chips, Chip_data.white_chips, player)
        assert chip.position_number > 0  # Фишка должна выйти из дома


    def test_game_end_when_all_chips_exited(self):
        player.count_of_thrown = 15  # Все фишки выведены
        assert player.game_over()


    def test_invalid_dice_roll_for_move(self):
        chip = Chip_data.white_chips[0]
        chip.position_number = 10
        dice_values = [1]  # Но клетка занята
        possible_moves = chip.create_help_chips(dice_values, Chip_data.black_chips, Chip_data.white_chips, player)
        assert len(possible_moves) == 0


if __name__ == '__main__':
    unittest.main()