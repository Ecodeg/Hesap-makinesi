class Calculator():
    def __init__(self):
        result=0

    def toplama(self,num1,num2):
        result=num1+num2
        print("Sonuç: ",result)

    def cikarma(Self,num1,num2):
        result=num1-num2
        print("Sonuç: ",result)

    def carpma(Self,num1,num2):
        result=num1*num2
        print("Sonuç: ",result)

    def bolme(self,num1,num2):
        if num2==0:
            print("Sıfıra bölme hatası!")
        else:
            result=num1/num2
            print("Sonuç: ",result)


while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("0. Çıkış")

    secim=int(input("Lütfen yapmak istediğiniz işlemi seçiniz (0-4): "))

    calculator=Calculator()

    if secim==1:
        num1=int(input("1. sayıyı giriniz: "))
        num2=int(input("2. sayıyı giriniz: "))
        calculator.toplama(num1,num2)
    elif secim==2:
        num1=int(input("1. sayıyı giriniz: "))
        num2=int(input("2. sayıyı giriniz: "))
        calculator.cikarma(num1,num2)
    elif secim==3:
        num1=int(input("1. sayıyı giriniz: "))
        num2=int(input("2. sayıyı giriniz: "))
        calculator.carpma(num1,num2)
    elif secim==4:
        num1=int(input("1. sayıyı giriniz: "))
        num2=int(input("2. sayıyı giriniz: "))
        calculator.bolme(num1,num2)
    elif secim==0:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Yanlış seçim yaptınız!")

















