def raqamni_tekshirish(raqam):
    return str(raqam) == str(raqam)[::-1]

def palindrom_raqam_tekshirish(raqam):
    original = raqam
    teskari = 0
    
    while raqam > 0:
        qoldiq = raqam % 10
        teskari = teskari * 10 + qoldiq
        raqam = raqam // 10
    
    return original == teskari

# Misollar
print(palindrom_raqam_tekshirish(121))  # True
print(palindrom_raqam_tekshirish(123))  # False
print(palindrom_raqam_tekshirish(12321))  # True
print(palindrom_raqam_tekshirish(12345))  # False

# Misollar
# print(raqamni_tekshirish(121))  # True
# print(raqamni_tekshirish(12521))  # False


s = [1,2,3,4,5,6]
print(s[::1])