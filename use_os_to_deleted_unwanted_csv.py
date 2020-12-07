import os
print(os.getcwd())
path= "C:\\859K_sl559\\Data\\ModisFire2001_2019\\2001"
os.chdir(path)
print(os.getcwd())
os.listdir(path)
len(os.listdir(path))
WantedFilelist= ["Bangladesh", "Bhutan", "China", "India", "Laos", "Myanmar", "Nepal", "Thailand", "Vietnam"]


for file in os.listdir(path):
    Country_name = file[11:file.rfind('.')]
    if Country_name in WantedFilelist:
        print(Country_name)
    else:
        os.rmdir("file")
    