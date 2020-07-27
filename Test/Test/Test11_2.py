# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/26 15:52


class Screen:

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution


samsung = Screen()
samsung.height = 1080
samsung.width = 1920
print(samsung.resolution)
