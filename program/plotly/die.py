from random import randint

class Die:
    """一個のサイコロを表すクラス"""

    def __init__(self, num_sides = 6):
        """六面のサイコロをデフォルトにする"""
        self.num_sides = num_sides
    
    def roll(self):
        """1から麺の数の間のランダムな数を返す"""
        return randint(1, self.num_sides)