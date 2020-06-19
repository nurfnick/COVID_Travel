import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv('/Users/jacob/PycharmProjects/dtata/USA_cases.csv')
scope = ['New York']
df_new = df[df['Province_State'].isin(scope)]

values = df_new['3/26/20'].tolist()
fips = df_new['FIPS'].tolist()

colorscale = ['#0d0887', '#46039f', '#7201a8', '#9c179e', '#bd3786',
              '#d8576b', '#ed7953', '#fb9f3a', '#fdca26', '#f0f921','#F0F8FF','#FAEBD7',
              'white', '#7FFFD4','#F0FFFF','#F5F5DC', '#FFE4C4','#000000','#FFEBCD', '#0000FF',
'#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E','#FF7F50','#6495ED','#FFF8DC','#DC143C'
,'#00008B',  '#008B8B','#B8860B','#A9A9A9','#006400',


]
fig = ff.create_choropleth(
    fips=fips, values=values, scope=scope,
    colorscale=colorscale,round_legend_values=True,
    simplify_county=0, simplify_state=0,
    county_outline={'color': 'rgb(15,15,55)','width':0.5},
    state_outline={'width':0.5},

    title = 'map map')
fig.show()