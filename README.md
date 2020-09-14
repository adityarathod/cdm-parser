<p align="center"><h1>CDM Parser (WIP)</h1></p>

A parser for public chargemaster data provided by hospitals.

### Project Goals
One of the key goals of this project is to develop a robust ETL pipeline for hospital chargemaster data.
However, since the state of medical billing is a mess in the United States (through systems such as proprietary
billing codes and lack of standardized description of charges across providers), this project may or may not
achieve this ideal.

### Setup Instructions
- Download chargemasters in bulk from https://data.chhs.ca.gov/dataset/chargemasters.
- Extract and place in an accessible path.
- Create file `datasource.ini` in the same folder as this project and put the following in it:

```ini
[chargemasters]
location = /path/to/chargemasters
```