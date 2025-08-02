from random import choice

class RandomWalk:
    """ランダムウォークを生成するためのクラス"""

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        #ランダムウォークの始点は(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ランダムウォークのすべての点を計算する"""

        #ステップ数が指定した数になるまでランダムウォークを続ける
        while len(self.x_values) < self.num_points:
            #移動する方向と距離を決定する
            x_step = self.get_step([1, -1], [0, 1, 2, 3, 4, 5])
            y_step = self.get_step([1, -1], [0, 1, 2, 3, 4])

            #どこにも移動しない場合は結果を破棄する
            if x_step == 0 and y_step == 0:
                continue

            #新しい位置を計算する
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self, direction, distance):
        """direction: 進む向き, distance: 移動距離"""
        return choice(direction) * choice(distance)