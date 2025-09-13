import cdsapi
import os

c = cdsapi.Client()

# Bounding box for Delhi
#  [North, West, South, East]
bbox = [29.0, 76.7, 28.3, 77.5]

years = ["2020", "2021", "2022", "2023"]
months = [f"{m:02d}" for m in range(1, 13)]

# Define variables and datasets
variables = {
    "Temperature": {"dataset": "reanalysis-era5-land", "vars": ["2m_temperature"]},
    # "RelativeHumidity": {"dataset": "reanalysis-era5-land","vars": ["2m_dewpoint_temperature"]},
    # "Rainfall": {"dataset": "reanalysis-era5-land", "vars": ["total_precipitation"]},
    # "SoilMoisture": {"dataset": "reanalysis-era5-land", "vars": ["volumetric_soil_water_layer_1", "volumetric_soil_water_layer_2", "volumetric_soil_water_layer_3", "volumetric_soil_water_layer_4"]},
    # "Evaporation": {"dataset": "reanalysis-era5-land", "vars": ["total_evaporation"]},
    # "AtmosphericPressure": {"dataset": "reanalysis-era5-land", "vars": ["surface_pressure"]},
    # "SoilType": {"dataset": "reanalysis-era5-single-levels", "vars": ["soil_type"]}
}

# Loop through variables
for folder_name, details in variables.items():
    dataset = details["dataset"]
    var_list = details["vars"]

    # Create folder if not exists
    folder_path = os.path.join("Copernicus_Data", f"Copernicus_{folder_name}")
    os.makedirs(folder_path, exist_ok=True)

    for var in var_list:
        for year in years:
            for month in months:
                outfile = os.path.join(
                    folder_path,
                    f"Delhi_{var}{year}{month}.nc"
                )
                print(f"Downloading {outfile}...")

                # Base request
                request = {
                    "variable": var,
                    "year": year,
                    "month": month,
                    "day": [f"{d:02d}" for d in range(1, 32)],
                    "time": [f"{h:02d}:00" for h in range(24)],
                    "area": bbox,
                    "data_format": "netcdf",
                    "download_format": "unarchived",
                }

                # Add product_type only for SoilType
                if folder_name == "SoilType":
                    request["product_type"] = "reanalysis"

                # Retrieve data
                c.retrieve(dataset, request, outfile)