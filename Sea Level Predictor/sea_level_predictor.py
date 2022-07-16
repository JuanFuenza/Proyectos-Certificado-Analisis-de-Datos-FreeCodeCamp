import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax = df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', figsize=(12,5), title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')

    # Create first line of best fit
    lin = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_extended = np.arange(df['Year'].min(), 2051, 1)
    ax = plt.plot(y_extended, lin.intercept + y_extended*lin.slope, 'r')

    # Create second line of best fit
    y_2000 = df[df['Year'] >= 2000]
    lin = linregress(y_2000['Year'], y_2000['CSIRO Adjusted Sea Level'])
    y_extended = np.arange(2000, 2051, 1)
    ax = plt.plot(y_extended, lin.intercept + y_extended*lin.slope, 'green')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()