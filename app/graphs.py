import plotly
import plotly.graph_objs as go
import chart_studio.plotly as py

import pandas as pd
import numpy as np
import json

def create_plot(pie_results, bar_results):

    keys = [i[0] for i in pie_results]
    values = [i[1] for i in pie_results]
    pie_chart = go.Figure(data=[go.Pie(labels=keys, values=values)])
    graphpieJSON = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)

    x_values = [i[0] for i in bar_results]
    y_values = [i[1] for i in bar_results]
    df = pd.DataFrame({'x': x_values, 'y': y_values})
    bar_chart = [
        go.Bar(
            x=df['x'],  # assign x as the dataframe column 'x'
            y=df['y'],
            name="Names frequency"
        )
    ]
    graphbarJSON = json.dumps(bar_chart, cls=plotly.utils.PlotlyJSONEncoder)


    return graphpieJSON, graphbarJSON