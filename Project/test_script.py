import script
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch


def test_run_read_data():
    result = script.run_read_data("Development of Average Annual Wages.csv")
    assert isinstance(result, pd.DataFrame)


def test_run_desc_stat():
    df = pd.read_csv("Development of Average Annual Wages.csv")
    col = "2022"

    result = script.run_desc_stat(df, col)
    assert "Target Column" in result
    assert "Mean" in result
    assert "Median" in result
    assert "Standard Deviation" in result


def test_run_visualizations():
    df = pd.read_csv("Development of Average Annual Wages.csv")
    col = "2022"

    script.run_visualizations(df, col)
    fig = plt.gcf()
    assert len(fig.axes) > 0


@patch("script.run_read_data")
@patch("script.run_desc_stat")
@patch("script.run_visualizations")
def test_main(mock_run_visualizations, mock_run_desc_stat, mock_run_read_data):
    mock_run_read_data.return_value = "mocked_dataframe"
    mock_run_desc_stat.return_value = "mocked_stats"
    mock_run_visualizations.return_value = "mocked_visualizations"

    script.main()

    mock_run_read_data.assert_called_once_with(
        "Development of Average Annual Wages.csv"
    )
    mock_run_desc_stat.assert_called_once_with("mocked_dataframe", "2022")
    mock_run_visualizations.assert_called_once_with("mocked_dataframe", "2022")


if __name__ == "__main__":
    test_run_read_data()
    test_run_desc_stat()
    test_run_visualizations()
    test_main()