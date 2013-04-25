# -*- coding: utf-8 -*-
"""
数値を1から100まで1ずつ加算していきます。
その数値が3の倍数のときは「a」、5の倍数のときは「b」、
3の倍数でもあり5の倍数でもあるときは「ab」、
いずれも満たさない場合はその数値を表示するプログラムを書いて下さい。
"""
class One(object):
    a = "a"
    b = "b"
    c = 3
    d = 5
    
    def __init__(self):
        self.text()

    def text(self):
        for x in range(1, 101):
            if self._fifteen(x):
                print a+b
            elif self._three(x):
                print a
            elif self._five(x):
                print b
            else:
                print x

    def _three(self, x):
        return x % 3 == 0

    def _five(self, x):
        return x % 5 == 0

    def _fifteen(self, x):
        return x % 15 == 0


