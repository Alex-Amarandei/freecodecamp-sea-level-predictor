import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    ## Use Pandas to import the data from epa-sea-level.csv.

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    ## Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    ## Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.

    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept

    plt.plot(x_pred, y_pred, color="red")

    ## Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

    # Create second line of best fit
    res = linregress(
        x=df.loc[df["Year"] >= 2000, "Year"],
        y=df.loc[df["Year"] >= 2000, "CSIRO Adjusted Sea Level"],
    )
    x_pred = pd.Series([i for i in range(2000, 2051)])
    y_pred = res.slope * x_pred + res.intercept

    plt.plot(x_pred, y_pred, color="green")

    ## The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
