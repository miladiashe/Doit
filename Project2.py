n1=35.6354
n2=82.8192
n3=3

result="n1 = {0}  n2 = {1}  n3={2}\n\n".format(n1, n2, n3)
result=(result+("n1+n2 = {0:10.2f}    n1-n2 ={1:10.2f}\nn1*n2 = {2:10.2f}    n1/n2 ={3:10.2f}\nn1**n3 ={4:10.2f}    n1%n2 ={5:10.2f}\nn2//n1 ={6:10.2f}"
                .format(n1+n2, n1-n2, n1+n2, n1/n2, n1**n3, n1%n2, n2//n1)))

print(result)
