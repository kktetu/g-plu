# -*- coding: utf-8 -*-
"""
問題
２つの球が存在しています。
現在この２つの球は重なった状態です。
この球の座標を変更し、重なっていない状態にしたいのですが
それを可能とするアルゴリズムを文章とコードにて説明してください。
ただし、球の半径はr1、r2とします。
"""
"""
回答
２つの球の中心、点と点の距離がR >= r1+r2の場合は重ならない。
または半径r2の球の中心座標が、半径r1+r2の球に入っていない
(球表面にある点の座標は引く)の場合は重ならない。
"""

class Three(object):
    
    def __init__(self, x1, y1, z1, r1, r2):
        """
        球の初期化テーダを設定
        """
        self.r1 = r1
        self.r2 = r2
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
    
    def is_overlapped_one(self, x2, y2, z2):
        """
        ２つの球の中心、点と点の距離R >= r1+r2の場合は重ならない。
        """
        return (x2-self.x1)**2 + \
               (y2-self.y1)**2 + \
               (z2-self.z1)**2 >= (self.r1 + self.r2)**2

    def is_ball_coordinates(self, x2, y2, z2):
        """
        半径(r1+r2)球の中に入っている点の座標か判断(球表面点は引く)
        """
        return (x2-self.x1)**2 + \
               (y2-self.y1)**2 + \
               (z2-self.z1)**2 < (self.r1+self.r2)**2

    @property
    def get_all_square_coordinates(self):
        """
        正方形の中に入っているすべて点の座標を取る
        """
        square_coordinates = []
        for x in range(self.x1-self.r1, self.x1+self.r1):
            for y in range(self.y1-self.r1, self.y1+self.r1):
                for z in range(self.z1-self.r1, self.z1+self.z1):
                    square_coordinates.append([x, y, z])
        
        return square_coordinates

    @property
    def get_all_ball_coordinates(self):
        ball_coordinates = []
        for square_coordinate in self.get_all_square_coordinates:
            if self.is_ball_coordinates(
                square_coordinate[0],
                square_coordinate[1],
                square_coordinate[2]):
                ball_coordinates.append(square_coordinate)
        
        return ball_coordinates 

    def is_overlapped_two(self, x2, y2, z2):
        """
        座標が[x1, y1, z1]半径がr1の球と重なるか判断
        """
        return [x2, y2, z2] is not self.get_all_ball_one_coordinates
