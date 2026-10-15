import pandas as pd

from churn.preprocessing import remove_missing_values


def main() -> None:
    df = pd.DataFrame(
        {
            "age": [25, 30, None],
            "monthly_spend": [50, 80, 40],
        }
    )

    cleaned = remove_missing_values(df)

    print(cleaned)


if __name__ == "__main__":
    main()