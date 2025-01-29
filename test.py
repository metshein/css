#18.12.2024 Yuna Antonenko
#KT
#10 12 15


#10. Kaugushüpe




# #12. Eurokalkulaator


#15. Temperatuurid
for rida in open('temperatuurid.txt', 'r', encoding= 'UTF-8'):
    osad = rida.split()
    kuu = osad[0]
    temp = map(int, osad[2:])
    print(f"{kuu}: {max(temp)}")
