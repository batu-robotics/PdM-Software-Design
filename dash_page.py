import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as pgo
from dash import Input, Output, State, dcc, html, Dash, callback_context
from dash_bootstrap_components._components.Container import Container

################################################
# Creating Data
# Creating Data Structures
a=np.random.random(100)
a=100*a+np.std(a)
x=np.linspace(1,len(a))

b=np.random.random(100)
b=100*b+np.std(b)

c=np.random.random(100)
c=100*c+np.std(c)

d=np.random.random(100)
d=100*d+np.std(d)

# Creating Data Structures
e=np.random.random(100)
e=100*e+np.std(e)

f=np.random.random(100)
f=100*f+np.std(f)

g=np.random.random(100)
g=100*g+np.std(g)

h=np.random.random(100)
h=100*h+np.std(h)

df=np.column_stack((a,b,c,d,e,f,g,h))
df=pd.DataFrame(df,columns=["Machine-1","Machine-2","Machine-3","Machine-4","Machine-5","Machine-6","Machine-7","Machine-8"])

###############################################
app2=Dash()
app2.layout=html.Div([
                html.Div([
                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-1", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary", id="machine-1"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               "marginTop":"10%",
                               "marginLeft": "5%"}
                    ),
                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-2", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               'marginTop': "10%",
                               "marginLeft":"5%"}
                    ),

                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-3", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               'marginTop': "10%",
                               "marginLeft":"5%"}
                    )
        ]),

        html.Div([
                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-4", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               "marginTop":"10%",
                               "marginLeft": "5%"}
                    ),
                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-5", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               'marginTop': "10%",
                               "marginLeft":"5%"}
                    ),

                    dbc.Card(
                        [
                            dbc.CardImg(src="gears_1.gif", top=True),
                            dbc.CardBody(
                                [
                                    html.H4("Machine-6", className="card-title"),
                                    html.P("Department: ....\n", className="card-text"),
                                    html.P("Serial Name: .....\n", className="card-text"),
                                    html.P("Built in: ....\n", className="card-text"),
                                    dbc.Button("Machine Info", color="primary"),
                                    dbc.Button("Home", color="secondary")
                                ]
                            ),
                        ],
                        style={"width": "20%",
                               "float": "Left",
                               'marginTop': "10%",
                               "marginLeft":"5%"}
                    )
        ]),

    html.Div([
        dbc.Card(
            [
                dbc.CardImg(src="gears_1.gif", top=True),
                dbc.CardBody(
                    [
                        html.H4("Machine-7", className="card-title"),
                        html.P("Department: ....\n", className="card-text"),
                        html.P("Serial Name: .....\n", className="card-text"),
                        html.P("Built in: ....\n", className="card-text"),
                        dbc.Button("Machine Info", color="primary"),
                        dbc.Button("Home", color="secondary")
                    ]
                ),
            ],
            style={"width": "20%",
                   "float": "Left",
                   "marginTop": "10%",
                   "marginLeft": "5%"}
        ),
        dbc.Card(
            [
                dbc.CardImg(src="gears_1.gif", top=True),
                dbc.CardBody(
                    [
                        html.H4("Machine-8", className="card-title"),
                        html.P("Department: ....\n", className="card-text"),
                        html.P("Serial Name: .....\n", className="card-text"),
                        html.P("Built in: ....\n", className="card-text"),
                        dbc.Button("Machine Info", color="primary"),
                        dbc.Button("Home", color="secondary")
                    ]
                ),
            ],
            style={"width": "20%",
                   "float": "Left",
                   'marginTop': "10%",
                   "marginLeft": "5%"}
        )
    ]),
    html.Div(id="on-screen")
])

@app2.callback(Output("on-screen","screen"),
              [Input("machine-1","n_clicks")])

def automate(button1):
    control=[p['prop_id'] for p in callback_context.triggered][0]

    if 'machine-1' in control:
        return html.Div([
            dcc.Graph(id='my_graph',
                      figure={'data': [
                          {'x': x, 'y': a, 'name': 'Machine-1'}
                      ],'layout': {'title': 'Machine Temperature'}})
                    ])

    elif 'machine-2' in control:
        return html.Div([
            dcc.Graph(id='my_graph',
                      figure={'data': [
                          {'x': x, 'y': b, 'name': 'Machine-2'}
                      ],'layout': {'title': 'Machine Temperature'}})
                    ])

###############################################
#Graph_app Design
graph_app=Dash()
graph_app.layout=html.Div([
    dcc.Graph(id='my_graph',
              figure={'data': [
                  {'x': x, 'y': a, 'name': 'Machine-1','animate':True},
                  {'x': x, 'y': b, 'name': 'Machine-2','animate':True},
                  {'x': x, 'y': c, 'name': 'Machine-3','animate':True},
                  {'x': x, 'y': d, 'name': 'Machine-4','animate':True},
                  {'x': x, 'y': e, 'name': 'Machine-5','animate':True},
                  {'x': x, 'y': f, 'name': 'Machine-6','animate':True},
                  {'x': x, 'y': g, 'name': 'Machine-7','animate':True},
                  {'x': x, 'y': h, 'name': 'Machine-8','animate':True}
              ], 'layout': {'title': 'Machine Temperatures'}}
              ),
    html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=a,
                                  boxpoints='all',
                                  name='Machine-1 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(255,0,0,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-1 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=b,
                                  boxpoints='all',
                                  name='Machine-2 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(200,100,0,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-2 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=c,
                                  boxpoints='all',
                                  name='Machine-3 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(0,0,255,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-3 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=d,
                                  boxpoints='all',
                                  name='Machine-4 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(100,200,0,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-4 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=e,
                                  boxpoints='all',
                                  name='Machine-5 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(0,100,200,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-5 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=f,
                                  boxpoints='all',
                                  name='Machine-6 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(0,200,200,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-6 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=g,
                                  boxpoints='all',
                                  name='Machine-5 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(200,200,100,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-7 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'}),

            html.Div([
                dcc.Graph(id='boxplot',
                          style={'width': '50vh', 'height': '50vh'},
                          figure={'data': [
                              pgo.Box(
                                  y=h,
                                  boxpoints='all',
                                  name='Machine-8 Temperature Statistics',
                                  jitter=0.3,
                                  pointpos=0,
                                  marker=dict(color='rgba(50,200,100,1)')
                              )],
                              'layout': pgo.Layout(title='Machine-8 Temperature Statistics',
                                                   yaxis={'title': 'Temperatures (oC)'})}
                          )
            ],style={'float':'Left'})

    ])


###############################################
#%% Main App Design
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top":0,
    "left":0,
    "bottom":0,
    "width":"16rem",
    "padding":"2rem 1rem",
    "background-color":"#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left":"18rem",
    "margin-right":"2rem",
    "padding":"2rem 1rem",
}

sidebar = html.Div(
    [
        html.Hr(),
        html.P(
            "Predictive Maintenance Tracking Automation", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Machines", href="/page-1", active="exact"),
                dbc.NavLink("Personal Info", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content],
                      )


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return graph_app.layout
            #html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return app2.layout
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run_server(port=8888)