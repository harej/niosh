# public domain

import bs4
#import requests
from pprint import pprint

def main():
    manifest = {}
    
    for id in range(1, 686):  # starting with PGCH #1 and going to #686, the last one
        print("Processing ID: " + str(id))
        if id in [44, 152, 372, 497, 540, 553, 678, 680]:  # missing/irregular IDs
            continue
        #url = "http://www.cdc.gov/niosh/npg/npgd" + str(id).zfill(4) + ".html"
        #r = requests.get(url)
        #if r.status_code == 200:

        manifest[id] = {}

        with open("./source/npgd" + str(id).zfill(4) + ".html") as f:
            contents = f.read()
            soup = bs4.BeautifulSoup(contents, 'html.parser')
            cells = soup.find_all('td')

            manifest[id]['cas_number'] = str(cells[2]).replace('<h6>CAS No.</h6>', '')
            manifest[id]['rtecs_number'] = str(cells[3]).replace('<h6>RTECS No.</h6>', '')
            manifest[id]['conversion'] = str(cells[6]).replace('<h6>Conversion</h6>', '')
            manifest[id]['idlh'] = str(cells[7]).replace('<h6>IDLH</h6>', '')
            manifest[id]['rel_and_pel'] = str(cells[8]).replace('<h5>Exposure Limits</h5>', '')
            manifest[id]['molecular_weight'] = str(cells[11]).replace('<h6>MW:</h6> ', '')
            manifest[id]['boiling_point'] = str(cells[12]).replace('<h6>BP:</h6> ', '')
            manifest[id]['melting_point'] = str(cells[13]).replace('MLT: ', '')
            manifest[id]['solubility'] = str(cells[14]).replace('<h6>Sol:</h6> ', '')
            manifest[id]['vapor_pressure'] = str(cells[15]).replace('<h6>VP:</h6> ', '')
            manifest[id]['ionization_potential'] = str(cells[16]).replace('<td><h6>IP:</h6> ', '')
            manifest[id]['specific_gravity'] = str(cells[17]).replace('h6>Sp.Gr:</h6> ', '')
            manifest[id]['flash_point'] = str(cells[18]).replace('<h6>Fl.P:</h6> ', '')
            manifest[id]['upper_explosive_limit'] = str(cells[19]).replace('<h6>UEL:</h6> ', '')
            manifest[id]['lower_explosive_limit'] = str(cells[20]).replace('<h6>LEL:</h6> ', '')
            manifest[id]['relative_gas_density'] = str(cells[21]).replace('<h6>RGasD:</h6> ', '')
            manifest[id]['minimum_explosive_concentration'] = str(cells[22])
            manifest[id]['combustibility'] = str(cells[23])
            manifest[id]['exposure_routes'] = str(cells[25]).replace('<h6>Exposure Routes</h6>', '')
            manifest[id]['symptoms'] = str(cells[26]).replace('<h6>Symptoms</h6>', '')
            manifest[id]['target_organs'] = str(cells[27]).replace('<h6>Target Organs</h6>', '')
            
            schema = len(cells)
            if schema == 32:  # schema for non-carcinogens
                manifest[id]['personal_protection_and_sanitation'] = str(cells[28]).replace('<h6>Personal Protection/Sanitation</h6>\n(<a href="protect.html">See protection codes</a>) <br/>', '')
                manifest[id]['first_aid'] = str(cells[29]).replace('<h6>First Aid</h6>\n(<a href="firstaid.html">See procedures</a>)<br/>', '')
            elif schema == 33:  # schema for carcinogens
                manifest[id]['personal_protection_and_sanitation'] = str(cells[29]).replace('<h6>Personal Protection/Sanitation</h6>\n(<a href="protect.html">See protection codes</a>) <br/>', '')
                manifest[id]['first_aid'] = str(cells[30]).replace('<h6>First Aid</h6>\n(<a href="firstaid.html">See procedures</a>)<br/>', '')

    #pprint(manifest)
    

if __name__ == "__main__":
    main()