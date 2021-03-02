# DATA TİPLƏRİ
# Yazı tipi : str
string = "Text"

# Ədəd tipi : int,float
integer = 5 # int tipi tam ədədlər üçün işlədilir
flt = 5.0 # float tipi kəsr ədədlər üçün istifadə olunur

# Toplu,massiv tiplər : list,tuple,range
listing = [5,6,7,9,"Mehemmed"]
tuples = (5,67,8,"Elovset") 
# bu siyahılarda hər bir element 0-dan başlayaraq bir indeks dəyərini sırayla özünə götürür
print(listing[4]) # Mehemmed
ranging = range(7,11) # range aralıq deməkdir,verilən iki ədəd arasındakı ədədləri siyahıya yığır
print(ranging[1]) # 8

# Mapping (Xəritələmə) tipləri : dict 
mapping = {
    "ad" : "Mehemmed",
    "soyad" : "Sadigzade"
}
print(mapping["ad"]) # Mehemmed
# boolean tipləri : bool
boolean =  True
boolean_1 = False 
# boolean tipləri doğru(true) və yanlış(false) dəyərləri alır
