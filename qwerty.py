from data_wrangling import *
import seaborn as sns

# =============================================================================
# parameter : change in terrorism frequency in the years for a country
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
# parameter: count of severe attacks and non severe attacks on acountry for a year
# =============================================================================

severe = df[df.nkill>df.nwound]
non_severe= df[df.nkill<df.nwound]
print(severe,"\n\n",non_severe)
with PdfPages ('severity_test.pdf') as pdf:
    tempdf1=severe.groupby(severe.country)
    tempdf2=non_severe.groupby(non_severe.country)
    
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
        k1=g1[g1.nkill>g1.nwound].year.agg(np.count_nonzero)
        k2=g1[g1.nkill>g1.nwound].year.agg(np.count_nonzero)
tempdf=df.groupby(df.weapon)
df1=tempdf.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(5)
df1.plot(kind="pie",subplots=True,autopct="%.2f%%",explode=[0,0,0,0.5,1],radius=1.5)
print(df1)
 
# =============================================================================
# parameter: distribution of attack places according to the year
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
# parameter : increase in attack at religious places and military since 2012
# =============================================================================

tempdf=df.groupby(["year","target0"])
filtered=tempdf.apply(lambda x: x['target0']=='Military')
print(filtered.value_count())

# =============================================================================
# parameter: most featured weapons of each terrorist group
# =============================================================================

tempdf=df.groupby(['gname'])   
fp=open("weapon of terrorist.txt","a")   
for name,group in tempdf:
    print(name,"\n")
    g1=group.groupby(group.weapon)
    res=g1.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(1)
    print(res)
for name,group in tempdf:
    print(name,"\n")
    g1=group.groupby(group.weapon)
    res=g1.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(1)
    print(res)

# =============================================================================
# parameter: attack places distribution by each terrorist group
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
# attack country distribution by each terrorrist group
# =============================================================================

tempdf=df.groupby(['gname']) 
with PdfPages ('attack_places_gname.pdf') as pdf:
    for name,group in tempdf:
        print(name,"\n")
        g1=group.groupby(group.country)
        res=g1.country.agg(np.count_nonzero).sort_values(ascending=False).head(10)
        res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
        pdf.savefig()
        plt.close()

# =============================================================================
# attack type by gname
# =============================================================================

tempdf=df.groupby(['gname']) 
with PdfPages ('attack_type_gname.pdf') as pdf:
    for name,group in tempdf:
        print(name,"\n")
        g1=group.groupby(group.attack1)
        res=g1.attack1.agg(np.count_nonzero).sort_values(ascending=False).head(10)
        res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
        pdf.savefig()
        plt.close()
# =============================================================================
tempdf=df.groupby(['']) 
with PdfPages ('attack_places_gname.pdf') as pdf:
    for name,group in tempdf:
        print(name,"\n")
        g1=group.groupby(group.target0)
        res=g1.weapon.agg(np.count_nonzero).sort_values(ascending=False).head(10)
        res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
        pdf.savefig()
        plt.close()

# =============================================================================
# casualties created by terrorrist group
# =============================================================================

df1=df.copy()
df1['total_cos']=np.nan
df1['total_cos']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.gname)
dict1={'name':[],'total':[]}
for name,group in tempdf:
    dict1['name'].append(name)
    dict1['total'].append(group.total_cos.agg(np.sum))
    plt.bar(name,group.total_cos.agg(np.sum))
for index,rows in df1.iterrows():
    rows.iloc[index]['total_cos']=rows.iloc[index]['nkill']
dft=pd.DataFrame.from_dict(dict1)
res=dft.sort(['total'],ascending=[0])
dft.sort_values(by=['total'],ascending=False,inplace=True)
res=dft.head(5)
plt.bar(res.name,res.total)
dft.head(10).plot(kind="bar",xticks=dft.head(10).name)
 
# =============================================================================
df1=df.copy()
df1['total_cos']=np.nan
df1['total_cos']=(df1['nkill']+df1['nwound'])/df1['nkill']
tempdf=df1.groupby(df1.gname)
dict1={'name':[],'total':[]}
for name,group in tempdf:
    dict1['name'].append(name)
    dict1['total'].append(group.total_cos.agg(np.sum))
# ============================================================================
    plt.bar(name,group.total_cos.agg(np.sum))
# # =============================================================================
for index,rows in df1.iterrows():
    rows.iloc[index]['total_cos']=rows.iloc[index]['nkill']
# =============================================================================
dft=pd.DataFrame.from_dict(dict1)
# # =============================================================================
res=dft.sort(['total'],ascending=[0])
# # =============================================================================
dft.sort_values(by=['total'],ascending=False,inplace=True)
res=dft.head(350)
plt.bar(res.name,res.total)
# # =============================================================================
dft.head(10).plot(kind="bar",xticks=dft.head(10).name)
# # =============================================================================
 
# =============================================================================
# count attack type
# =============================================================================

df1=df.copy()
p=df1['attack1'].value_counts()
ap=p.plot(kind="pie",subplots=True,figsize=(5,5),radius=1)

# =============================================================================
# each city in each place
# =============================================================================


tempdf=df.groupby(['country']) 
with PdfPages ('city_place.pdf') as pdf:
    for name,group in tempdf:
         print(name,"\n")
         g1=group.groupby(group.city)
         res=g1.city.agg(np.count_nonzero).sort_values(ascending=False).head(10)
         res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
         pdf.savefig()
         plt.close()

# =============================================================================
# attack type distribution f each country
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
# find the vulnarable countries
# =============================================================================

df1=df.copy()
df1['total_cos']=np.nan
df1['total_cos']=df1['nkill']+df1['nwound']
tempdf=df1.groupby(df1.country)
dict1={'name':[],'total':[]}
for name,group in tempdf:
    dict1['name'].append(name)
    dict1['total'].append(group.total_cos.agg(np.sum))
dft=pd.DataFrame.from_dict(dict1)
dft.sort_values(by=['total'],ascending=False,inplace=True)
res=dft.head(50)
plt.bar(res.name,res.total)
 
# =============================================================================
# targets vs casualties 9
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
  
tempdf=df.groupby(['country']) 
with PdfPages ('inter_dom.pdf') as pdf:
    for name,group in tempdf:
         print(name,"\n")
         g1=group.groupby(group.nationality)
         res=g1.nationality.agg(np.count_nonzero).sort_values(ascending=False).head(10)
         res.plot(kind="pie",subplots=True,title=name,autopct="%.2f%%")
         pdf.savefig()
         plt.close()
 
# =============================================================================
import plotly.plotly as py

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +\
    'Beef '+df['beef']+' Dairy '+df['dairy']+'<br>'+\
    'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+\
    'Wheat '+df['wheat']+' Corn '+df['corn']

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['code'],
        z = df['total exports'].astype(float),
        locationmode = 'USA-states',
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Millions USD")
        ) ]

layout = dict(
        title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict( data=data, layout=layout )
py.iplot( fig, filename='d3-cloropleth-map' )
