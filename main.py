dcoded = ""
with open("text.txt",'r') as t:
    for line in t:
        for word in line.split():
            a = chr(int(word))
            dcoded += str(a)
print(dcoded)
            

            
