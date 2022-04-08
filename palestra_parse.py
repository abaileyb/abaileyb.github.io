import csv
import json

filename = "palestra.csv"

fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)

    for field in fields:
        print field
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

vips = []
premiums = []
ga = []
ponly = []

for row in rows:
    print row
    if row['\xef\xbb\xbfBarcode '][0:3] == "BC=":
        #is an actual barcode
        if row['Seatblock '][0:3] == "VIP":
            #is a vip
            vips.append(row['\xef\xbb\xbfBarcode '][3:].strip())
        elif row['Seatblock '][0:3] == "PRE":
            #is a premium
            premiums.append(row['\xef\xbb\xbfBarcode '][3:].strip())
        elif row['Seatblock '][0:3] == "GEN":
            #is a genad
            ga.append(row['\xef\xbb\xbfBarcode '][3:].strip())
        elif row['Seatblock '][0:3] == "PON":
            #is a ponly
            ponly.append(row['\xef\xbb\xbfBarcode '][3:].strip())
        else:
            print("MAJOR ERROR!!" + row['Seatblock '])

print("NUM VIPS: " + str(len(vips)))
print("NUM PRE: " + str(len(premiums)))
print("NUM GEN: " + str(len(ga)))
print("NUM PO: " + str(len(ponly)))

# with open('vip_json.json', 'w') as outfile:
#     json.dump(vips, outfile)

# with open('premium_json.json', 'w') as outfile:
#     json.dump(premiums, outfile)

# with open('ga.json', 'w') as outfile:
#     json.dump(ga, outfile)

# with open('ponly.json', 'w') as outfile:
#     json.dump(ponly, outfile)

with open('vips.js', 'w') as f:
    print >> f, "const vips = ["
    for vip in vips:
        print >> f, "\"" + vip + "\"" + ", "
    print >> f, "];"

with open('premiums.js', 'w') as f:
    print >> f, "const premiums = ["
    for premium in premiums:
        print >> f, "\"" + premium + "\"" + ", "
    print >> f, "];"

with open('ga.js', 'w') as f:
    print >> f, "const ga = ["
    for eaga in ga:
        print >> f, "\"" + eaga + "\"" + ", "
    print >> f, "];"

with open('ponly.js', 'w') as f:
    print >> f, "const ponly = ["
    for ponlyea in ponly:
        print >> f, "\"" + ponlyea + "\"" + ", "
    print >> f, "];"