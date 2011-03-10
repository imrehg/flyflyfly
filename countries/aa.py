import csv
regions = {"Europe": [20,30,50,62.5],
           "India": [45,45,67.5,90],
           "Asia1":[25,32.5,50,62.5],
           "Asia2":[35,35,55,67.5],
           "Pacific":[37.5,37.5, 62.5, 72.5],
           "Africa": [37.5, 37.5, 75,100],
           "SouthAmerica1": [17.5,17.5,30,40],
           "SouthAmerica2": [20,30,50,62.5],
           "Continental": [12.5, 12.5, 25, 32.5],
           "NearAmerica":[17.5,17.5,30,40],
           }

out = csv.writer(open("regions.csv","w"), delimiter=",")
out.writerow(["Airline","Origin","Destination","Low","High","Class"])

filename = "regions.list.aa"
data = open(filename, "r")
for line in data.readlines():
    line = line.strip()
    region, countries = line.split(";")
    clist = countries.split(",")
    prices = regions[region]
    origin = "US"
    airline = "AA"
    for cname in clist:
        p1 = [airline, origin, cname, prices[0], prices[1], "ECO"]
        p2 = [airline, origin, cname, prices[2], prices[3], "FIRST"]
        out.writerow(p1)
        out.writerow(p2)


