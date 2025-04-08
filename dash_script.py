# Importar las librerías necesarias
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Leer el dataset
spacex_df = pd.read_csv("spacex_launch_dash.csv")
# Limpiar los nombres de columnas (eliminar espacios al inicio o final)
spacex_df.columns = spacex_df.columns.str.strip()
print(spacex_df.columns.tolist())  # Para verificar los nombres de columnas

# Definir min y max para el payload usando el nombre correcto de la columna
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

# Crear la instancia de la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Dropdown para seleccionar el sitio de lanzamiento
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    # Gráfico circular (Pie Chart)
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: RangeSlider para seleccionar el rango de payload
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),
    html.Br(),

    # Gráfico de dispersión (Scatter Plot)
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# TASK 2: Callback para renderizar el gráfico circular (Pie Chart)
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Para todos los sitios: agrupar por Launch Site y contar los éxitos (se asume que 'class' = 1 es éxito)
        success_counts = spacex_df[spacex_df['class'] == 1]['Launch Site'].value_counts().reset_index()
        success_counts.columns = ['Launch Site', 'Successes']
        fig = px.pie(success_counts, values='Successes', names='Launch Site',
                     title='Total Successful Launches by Site')
        return fig
    else:
        # Para un sitio específico: filtrar el dataframe y contar éxitos y fracasos
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        success_count = filtered_df[filtered_df['class'] == 1].shape[0]
        failure_count = filtered_df[filtered_df['class'] == 0].shape[0]
        pie_df = pd.DataFrame({
            'Outcome': ['Success', 'Failure'],
            'Count': [success_count, failure_count]
        })
        fig = px.pie(pie_df, values='Count', names='Outcome',
                     title=f'Launch Outcomes for site {selected_site}')
        return fig

# TASK 4: Callback para renderizar el gráfico de dispersión (Scatter Plot)
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    if selected_site == 'ALL':
        filtered_df = spacex_df[(spacex_df["Payload Mass (kg)"] >= low) & (spacex_df["Payload Mass (kg)"] <= high)]
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) &
                                 (spacex_df["Payload Mass (kg)"] >= low) &
                                 (spacex_df["Payload Mass (kg)"] <= high)]
    fig = px.scatter(filtered_df, x="Payload Mass (kg)", y="class",
                     color="Booster Version",
                     title="Payload vs. Outcome for " + ("All Sites" if selected_site == 'ALL' else selected_site))
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(port=8050, debug=True)