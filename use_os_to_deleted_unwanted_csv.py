import os
print(os.getcwd())
path= "C:\\859K_sl559\\Data\\ModisFire2001_2019\\2001"
os.chdir(path)
print(os.getcwd())
os.listdir(path)
len(os.listdir(path))
WantedFilelist= ["Bangladesh", "Bhutan", "China", "India", "Laos", "Myanmar", "Nepal", "Thailand", "Vietnam"]
filelist= os.listdir(path)
file = filelist.next()
for file in os.listdir(path):
    print(file)
    Country_name = file[11:file.rfind('.')]
    print(Country_name)
    if Country_name in WantedFilelist:
        print("This {} fire dataset is selected".format(Country_name))
    else:
        os.remove(file)
        file = filelist.next()