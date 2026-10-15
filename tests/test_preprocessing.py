import pandas as pd

from churn.preprocessing import remove_missing_values


def test_remove_missing_values():
    df = pd.DataFrame(
        {
            "age": [25, None, 40],
            "spend": [100, 200, 300],
        }
    )

    result = remove_missing_values(df)

    assert len(result) == 2
    assert result["age"].notna().all()