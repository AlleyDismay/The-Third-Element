def saveStats(self):
    f = open("save.dat", "w")
    gems = self.treasure.gems
    if gems["earth"]: f.write("earth ")
    if gems["fire"]: f.write("fire ")
    if gems["water"]: f.write("water ")
    f.write("\n")
    f.write(str(self.treasure.health)+"\n")
    f.write(str(self.treasure.money)+"\n")
    for i in self.treasure.collectedItems:
        f.write(i + " ")
    f.write("\n")
    f.close()
