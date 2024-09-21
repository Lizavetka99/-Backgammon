import Chip_data as data


class Chip:
    def __init__(self, x, y, owner):
        self.x = 0
        self.y = 0
        self.owner = owner
        self.texture = data.textures_dict[owner]
