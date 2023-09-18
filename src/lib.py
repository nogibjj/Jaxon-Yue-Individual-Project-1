import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_path):
    return pd.read_csv(file_path)

def return_mean(df, col):
    mean = df[col].mean()
    return mean

def return_median(df, col):
    median = df[col].median()
    return median

def return_sd(df, col):
    sd = df[col].std()
    return sd

def plot_hist(df, col, jupyter = False):
    data = df[col].dropna()
    plt.hist(data, bins=5, edgecolor="k")

    plt.xlabel('Average Annual Wages')
    plt.ylabel('Frequency')
    plt.title('Histogram of Average Annual Wages')
    plt.show()
    
    if not jupyter:
        hist_path = 'output/visualization_histogram.png'
        plt.savefig(hist_path)
        
def plot_growth(df, col, jupyter = False):
    # Find the mean for every year's data
    mean_2000 = np.mean(df['2000'])
    mean_2010 = np.mean(df['2010'])
    mean_2020 = np.mean(df['2020'])
    mean_2022 = np.mean(df['2022'])
    means = [mean_2000, mean_2010, mean_2020, mean_2022]
    years = [2000, 2010, 2020, 2022]

    plt.plot(years, means)
    plt.xlabel('Year')
    plt.xticks(ticks = years, labels = ['2000', '2010', '2020', '2022'])
    plt.ylabel('Average Annual Wages')
    plt.title('Growth of Average Annual Wages')
    plt.show()

    if not jupyter:
        growth_path = 'output/visualization_growth.png'
        plt.savefig(growth_path)

if __name__ == "__main__":
    df = pd.read_csv("Development of Average Annual Wages.csv")
    col = "2022"

    print('Target Column: ', 'col')
    print('Mean: ', return_mean(df, col))
    print('Median: ', return_median(df, col))
    print("Standard Deviation: ", return_sd(df, col))

    plot_hist(df, col, jupyter=True)