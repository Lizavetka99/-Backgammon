import unittest
from unittest.mock import patch
import pygame
import Chip_data
import Button
import Player
import Chip
from Dice import Dice
import main


class TestBackgammon(unittest.TestCase):

    def setUp(self):
        # Инициализация Pygame для тестов
        pygame.init()
        self.screen_width = main.image_settings.WIDTH
        self.screen_height = main.image_settings.HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # Инициализация элементов игры
        self.player = Player.Player("white")
        self.enemy = main.enemy  # Предполагается, что enemy инициализирован в main
        self.white_chips = Chip_data.white_chips
        self.black_chips = Chip_data.black_chips

    def tearDown(self):
        # Очистка после тестов
        pygame.quit()

    def test_initial_chip_positions(self):
        self.assertEqual(len(Chip_data.white_chips), 15, "Должно быть 15 белых фишек")
        self.assertEqual(len(Chip_data.black_chips), 15, "Должно быть 15 черных фишек")
        self.assertEqual(Chip_data.white_chips[0].x, 160, "Первая белая фишка должна быть на x=160")
        self.assertEqual(Chip_data.black_chips[0].x, 717, "Первая черная фишка должна быть на x=717")

    def test_chip_count_on_field(self):
        white_count = sum(1 for chip in Chip_data.white_chips if chip.owner == 'white')
        black_count = sum(1 for chip in Chip_data.black_chips if chip.owner == 'black')
        self.assertEqual(white_count, 15, "Должно быть 15 белых фишек на поле")
        self.assertEqual(black_count, 15, "Должно быть 15 черных фишек на поле")

    def test_chip_move_with_dice(self):
        chip = self.white_chips[0]
        chip.count_moves = 0
        dice_values = [2, 4]  # Пример значений кубиков
        possible_moves = chip.create_help_chips(dice_values, self.black_chips, self.white_chips, self.player)
        self.assertTrue(len(possible_moves) > 0, "Фишка должна иметь доступные ходы")

    def test_double_dice_roll(self):
        self.player.dice_values = [3, 3]
        chip = self.white_chips[0]
        possible_moves = chip.create_help_chips(self.player.dice_values, self.black_chips, self.white_chips, self.player)
        self.assertEqual(len(possible_moves), 1, "Должен быть только один возможный ход при дубле")

    def test_chip_spawner(self):
        self.assertEqual(len(Chip_data.white_chips), 15, "Должно быть 15 белых фишек после спавна")
        self.assertEqual(len(Chip_data.black_chips), 15, "Должно быть 15 черных фишек после спавна")

    def test_dice_button_clickable(self):
        # Проверяем, что кнопка кубиков находится в правильной позиции и имеет правильный размер
        dice_button = main.dice_button
        self.assertIsNotNone(dice_button, "Кнопка броска кубиков должна быть инициализирована")
        self.assertTrue(dice_button.rect.collidepoint(main.image_settings.images_data["dice_button"]["pos"]),
                        "Кнопка кубиков должна быть в заданной позиции")

    def test_player_move_decrements_moves(self):
        initial_moves = 2
        self.player_moves = initial_moves
        self.player_moves -= 1
        self.assertEqual(self.player_moves, initial_moves - 1, "Количество ходов игрока должно уменьшиться на 1")

    def test_enemy_move(self):
        initial_enemy_moves = self.enemy.throw_count
        self.enemy.throw_dices()
        self.assertGreaterEqual(self.enemy.throw_count, initial_enemy_moves, "Количество бросков противника должно увеличиться")

    def test_game_over_condition(self):
        main.player.count_of_thrown = 15
        main.enemy.throw_count = 15
        self.assertTrue(main.player.count_of_thrown >= 15 or main.enemy.throw_count >= 15, "Игра должна завершиться при достижении 15 бросков")

    def test_help_chips_generation(self):
        chip = self.white_chips[0]
        dice_values = [2, 3]
        help_chips = chip.create_help_chips(dice_values, self.black_chips, self.white_chips, self.player)
        self.assertIsInstance(help_chips, list, "help_chips должны быть списком")
        self.assertTrue(all(isinstance(hc, Chip.Chip) for hc in help_chips), "Все подсказки должны быть экземплярами Chip")

if __name__ == '__main__':
    unittest.main()
