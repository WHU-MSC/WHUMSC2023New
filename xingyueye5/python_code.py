import os

path='D:\Desktop\Files\Files'
files = os.listdir(path)
for file in files:
    file_path=os.path.join(path,file)
    with open(file_path) as f:
        data=f.readlines()
        if data[0]=="MSC2023":
            print(file)



