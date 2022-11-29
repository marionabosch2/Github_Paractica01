def trapezi(): # 7
    print("Càlcul de l'àrea i del perímetre d'un trapezi")
    B = float(input("Base major B = "))
    b = float(input("Base menor b = "))
    a = float(input("Costat a = "))
    c = float(input("Costat c = "))
    h = float(input("Alçada = "))
    area = (B + b) * h * (1/2)
    perimetre = B + b + a + c
    return area, perimetre

a,b = trapezi()
print("L'àrea és: ",a," i el perimetre és: ",b)