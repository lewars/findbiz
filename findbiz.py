# https://developers.google.com/places/web-service/search#PlaceSearchRequests

import sys
import pprint
import csv
import googlemaps

key="INSERT_API_KEY_HERE"
fields = ['formatted_address', 'formatted_phone_number', 'url', 'website', 'rating']
rows = []

def get_csv_row(details, company_name, user_ratings_total=0):

    result = details['result']

    if 'formatted_phone_number' not in result:
        result['formatted_phone_number'] = ''

    if 'rating' not in result:
        result['rating'] = 0

    if 'website' not in result:
        result['website'] = 'none'
        name_link = company_name
    else:
        company_name = company_name.replace("|", "_")
        name_link = f'=HYPERLINK("{result["url"]}","{company_name}")'

    row = [name_link,
           result['formatted_address'],
           result['formatted_phone_number'],
           result['website'],
           result['rating'],
           user_ratings_total]

    return row

if __name__ == '__main__':
    keyword = sys.argv[1]
    token = None
    client = googlemaps.Client(key)

    for c in range(0,4):
        if token is None:
            results = client.places_nearby(
                location=(40.722471,-74.271519),
                radius=16186,
                keyword=keyword,
                language="en",
                open_now=False)
        else:
            try:
                results = client.places_nearby(page_token=token)
                # pprint.pprint(results)
            except googlemaps.exceptions.ApiError:
                break

        for r in results['results']:
            details = client.place(r['place_id'],
                                   fields=fields,
                                   language="en")
            rows.append(get_csv_row(details, r['name'], r['user_ratings_total']))

        if 'next_page_token' in results and c != 3:
            token = results['next_page_token']
        else:
            break

    with open('bizz.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|', quotechar='|')
        writer.writerows(rows)
