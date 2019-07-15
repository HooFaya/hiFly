
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput:
            return
        if k>len(tinput):
            return
        for i in range(k):
            for j in range(len(tinput)-i):
                if tinput[j]<tinput[j+1]:
                    tinput[j],tinput[j+1]=tinput[j+1],tinput[j]
        return tinput[-k:]

