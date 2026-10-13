#%%
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=41.03,llcrnrlat=24.06,urcrnrlon=64.33,urcrnrlat=40.78,
            rsphere=(6378137.00,6356752.3142),
            resolution='l',projection='merc',
            lat_0=40.,lon_0=-20.,lat_ts=20.)
m.drawcountries(linewidth=1.2, color='black')
m.drawcoastlines(color="blue")
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='white',lake_color='lightblue')
m.drawstates(color="white")
cities_dict = [{"Name":"Tehran","longd":50,"longm":23 ,"longs":20 ,"latd":35,"latm":41 ,"lats":21,"pop":869/3706},
               {"Name":"Shiraz","longd":51,"longm":35 ,"longs":1 ,"latd":29,"latm":35 ,"lats":30,"pop":156/5572},
               {"Name":"Isfahan","longd":50,"longm":40 ,"longs":5 ,"latd":32,"latm":39 ,"lats":17,"pop":196/1260},
               {"Name":"Kashan","longd":50,"longm": 24,"longs":36 ,"latd":33,"latm":59 ,"lats":6,"pop":30/4487},
               {"Name":"Tabriz","longd":45,"longm":16 ,"longs":26 ,"latd":38,"latm":5 ,"lats":46,"pop":155/8693},
               {"Name":"Yazd","longd":53,"longm":21 ,"longs":25 ,"latd":31,"latm":53 ,"lats":50,"pop":52/9673},
               {"Name":"Mashhad","longd":58,"longm":36 ,"longs":24 ,"latd":36,"latm":17 ,"lats":50,"pop":320/8000},
               {"Name":"Rasht","longd":48,"longm":34 ,"longs":5 ,"latd":37,"latm":16 ,"lats":50,"pop":67/9995},
               {"Name":"Ramsar","longd":49,"longm":39 ,"longs":30 ,"latd":36,"latm":54 ,"lats":12,"pop":4/4725},
               {"Name":"Kerman","longd":56,"longm":5 ,"longs":0 ,"latd":30,"latm":17 ,"lats":2,"pop":53/7718}]
df = pd.DataFrame(cities_dict)

df["decimallong"] = df['longd']+(df['longm']/60)+(df['longs']/3600)
df["decimallat"] = df['latd']+(df['latm']/60)+(df['lats']/3600)
scale_factor = 5000
x,y=m(df['decimallong'].values,df['decimallat'].values)
m.scatter(x,y,s=(df["pop"])*scale_factor,color="red")
for i, name in enumerate(df["Name"]):
    ax.text(x[i] + 0.1, y[i] + 0.1, name)





# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
ax.set_title('Top tourist cities in Iran')
plt.show()