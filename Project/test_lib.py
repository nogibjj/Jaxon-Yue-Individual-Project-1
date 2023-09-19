import lib
import pandas as pd
import matplotlib.pyplot as plt

def test_read_data():
    expected = pd.read_csv('Development of Average Annual Wages.csv')
    result = lib.read_data('Development of Average Annual Wages.csv')
    assert expected.equals(result)

def test_return_mean():
    df = lib.read_data('Development of Average Annual Wages.csv')
    col = '2022'
    expected = 49685.529411764706
    result = lib.return_mean(df, col)
    assert expected == result

def test_return_median():
    df = lib.read_data('Development of Average Annual Wages.csv')
    col = '2022'
    expected = 50564.5
    result = lib.return_median(df, col)
    assert expected == result

def test_return_sd():
    df = lib.read_data('Development of Average Annual Wages.csv')
    col = '2022'
    expected = 15794.866072768218
    result = lib.return_sd(df, col)
    assert expected == result

def test_visualization_hist():
    df = lib.read_data('Development of Average Annual Wages.csv')
    col = '2022'

    lib.plot_hist(df, col)
    fig = plt.gcf()
    assert len(fig.axes) > 0

def test_visualization_growth():
    df = lib.read_data('Development of Average Annual Wages.csv')
    col = '2022'

    lib.plot_growth(df, col)
    fig = plt.gcf()
    assert len(fig.axes) > 0


if __name__ == "__main__":
    test_return_mean()
    test_return_median()
    test_return_sd()
    test_visualization_hist()
    test_visualization_growth()
