"""This is a script that calls the descriptive statistics function from lib.py"""
import lib

def run_read_data(file_path):
    return lib.read_data(file_path)

def run_desc_stat(df, col):
    stats = {
        'Target Column: ': col + " Average Annual Wages in the World",
        'Mean: ': lib.return_mean(df, col),
        'Median: ': lib.return_median(df, col),
        "Standard Deviation: ": lib.return_sd(df, col),
    }
    return stats

def run_visualizations(df, col):
    lib.plot_hist(df, col)
    lib.plot_growth(df)

if __name__ == "__main__":
   df = run_read_data("Development of Average Annual Wages.csv")
   col = '2022'

   run_desc_stat(df, col)
   run_visualizations(df, col)