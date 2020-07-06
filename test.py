import plotly.figure_factory as ff
import dash
from urllib.request import urlopen
import json
import plotly.express as px
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig = go.Figure()

COVID = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
dates = COVID.columns[64:]
COVID['UID']=COVID['UID'].astype('str')
COVID['UID'] = COVID.UID.str.slice(3,10)
COVID['Province_State'] = COVID.Admin2 +", " +COVID.Province_State
CovidSmoothed = pd.melt(COVID,id_vars=['UID','FIPS','Admin2','Province_State'],value_vars=dates)
fig2  = px.choropleth(CovidSmoothed,   geojson=counties, locations='UID', color='value',
                           color_continuous_scale="Inferno",
                           animation_frame='variable',
                           animation_group='UID',
                           range_color =(0, 12000),
                           scope="usa",
                           hover_name = 'Province_State',
                           labels={'value':'Covid Cases','Province_State':'County','variable':'Date'},
                          )
fig2.update_layout(template='plotly_white')
fig2.update_layout(title='COVID cases by County in US')
fig2.layout.xaxis.fixedrange = False
fig2.layout.yaxis.fixedrange = False


app = dash.Dash()
df = pd.read_csv('/Users/jacob/PycharmProjects/dtata/USA_cases.csv')
COVID = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
all_options= df['Province_State'].unique()
server = app.server
app.layout =  html.Div(children=[html.Div("Covid-19",style={
                                                      "text-align": "center",
                                                      "font-size": "40px",
                                                      "border-bottom-style":"solid",
                                                      "width":"100%",

                                                    }),
                            html.Div("State Covid Cases",style={
                                                    "text-align": "center",
                                                    "font-size": "20px",
                                                    "width":"50%",
                                                    "display":"inline-block",
                                                     }),
                             html.Div("USA Covid Cases",style={
                                                    "text-align": "center",
                                                    "font-size": "20px",
                                                    "width":"50%",
                                                    "display":"inline-block",
                                                  }),

            html.Div(dcc.Dropdown(
                 id='states',
                 options=[
                                                            {'label': 'Alabama', 'value': 'Alabama'},
                                                            {'label': 'Alaska', 'value': 'Alaska'},
                                                            {'label': 'Arizona', 'value': 'Arizona'},
                                                            {'label': 'Arkansas', 'value': 'Arkansas'},
                                                            {'label': 'Alaska', 'value': 'Alaska'},
                                                            {'label': 'California', 'value': 'California'},
                                                            {'label': 'Colorado', 'value': 'Colorado'},
                                                            {'label': 'Connecticut ', 'value': 'Connecticut'},
                                                            {'label': 'Delaware', 'value': 'Delaware'},
                                                            {'label': 'Florida', 'value': 'Florida'},
                                                            {'label': 'Georgia', 'value': 'Georgia'},
                                                            {'label': 'Hawaii', 'value': 'Hawaii'},
                                                            {'label': 'Idaho', 'value': 'Idaho'},
                                                            {'label': 'Illinois ', 'value': 'Illinois'},
                                                            {'label': 'Indiana', 'value': 'Indiana'},
                                                            {'label': 'Iowa', 'value': 'Iowa'},
                                                            {'label': 'Kansas', 'value': 'Kansas'},
                                                            {'label': 'Kentucky', 'value': 'Kentucky'},
                                                            {'label': 'Louisiana', 'value': 'Louisiana'},
                                                            {'label': 'Maine', 'value': 'Maine'},
                                                            {'label': 'Maryland', 'value': 'Maryland'},
                                                            {'label': 'Massachusett', 'value': 'Massachusett'},
                                                            {'label': 'Michigan ', 'value': 'Michiga'},
                                                            {'label': 'Minnesota', 'value': 'Minnesota'},
                                                            {'label': 'Mississippi', 'value': 'Mississippi'},
                                                            {'label': 'Missouri ', 'value': 'Missouri'},
                                                            {'label': 'Montana', 'value': 'Montana'},
                                                            {'label': 'Nebraska', 'value': 'Nebraska '},
                                                            {'label': 'Nevada', 'value': 'Nevada'},
                                                            {'label': 'New Hampshire', 'value': 'New Hampshire'},
                                                            {'label': 'New Jersey', 'value': 'New Jersey'},
                                                            {'label': 'New Mexico', 'value': 'New Mexico'},
                                                            {'label': 'New York', 'value': 'New York'},
                                                            {'label': 'North Carolina ', 'value': 'North Carolina'},
                                                            {'label': 'North Dakota ', 'value': 'North Dakota'},
                                                            {'label': 'Ohio', 'value': 'Ohio'},
                                                            {'label': 'Oklahoma ', 'value': 'Oklahoma'},
                                                            {'label': 'Oregon ', 'value': 'Oregon'},
                                                            {'label': 'Pennsylvania', 'value': 'Pennsylvania'},
                                                            {'label': 'Rhode Island ', 'value': 'Rhode Island'},
                                                            {'label': 'South Carolina ', 'value': 'South Carolina'},
                                                            {'label': 'South Dakota', 'value': 'South Dakota'},
                                                            {'label': 'Tennessee', 'value': 'Tennessee'},
                                                            {'label': 'Texas', 'value': 'Texas'},
                                                            {'label': 'Utah', 'value': 'Utah'},
                                                            {'label': 'Vermont', 'value': 'Vermont'},
                                                            {'label': 'Virginia ', 'value': 'Virginia'},
                                                            {'label': 'Washington', 'value': 'Washington'},
                                                            {'label': 'West Virginia ', 'value': 'West Virginia'},
                                                            {'label': 'Wisconsin', 'value': 'Wisconsin'},
                                                            {'label': 'Wyoming', 'value': 'Wyoming'},

                                                             ],
                                                value='',
                                                placeholder='Please select a state'
                                                     ),style={
                                                     "width": "50%",

            }),
                                 html.Div(
                                     dcc.Graph(id='graph',figure=fig,
                                 ), style = {'display': 'inline-block', "width":"50%"}),
                                     html.Div(
                                         dcc.Graph(id='map',figure=fig2
                                          ), style={'display': 'inline-block', "width":"50%"})





])
@app.callback(
    Output('graph', 'figure'),
    [Input('states', 'value')])
def update_data(val_dropdown):
    df_new = df[df['Province_State'] == val_dropdown]
    values1 = df_new['5/10/20'].tolist()
    fips = df_new['FIPS'].tolist()
    fig = ff.create_choropleth(
                 fips=fips, values=values1, scope=df_new,
                 round_legend_values=True,
                 simplify_county=0, simplify_state=0,
                 county_outline={'color': 'rgb(25,25,25)', 'width': 0.5},
                 state_outline={'width': 0.5},
                 title= val_dropdown)
    return (fig)



if __name__ == '__main__':



    app.run_server()
