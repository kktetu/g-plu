# -*- coding: utf-8 -*-
"""
以下の条件を満たすようなアルゴリズムを考えてください。
コードを記述する場合は、必要な箇所だけで構いません。
        　
・ユニットA、ユニットB、ユニットCが存在する
・１処理でユニットAはX方向に１進む
・１処理でユニットBはY方向に１進む
・１処理でユニットCはZ方向に１進む
・全てのユニットの初期位置はX,Y,Z座標共に-100～100の間でランダム
・各ユニットの数は不定
・なるべくまとめて簡単に処理したい
"""

import random


class Four(object):
    """
    回答:
        ベクトルがs(1, 1, 1)で点m(X1,Y1,Z1)を通る直線
        アルゴリズムは(x-X1)/1 == (y-Y1)/1 == (z-Z1)/1
    """
    def __init__(self):
        self.X = random.randint(-100, 100)
        self.Y = random.randint(-100, 100)
        self.Z = random.randint(-100, 100)
    
    def get_algorithm(self, x, y, z):
        return x-self.X == y-self.Y == z-self.Z
