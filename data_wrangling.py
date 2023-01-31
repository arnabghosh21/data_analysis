from header import *
import math

df.corp1.replace('Not Applicable',np.nan,inplace=True)
df.drop(['ransomamt'],axis=1,inplace=True)
df.target0.replace(np.nan,"Private Citizens & Property",inplace=True)
df.attack1.replace('Unknown',"Bombing/Explosion",inplace=True)
df.nkill.replace(np.nan,int(df.nkill.mean()),inplace=True)
df.nwound.replace(np.nan,int(df.nwound.mean()),inplace=True)
df.drop(df[(df.nkill==1500)|(df.nwound==1500)].index,inplace=True)
df.weapon.replace("Unknown","Explosives/Bombs/Dynamite",inplace=True)
for i,rows in df.iterrows():
   
   if (df.loc[i,'nationality'] is np.nan):
       df.loc[i,'nationality']=df.loc[i,'country']

# =============================================================================
df.drop(['ransomamt'],axis=1,inplace=True)
tempdf=df.groupby(df.nationality)
df1=tempdf.nationality.agg(np.count_nonzero).sort_values(ascending=False).head(10)
print(df1)
# =============================================================================

# =============================================================================
tempdf=df.groupby(df.country)
for name,group in tempdf:
   print(name,"\n")
# =============================================================================
    g1=group.groupby(group.nationality)
    g2=g1.nationality.agg(np.count_nonzero).sort_values(ascending=False).head(1)
    d=g2.to_dict()
    df[df.country==name].nationality.replace(np.nan,name,inplace=True)
    print(df[df.country==name].nationality)
    break
# =============================================================================
# =============================================================================
    for key in d:
        print(key.)
# =============================================================================
# =============================================================================
    dfs=pd.DataFrame(g2)
# # =============================================================================
    dfs.rename(columns={'nationality':'count'},inplace=True)
# # =============================================================================
    print(dfs.name)
# =============================================================================

# =============================================================================
fp=open("df_describe.txt","a")
fp.write(df.describe().to_string())
fp.close()
# 
fp=open("df_corelation.txt","a")   
fp.write(df.corr().to_string())
fp.close()
#
print ("Not Applicable count count in corp1:  ",df.corp1.value_counts()['Not Applicable'])

# =============================================================================
a=df['gname'].value_counts()
print(a[1:2])
# =============================================================================
plt.pie(a[:10],radius=1.4)
# =============================================================================
#==============================================================================
