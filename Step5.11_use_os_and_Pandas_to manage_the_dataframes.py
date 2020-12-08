#Pandas
#Import the Pandas librar
import os
import pandas as pd
overwrite == "y"

#Construct an empty datafram to hold all the subset dataframes
Detailed_dfs = pd.DataFrame(columns =["Country_name","Year", "latitude","longitude","confidence","acq_date", "acq_time"]) 
#Construct an empty datafram to hold all the summary rows
CountrySummary_dfs=pd.DataFrame(columns =["Country_name","Year","NumberOfFire"]) 


bathpath="C:\\859K_sl559\\Data\\ModisFire2001_2019"
Yearlist=["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010",
          "2011","2012","2013","2014","2015","2016","2017","2018","2019"]
for Year in Yearlist:
    print(Year)
    path= os.path.join(bathpath,Year) 
    os.chdir(path)
    #print(os.getcwd())
    os.listdir(path)
    #print(len(os.listdir(path)))
    WantedFilelist= ["Bangladesh", "Bhutan", "China", "India", "Lao_PDR", "Myanmar", "Nepal", "Thailand", "Vietnam"]
    filelist= os.listdir(path)
    for file in filelist:
        #print(file)
        Country_name = file[11:file.rfind('.')]
        print(Country_name)
        if Country_name in WantedFilelist:
            #print("This {} file dataset is selected".format(Country_name))
            #Construct each subset dataframe
            df_raw_0 = pd.read_csv(file)
            df_raw_0["Country_name"] = Country_name
            df_raw_0["Year"] = Year
            df_raw_1=df_raw_0[["Country_name","Year", "latitude","longitude","confidence","acq_date", "acq_time"]]
            #Set confidence threshold
            df_raw_2= df_raw_1.loc[df_raw_1["confidence"] >= 90]
            NumberOfFire= len(df_raw_2)
            print(NumberOfFire)
            #print(df_raw_1.tail())
            #print(df_raw_2.tail())
            
            #Append the subset detailed dataframe to the huge detailed dataframe
            Detailed_dfs = Detailed_dfs.append(df_raw_2, ignore_index=True, sort=False)
            #print(len(dfs)) 
            
            #Construct and Append the summary row to the summary dataframe
            new_row = {"Country_name":Country_name, "Year":Year, "NumberOfFire":NumberOfFire}
            CountrySummary_dfs = CountrySummary_dfs.append(new_row,ignore_index=True, sort=False)
            
        else:
            os.remove(file)       

#Check Detailed_dfs
print(len(Detailed_dfs))
#print(Detailed_dfs[0:1000])
#print(Detailed_dfs[20000:24005])

#Check CountrySummary_dfs
print(len(CountrySummary_dfs))
print(CountrySummary_dfs[0:8])
print(CountrySummary_dfs[-9:])

#df.to_excel('output.xlsx', 'Sheet1')

#Construct 2001-2019 summary dataset for each country
#df_raw_2= df_raw_1.loc[df_raw_1["confidence"] >= 90]
os.remove("C:\859K_sl559\Doc\ModisFire\CountrySummary.xlsx") 
n=1
for Country_name in WantedFilelist:
    CountrySummary_China_df= CountrySummary_dfs.loc[CountrySummary_dfs["Country_name"]==Country_name]
    CountrySummary_China_df[0:18]
    sheetNumber="Sheet"+str(n)
    CountrySummary_China_df.to_excel('C:\\859K_sl559\\Doc\\ModisFire\\CountrySummary.xlsx', sheetNumber)
    n=n+1
    