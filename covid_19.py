import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div(children=[html.Div("Covid-19",style={
                                                      "text-align": "center",
                                                      "font-size": "40px",
                                                      "border-bottom-style":"solid",
                                                      "width":"100%",

                                                    }),
                            html.Div("USA",style={
                                                    "text-align": "center",
                                                    "font-size": "20px",
                                                    "width":"50%",
                                                    "display":"inline-block",
                                                     }),
                             html.Div("State",style={
                                                    "text-align": "center",
                                                    "font-size": "20px",
                                                    "width":"50%",
                                                    "display":"inline-block",
                                                  }),
                             html.Div(dcc.Slider(
                                                    min=-5,
                                                    max=10,
                                                    step=0.5,
                                                    value=-3
                                                  ),style={
                                                     "width": "50%",
                                                     "display": "inline-block",
                             }),
                              html.Div(dcc.Dropdown(options=[
                                                            {'label': 'Alabama ', 'value': 'AL'},
                                                            {'label': 'Alaska ', 'value': 'AK'},
                                                            {'label': 'Arizona', 'value': 'AZ'},
                                                            {'label': 'Arkansas', 'value': 'AR'},
                                                            {'label': 'Alaska ', 'value': 'AK'},
                                                            {'label': 'California', 'value': 'CA'},
                                                            {'label': 'Colorado ', 'value': 'CO'},
                                                            {'label': 'Connecticut ', 'value': 'CT'},
                                                            {'label': 'Delaware', 'value': 'DE'},
                                                            {'label': 'Florida ', 'value': 'FL'},
                                                            {'label': 'Georgia ', 'value': 'GA'},
                                                            {'label': 'Hawaii', 'value': 'HI'},
                                                            {'label': 'Idaho ', 'value': 'ID'},
                                                            {'label': 'Illinois ', 'value': 'IL'},
                                                            {'label': 'Indiana', 'value': 'IN'},
                                                            {'label': 'Iowa  ', 'value': 'IA'},
                                                            {'label': 'Kansas ', 'value': 'KS'},
                                                            {'label': 'Kentucky', 'value': 'KY'},
                                                            {'label': 'Louisiana', 'value': 'LA'},
                                                            {'label': 'Maine ', 'value': ''},
                                                            {'label': 'Maryland', 'value': 'MD'},
                                                            {'label': 'Massachusett', 'value': 'MA'},
                                                            {'label': 'Michigan ', 'value': 'MI'},
                                                            {'label': 'Minnesota', 'value': 'MN'},
                                                            {'label': 'Mississippi', 'value': 'MS'},
                                                            {'label': 'Missouri ', 'value': 'MO'},
                                                            {'label': 'Montana', 'value': 'MT'},
                                                            {'label': 'Nebraska ', 'value': 'NE'},
                                                            {'label': 'Nevada ', 'value': 'NV'},
                                                            {'label': 'New Hampshire', 'value': 'NH'},
                                                            {'label': 'New Jersey ', 'value': 'NJ'},
                                                            {'label': 'New Mexico', 'value': 'NM'},
                                                            {'label': 'New York', 'value': 'NY'},
                                                            {'label': 'North Carolina ', 'value': 'NC'},
                                                            {'label': 'North Dakota ', 'value': 'ND'},
                                                            {'label': 'Ohio', 'value': 'OH'},
                                                            {'label': 'Oklahoma ', 'value': 'OK'},
                                                            {'label': 'Oregon ', 'value': 'OR'},
                                                            {'label': 'Pennsylvania', 'value': 'PA'},
                                                            {'label': 'Rhode Island ', 'value': 'RI'},
                                                            {'label': 'South Carolina ', 'value': 'SC'},
                                                            {'label': 'South Dakota', 'value': 'SD'},
                                                            {'label': 'Tennessee ', 'value': 'TN'},
                                                            {'label': 'Texas  ', 'value': 'TX'},
                                                            {'label': 'Utah ', 'value': 'UT'},
                                                            {'label': 'Vermont ', 'value': 'VT'},
                                                            {'label': 'Virginia ', 'value': 'VA'},
                                                            {'label': 'Washington', 'value': 'WA'},
                                                            {'label': 'West Virginia ', 'value': 'WV'},
                                                            {'label': 'Wisconsin', 'value': 'WI'},
                                                            {'label': 'Wyoming ', 'value': 'WY'},

                                                             ],
                                                    value='MTL'
                                                     ),style={
                                                     "width": "50%",
                                                     "display": "inline-block",
                                                      })])

if __name__== '__main__':

    app.run_server()


