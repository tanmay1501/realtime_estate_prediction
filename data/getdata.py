from homeharvest import scrape_property
from datetime import datetime

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

filename = "HomeHarvest" + current_time
type = "for_sale"
property = scrape_property(
    location="Dallas, TX",
    listing_type=type,
    past_days =30,
    
)
print(len(property))
property.to_csv(filename+"_"+type+".csv", index=False)
print(property.head())

