f = open(r"D:\ad.txt","r+")
print(f.read())
f.close()
f1 = open(w"D:\ad.txt","w+")
f1.write("abdi")
f1.close()
f2 = open(r"D:\ad.txt","r+")
print(f2.read())
f2.close()