import csv
datafile = "countries.csv"
datacsv = csv.reader(open(datafile,"r"), delimiter=',')
data = {}
for d in datacsv:
    data[d[0]] = d[1]

def getlist(clist, datain):
    got = []
    remove = []
    for country in datain.keys():
        if country in clist:
            got += [datain[country]]
            remove += [country]
            # clist.remove(country)
            # datain.remove([country, code])
    got = sorted(got)
    # for rname in remove:
    #     del datain[rname]
    print header+";"+",".join(got)

header = "Africa"
continent = "Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Congo, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Ivory Coast, Kenya, Lesotho, Liberia, Libyan Arab Jamahiriya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Melilla, Morocco, Mozambique, Namibia, Niger, Nigeria, Republic of Congo, Reunion, Rwanda, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

india = "Afghanistan, Bahrain, Bangladesh, Egypt, India, Iran, Iraq, Israel, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon, Maldives, Nepal, Oman, Pakistan, Qatar, Saudi Arabia, Syria, Tajikistan, Turkmenistan, United Arab Emirates, Uzbekistan"
indialist = india.replace(", ",",").split(',')
header = "India"
continentlist = indialist
getlist(continentlist,data)

header = "Asia1"
continent = "Japan, South Korea, Mongolia"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "Asia2"
continent = "Bhutan, Brunei Darussalam, Cambodia, China, Guam, Hong Kong, Indonesia, Laos, Malaysia, Myanmar, Philippines, Saipan, Singapore, Sri Lanka, Taiwan, Thailand, Vietnam"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "Pacific"
continent = "Australia, Easter Island, Fiji, French Polynesia, New Caledonia, New Zealand, Papua New Guinea, Tonga, Vanuatu, American Samoa, Samoa"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "Europe"
continent = "Albania, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia-Herzegovinia, Bulgaria, Canary Islands, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Gibraltar, Greece, Greenland, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Yugoslavia, Bosnia and Herzegovina"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "SouthAmerica1"
continent = "Belize, Colombia, Costa Rica, Ecuador, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Peru, Venezuela"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "SouthAmerica2"
continent = "Argentina, Bolivia, Brazil, Chile, Paraguay, Uruguay"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

# header = "NorthAmerica"
# continent = "United States, Canada, Mexico, Bermuda, Bahamas, Cuba, Trinidad and Tobago, Turks and Caicos Islands, Dominican Republic, Haiti, Jamaica, Cayman Islands, Puerto Rico, Antigua and Barbuda, Anguilla, Saint Kitts and Nevis, Montserrat, Guadeloupe, Dominica, Martinique, Saint Lucia, Saint Vincent and the Grenadines, Grenada, Barbados, Aruba, Bonaire, Curacao, British Virgin Islands, US Virgin Islands"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

header = "Continental"
continent = "United States"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

header = "NearAmerica"
continent = "Canada, Mexico, Cuba, Bermuda, Bahamas, Cuba, Trinidad and Tobago, Turks and Caicos Islands, Dominican Republic, Haiti, Jamaica, Cayman Islands, Puerto Rico, Antigua and Barbuda, Anguilla, Saint Kitts and Nevis, Montserrat, Guadeloupe, Dominica, Martinique, Saint Lucia, Saint Vincent and the Grenadines, Grenada, Barbados, Aruba, Bonaire, Curacao, British Virgin Islands, US Virgin Islands"
continentlist = continent.replace(", ",",").split(',')
getlist(continentlist,data)

# # What's left
# print data
