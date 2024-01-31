#Part 1
#Level 1

customer = ['James','John','Robert','Mary','Patricia','Jennifer']
salary = [155000,755000,455000,1255000,635000,575000]
taxes = [55800,317100,182000,451800,171450,71400]

#taxrate = taxes/salary*100
count = 0
for i in customer:
    taxrate = taxes[count]/salary[count] * 100
    if(taxrate < 30):
        print(f"Fraud detected on {i} with a taxrate of {taxrate}")
    count += 1



