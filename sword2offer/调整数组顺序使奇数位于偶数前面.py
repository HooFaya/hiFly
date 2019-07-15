# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。


class Solution:

    """
    此题python一行代码能写完，
    return sorted(array,key=lambda x: x%2==0)
    但是插入排序的思想很重要，所以以下代码要懂思路
    因为是先奇后偶，所以我们遇到一个奇数就往前面插

    """
    def reOrderArray(self, array):
        for i in range(1, len(array)):
            j = i
            if array[j] % 2 == 1:
                while (j > 0):
                    if array[j - 1] % 2 == 0:
                        array[j], array[j - 1] = array[j - 1], array[j]
                        j -= 1
                    else:
                        break

        return array
