import os
import zipfile



os.mkdir("Textos")

for i in range(3):
    with open(f"Textos/arquivo{i}.txt", "w") as file:
        file.write("Python Essencial")

with zipfile.ZipFile("Textos.zip", "w", compresslevel=9, compression=zipfile.ZIP_DEFLATED) as zip:
    for i in range(3):
        zip.write(f"Textos/arquivo{i}.txt")