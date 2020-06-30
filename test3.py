import plotly.figure_factory as ff
import dash
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
import datetime
from datetime import date, timedelta
import plotly.express as px
from urllib.request import urlopen


tday =  datetime.date.today()
tdelta =datetime.timedelta(days=3)

print(tday)
####
past= (tday - tdelta)
past = past.strftime('%m/%d/%y')
if past[0] == '0':
    past = past[1:]
print(past)
#### use this on state map!! to get most recent cases


df = pd.read_csv('/Users/jacob/PycharmProjects/dtata/USA_cases.csv')
df = df.drop(['iso2', 'iso3', 'Lat', 'Long_', 'Combined_Key',"j","Admin3"], axis=1)

df3=df.melt(id_vars=["Province_State", "Admin2","FIPS"],
    var_name="Date",
    value_name = "Value")

df3.to_csv('j.csv')
sdate = date(2020, 1, 22)   # start date
#edate = tday   # end date
edate = date(2020, 6, 16)
delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    day = day.strftime('%m/%-d/%y')
    if day[0] == '0':
        day = day[1:]

