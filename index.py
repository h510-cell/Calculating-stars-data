import pandas as pd
import csv

df = pd.read_csv("finale.csv")

solar_mass = []
solar_radius= []
Star_Names = []

solar_mass = float(solar_mass) * 1.989e+30
solar_radius = float(solar_radius) * 6.957e+8

stars_gravity = []
def calculate_gravity():
    for index,name in enumerate:
        gravity = (float(solar_mass[index])*5.972e+24) /(float(solar_radius[index])*float(solar_radius[index])*6371000*6371000) * 6.674e-11
        stars_gravity.append(gravity)
df["gravity"] = df.apply(calculate_gravity,axis=1)
df.head()

calculate_gravity()
