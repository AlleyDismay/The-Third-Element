def save(treasure):
    f = open("save.dat", "w")
    gems = treasure.gems
    if gems["earth"]: f.write("earth ")
    if gems["fire"]: f.write("fire ")
    if gems["water"]: f.write("water ")
    f.write("\n")
    f.write(str(treasure.health)+"\n")
    f.write(str(treasure.money)+"\n")
    for i in treasure.collectedItems:
        f.write(i + " ")
    f.write("\n")
    f.close()