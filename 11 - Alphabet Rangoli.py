def print_rangoli(size):
    width = (size*4)-3
    for j in range(1,size):
        s = []
        for i in range(j):
            s.append(chr(96+size-i))
        for k in range(i, 0, -1):
            s.append(chr(96+size-k+1))
        st = '-'.join(str(p) for p in s)
        print(st.center(width,"-"))
        
    for j in range(size):
        s = []
        for i in range(size-j, 0, -1):
            s.append(chr(96+i+j))
        while(i<size-j):
            i += 1
            s.append(chr(96+i+j))
        st = '-'.join(str(p) for p in s)
        print(st.center(width,"-"))