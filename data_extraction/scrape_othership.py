import requests
import pandas as pd
import openpyxl
from datetime import datetime


def scrape_othership_schedule(min_start_date, max_start_date, output_file="othership_schedule_data.xlsx"):
    """
    Scrape Othership class schedule data and save to Excel.

    Args:
        min_start_date (str): Minimum start date in YYYY-MM-DD format
        max_start_date (str): Maximum start date in YYYY-MM-DD format
        output_file (str): Output Excel file path (default: "othership_schedule_data.xlsx")

    Returns:
        pd.DataFrame: DataFrame containing the scraped schedule data
    """
    url = "https://othership.marianatek.com/api/customer/v1/classes"

    params = {
        "min_start_date": min_start_date,
        "max_start_date": max_start_date,
        "page_size": 500,
        "location": "48750,48717",
        "region": "48541",
        "page": 1
    }

    all_results = []

    while True:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print("No more pages. Finished processing")
                break
            else:
                raise e


        data = response.json()

        results = data.get("results", [])

        if not results:
            break

        structured_data = [
            {
                "id": result["id"],
                "available_spot_count": result["available_spot_count"],
                "capacity": result["capacity"],
                "start_datetime": result["start_datetime"],
                "location": result["location"]["name"]
            }
            for result in results
        ]

        all_results.extend(structured_data)

        print(f"Fetched page {params['page']} with {len(results)} classes")

        # Stop if last page is incomplete
        if len(results) < params['page_size']:
            print("Last page reached.")
            break

        params['page'] += 1

    df = pd.DataFrame(all_results)

    df["start_datetime"] = pd.to_datetime(df["start_datetime"], utc=True)
    df["start_datetime"] = df["start_datetime"].dt.tz_convert("America/Toronto")
    df["start_datetime"] = df["start_datetime"].dt.tz_localize(None)
    df["start_time"] = df["start_datetime"].dt.strftime("%I:%M %p")

    df.to_excel(output_file)

    print(df.head())

    return df


if __name__ == "__main__":
    scrape_othership_schedule(
        min_start_date="2024-11-18",
        max_start_date="2025-11-18",
        output_file="othership_schedule_data_new.xlsx"
    )