import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # For deployment on Render

# Sample data
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50],
    "category": ["A", "B", "A", "B", "A"]
})

# Layout of the app
app.layout = html.Div([
    html.H1("Sample Dash Dashboard"),
    html.P("Select a category to filter the data:"),
    dcc.Dropdown(
        id="category-filter",
        options=[
            {"label": "All", "value": "All"},
            {"label": "A", "value": "A"},
            {"label": "B", "value": "B"}
        ],
        value="All"
    ),
    dcc.Graph(id="scatter-plot")
])

# Callback to update the graph based on the dropdown
@app.callback(
    Output("scatter-plot", "figure"),
    Input("category-filter", "value")
)
def update_graph(selected_category):
    filtered_df = df if selected_category == "All" else df[df["category"] == selected_category]
    fig = px.scatter(filtered_df, x="x", y="y", title="Scatter Plot", color="category")
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

