# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        key=0
        for item in array:
            key^=item
        index=0
        while(key&1==0):
            key>>=1
            index+=1
        a,b=0,0
        for item in array:
            if self.is_bit_1(item,index):
                a^=item
            else:
                b^=item
        return [a,b]


    def is_bit_1(self,item,index):
        c=0
        while(c<index):
            item>>=1
            c+=1
        return item==1


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        key = 0
        for item in array:
            key ^= item
        index = 0
        while (key & 1 == 0):
            key >>= 1
            index += 1
        a = 0
        b = 0
        for item in array:
            if self.is_bit_1(item, index):
                a ^= item
            else:
                b ^= item
        return [a, b]

    def is_bit_1(self, item, index):
        c = 0
        while (c < index):
            item >>= 1
            c += 1
        return item & 1 == 1

