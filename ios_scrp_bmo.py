from bmo_reviews import result
import csv

filename = "reviews_ios_bmo.csv"

#CHAT GPT FIX 
all_keys = set()
for entry in result:
    all_keys.update(entry.keys())  # Collect all unique keys

fieldnames = list(all_keys)  # Convert to list for fieldnames in DictWriter

# Write the data to a CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the column headers
    
    # Ensure all dictionaries have all keys (set missing ones to None)
    for entry in result:
        # Add any missing keys with value None
        for key in fieldnames:
            entry.setdefault(key, None)
        writer.writerow(entry)  # Write each row
        
