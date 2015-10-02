# public domain

import bs4
import csv

def main():
    header = ['id', 'cas_number', 'rtecs_number', 'conversion', 'idlh',
              'rel_and_pel', 'molecular_weight', 'boiling_point', 'melting_point',
              'solubility', 'vapor_pressure', 'ionization_potential',
              'specific_gravity', 'flash_point', 'upper_explosive_limit',
              'lower_explosive_limit', 'relative_gas_density',
              'minimum_explosive_concentration', 'combustibility', 'exposure_routes',
              'symptoms', 'target_organs', 'personal_protection_and_sanitation',
              'first_aid']

    with open('output.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header row

        for id in range(1, 686):  # starting with PGCH #1 and going to #685, the last one
            print("Processing ID: " + str(id))
            if id in [44, 152, 372, 497, 540, 553, 678, 680]:  # missing/irregular IDs
                continue
    
            with open("./source/npgd" + str(id).zfill(4) + ".html") as f:
                contents = f.read()
                soup = bs4.BeautifulSoup(contents, 'html.parser')
                cells = soup.find_all('td')

                # Initializing row
                X = None  # Takes up less space
                row = [X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X]

                row[0] = str(id).zfill(4)
                row[1] = str(cells[2]).replace('<h6>CAS No.</h6>', '')
                row[2] = str(cells[3]).replace('<h6>RTECS No.</h6>', '')
                row[3] = str(cells[6]).replace('<h6>Conversion</h6>', '')
                row[4] = str(cells[7]).replace('<h6>IDLH</h6>', '')
                row[5] = str(cells[8]).replace('<h5>Exposure Limits</h5>', '')
                row[6] = str(cells[11]).replace('<h6>MW:</h6> ', '')
                row[7] = str(cells[12]).replace('<h6>BP:</h6> ', '')
                row[8] = str(cells[13]).replace('MLT: ', '')
                row[9] = str(cells[14]).replace('<h6>Sol:</h6> ', '')
                row[10] = str(cells[15]).replace('<h6>VP:</h6> ', '')
                row[11] = str(cells[16]).replace('<td><h6>IP:</h6> ', '')
                row[12] = str(cells[17]).replace('h6>Sp.Gr:</h6> ', '')
                row[13] = str(cells[18]).replace('<h6>Fl.P:</h6> ', '')
                row[14] = str(cells[19]).replace('<h6>UEL:</h6> ', '')
                row[15] = str(cells[20]).replace('<h6>LEL:</h6> ', '')
                row[16] = str(cells[21]).replace('<h6>RGasD:</h6> ', '')
                row[17] = str(cells[22])
                row[18] = str(cells[23])
                row[19] = str(cells[25]).replace('<h6>Exposure Routes</h6>', '')
                row[20] = str(cells[26]).replace('<h6>Symptoms</h6>', '')
                row[21] = str(cells[27]).replace('<h6>Target Organs</h6>', '')
                
                schema = len(cells)
                if schema == 32:  # schema for non-carcinogens
                    row[22] = str(cells[28])
                    row[23] = str(cells[29])
                elif schema == 33:  # schema for carcinogens
                    row[22] = str(cells[29])
                    row[23] = str(cells[30])

                row[22] = row[22].replace('<h6>Personal Protection/Sanitation</h6>\n(<a href="protect.html">See protection codes</a>) <br/>', '')
                row[23] = row[23].replace('<h6>First Aid</h6>\n(<a href="firstaid.html">See procedures</a>)<br/>', '')

                writer.writerow(row)  # Write row to file

if __name__ == "__main__":
    main()