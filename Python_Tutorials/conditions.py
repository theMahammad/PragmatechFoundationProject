#Şərtlər
#Bir əməliyyatı müəyyən şərt ödəndikdə etmək istəyiriksə,bunun üçün köməyimizə "condition" anlayışı yetir :
age = input("Yaşınızı daxil edin : ") # İstifadəçidən dəyər almaq üçün "input()" istifadə edirik
age = int(age) # Daxil etdiyimiz dəyər string tipində olur,onu integer-ə çeviririk
# **************************************
# if age >= 18:
#    print("Siz bu iş üçün uyğunsunuz")
# else:
#     print("Siz bu iş üçün kiçiksiniz")    
# indi isə başqa bir şərt qoyaq
# *************************************
# if age>=18:
#     print("Siz bu iş üçün uyğunsunuz")
# elif age<=0:
#     print("Yaşınızı düzgün daxil edin") # Əgər ilk şərt ödənməsə,qoyduğumuz ikinci şərti yoxlayacaq
# else:
#     print("Siz bu iş üçün uyğun deyilsiniz")
# İÇ-İÇƏ ŞƏRTLƏR
boy = int(input("Boyunuzu daxil edin (cm) : "))
if age>=18:
    if boy>=180: # Əgər yaş şərti uyursa,boy şərtini də yoxlayır
        print("Yaşınız da uyur,boyunuz da")
    else:
        print("Yaşınız uysa da,boyunuz uymur")
elif age <= 0:
    print("Yaşınızı düzgün daxil edin!")
else:
    print("Siz bu iş üçün uyğun deyilsiniz,təşəkkürlər")       

    
