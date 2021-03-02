# OPERATORLAR
# Riyazi operatorlar 
# + , - , * , /, % ,** ,//
def arithmeticOperators():
    print(6+7) # 13
    # String tipləri də toplamaq mümkündür(bir-birinə yapışır)
    print("Sadigzade "+"Mehemmed")
    print(6-7) # -1
    print(6*7) # 42
    # int tipi ilə str tipini vurmaq mümkündür
    print("Mehemmed"*3) # MehemmedMehemmedMehemmed
    print(9/2) # 4.5 float
    # Qalığı almaq üçün % işlədə bilərik :
    print(17%3) # 2 int
    print(17.5%3) # 2.5 float
    # Tam hissəni almaq üçün // istifadə edə bilərik
    print(78//10) # 7 int
    # Qüvvətə yüksəltmək üçün ** istifadə olunur
    print(2**4) # 16 int
    print(7.5**2) # 56.25 float

# Təyin operatorları
def assignmentOperators():
    x=5
    x=x+5 # 5+5 = 10
    x+=5 # 10+5 = 15
    print(x) # 15
    x-=7 # 15 - 7 = 8
    print(x) # 8
    x*=4 # 8*4  = 32
    print(x) # 32
    x/=2 # 32/2 = 16.0
    print(x) # 16.0 float
    x=int(x) # 16.0 -> 16
    x**=2  # 16*16 = 256
    print(x) # 256
    x%=40 # 256%40=16
    print(x) # 16
    x//=5 # 16//5 = 3
    print(x) # 3
# Müqayisə operatorları 
def comparisonOperators():
    # Müqayisə operatorları boolean dəyər qaytarır
    # == Bərabər olmağını yoxlayır
    print(5==6) # False
    # != Bərabər olmamağını yoxlayır
    print(5!=6) # True
    # >,<,>=,<=
    print(6>5) # True
    print(7<3) # False
    print(6>=6) # True
    print(7<=8) # True
#Məntiqi operatorlar 
def logicalOperators():
    #and
    # and halında  bütün şərtlər də true olarsa,nəticə true olur :
    print(5>3 and 7<9 and 5<8) #true
    print(6>7 and 7<9) # false
    #or
    #or halında şərtlərdən biri true olsa,kifayətdir :
    print(5>8 or 7<9) #true
    #not
    #not halında isə  dəyər tərsinə çevirilir
    print(not(6>7 and 7<9)) # true
    print(not(not(6>7) and 7<9 ))  # false
#Üzvlük operatorları

def membershipOperators():
    # Bir elementin hansısa massivin içində olub-olmadığını yoxlamaq üçün istifadə olunur
    arr_names= ["Mehemmed","Gulcicek","Hikmet","Benovshe"]
    print("Mehemmed" in arr_names) # Mehemmed stringinin massivin içində olması şərtini yoxlayır (true)
    print("Ay" in arr_names) # false
    print("Ay" not in arr_names) # true
