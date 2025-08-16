import datetime
import googlemaps
import pandas as pd

api_key = "YOUR_GOOGLE_API_KEY"
gmaps = googlemaps.Client(key=api_key)

train = pd.read_csv("./Corona_NLP_train.csv", encoding='latin-1')
test = pd.read_csv("./Corona_NLP_test.csv", encoding='latin-1')
combined_df: pd = pd.concat([train, test], ignore_index=True)

# [
#    {
#       "address_components":[
#          {
#             "long_name":"Maidenhead",
#             "short_name":"Maidenhead",
#             "types":[
#                "locality",
#                "political"
#             ]
#          },
#          {
#             "long_name":"Maidenhead",
#             "short_name":"Maidenhead",
#             "types":[
#                "postal_town"
#             ]
#          },
#          {
#             "long_name":"Berkshire",
#             "short_name":"Berkshire",
#             "types":[
#                "administrative_area_level_2",
#                "political"
#             ]
#          },
#          {
#             "long_name":"England",
#             "short_name":"England",
#             "types":[
#                "administrative_area_level_1",
#                "political"
#             ]
#          },
#          {
#             "long_name":"United Kingdom",
#             "short_name":"GB",
#             "types":[
#                "country",
#                "political"
#             ]
#          },
#          {
#             "long_name":"SL6",
#             "short_name":"SL6",
#             "types":[
#                "postal_code",
#                "postal_code_prefix"
#             ]
#          }
#       ],
#       "formatted_address":"Maidenhead SL6, UK",
#       "geometry":{
#          "bounds":{
#             "northeast":{
#                "lat":51.5474174,
#                "lng":-0.6843697999999999
#             },
#             "southwest":{
#                "lat":51.4886118,
#                "lng":-0.7729980999999999
#             }
#          },
#          "location":{
#             "lat":51.5225605,
#             "lng":-0.7243082
#          },
#          "location_type":"APPROXIMATE",
#          "viewport":{
#             "northeast":{
#                "lat":51.5474174,
#                "lng":-0.6843697999999999
#             },
#             "southwest":{
#                "lat":51.4886118,
#                "lng":-0.7729980999999999
#             }
#          }
#       },
#       "place_id":"ChIJk8fCnEBidkgR9px0PvTGVN4",
#       "types":[
#          "locality",
#          "political"
#       ]
#    }
# ]

def get_canonical_address(location: str):
    geocode_result: list[dict] = gmaps.geocode(location)

    if geocode_result:
        if len(geocode_result) == 1:
            formatted_address = geocode_result[0]['formatted_address']
            country_long_name = "N/A"
            country_short_name = "N/A"
            for component in geocode_result[0]['address_components']:
                if 'country' in component['types']:
                    country_long_name = component['long_name']
                    country_short_name = component['short_name']
                    break
            return formatted_address, country_long_name, country_short_name
        else:
            return "N/A", "N/A", "N/A"
    return "N/A", "N/A", "N/A"

# 


import html

cache = {}
for l in combined_df.Location.disctinct():

    try:
        canonical_address, long_name, short_name = get_canonical_address(l)
    except Exception as e:
        print(f"Error processing location '{l}': {e}")
        canonical_address, long_name, short_name = "N/A", "N/A", "N/A"
    print(f"{datetime.datetime.now()} - Canonical address for '{l}': {canonical_address}, Long Name: {long_name}, Short Name: {short_name}")

    cache[l] = {
        "canonical_address": canonical_address,
        "long_name": long_name,
        "short_name": short_name
    }

# Save the cache to a JSON file
import json
with open('location_cache.json', 'w') as f:
    json.dump(cache, f, indent=4)

