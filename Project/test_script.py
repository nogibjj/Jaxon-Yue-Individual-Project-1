import script
import pandas as pd

def test_run_desc_stat():
    result = script.run_desc_stat(df, col)
    assert 'Target Column' in result
    assert 'Mean' in result
    assert 'Median' in result
    assert 'Standard Deviation' in result

if __name__ == "__main__":
    df = pd.read_csv('Development of Average Annual Wages.csv')
    col = '2022'
    test_run_desc_stat()