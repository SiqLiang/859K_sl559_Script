#Pandas
#Import the Pandas librar
import os
import pandas as pd
print(os.getcwd())
bathpath="C:\\859K_sl559\\Data\\ModisFire2001_2019"
yearlist=["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010",
          "2011","2012","2013","2014","2015","2016","2017","2018","2019"]
for year in yearlist:
    path= os.path.join(bathpath,year) 
    os.chdir(path)
    print(os.getcwd())
    os.listdir(path)
    print(len(os.listdir(path)))
    WantedFilelist= ["Bangladesh", "Bhutan", "China", "India", "Lao_PDR", "Myanmar", "Nepal", "Thailand", "Vietnam"]
    filelist= os.listdir(path)
    for file in filelist:
        print(file)
        Country_name = file[11:file.rfind('.')]
        print(Country_name)
        if Country_name in WantedFilelist:
            print("This {} file dataset is selected".format(Country_name))
            #df_out = Country_name+"_"+year+"_df"
            #print(df_out)
            df_out = pd.read_csv(file)
            print(df_out[1:5])
            #df_out_confident_fire= df_out["confidence"].#int.isin(80,81)
            #df_out_confident_fire[1:5]
            df_out['FileName'] = Country_name+"_"+year#+"_df"
            print(df_out[1:5])
        else:
            os.remove(file)
            

#df = pd.read_csv()
#len(land_df)