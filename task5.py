import pytest
from dash import Dash, html, dcc
import dash.testing as dt

# Sample Dash app for testing
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Data Visualization for Pink Morsels", id='header'),
    dcc.Graph(id='sales-line-chart'),  # Example visualization
    dcc.Dropdown(id='region-picker', options=[
        {'label': 'Region 1', 'value': 'region1'},
        {'label': 'Region 2', 'value': 'region2'},
    ])
])

@pytest.fixture
def dash_duo():
    """Create a Dash test client."""
    app.testing = True
    return dt.DashClient(app)

def test_header_present(dash_duo):
    """Test that the header is present."""
    dash_duo.start_server()
    assert dash_duo.get('#header').text == "Sales Data Visualization for Pink Morsels"

def test_visualization_present(dash_duo):
    """Test that the visualization is present."""
    dash_duo.start_server()
    assert dash_duo.get('#sales-line-chart') is not None

def test_region_picker_present(dash_duo):
    """Test that the region picker is present."""
    dash_duo.start_server()
    assert dash_duo.get('#region-picker') is not None
