#!/usr/bin/env python3

import fastbook
from fastbook import *
from fastai.vision.all import *


path = untar_data(URLs.MNIST_SAMPLE)
Path.BASE_PATH = path
print(path.ls())
