import os


os.mkdir("temp")
with open("temp/temp.txt", "w") as file:
    file.write("Arquivo temporário")