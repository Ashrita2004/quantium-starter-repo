import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the sales data
data = pd.read_csv('combined_data.csv')

# Ensure the date column is in datetime format
data['date'] = pd.to_datetime(data['date'])

# Sort the data by date
data = data.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the line chart
fig = px.line(data, x='date', y='sales', title='Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales'},
              markers=True)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Visualizer'),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
