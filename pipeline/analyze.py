
def analyze_data(df):
    """Generate book price statistics."""

    report = {
        "total_books": len(df),
        "average_price": round(df["price"].mean(), 2),
        "minimum_price": round(df["price"].min(), 2),
        "maximum_price": round(df["price"].max(), 2)
    }

    return report
