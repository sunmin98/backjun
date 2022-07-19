
a = int(input())
length = len(str(a))

num_list = list(map(int, str(a)))



if a>999999:
    for i4 in range(0, 10):  # 1000000자리
        for i3 in range(0, 10):  # 100000자리
            for i2 in range(0, 10):  # 10000자리
                for i1 in range(0, 10):  # 1000자리
                    for i in range(0,10) :  #100자리
                        for n in range(0,10) :  #10자리
                            for m in range(0,10) :  #1자리리
                                if a == i4*10^6+i3*10^5+i2*10^4+i1*1000+i*100+n*10+m+i+n+m+i1+i2+i3+i4 :
                                    print(i4*10^6+i3*10^5+i2*10^4+i1*1000+i*100+n*10+m)
                                    quit()

if a>99999:
    for i3 in range(0, 10):  # 100000자리
        for i2 in range(0, 10):  # 10000자리
            for i1 in range(0, 10):  # 1000자리
                for i in range(0,10) :  #100자리
                    for n in range(0,10) :  #10자리
                        for m in range(0,10) :  #1자리리
                            if a == i3*10^5+i2*10^4+i1*1000+i*100+n*10+m+i+n+m+i1+i2+i3 :
                                print(i3*10^5+i2*10^4+i1*1000+i*100+n*10+m)
                                quit()

if a>9999:
    for i2 in range(0, 10):  # 10000자리
        for i1 in range(0, 10):  # 1000자리
            for i in range(0,10) :  #100자리
                for n in range(0,10) :  #10자리
                    for m in range(0,10) :  #1자리리
                        if a == i2*10^4+i1*1000+i*100+n*10+m+i+n+m+i1+i2 :
                            print(i2*10^4+i1*1000+i*100+n*10+m)
                            quit()

if a>999:
    for i1 in range(0, 10):  # 1000자리
        for i in range(0,10) :  #100자리
            for n in range(0,10) :  #10자리
                for m in range(0,10) :  #1자리리
                    if a == i1*1000+i*100+n*10+m+i+n+m+i1 :
                        print(i1*1000+i*100+n*10+m)
                        quit()

if a>99:
    for i in range(0,10) :  #100자리
        for n in range(0,10) :  #10자리
            for m in range(0,10) :  #1자리리
                if a == i*100+n*10+m+i+n+m :
                    print(i*100+n*10+m)
                    quit()
if a>=9:
    for n in range(0, 10):  # 10자리
        for m in range(0, 10):  # 1자리리
            if a == n * 10 + m  + n + m:
                print(n * 10 + m)
                quit()

elif a<9:
    for m in range(0, 10):  # 1자리리
        if a == m:
            print(m)
            quit()

else: print(0)