import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


def get_scatterplot_matrix(df, col_list):
    """Function will create a Scatter plot given a list of columns

    Args:
        df (Dataframe): Dataframe related to data
        col_list (list): list of columns to use for scatter plot
    """
    fig = px.scatter_matrix(df[col_list])
    fig["layout"].update(
        title={
            "text": "Scatter plot Matrix",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        }
    )
    fig.update_traces(diagonal_visible=False)
    fig.show()


def get_histogram(df, col_name):
    pass


if __name__ == "__main__":
    data = pd.read_csv("Cars93.csv")
    print(f"Data shape read - {data.shape}")

    data.drop("Unnamed: 0", axis=1, inplace=True)
    print("Size of the dataset", data.shape)

    # Draw Scatterplot Matrix
    get_scatterplot_matrix(
        data,
        col_list=[
            "Horsepower",
            "MPG.city",
            "Price",
            "Rear.seat.room",
            "Luggage.room",
        ],
    )

    # TODO:- Create a function to create histogram given a column
    # using any other python library
