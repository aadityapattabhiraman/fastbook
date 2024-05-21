#!/usr/bin/env python3

import fastbook
from fastbook import *
from fastai.vision.all import *


path = untar_data(URLs.MNIST_SAMPLE)
Path.BASE_PATH = path
print(path.ls())

threes = (path / "train" / "3").ls().sorted()
sevens = (path / "train" / "7").ls().sorted()
print(threes)

im3_path = threes[1]
im3 = Image.open(im3_path)
# im3.show()

array(im3)[4: 10, 4: 10]
