# Step 5: Prepare HTML table that lists each item/property of interest, highlighting cells where values are missing
# Step 6: Take percentages of coverage in each language; save to a timestamped log

# Public domain

import requests
import datetime
from pprint import pprint


def wdqs(encoded_query):
    # Takes URL-encoded SPARQL query for the Wikidata Query Service
    # Returns list of Wikidata items
    base_url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?query={0}&format=json"
    r = requests.get(base_url.format(encoded_query))
    blob = r.json()
    output = []
    for item in blob['results']['bindings']:
        cleaned_value = item['item']['value'].replace("http://www.wikidata.org/entity/", "")
        output.append(cleaned_value)
    return output

def entitydata(identifier):
    # Takes Wikidata entity identifier
    # Returns dictionary based on JSON blob from Special:EntityData

    base_url = "https://www.wikidata.org/wiki/Special:EntityData/{0}.json"
    r = requests.get(base_url.format(identifier))
    return r.json()

def linked_on_page(blob):
    # Takes EntityData dictionary and returns list of items and properties linked on a Wikidata item

    output = []
    for entity in blob['entities']:  # There will only ever be one
        for claim in entity['claims']:
            for subclaim in claim:
                output.append(subclaim['mainsnak']['property'])  # Property number
                if subclaim['mainsnak']['datatype'] == "wikibase-item":
                    output.append('Q' + str(subclaim['mainsnak']['data-value']['value']['numeric-id']))  # Item number
                elif subclaim['mainsnak']['datatype'] == "quantity":  # If the claim involves a unit of measurement
                    measurement_item = subclaim['mainsnak']['datavalue']['value']['unit']
                    measurement_item = measurement_item.replace("http://www.wikidata.org/entity/", "")
                    output.append(measurement_item)  # Item number for the unit of measurement

    return output

def other_language_labels(blob, language_codes):
    # Takes EntityData dictionary, list of ISO language codes (e.g. ['en', 'de'])
    # Returns dictionary of language code -> label (or language code -> None)

    print(blob)  # debug
    output = {x: None for x in language_codes}  # Default is no label
    for entity in blob['entities']:
        for language_code in language_codes:
            if language_code in entity['labels']:
                output[language_code] = entity['labels'][language_code]['value']
    return output

def gap_analysis(manifest):
    # Takes a dictionary of dictionaries {item -> {language: label}}
    # Returns a dictionary of language -> percent covered

    total = len(manifest)
    counter = {}

    for entry in manifest:
        for code, label in entry.items():
            if label != None:
                if code not in counter:
                    counter[code] = 1
                else:
                    counter[code] += 1

    return {code: sum / total for code, sum in counter.items()}

#def web_page_generator(manifest):
    # Takes a dictionary of dictionaries {item -> {language: label}}
    # Returns nothing; creates two web pages

def main():
    language_codes = ['en', 'es', 'zh', 'fr', 'de']
    
    print("Querying for list of chemical/exposure items...")
    chemicals_and_exposures_query = "prefix%20wdt%3A%20<http%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F>%0Aprefix%20entity%3A%20<http%3A%2F%2Fwww.wikidata.org%2Fentity%2F>%0ASELECT%20%3Fitem%20WHERE%20%7B%0A%7B%0A%20%20%20%20%3Fitem%20wdt%3AP1931%20%3Fdummy0%20.%0A%7D%20UNION%20%7B%0A%20%20%20%20%3Fitem%20wdt%3AP279%20entity%3AQ21167512%20.%0A%7D%0A%7D"
    chemicals_and_exposures = wdqs(chemicals_and_exposures_query)
    
    master_list = {}
    for item in chemicals_and_exposures:
        print("Processing chemical/exposure item: " + item)
        blob = entitydata(item)
        chemicals_and_exposures_labels = other_language_labels(blob, language_codes)
        for entry in chemicals_and_exposures_labels:
            master_list[item] = entry
        for link in linked_on_page(blob):
            if link in master_list:
                continue
            else:
                print("Processing linked entity: " + link)
                labels = other_language_labels(entitydata(link), language_codes)
                for entry in labels:
                    master_list[link] = entry

    master_list = list(set(master_list))  # just in case

    print("Doing gap analysis...")
    gap_report = gap_analysis(master_list)
    pprint(gap_report)  # debug


if __name__ == "__main__":
    main()