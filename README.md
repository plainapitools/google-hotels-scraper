# Google Hotels prices with Python or Node.js

Example scripts for pulling hotel prices from Google Hotels through the [Google Hotels Scraper](https://apify.com/plainapi-tools/google-hotels-scraper) on Apify. One row per hotel: nightly price, stay total, stars, rating, review count, coordinates, website and Google link, for any city, dates and currency.

## Setup

1. Make a free Apify account and copy your API token from [Settings > Integrations](https://console.apify.com/settings/integrations).
2. Set it as an environment variable:

```bash
export APIFY_TOKEN=your_token_here
```

## Python: a 7-day price calendar to CSV

```bash
pip install "apify-client>=3"
python example.py
```

[example.py](example.py) searches "hotels in Lisbon" for 7 check-in dates in a row (2 nights each, starting 30 days from today) and writes `lisbon_hotels.csv`:

```
checkIn,name,hotelClass,rating,pricePerNight,totalPrice,currency,googleUrl
2026-11-21,Brown's | Avenue Hotel,5,4.6,147,294,EUR,https://www.google.com/travel/hotels/entity/...
2026-11-21,Dos Reis by The Beautique Hotels,4,4.4,84,168,EUR,https://www.google.com/travel/hotels/entity/...
```

## Node.js: cheapest 4-star hotels near Times Square

```bash
npm install
node example.mjs
```

[example.mjs](example.mjs) prints the 10 cheapest 4-star hotels for a 3-night stay.

## Input options

| Option | Example | Notes |
|---|---|---|
| `queries` | `["hotels in Paris"]` | Anything you would type into Google Hotels, including a hotel name |
| `checkIn` | `"2026-12-18"` or `"30 days"` | Relative dates count from the day the run starts |
| `checkOut` / `nights` | `"2026-12-21"` / `3` | Up to 30 nights |
| `checkInDays` | `14` | Same stay priced for this many check-in dates in a row |
| `adults` | `2` | 1-10 |
| `currency` | `"EUR"` | ISO code |
| `maxHotels` | `50` | Per search and date |
| `includeVacationRentals` | `false` | Hotels only by default |

Full field list and pricing are on the [Apify page](https://apify.com/plainapi-tools/google-hotels-scraper).

## Running it daily

In Apify Console, save your input as a task and add a schedule. With `checkIn: "30 days"` each run prices the stay 30 days ahead of that day.
