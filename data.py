import pandas as pd
df=pd.read_csv("main.csv")
radius=df["Radius"].tolist()
mass=df["Mass"].tolist()
gravity=[]
newMass=[]
newRadious=[]
for index in range(1,51,2):
    r=float(radius[index]) *6.957e+8
    newRadious.append(r)
    m=float(mass[index])* 1.989e+30
    newMass.append(m)
    g=(6.67 * pow(10,-11) * m) / pow(r,2)
    gravity.append(g)
    
new_df=pd.DataFrame({'radious':newRadious,'mass':newMass,'gravity':gravity})
new_df.to_csv("new.csv")