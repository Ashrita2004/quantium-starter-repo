import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load sales data
data = pd.read_csv('./combined_data.csv')
data['date'] = pd.to_datetime(data['date'])
data.sort_values(by='date', inplace=True)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=['/style.css'])

# Define the layout of the app
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f7f9fc', 'padding': '20px'}, children=[
    html.H1('Soul Foods Pink Morsel Sales Visualizer', style={'textAlign': 'center', 'color': '#333'}),
    
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All Regions', 'value': 'all'}
        ],
        value='all',
        labelStyle={'display': 'block', 'margin': '10px'},
        style={'margin': '20px', 'padding': '10px', 'fontSize': '18px'}
    ),
    
    dcc.Graph(id='sales-graph', style={'height': '70vh'}),
    
    html.Div(id='output', style={'textAlign': 'center', 'marginTop': '20px'})
])

# Define the callback to update the graph
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == selected_region]

    figure = px.line(
        filtered_data,
        x='date',
        y='sales',
        title=f'Sales Data for {selected_region.capitalize()} Region',
        labels={'sales': 'Sales ($)', 'date': 'Date'},
        template='plotly_white'
    )
    
    # Update the layout for better aesthetics
    figure.update_layout(
        title_font=dict(size=24, color='#007bff'),
        xaxis_title_font=dict(size=18),
        yaxis_title_font=dict(size=18),
        legend_title_font=dict(size=16),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
