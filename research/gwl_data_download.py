import requests
import pandas as pd

startdate = "2020-01-01"
enddate = "2023-12-31"
param = "gwl"  # Options: gwl, temp, sm, rwl, rl, rf, ev, ap

wris_api = {
    "gwl": ["CGWB", "https://indiawris.gov.in/Dataset/Ground%20Water%20Level"],
    "temp": ["Uttar Pradesh", "https://indiawris.gov.in/Dataset/Temperature"],
    "sm": ["NRSC VIC MODEL", "https://indiawris.gov.in/Dataset/Soil%20Moisture"],
    "rwl": ["CWC", "https://indiawris.gov.in/Dataset/River%20Water%20Level"],
    "rl": ["CWC", "https://indiawris.gov.in/Dataset/Relative%20Humidity"],
    "rf": ["CWC", "https://indiawris.gov.in/Dataset/RainFall"],
    "ev": ["NRSC VIC MODEL", "https://indiawris.gov.in/Dataset/Evapo%20Transpiration"],
    "ap": ["Uttar Pradesh SW", "https://indiawris.gov.in/Dataset/Atmospheric%20Pressure"],
}

state = "Delhi"
# districts = ["Baghpat", "Buland shahar", "G. b. nagar", "Ghaziabad", "Hapur", "Meerut", "Muzaffarnagar"]
districts = ["Central","East","New","North","North East","North West","Shahdara","South","South East","South West","West"]
all_data = []

for dist in districts:
    page = 0
    while True:
        params = {
            "stateName": state,
            "districtName": dist,
            "agencyName": wris_api[param][0],
            "startdate": startdate,
            "enddate": enddate,
            "download": "false",
            "page": page,
            "size": 1000
        }

        response = requests.post(wris_api[param][1], params=params)
        data = response.json()

        if "data" in data and data["data"]:
            print(f"✅ Got {len(data['data'])} records for {dist}, page {page}")
            all_data.extend(data["data"])
            page += 1  # go to next page
        else:
            print(f"⚠ No more data for {dist} (stopped at page {page})")
            break

# Save to CSV
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv(f"{state}_{param}_20-23.csv", index=False)
    print(f"💾 Data saved to {state}_{param}_20-23.csv")
else:
    print("❌ No data collected for any district")
