dia = int(input("Ingresa tu dia de nacimiento: "))
mes = int(input("Ingresa tu numero de mes de nacimiento:"))
if (((dia >= 21 and dia <= 31) and mes <= 3) or (mes ==4 and (dia >=1 and dia <=20))):
    print("aries")
elif (((dia >= 21 and dia <= 30) and mes <= 4) or (mes ==5 and (dia >=1 and dia <=20))):
    print("tauro")
elif (((dia >= 21 and dia <= 31) and mes <= 5) or (mes ==6 and (dia >=1 and dia <=21))):
    print("geminis")
elif (((dia >= 22 and dia <= 30) and mes <= 6) or (mes ==7 and (dia >=1 and dia <=22))):
    print("cancer")
elif (((dia >= 23 and dia <= 31) and mes <= 7) or (mes ==8 and (dia >=1 and dia <=22))):
    print("leo")
elif (((dia >= 23 and dia <= 31) and mes <= 8) or (mes ==9 and (dia >=1 and dia <=22))):
    print("virgo")
elif (((dia >= 23 and dia <= 30) and mes <= 9) or (mes ==10 and (dia >=1 and dia <=22))):
    print("libra")
elif (((dia >= 23 and dia <= 31) and mes <= 10) or (mes ==11 and (dia >=1 and dia <=22))):
    print("escorpio")
elif (((dia >= 23 and dia <= 30) and mes <= 11) or (mes ==12 and (dia >=1 and dia <=21))):
    print("sagitario")
elif (((dia >= 22 and dia <= 30) and mes <= 12) or (mes ==1 and (dia >=1 and dia <=20))):
    print("capricornio")
elif (((dia >= 21 and dia <= 30) and mes <= 1) or (mes ==2 and (dia >=1 and dia <=18))):
    print("acuario")
elif (((dia >= 19 and dia <= 29) and mes <= 2) or (mes ==3 and (dia >=1 and dia <=20))):
    print("piscis")
