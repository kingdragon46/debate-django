import random
import string

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    print(max(s1))
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    ch = int(input('Press 1 for simple password and 2 for complex password: \n'))
    if ch == 1:
        plen = int(input('Enter desired password length: '))
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        print("".join(random.sample(s,plen)))
    elif ch == 2:
        plen = int(input('Enter desired password length: '))
        llen = int(input('How many lowercase characters desied? : '))
        ulen = int(input('How many uppercase character desired?  '))
        nlen = int(input('How many numeric length desired? : '))
        slen = int(input('How many password length desired? : '))
        tlen = llen+ulen+nlen+slen
        if plen == tlen:
            s = []
            s.extend(list(random.sample(s1,llen)))
            s.extend(list(random.sample(s2,ulen)))
            s.extend(list(random.sample(s3,nlen)))
            s.extend(list(random.sample(s4,slen)))
            for i in range(5):
                print("Password",i, ": ", "".join(random.sample(s,plen)))
        else:
            pass
    else:
        pass