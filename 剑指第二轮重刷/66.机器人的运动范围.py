"""
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        flag=[[0]*cols for i in range(rows)]
        return  self.helper(0,0,flag,threshold, rows, cols)

    def rc2num(self,i,j):
        res=0
        for k in str(i):
            res+=int(k)
        for k in str(j):
            res+=int(k)
        return res
    def helper(self,i,j,flag,threshold, rows, cols):
        if i<0 or j<0 or i>=rows or j>=cols or flag[i][j]==1 or self.rc2num(i,j)>threshold:
            return 0
        flag[i][j]=1
        return 1+self.helper(i-1,j,flag,threshold, rows, cols)\
                +self.helper(i,j-1,flag,threshold, rows, cols) \
                +self.helper(i, j+1, flag, threshold, rows, cols) \
                +self.helper(i+1, j, flag, threshold, rows, cols)
s=Solution()
print(s.movingCount(5,10,10))