// Cheapest 4-star hotels near Times Square for one stay.
// npm install apify-client
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor("plainapi-tools/google-hotels-scraper").call({
    queries: ["hotels near Times Square"],
    checkIn: "2026-12-18",
    checkOut: "2026-12-21",
    adults: 2,
    currency: "USD",
    maxHotels: 60,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
items
    .filter(h => h.hotelClass === 4)
    .sort((a, b) => a.pricePerNight - b.pricePerNight)
    .slice(0, 10)
    .forEach(h => console.log(`${h.priceText.padEnd(8)} ${h.rating ?? "-"}  ${h.name}`));
