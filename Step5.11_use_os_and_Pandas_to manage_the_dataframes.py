#Pandas
#Import the Pandas librar
import os
import pandas as pd

#print(os.getcwd())
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
    #construct an empty datafram to hold all the subset dataframes
    detailed_dfs = pd.DataFrame(columns =["Country_name","Year", "latitude","longitude","confidence","acq_date", "acq_time"]) 
    CountrySummary_dfs=pd.DataFrame(columns =["Country_name","Year","NumberOfFire"]) 
    #print(dfs)
    #print(len(dfs))
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
            df_raw_2= df_raw_1.loc[df_raw_1["confidence"] >= 80]
            NumberOfFire= len(df_raw_2)
            print(NumberOfFire)
            #print(df_raw_1.tail())
            #print(df_raw_2.tail())
            
            #Append the subset detailed dataframe to the huge detailed dataframe
            #detailed_dfs = detailed_dfs.append(df_raw_2, ignore_index=True, sort=False)
            detailed_dfs = detailed_dfs.append(df_raw_2, ignore_index=True)
            #print(len(dfs)) 
            
            #Construct and Append the summary row to the summary dataframe
            new_row = {"Country_name":Country_name, "Year":Year, "NumberOfFire":NumberOfFire}
            CountrySummary_dfs = CountrySummary_dfs.append(new_row, ignore_index=True)
        else:
            os.remove(file)       

#Check
print(len(detailed_dfs))
print(detailed_dfs[0:5])
print(detailed_dfs[10000:10005])


print(len(CountrySummary_dfs))
print(CountrySummary_dfs[0:5])

#df.to_excel('output.xlsx', 'Sheet1')

