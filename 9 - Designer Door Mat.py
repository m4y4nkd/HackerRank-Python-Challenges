str = input()
m, n = str.split()
m, n = int(m), int(n)
st = ".|."
for s in range(1,m,2):
    stf = st * s
    print(stf.center(n,"-"))
print("WELCOME".center(n,"-"))
for s in range(s,0,-2):
    stb = st * s
    print(stb.center(n,"-"))