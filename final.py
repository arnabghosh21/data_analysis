from google.colab import files
files.upload()
# ls

# =============================================================================
from data_wrangling import *
print(df)

# =============================================================================
# parameter 1:change in terrorism frequency in the years for a country
# =============================================================================

tempdf=df.groupby(df.country)
with PdfPages ('year_wise_terrorism.pdf') as pdf:
     for name,group in tempdf:
         print("\n",name,"\n")
         t=group.groupby(group.year)
         k=t.year.agg(np.count_nonzero)
         k2=k.diff()
         k.plot(title=name)
         pdf.savefig()
         plt.close()

# =============================================================================
# parameter 2: count of severe attacks and non severe attacks on acountry for a year
# =============================================================================

severe = df[df.nkill>df.nwound]
non_severe= df[df.nkill<df.nwound]
# =============================================================================
print(severe,"\n\n",non_severe)
# =============================================================================
with PdfPages ('severity_test.pdf') as pdf:
     tempdf1=severe.groupby(severe.country)
     tempdf2=non_severe.groupby(non_severe.country)
#      
     for name,group in tempdf1:
         for name1,group1 in tempdf2:
             g1=group.groupby(group.year)
             g2=group1.groupby(group1.year)
             if name==name1:
                 k1=g1.year.agg(np.count_nonzero)
                 k2=g2.year.agg(np.count_nonzero)
                 k1.plot(kind="bar",title=name+' severe')
                 pdf.savefig()
                 plt.close()
                 k2.plot(kind="bar",title=name1+' non-severe')
                 pdf.savefig()
                 plt.close()
                
# =============================================================================
# parameter 3: Distribution of weapons
# =============================================================================

tempdf=df.groupby(df.weapon) 
df1=tempdf.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(5)
df1.plot(kind="pie",subplots=True,autopct="%.2f%%",explode=[0,0,0,0.5,1],radius=1.5)
print(df1)

# =============================================================================
# parameter 4:  to see distribution of global terrorirm through out years
# =============================================================================

tempdf=df.groupby(df.year)
df1=tempdf.year.agg(np.count_nonzero)
df1.plot(kind="bar")

# =============================================================================
# parameter 5: to display the top 10 countries affected by terrorirsm
# =============================================================================

tempdf=df.groupby(df.country)
df1=tempdf.country.agg(np.count_nonzero).sort_values(ascending=False).head(10)
print (df1)

# =============================================================================
# parameter 6:  to see how each country was attacked
# =============================================================================

tempdf=df.groupby(df.country)
with PdfPages ('param6.pdf') as pdf:
    for name,group in tempdf:
        print("\n",name,"\n")
        t=group.groupby(group.attack1)
        k=t.attack1.agg(np.count_nonzero)
        
        fig=k.plot(kind="bar",title=name).get_figure()
        pdf.savefig(fig)
        
# =============================================================================
# parameter 7: most vurnerable terrorist group
# =============================================================================

df1=df.copy()
df1['total']=np.nan
df1['total']=df['nkill']+df['nwound']
tempdf=df1.groupby(df1.gname)
dict1={'name':[],'total_cas':[]}
for name,group in tempdf:
  g1=group.total.agg(np.sum)
  dict1['name'].append(name)
  dict1['total_cas'].append(g1)
df2=pd.DataFrame.from_dict(dict1) 
res=df2.sort_values(by=['total_cas'],ascending=[False]).head(5)
res.plot(x=res.name,kind='bar')
 
# =============================================================================
# parameter 8: top 10 terrorist group with highest kill to wound ratio
# =============================================================================

df1=df.copy()
tempdf=df1.groupby(df1.gname)
dict1={'name':[],'ratio':[]}
for name,group in tempdf:
  kill=group.nkill.agg(np.sum)
  wound=group.nwound.agg(np.sum)
  if wound!=0:
    res1=kill/wound
  else:
    res1=0
  dict1['name'].append(name)
  dict1['ratio'].append(res1)
df2=pd.DataFrame.from_dict(dict1) 
res=df2.sort_values(by=['ratio'],ascending=[False]).head(5)
print(res)
res.plot(x=res.name,kind='bar')
 
# =============================================================================
# parameter 9: top 10 vurnarable places to terrorism
# =============================================================================

tempdf=df.groupby(df.country)
res=tempdf.country.agg(np.count_nonzero).sort_values(ascending=False).head(10)
res.plot(kind="bar")

# =============================================================================
# parameter 10: favoured way of attack of each terrorist group
# =============================================================================

tempdf=df.groupby(df.gname)
for name,group in tempdf:
  g1=group.groupby(group.weapon)
  res=g1.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(1)
  print("name:  ",name,end="\t")
  res1=res.to_dict()
  for key in res1:
    print("way:  ",key)
    
# =============================================================================
# parameter 11: distribution of attack places according to the year
# =============================================================================

tempdf=df.groupby(df.year)
with PdfPages ('target_places_year.pdf') as pdf:
     for name,group in tempdf:
         g1=group.groupby(group.target0)
         res=g1.target0.agg(np.count_nonzero).sort_values(ascending=False).head(10)
         res.plot(kind='pie',subplots=True,title=name,autopct="%.02f%%",radius=1.5)
         pdf.savefig()
         plt.close()
        
# =============================================================================
# parameter 12:attack places distribution by each terrorist group
# =============================================================================

tempdf=df.groupby(['gname']) 
with PdfPages ('attack_places_gname.pdf') as pdf:
     for name,group in tempdf:
         print(name,"\n")
         g1=group.groupby(group.target0)
         res=g1.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(10)
         res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
         pdf.savefig()
         plt.close()
          
# =============================================================================
# parameter 13: categories of damage per year
# =============================================================================

tempdf=df.groupby(df.year)
for name,group in tempdf:
  print("\n",name,"\n")
  g1=group.groupby(group.damage)
  print(g1.size())

# =============================================================================
# parameter 14:top 10 attack type doing the major no of casualties
# =============================================================================

df1=df.copy()
df1['total']=np.nan
df1['total']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.attack1)
dict={'name':[],'total_cas':[]}
for name,group in tempdf:
  print("\n",name,"\n")
  res=group.total.agg(np.sum)
  dict['name'].append(name)
  dict['total_cas'].append(res)
dfr=pd.DataFrame.from_dict(dict)  
fr.plot(kind='pie',subplots=True,autopct="%.2f%%",radius=1.5)
dfr.plot(kind="bar",x=dfr.name)
 

# =============================================================================
# parameter 15:top 10 attack targets
# =============================================================================

df1=df.copy()
df1['total']=np.nan
df1['total']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.target0)
dict={'name':[],'total_cas':[]}
for name,group in tempdf:
  print("\n",name,"\n")
  res=group.total.agg(np.sum)
  dict['name'].append(name)
  dict['total_cas'].append(res)
dfr=pd.DataFrame.from_dict(dict)  
dfr.plot(kind='pie',subplots=True,radius=1.5)
dfr.plot(kind="bar",x=dfr.name)

# =============================================================================
# parameter 16: Distribution of terrorism within cities
# =============================================================================

df1=df.copy()
df1.city.replace('Unknown',np.nan,inplace=True)
tempdf=df1.groupby(df1.country)
with PdfPages ('city.pdf') as pdf:
  for name,group in tempdf:
    g1=group.groupby(group.city)
    res=g1.city.agg(np.count_nonzero).sort_values(ascending=False).head(10)
    if res.empty:
      pass
    else:
      res.plot(kind="pie",title=name,subplots=True,autopct="%.2f%%")
      pdf.savefig()
      plt.close()

# =============================================================================
# parameter 17: no of domestic and international casualties
# =============================================================================

tempdf=df.groupby(df.country)
with PdfPages ('national_international.pdf') as pdf:
     for name,group in tempdf:
         ar={'national':0,'international':0}
         international=0
         print("\n\n",name,"\n")
         g1=group.groupby(group.nationality)
         res=g1.nationality.agg(np.count_nonzero)
         d1=res.to_dict()
         for key in d1:
             if (key==name):
                 ar['national']=d1[key]
             else:
                 international+=d1[key]
         ar['international']=international
         df1=pd.DataFrame.from_dict(ar,orient='index')
         df1.plot(kind='bar',title=name)
         pdf.savefig()
         plt.close()
# =============================================================================
# parameter 18: which weapon type was the most vurnerable
# =============================================================================

df1=df.copy()
df1['total']=np.nan
df1['total']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.weapon_sub)
dict={'name':[],'total_cas':[]}
for name,group in tempdf:
  print("\n",name,"\n")
  res=group.total.agg(np.sum)
  dict['name'].append(name)
  dict['total_cas'].append(res)
dfr=pd.DataFrame.from_dict(dict)  
dfr.plot(kind='pie',subplots=True,radius=1.5)
dfr.plot(kind="bar",x=dfr.name)

# =============================================================================
# parameter 19: distribution of terrorism within months of year
# =============================================================================

df1=df.copy()
df1.replace({'month':{1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'july',\
                     8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}},inplace=True)
tempdf=df1.groupby(df1.year)
with PdfPages ('monthly_distribution.pdf') as pdf:
  for name,group in tempdf:
    g1=group.groupby(group.month)
    res=g1.month.agg(np.count_nonzero).sort_values(ascending=False)
    res.plot(kind='pie',subplots=True,title=name,autopct="%.2f%%")
    pdf.savefig()
    plt.close()

# =============================================================================
# parameter 20: attack prob of each country
# =============================================================================

tempdf=df.groupby(df.country)
res=tempdf.country.agg(np.count_nonzero)
df2=res.to_frame()
df2['prob']=np.nan
df2['prob']=df2['country']/43914
df2.sort_values(by=['prob'],ascending=[False],inplace=True)
res=df2.prob.head(10)
res.plot(kind='pie',subplots=True)

# =============================================================================
# parameter 21: military and religious attacxks in years
# =============================================================================

tempdf=df.groupby(df.year)
df2=pd.DataFrame(columns=['military','religious'])
for name,group in tempdf:
  res1=group[group.target0=='Military']
  res2=group[group.target0=='Religious Figures/Institutions']
  c1=res1.year.agg(['count'])
  c2=res2.year.agg(['count'])
  list1=[c1.loc['count'],c2.loc['count']]
  df2.loc[name]=[c1.loc['count'],c2.loc['count']]
df2.plot()

# =============================================================================
# parameter 22: distribution of global terrorism in the world map
# =============================================================================

from pygal_maps_world.maps import World
dfc=pd.read_csv('gg.csv')
df1=df.copy()
d2=dfc.to_dict()
d2=dfc.set_index('country').T.to_dict()
mm =World()
tempdf=df.groupby(df.country)
res=tempdf.country.agg(np.count_nonzero)
d1=res.to_dict()
dt={}
for key in d1:
  if key in d2.keys():
    dt[d2[key]['code']]=d1[key]
    
d1=dt    
dn={}
for key in d1:
  r=key.rstrip()
  dn[r]=d1[key]
mm.add('terrorism distribution in world',dn)

# =============================================================================
# distribtion of casualties in world
# =============================================================================

dfc=pd.read_csv('gg.csv')
df1=df.copy()
d2=dfc.to_dict()
d2=dfc.set_index('country').T.to_dict()
mm =World()
tempdf=df.groupby(df.country)
res1=tempdf.nkill.agg(np.count_nonzero)
res2=tempdf.nwound.agg(np.count_nonzero)
dr1=res1.to_dict()
dr2=res2.to_dict()
dt={}
for key in dr1:
  if key in d2.keys():
    dt[d2[key]['code']]=dr1[key]
    
dr1=dt  
dt={}
for key in dr2:
  if key in d2.keys():
    dt[d2[key]['code']]=dr2[key]
 
dr2=dt
dn1={}
dn2={}
for key in dr1:
  r=key.rstrip()
  dn1[r]=dr1[key]
 
print(dn2)  
mm.add('nkill',dn1)

# =============================================================================
# parameter 23: count the different attacktype
# =============================================================================

df1=df.copy()
p=df1['attack1'].value_counts()
ap=p.plot(kind="pie",subplots=True,figsize=(5,5),radius=1)

# =============================================================================
# parameter 24: attack type in country
# =============================================================================

tempdf=df.groupby(['country']) 
with PdfPages ('country_attack.pdf') as pdf:
    for name,group in tempdf:
         print(name,"\n")
         g1=group.groupby(group.attack1)
         res=g1.attack1.agg(np.count_nonzero).sort_values(ascending=False).head(10)
         res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
         pdf.savefig()
         plt.close()

# =============================================================================
# parameter 25: targets vs casualties 9
# =============================================================================

df1=df.copy()
df1['total_cos']=np.nan
df1['total_cos']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.target0)
dict1={'name':[],'total':[]}
for name,group in tempdf:
    dict1['name'].append(name)
    dict1['total'].append(group.total_cos.agg(np.sum))
dft=pd.DataFrame.from_dict(dict1)
dft.sort_values(by=['total'],ascending=False,inplace=True)
res=dft.head(10)
plt.xticks(rotation=90)
plt.bar(res.name,res.total)

# =============================================================================
