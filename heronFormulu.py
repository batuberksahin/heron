import math

def heron(x, y, z):
    u = (x + y + z) / 2

    if (u-x) <= 0 or (u-y) <= 0 or (u-z) <= 0:
        return "Bu bir üçgen degil!"
    else:
        return round(math.sqrt(u * (u - x) * (u - y) * (u - z)), 3)


while 1:
    try:

        giris = input("Üçgenin kenarlarının uzunluklarını giriniz: ")
        kenarlar = giris.split(",")

        tamsayiKenarlar = [1, 1, 1];

        hataver = 0
        sira = 0
        for i in kenarlar:
            try:
                tamsayiKenarlar[sira] = int(kenarlar[sira])
                sira += 1
            except ValueError:
                hataver = 1
                break

        if hataver == 1:
            print("Hatalı kenar uzunlukları girdiniz!")
            hataver = 0
        else:
            print("Üçgenin alanı: " + str(heron(tamsayiKenarlar[0], tamsayiKenarlar[1], tamsayiKenarlar[2])))
            hataver = 0

    except:

        print("oha.")
