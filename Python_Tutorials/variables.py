#Python-da bir çox dillərdən fərqli olaraq dəyişənə dəyər verərkən tipini yazmaq lazım olmur
x = 5 # x bir integer-tam ədəddir
y = "Mehemmed" # y bir string - yazı tipidir
z = 5.0 # z bir float - kəsr ədəd tipidir
# TİP DƏYİŞİMİ
x_1 = str(5) # 5-> "5"
y_1 = int("5") # "5" -> 5
z_1 = float("5") # "5" -> 5.0 (Float kəsr ədəd deməkdir)
print(type(z_1)) # Dəyişənin tipinə burdan baxa bilərik 
# ******************************************************
# Dəyişən adları aşağıdakı kimi ola  bilər :
"""
myvar
myVar
my_var
_my_var
MYVAR
myvar2
"""
# Aşağıdakı kimi ola bilməz
"""
my-var
my var
1myvar
"""
# Əsasən aşağıdakı üç stil daha çox işlədilir
myVar = "Salam"
MyVar = "Salam"
my_var = "Salam"
# Birdən çox dəyişəni eyni anda təyin etmək üsulları
var1,var2,var3="Mehemmed","Sadigzade",19
print(var1) # Mehemmed
print(var2) # Sadigzade
print(var3) # 19
#Eyni dəyəri birdən çox dəyişənə ötürmək 
var1_1 = var2_1 = var3_1 ="Mehemmed"
print(var1_1) # Mehemmed
print(var2_1) # Mehemmed
print(var3_1) # Mehemmed
# Massivdən müvafiq olaraq dəyər ötürmək(Dəyişənlərin sayı massivdəki elementlərin sayına bərabər olmalıdır)

variables = [1,2,3]
var1_3,var2_3,var3_3 = variables
print(var1_3) # 1
print(var2_3) # 2
print(var3_3) # 3
variables = [1,2,3,4,5,6,7,19 ]
var1_3,var2_3 = variables[6:8]
print(var1_3) # 7
print(var2_3) # 19
