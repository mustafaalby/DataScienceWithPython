#%%
import pandas as pd
import numpy as np
#%%
dictionary={"Mclaren":["Alonso","Vandoorne"],"Mercedes":["Hamilton","Bottas"],"Ferrari":["Vettel","Raikonen"]}
print(dictionary.keys())
print(dictionary.values())
#update veya yeni key girişi
dictionary["Renault"]=["Hulkenberg","Carlos Sainz Jr."]
#dictionary.clear() tüm entry leri siler

#%%
data=pd.read_csv("Data\pokemon.csv")
data.head()

#%%
#Filtering
AttackAbove50=data["Attack"]>95
data[AttackAbove50]

#%%
#filtering with logic
data[(data["Defense"]>130) & (data["Attack"]>120)]
#%%
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)
#%%
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)

#%%
#gerekli dataları bulup düzeltme
data=pd.read_csv("Data\pokemon.csv")
print(data["Type 1"].value_counts(dropna=False))
#hangi type tan kaç adet olduğunu gösterir
#%%
#Melt etme
melted=pd.melt(frame=data,id_vars="Name",value_vars=["Attack","Defense"])
melted

#%%
#pivot etme; melt edilen datayı eski haline çevirir
melted.pivot(index="Name",columns="variable",values="value")
melted


#%%
#concatenating data
data1=data.head()
data2=data.tail()
conc_data=pd.concat([data1,data2],axis=0,ignore_index=True)
conc_data
#data1 ve 2 satırlar bazında birleştirildi, yeniden index verildi

#%%
data1=data["Attack"].head()
data2=data["Defense"].head()
conc_data=pd.concat([data1,data2],axis=1)
conc_data

#%%
#sütun 
data["Type 1"]=data["Type 1"].astype("category")
data["Speed"]=data["Speed"].astype("float")
data.info()

#%%
#Missing data fixing
data=pd.read_csv("Data\pokemon.csv")
data["Type 2"].value_counts(dropna=False)
##
#
data1=data.copy()
data1["Type 2"].dropna(inplace=True)
data1.info()

#%%
data2=data.copy()
data2["Type 2"].fillna(inplace=True)

#%%
data=pd.read_csv("Data\pokemon.csv")
data.head()
data.set_index("#")
data.head()

#%%
print(type(data["hp"]))#series
print(type(data[["HP"]]))#DataFrame
#%%
print(data.index.name)#index isim değiştirme
data.index.name = "index_name"
data.head()
#%%
data.head()
data2 = data.copy()
data2.index = range(100,900,1)
data2.head()
#%%
data = pd.read_csv("Data\pokemon.csv")
data1 = data.set_index(["Type 1","Type 2"]) 
data1.head(100)