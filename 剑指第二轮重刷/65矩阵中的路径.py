# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while (True):

            res.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix = self.turn_matrix(matrix)
        return res

    def turn_matrix(self, matrix):
        new = []
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            new.append(tmp[:])
        new.reverse()
        return new
