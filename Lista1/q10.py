import os

path = input("Digite o nome da pasta: ")

# check whether directory already exists
if not os.path.exists(path):
  os.mkdir(path)
  print("Folder %s created!" % path)
else:
  print("Folder %s already exists" % path)