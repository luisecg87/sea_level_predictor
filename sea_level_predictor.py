import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = line1.slope * x_pred1 + line1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Fitted line 1')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    line2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = line2.slope * x_pred2 + line2.intercept
    plt.plot(x_pred2, y_pred2, 'g', label='Fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
