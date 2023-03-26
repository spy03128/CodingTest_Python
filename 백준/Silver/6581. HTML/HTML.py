import sys
tmp = ""
while True:
    try:
        st = input()
        for x in st.split():
            if x == "<br>":
                print(tmp.strip())
                tmp = ""
            elif x == "<hr>":
                if len(tmp)>0:
                    print(tmp.strip())
                tmp = ""
                print("-"*80)
            elif len(tmp+x) >=80:
                print(tmp.strip())
                tmp = x+ " "
            else:
                tmp+=x+" "
    except:
        break

print(tmp.strip())