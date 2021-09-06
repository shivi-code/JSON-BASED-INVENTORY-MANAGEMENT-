#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
fd = open("records.json",'r')
r = fd.read()
fd.close()

record = json.loads(r)


# In[2]:


record


# In[ ]:


# add a new item in inventory
prod_id = str(input("Enter product id:"))
name = str(input("Enter name:"))
pr = int(input("Enter price:"))
qn = int(input("Enter quantity:"))
taste = str(input("Enter taste of item :"))
weight = int(input("Enter weight of the item in gram:"))


record[prod_id] = {'name': name, 'price': pr, 'qty': qn,'taste':taste,'weight':weight}

js = json.dumps(record)

fd = open("records.json",'w')

fd.write(js)
fd.close()


# In[ ]:


record


# In[ ]:


#purchase a item
ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))


print("Product: ", record[ui_prod]['name'])
print("Price: ", record[ui_prod]['price'])
print("----------------------------------------")
print("Billing Amount: ", record[ui_prod]['price'] * ui_quant)
print("----------------------------------------")

record[ui_prod]['qty'] = record[ui_prod]['qty'] - ui_quant


# In[ ]:



js = json.dumps(record)

fd = open("record.json",'w')
fd.write(js)
fd.close()


# In[ ]:


record


# In[ ]:


# update a quantity and price of item
prod_id= input("Enter product ID: ")
pr = int(input("Enter price of item: "))
qty= int(input("Enter quantity of product: "))  
record[prod_id]['price'] = pr;
record[prod_id]['qty'] = qty;

js = json.dumps(record)

fd = open("records.json",'w')
fd.write(js)
fd.close()


# In[8]:


record


# In[7]:


#remove an item
prod_id = input("enter a product id")
if(prod_id in record):
    sure = input("are you sure you want to remove that item(y/n)?")
    if(sure=='y' or sure=='Y'):
        record.pop(prod_id)
        print("item Sucessfully removed!")
    else:
        print("sorry,we do'nt have such a item!")
        


# In[16]:


js = json.dumps(record)

fd = open("records.json",'w')
fd.write(js)
fd.close()
record


# In[ ]:


#enquiry about the product
prod_id = input("enter a product_id ")
if(prod_id in record):
    print("DETAILS ABOUT THE PRODUCT.........")
    print( "NAME: ",record[prod_id]['name'])
    print("PRICE: ",record[prod_id]['price'])
    print("QUANTITY:",record[prod_id]['qty'])
    print("TASTE:  ",record[prod_id]['taste'])
    print("WEIGHT: ",record[prod_id]['weight'])
else:
    print("sorry we dont have such item")
    


# In[5]:


#checkout the quantity
prod_id = str(input("enter"))

if(record[prod_id]['qty']<10):
        print("quantity of  product ",record[prod_id]['name'],"is ",record[prod_id]['qty'])
        print(record[prod_id]['name']," :need to refill the product..........." )
else:
    print("quantity of  product ",record[prod_id]['name'],"is ",record[prod_id]['qty'])
    print(record[prod_id]['name']," :it is in sufficient amonut  in shop......")
        
    
        
        


        


# In[4]:


#list of all product and their prices 
n = len(record)
print("LIST OF PRODUCTS AND THEIR PRICES....")
print("PRODUCT : PRICE")
k = 1000 
l = k+n
prod_id = '1000'
for i in range(k,l,1):
    print(record[prod_id]['name'],":",record[prod_id]['price'])
    t = (int)(prod_id)
    t = t+1
    prod_id  =(str)(t)


# In[ ]:



    
    
    
    

