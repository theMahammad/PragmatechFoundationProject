# String dəyərləri həm tək dırnaqlar ,həm də cüt dırnaqlar arasında yazıla bilər
var = "Mehemmed"
var_1 = 'Mehemmed'
print(var==var_1) # true (==) müqayisə üçündür
# Çox sətirli string təyin etmək :
multiLineString = """Salam
Necesen
Gozel"""
multiLineString_1 = '''Salam
Necesen
Gozel'''
print(multiLineString)
# Stringlər həm də bir massivdir :
str_1 = "Men bir massivem"
print(str_1[1]) # e
