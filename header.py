import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df=pd.read_csv("terrorism.csv",encoding="latin")
df.rename(columns={'iyear':'year','imonth':'month','iday':'day','country_txt':'country',\
                   'attacktype1_txt':'attack1','targtype1_txt':'target0','natlty1_txt':'nationality',\
                   'weaptype1_txt':'weapon','weapsubtype1_txt':'weapon_sub',\
                   'propextent_txt':'damage'},inplace=True)



