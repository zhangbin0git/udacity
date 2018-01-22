#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-01-23 1:18
# @Author  : Zhang Bin
# @Site    : home
# @File    : parameterization.py
# @Software: PyCharm

class Parameterization():
    """根据基准点和方向向量参数化解集"""
    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = ('The basepoint and '
    'direction vectors shouldn all live in the same dimension')
    def __init__(self, basepoint, direction_vectors):
        """初始化类"""
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension
        except AssertionError:
            raise Exception(BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)