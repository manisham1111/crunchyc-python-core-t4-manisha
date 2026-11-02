
import logging
from logging.handlers import RotatingFileHandler

from pipeline.fetch import fetch_data
from pipeline.clean import clean_data
from pipeline.analyze import analyze_data
from pipeline.deliver import deliver_data


# Rotating log configuration
handler = RotatingFileHandler(
    "logs/pipeline.log",
    maxBytes=1024 * 1024,
    backupCount=3
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[handler]
)


def main():
    try:
        logging.info("Pipeline started")

        # Step 1: Fetch
        books = fetch_data()
        logging.info("Fetched %s books", len(books))

        # Step 2: Clean
        df = clean_data(books)
        logging.info("Cleaned data: %s books", len(df))

        # Step 3: Analyze
        report = analyze_data(df)
        logging.info("Analysis completed")

        # Step 4: Deliver
        deliver_data(df, report)
        logging.info("Pipeline completed successfully")

        print("Pipeline completed successfully!")

    except Exception as error:
        logging.exception("Pipeline failed")
        print(f"Pipeline failed: {error}")


if __name__ == "__main__":
    main()
