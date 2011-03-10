import csv
out = csv.writer(open("regions.csv","w"), delimiter=",")
out.writerow(["Airline","Origin","Destination","Low","High","Class"])
total = []

# American Airlines:
code = "AA"
filename = "regions.list.aa"
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
total += [[code, filename, regions]]

# Delta
code = "DL"
filename = "regions.list.delta"
regions = {"Continental": [12.5, 30, 22.5, 50],
           "Caribbean": [17.5, 45, 30, 70],
          "Mexico": [17.5, 45, 30, 70],
          "CentralAmerica": [17.5, 45, 30, 70],
          "NorthernSouthAm": [22.5, 50, 45, 90],
          "SouthernSouthAm": [30, 62.5, 50, 162.5],
          "Europe": [30, 62.5, 50, 162.5],
          "Africa": [40, 80, 60, 175],
          "MiddleEast": [40, 80, 60, 175],
          "SouthAsia": [40, 80, 60, 175],
          "NorthAsia": [35, 80, 60, 170],
          "SouthEastAsia": [40, 87.5, 60, 185],
          "SouthWestPacific": [50, 95, 75, 185],
          "SouthAfrica": [50, 100, 70, 190],
          }
total += [[code, filename, regions]]


def airlines(code, filename, regions, csv):
    data = open(filename, "r")
    for line in data.readlines():
        line = line.strip()
        region, countries = line.split(";")
        clist = countries.split(",")
        prices = regions[region]
        origin = "US"
        code = "AA"
        for cname in clist:
            p1 = [code, origin, cname, prices[0], prices[1], "ECO"]
            p2 = [code, origin, cname, prices[2], prices[3], "FIRST"]
            out.writerow(p1)
            out.writerow(p2)

for line in total:
    airlines(code, filename, regions, csv)
