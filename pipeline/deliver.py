
import json
import matplotlib.pyplot as plt


def deliver_data(df, report):
    """Save CSV, JSON report and chart."""

    df.to_csv("output/books.csv", index=False)

    with open("output/report.json", "w") as file:
        json.dump(report, file, indent=4)

    plt.figure(figsize=(8, 5))
    df["price"].plot(kind="hist", bins=10)
    plt.title("Book Price Distribution")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Books")
    plt.savefig("output/price_chart.png")
    plt.close()

    print("CSV, JSON and Chart generated successfully!")
