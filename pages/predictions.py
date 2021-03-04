# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app
from joblib import load
pipeline = load('assets/pipeline.joblib')

@app.callback(
    Output('prediction-content', 'children'),
    [Input('accommodates', 'value'),
     Input('beds', 'value'),
     Input('bedrooms', 'value'),
     Input('room_type', 'value'),
     Input('latitude', 'value'),
     Input('longitude', 'value'),
     Input('host_response_time', 'value'),
     Input('host_is_superhost', 'value'),
     Input('host_identity_verified', 'value'),
     Input('instant_bookable', 'value')]
)
def predict(accommodates, beds, bedrooms,
            room_type,latitude,longitude,
            host_response_time,host_is_superhost,
            host_identity_verified, instant_bookable):
    df = pd.DataFrame(
        columns = ['accommodates', 'beds','bedrooms',
                    'room_type','latitude','longitude',
                    'host_response_time','host_is_superhost',
                    'host_identity_verified', 'instant_bookable'],
        data = [[accommodates,beds,bedrooms,
                room_type,latitude,longitude,
                host_response_time,host_is_superhost,
                host_identity_verified, instant_bookable]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'The Base Estimated price is: {y_pred:.0f} JPY'
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(children=[
        
        html.H2('Predicted Tokyo AirBnB Price', className='mb-5'),
        
        html.Div(id='prediction-content', className='lead'),
        

    ],


    

    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Specifications', className='mb-5'),
        dcc.Markdown('#### Guests'),
        dcc.Slider(
            id='accommodates',
            min=1,
            max=16,
            step=1,
            value=0,
            marks={n: str(n) for n in range(1,16,1)},
            className='mb-5'
        ),
        dcc.Markdown('#### Beds'),
        dcc.Slider(
            id='beds',
            min=1,
            max=10,
            step=1,
            value=0,
            marks={n: str(n) for n in range(1,10,1)},
            className='mb-5'
        ),
        dcc.Markdown('#### Number of bedrooms'),
        dcc.Slider(
            id='bedrooms',
            min=1,
            max=10,
            step=1,
            value=0,
            marks={n: str(n) for n in range(1,10,1)},
            className='mb-5'
        ),
        dcc.Markdown('#### Room Type'),
        dcc.Dropdown(
            id='room_type',
            options=[
                {'label': 'Entire home/apt','value': 'Entire home/apt'},
                {'label': 'Private room','value': 'Private room'},
                {'label': 'Shared room','value': 'Shared room'},
                {'label': 'Hotel room','value': 'Hotel room'}
            ],
            value='Entire home/apt'
        ),#add pred from here
        dcc.Markdown('#### Latitude'),
        dcc.Slider(
            id='latitude',
            min=35.540520,
            max=35.832220,
            step=0.0001,
            value=0,
            marks={i: '{}'.format(i) for i in range(35,36)},
            className='mb-5'
        ),
        dcc.Markdown('#### Longitude'),
        dcc.Slider(
            id='longitude',
            min=139.095630,
            max=139.911430,
            step=0.0001,
            value=0,
            marks={i: '{}'.format(i) for i in range(139,140)},
            className='mb-5'
        ),
        dcc.Markdown('#### Host Response Time'),
        dcc.Dropdown(
            id='host_response_time',
            options=[
                {'label': 'within an hour','value': 'within an hour'},
                {'label': 'within a few hours','value': 'within a few hours'},
                {'label': 'within a day ','value': 'within a day' },
                {'label': 'a few days or more ','value': 'a few days or more'}
            ],
            value='within an hour'
        ),
        dcc.Markdown('#### Is Host Superhost?'),
        dcc.Dropdown(
            id='host_is_superhost',
            options=[
                {'label': 'Yes','value': '1'},
                {'label': 'No','value': '0'},
                
            ],
            value='1'
        ),
        dcc.Markdown('#### Host Identity Verified?'),
        dcc.Dropdown(
            id='host_identity_verified',
            options=[
                {'label': 'Yes','value': '1'},
                {'label': 'No','value': '0'},
                
            ],
            value='1'
        ),
        dcc.Markdown('#### Instantly Bookable?'),
        dcc.Dropdown(
            id='instant_bookable',
            options=[
                {'label': 'Yes','value': '1'},
                {'label': 'No','value': '0'},
                
            ],
            value='1'
        ),


    ])
layout = dbc.Row([column1, column2])