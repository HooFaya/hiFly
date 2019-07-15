def fix_time(s):
    m31=["1","3","5","7","8","10","12"]
    m30=["4","6","9","11"]
    m28=["2"]
    tmp=s.split(" ")
    x=tmp[0].split("-")
    y=tmp[1].split(":")
    #时，分，秒为24，60，60
    if int(y[-1])==60:
        y[-1]="0"
        y[-2]=str(int(y[-2])+1)
    if int(y[-2])>=60:
        y[-2]="0"
        y[-3]=str(int(y[-3])+1)
    if int(y[-3])>=24:
        y[-3]="0"
        x[-1]=str(int(x[-1])+1)
    if int(x[-1])>31:
        x[-1]="1"
        x[-2]=str(int(x[-2])+1)
    if int(x[-2])>12:
        x[-2]="1"
        x[-3]=str(int(x[-3])+1)
    #每个月不同的天数，闰年和非闰年
    if x[1] in m30:
        if int(x[2])>30:
            x[2]="1"
            x[1]=str(int(x[1])+1)
    if x[1] in m28 and int(x[0])%4 != 0:
        if int(x[2])>28:
            x[2]="1"
            x[1]=str(int(x[1])+1)
    if x[1] in m28 and int(x[0])%4 == 0:
        if int(x[2])>29:
            x[2]="1"
            x[1]=str(int(x[1])+1)
    pre="-".join(x)
    after=":".join(y)
    return pre+" "+after
print(fix_time("2008-2-29 1:60:22"))