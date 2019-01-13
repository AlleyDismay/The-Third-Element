def saveStats(earth, fire, water, health, money, items):
    f = open("save.dat", "w")
    if earth: f.write("earth ")
    if fire: f.write("fire ")
    if water: f.write("water ")
    f.write("\n")
    f.write(str(health)+"\n")
    f.write(str(money)+"\n")
    for i in items:
        f.write(i + " ")
    f.write("\n")
    f.close() 
