# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        B=[1 for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if j!=i:
                    B[i]*=A[j]
        return B
