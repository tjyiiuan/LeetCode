# -*- coding: utf-8 -*-
"""
661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution:
    def imageSmoother(self, matrix):
        res = []
        row_max = len(matrix)
        col_max = len(matrix[0])

        for r_ind, row in enumerate(matrix):
            new_row = []
            for c_ind, val in enumerate(row):
                res_val = []

                for cur_row_ind in [r_ind - 1, r_ind, r_ind + 1]:
                    if cur_row_ind < 0 or cur_row_ind >= row_max:
                        continue
                    for cur_col_ind in [c_ind - 1, c_ind, c_ind + 1]:
                        if cur_col_ind < 0 or cur_col_ind >= col_max:
                            continue

                        res_val.append(matrix[cur_row_ind][cur_col_ind])
                new_row.append(int(sum(res_val)/ len(res_val)))

            res.append(new_row)

        return res
