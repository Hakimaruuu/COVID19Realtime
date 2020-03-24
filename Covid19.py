# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:04:29 2020

@author: ASUS
"""

import COVID19Py
import matplotlib.pyplot as plt
covid19 = COVID19Py.COVID19()
data = covid19.getAll(timelines= True)
virusdata = dict(data["latest"])
names = list(virusdata.keys())
values = list(virusdata.values())
print("")
print("Total cases in the world today")
print(virusdata)

plt.bar(range(len(virusdata)), values, tick_label = names)
plt.show()

location = covid19.getLocationByCountryCode("ID", timelines = True)
loc_data = location[0]
virusdata2 = dict(loc_data['latest'])
names2 = list(virusdata2.keys())
values2 = list(virusdata2.values())
print("")
print("Total cases in Indonesia today")
print(virusdata2)

plt.bar(range(len(virusdata2)), values, tick_label = names)
plt.show()
