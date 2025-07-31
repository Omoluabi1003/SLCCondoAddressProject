import csv
import sys
import arcpy


def main(feature_class: str, csv_path: str) -> None:
    """Update parcel numbers in the feature class using SAPid.csv."""
    updates = {}
    with open(csv_path, newline='', encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gid = row.get("GlobalID")
            parcel = row.get("parcelnum")
            if gid:
                updates[gid] = parcel

    updated = 0
    with arcpy.da.UpdateCursor(feature_class, ["GlobalID", "parcelnum"]) as cursor:
        for row in cursor:
            gid = row[0]
            if gid in updates:
                row[1] = updates[gid]
                cursor.updateRow(row)
                updated += 1

    print(f"Updated {updated} records in {feature_class}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python merge_sapid_into_gdb.py <feature_class> <SAPid.csv>",
            file=sys.stderr,
        )
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
