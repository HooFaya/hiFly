"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

"""
插排的思想
定义一个函数，使两个数被组合并比较，再插排
"""
class Solution:
    def PrintMinNumber(self, numbers):
        for i in range(1,len(numbers)):
            j=i
            while(j>0):
                if self.compare(numbers[j-1],numbers[j]):
                    numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
                    j-=1
                else:
                    break
        return "".join(list(map(str,numbers)))



    def compare(self,x1,x2):
        x1=str(x1)
        x2=str(x2)
        x1_x2=int(x1+x2)
        x2_x1=int(x2+x1)
        if x1_x2>x2_x1:
            return 1
        else:
            return 0
