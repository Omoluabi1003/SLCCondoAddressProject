# SLC Condo Address Project

## Project at a glance

**Category:** St. Lucie County condominium site-address QA utilities  
**Purpose:** Find parcel-linkage mismatches and update GIS address-point identifiers using reviewed correction files  
**Audience:** Users, contributors, implementers and project reviewers  
**Source repository:** https://github.com/Omoluabi1003/SLCCondoAddressProject

**Readiness boundary:** Writes to geodatabases require ArcPy, validated field mappings, backups and approval by authorized data custodians.

Continue below for the existing documentation, including setup, architecture or deployment instructions where provided. Planned capabilities must be independently validated before being described as live.

---


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
