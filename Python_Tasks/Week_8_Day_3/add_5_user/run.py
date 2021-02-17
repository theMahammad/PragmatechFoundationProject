
def getUserData():
    name = input(' please enter the name ')
    surname = input(' please enter the surname ')
    age = input(' please enter the age ')
    return{
        'name' : name,
        'surname' : surname,
        'age' : age
    }

def add5User():
    
    con=open('userdata.txt','a')
    for i in range(5):
        print(f'Add {i+1}.user')
        userData = getUserData()
        

    
        con.write(
            f"""Name : {userData['name']}   |    Surname : {userData['surname']}    |  Age : {userData['age']} \n""")

    con.close()

add5User()