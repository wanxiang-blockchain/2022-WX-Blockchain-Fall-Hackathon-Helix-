#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2022/5/13 10:07
#  @Author  : Louis Li
#  @Email   : vortex750@hotmail.com


import os

"""
https://download.pytorch.org/models/vgg19-dcbb9e9d.pth
"""


def create():
    for i in os.listdir("contents"):
        for j in os.listdir("styles"):
            os.system("python gen.py "
                      # "--epsilon 0.0005 "
                      "--max_iter 150 "
                      "--alpha 1 "
                      f"--c_img contents/{i} "
                      f"--s_img styles/{j} "
                      f"--r_img results/{i[:-4] + j} "
                      "--im_size 720")


if __name__ == '__main__':
    create()
