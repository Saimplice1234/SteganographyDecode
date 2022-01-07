rgb=(
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
)

hidden_rgb=(
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],
)

def display_initial_value():
    i=0
    for x in range(0,len(rgb)):
        i+=1
        r=rgb[x][0]
        g=rgb[x][1]
        b=rgb[x][2]

        if i < 10:
            print("0{} pixel initial : RGB({},{},{})".format(
                i,r,g,b,
            ))
        else:
            print("{} pixel initial : RGB({},{},{})".format(
                i,r,g,b,
            ))
    print("\n")
    pass

display_initial_value()

while True:

    pix=int(input("Which pixel you want to provide ? : "))
    
    if pix <= 16:

        for entry in range(0,3):

            sec=""
            if entry == 0:
                sec="red"
            elif entry == 1:
                sec="green"
            else:
                sec="blue"

            pix_entry=int(input("For the {} pixel enter the {} value : ".format(pix,sec)))

            if pix_entry > 255:
                print("\n[-] RGB is not > 255")
                print("[-] Rechoose the {} pixel and redefine the {} value ".format(pix,sec))
            else:
                rgb[pix-1][entry]=pix_entry
            
            r=rgb[pix-1][0]
            g=rgb[pix-1][1]
            b=rgb[pix-1][2]

            print("{} pixel hidden: RGB({},{},{})\n".format(
                pix,r,g,b
            ))
        
        rq=input("You want to continue the process (Y) or (N) ? :")
        
        if rq == "N" or rq == "n":
            break

        display_initial_value()  

    else:
        print("Image 4x4 is not > 16 pixels\n")

def binary_leading_process(n):

    div,binary=[n],[]
    q=0
    temp=n
    pow,hidden_value=1,0
    digits,digits_decimal=[],[]

    while q != 1 and n != 1 and n!=0:
        q=int(temp/2)
        temp=q
        div.insert(0,q)
        if q == 1:
            break
    pass

    for x in div:
        if x % 2 == 0:
            binary.append(0)
        else:
            binary.append(1)

    least_significant=0

    if len(binary) == 8:
        least_significant=binary[4:]
        
        for x in range(0,4):
            least_significant.append(0)

    else:
        while len(binary) < 8:
            binary.insert(0,0)
        least_significant=binary[4:]
        
        for x in range(0,4):
            least_significant.append(0)
            
    pass

    least_significant=int("".join(str(elem) for elem in least_significant))

    for x in str(least_significant):
        if int(x) > 1 or int(x) < 0:
            break
        else:
            digits.append(int(x))

    digits=digits[::-1]

    for x in digits:
        digits_decimal.append(x*pow)
        pow*=2

    for x in  digits_decimal:
        hidden_value+=x

    return hidden_value
    pass
    
def search_hidden():
    for x in range(0,len(rgb)):
        for y in range(0,3):
            decoded=binary_leading_process(rgb[x][y])
            hidden_rgb[x][y]=decoded
    

search_hidden()

def display_hidden_initial():
    i=0
    for x in range(0,len(hidden_rgb)):
        i+=1
        r=rgb[x][0]
        g=rgb[x][1]
        b=rgb[x][2]
        r_h=hidden_rgb[x][0]
        g_h=hidden_rgb[x][1]
        b_h=hidden_rgb[x][2]
        if i < 10:
            print("0{} pixel initial: RGB({},{},{})".format(
                i,r,g,b,
            ))

            print("0{} pixel hidden: RGB({},{},{})\n".format(
                i,r_h,g_h,b_h
            ))
        else:
            print("{} pixel initial: RGB({},{},{})".format(
                i,r,g,b,
            ))

            print("{} pixel hidden: RGB({},{},{})\n".format(
                i,r_h,g_h,b_h
            ))

display_hidden_initial()
