dostlar=['Ehmed','Memmed','Sabir','Efsane','Qurban']
index=-1
amount=0
for i in dostlar:
    index=index+1
    if(i.count('a')):
        amount=amount+1
        
        print(f'index:{index}')

print(f'Amount of string with "a" : {amount}')