a = 1
b = 2
c = 3

la = 0;
lb = 0;
lc = 0;

prod = 0
num = 1000

while prod != num:
    for a in range (1,num):
        for b in range(a,num):
            for c in range(b,num):
                if (a*a + b*b) == c*c:
                    la = a
                    lb = b
                    lc = c
                    msum = a + b +c
                    if(msum == num):
                        prod = la*lb*lc
                        print "a: %d, b: %d, c: %d\n" % (la,lb,lc)
                        print "num %d\n" % num
                        print "prod %d\n" % prod
