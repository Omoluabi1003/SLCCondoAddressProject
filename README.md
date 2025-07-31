# SLC Condo Address Project

This repository contains datasets and utilities for maintaining St. Lucie County's condo site address points.

## Scripts

- `identify_mismatches.py` – identifies addresses whose `parcelnum` does not match those in `PID.csv`.
- `merge_sapid_into_gdb.py` – updates parcel numbers in an ArcGIS feature class using corrected values from `SAPid.csv`.

## Usage

The `merge_sapid_into_gdb.py` script requires a local ArcGIS Python environment with `arcpy` installed.

```bash
python merge_sapid_into_gdb.py <path/to/feature_class> <path/to/SAPid.csv>
```

The `<path/to/feature_class>` argument is the feature class within a geodatabase (for example, `C:/GIS/SiteAddressPoints.gdb/SiteAddressPoint`). `SAPid.csv` must contain `GlobalID` and `parcelnum` columns. The script reads the CSV, matches rows on `GlobalID`, and updates the existing `parcelnum` field.
