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

# US Airways
code = "US"
filename = "regions.list.usair"
regions = {"Continental": [25, 25, 50, 50],
           "Caribbean": [35, 35, 60, 60],
           "MexicoCentral": [35, 35, 60, 60], 
           "SouthAmerica": [60, 60, 100, 125],
           "Europe": [60, 60, 100, 125],
           "NorthAsia": [60, 60, 90, 120],
           "SouthCentralAsia": [80, 80, 120, 160],
           "SouthPacific": [80, 80, 110, 140],
           "MiddleEast": [80, 80, 120, 180],
           "Africa": [70, 70, 110, 150],
          }
total += [[code, filename, regions]]

# United
code = "UA"
filename = "regions.list.united"
regions = {"NorthAmerica": [12.5, 25, 25, 70],
           "Caribbean": [17.5, 35, 40, 80],
           "CentralAmerica": [17.5, 35, 40, 80],
           "NorthSouthAm": [17.5, 35, 40, 80],
           "SouthSouthAmerica": [27.5, 55, 67.5, 135],
           "Europe": [27.5, 55, 67.5, 135],
           "Japan": [32.5, 65, 67.5, 135],
           "NorthAsia": [32.5, 65, 72.5, 145],
           "SouthAsia": [32.5, 65, 72.5, 145],
           "CentralAsia": [40, 40, 60, 80],
           "OzKiwi": [40, 80, 80, 160],
           "Oceania": [40, 40, 60, 74],
           "MiddleEast": [37.5, 75, 72.5, 145],
           "NorthAfrica": [37.5, 90, 72.5, 160],
           "CentralSouthAfrica": [45, 45, 62.5, 80],
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
        for cname in clist:
            p1 = [code, origin, cname, prices[0], prices[1], "ECO"]
            p2 = [code, origin, cname, prices[2], prices[3], "FIRST"]
            out.writerow(p1)
            out.writerow(p2)

for line in total:
    code, filename, regions = line
    airlines(code, filename, regions, csv)
