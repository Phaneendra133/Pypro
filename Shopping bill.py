#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum = 0
while True:
    price=input("please enter price of the product:\n")
    if price!='q':
        sum=sum+int(price)
        print(f"total bill so far: {sum}")
    else:
        print(f"total bill: {sum}, Thank you for shopping with us")
        break  


# In[ ]:




