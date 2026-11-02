
import pandas as pd


def clean_data(books):
    """Clean and normalize book data."""

    df = pd.DataFrame(books)

    df.drop_duplicates(subset=["title"], inplace=True)
    df.dropna(subset=["title", "price"], inplace=True)

    df["price"] = (
        df["price"]
        .str.replace("Â", "", regex=False)
        .str.replace("£", "", regex=False)
        .astype(float)
    )

    df["title"] = df["title"].str.strip()

    return df
