def find_num(n):
    res=[]
    for i in range(2,n+1):
        if is_prime(i):
            res.append(i)
    return  res

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


print(find_num(10))