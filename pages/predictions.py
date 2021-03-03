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
     Input('beds', 'value')],
)
def predict(accommodates, beds):
    df = pd.DataFrame(
        columns = ['accommodates', 'beds'],
        data = [[accommodates,beds]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} JPY'
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
            value=1,
            marks={n: str(n) for n in range(1,16,1)},
            className='mb-5'
        ),
        dcc.Markdown('#### Beds'),
        dcc.Slider(
            id='beds',
            min=1,
            max=10,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,10,1)},
            className='mb-5'
        )    

    ])
layout = dbc.Row([column1, column2])