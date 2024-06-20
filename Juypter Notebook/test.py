fd = open('inventory3.txt','w')

fd.close()
d = open('inventory3.txt','r')
text = d.read()
d.close()


products = text.split('\n')
usr_id = input("enter product id:")
usr_qn = input("enter the quantity :")
upd_lst  = []
for product in products:
    pro_detail = product.split(',')
    if(pro_detail[0] == usr_id):
        print('-'*30)
        print("Product :",pro_detail[1])
        print("Price :",pro_detail[2])
        print("Quantity:",usr_qn)
        print('-'*30)
        print("Bill :",int(pro_detail[2]) * int(usr_qn))
        pro_detail[3] = str(int(pro_detail[3]) - int(usr_qn))
        print(pro_detail[3])
    
    upd_lst.append(pro_detail)

new_lst = []
for i in upd_lst:
    prod = i[0] +','+i[1] +','+ i[2] +','+ i[3] 
    
    new_lst.append(prod)
   
print(new_lst)

fd = open('inventory2.txt','w')

for i in new_lst:
    fd.write(i)
fd.close() 