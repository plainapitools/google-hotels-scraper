# Google Hotels prices for one city, 7 check-in dates in a row, saved to CSV.
# pip install "apify-client>=3"
import csv
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])  # https://console.apify.com/settings/integrations

run = client.actor("plainapi-tools/google-hotels-scraper").call(run_input={
    "queries": ["hotels in Lisbon"],
    "checkIn": "30 days",   # relative, so a daily schedule always looks 30 days ahead
    "nights": 2,
    "checkInDays": 7,       # price calendar: 7 check-in dates in a row
    "currency": "EUR",
    "maxHotels": 20,
})

rows = list(client.dataset(run.default_dataset_id).iterate_items())
fields = ["checkIn", "name", "hotelClass", "rating", "pricePerNight", "totalPrice", "currency", "googleUrl"]
with open("lisbon_hotels.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print(f"{len(rows)} rows saved to lisbon_hotels.csv")
