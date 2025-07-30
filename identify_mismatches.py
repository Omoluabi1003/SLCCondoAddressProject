import csv

# Load valid parcel IDs from PID.csv
valid = set()
with open('PID.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        valid.add(row['ParcelID'].strip())
        valid.add(row['PARCEL_NUMBER'].strip())

# Identify addresses with parcel numbers not in valid set
mismatched = []
with open('SiteAddressCondo.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pid = row['parcelnum'].strip()
        if pid and pid not in valid:
            mismatched.append({
                'fulladdr': row['fulladdr'],
                'placename': row['placename'],
                'usngcoord': row['usngcoord'],
                'parcelnum': row['parcelnum']
            })

# Write out mismatched points
out_file = 'mismatched_addresses.csv'
with open(out_file, 'w', newline='') as f:
    fieldnames = ['fulladdr', 'placename', 'usngcoord', 'parcelnum']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(mismatched)

print(f'Wrote {len(mismatched)} mismatched addresses to {out_file}')
