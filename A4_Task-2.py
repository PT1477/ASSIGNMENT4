
f1 = open('output.txt','w')
a = f1.write(input("Enter a text to write in a file :"))
print("Data written successfully in output.txt")
f1.close()

fa = open('output.txt','a')
a = fa.write(input("Enter a text to write in a file :"))
print("Data Successfully appended")
fa.close()

print("Final content of output .txt")
fr = open('output.txt','r')
r=fr.read()
print(r)
