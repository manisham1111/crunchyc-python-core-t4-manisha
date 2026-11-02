
import pandas as pd

from pipeline.clean import clean_data
from pipeline.analyze import analyze_data


def test_clean_removes_duplicates():
    books = [
        {"title": "Book A", "price": "£10.00"},
        {"title": "Book A", "price": "£10.00"},
        {"title": "Book B", "price": "£20.00"}
    ]

    df = clean_data(books)

    assert len(df) == 2


def test_analyze_total_books():
    df = pd.DataFrame({"price": [10, 20, 30]})

    report = analyze_data(df)

    assert report["total_books"] == 3
    assert report["average_price"] == 20
