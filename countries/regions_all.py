import csv
datafile = "countries.csv"
datacsv = csv.reader(open(datafile,"r"), delimiter=',')
data = {}
for d in datacsv:
    data[d[0]] = d[1]

DEBUG = True
# DEBUG = False

def getlist(clist, datain, header):
    got = []
    remove = []
    for country in datain.keys():
        if country in clist:
            got += [datain[country]]
            remove += [country]
            clist.remove(country)
            # datain.remove([country, code])
    got = sorted(got)
    if DEBUG:
        print "%s => %d / %d" %(header, len(clist), len(got))
        print clist
    print header+";"+",".join(got)

def dorun(header, continent):
    continentlist = continent.replace(", ",",").split(',')
    getlist(continentlist,data, header)

##### Delta Airlines
delta = {"Continental" : "United States, Canada",
          "Caribbean" : "Anguilla, Antigua and Barbuda, Aruba, Bahamas, Barbados, Bermuda, Bonaire and Saint Eustatius and Saba, British Virgin Islands, Cayman Islands, Cuba, Curacao, Dominica, Dominican Republic, Grenada, Guadeloupe, Guyana, Haiti, Jamaica, Martinique, Montserrat, Saint Kitts and Nevis, Saint Lucia, Sint Maarten, Saint Vincent and the Grenadines, Trinidad and Tobago, Turks and Caicos Islands, US Virgin Islands, Puerto Rico",
          "Mexico": "Mexico",
          "CentralAmerica": "Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panama",
          "NorthernSouthAm": "Bolivia, Colombia, Ecuador, Peru, Venezuela, French Guiana, Suriname",
          "SouthernSouthAm": "Argentina, Brazil, Chile, Paraguay, Uruguay",
          "Europe": "Albania, Algeria, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Faroe Islands, Finland, France, Georgia, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Montenegro, Monaco, Morocco, Netherlands, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Svalbard and Jan Mayen, Sweden, Switzerland, Tunisia, Turkey, Ukraine, United Kingdom, Vatican City",
          "Africa": "Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Congo-Brazzaville, Congo-Kinshasa, Ivory Coast, Djibouti, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Libyan Arab Jamahiriya, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mauritius, Mayotte, Mozambique, Namibia, Niger, Nigeria, Reunion, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, Swaziland, Tanzania, Togo, Uganda, Zambia, Zimbabwe, Sudan, South Africa",
          "MiddleEast": "Bahrain, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Saudi Arabia, Syria, United Arab Emirates, Yemen, Kazakhstan, Kyrgyzstan, Uzbekistan",
          "SouthAsia": "Afghanistan, Bangladesh, Bhutan, British Indian Ocean Territory, India, Nepal, Pakistan, Maldives, Sri Lanka",
          "NorthAsia": "Japan, North Korea, South Korea, China, Hong Kong, Taiwan, Micronesia, Philippines",
          "SouthEastAsia": "Brunei Darussalam, Cambodia, Indonesia, Laos, Macau, Malaysia, Mongolia, Myanmar, Singapore, Tajikistan, Thailand, Timor-Leste, Turkmenistan, Vietnam, Papua New Guinea",
          "SouthWestPacific": "American Samoa, Australia, Christmas Island, Cocos (Keeling) Islands, Cook Islands, Fiji, French Polynesia, Kiribati, Nauru, New Caledonia, New Zealand, Niue, Norfolk Island, Pitcairn, Samoa, Solomon Islands, Tokelau, Tonga, Tuvalu, Vanuatu, Wallis and Futuna Islands",
          "SouthAfrica": "South Africa",
          }
airline = delta


##### US Airways (
usair = {"Continental": "United States, Canada",
         "Caribbean": "Anguilla, Antigua and Barbuda, Aruba, Bahamas, Barbados, Bermuda, Bonaire and Saint Eustatius and Saba, British Virgin Islands, Cayman Islands, Cuba, Curacao, Dominica, Dominican Republic, Grenada, Guadeloupe, Guyana, Haiti, Jamaica, Martinique, Montserrat, Saint Kitts and Nevis, Saint Lucia, Sint Maarten, Saint Vincent and the Grenadines, Trinidad and Tobago, Turks and Caicos Islands, US Virgin Islands, Puerto Rico",
         "MexicoCentral": "Mexico, Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panama",
         "SouthAmerica": "Bolivia, Colombia, Ecuador, Peru, Venezuela, French Guiana, Suriname, Argentina, Brazil, Chile, Paraguay, Uruguay",
         "Europe": "Albania, Algeria, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Faroe Islands, Finland, France, Georgia, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Montenegro, Monaco, Morocco, Netherlands, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Svalbard and Jan Mayen, Sweden, Switzerland, Tunisia, Turkey, Ukraine, United Kingdom, Vatican City",
         "NorthAsia": "China, Hong Kong, Japan, Kazakhstan, Kyrgyzstan, Macau, Mongolia, South Korea, Taiwan, Tajikistan, Turkmenistan, Uzbekistan",
         "SouthCentralAsia": "Afghanistan, Bangladesh, Brunei Darussalam, Cambodia, India, Indonesia, Laos, Malaysia, Maldives, Myanmar, Nepal, Pakistan, Philippines, Singapore, Sri Lanka, Thailand, Vietnam",
         "SouthPacific": "American Samoa, Australia, Christmas Island, Cocos (Keeling) Islands, Cook Islands, Fiji, French Polynesia, Kiribati, Nauru, New Caledonia, New Zealand, Niue, Norfolk Island, Pitcairn, Samoa, Solomon Islands, Tokelau, Tonga, Tuvalu, Vanuatu, Wallis and Futuna Islands",
          "MiddleEast": "Bahrain, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Saudi Arabia, Syria, United Arab Emirates, Yemen, Kazakhstan, Kyrgyzstan, Uzbekistan",
         "Africa": "Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Congo-Brazzaville, Congo-Kinshasa, Ivory Coast, Djibouti, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Libyan Arab Jamahiriya, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mauritius, Mayotte, Mozambique, Namibia, Niger, Nigeria, Reunion, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, Swaziland, Tanzania, Togo, Uganda, Zambia, Zimbabwe, Sudan, South Africa",
          }
airline = usair

##### United
united = {"NorthAmerica": "United States, Canada",
         "Caribbean": "Antigua and Barbuda, Aruba, Bahamas, Barbados, Bermuda, British Virgin Islands, Dominican Republic, Grenada, Guadeloupe, Cayman Islands, Haiti, Jamaica, Martinique, Netherlands Antilles, Puerto Rico, Saint Lucia, Saint Kitts and Nevis, Trinidad and Tobago, Turks and Caicos Islands, US Virgin Islands",
          "CentralAmerica": "Belize, Costa Rica, El Salvador, Guatemala, Honduras, Mexico, Nicaragua, Panama",
          "NorthSouthAm": "Colombia, Ecuador, French Guiana, Guyana, Peru, Suriname, Venezuela",
          "SouthSouthAmerica": "Argentina, Bolivia, Brazil, Chile, Paraguay, Uruguay",
          "Europe": "Albania, Armenia, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Greenland, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom",
          "NorthAsia": "China, Guam, Mongolia, South Korea, Taiwan",
          "Japan": "Japan",
          "SouthAsia": "Bangladesh, Brunei Darussalam, Cambodia, Hong Kong, Indonesia, Laos, Macau, Myanmar, Philippines, Singapore, Thailand, Vietnam",
          "CentralAsia": "India, Kazakhstan, Kyrgyzstan, Maldives, Nepal, Pakistan, Sri Lanka, Turkmenistan, Uzbekistan",
          "OzKiwi": "New Zealand, Australia, Norfolk Island",
          "Oceania": "Cook Islands, Fiji, Micronesia, Marshall Islands, New Caledonia, Northern Mariana Islands, Palau, French Polynesia, Tonga, Vanuatu, Samoa",
          "MiddleEast": "Azerbaijan, Bahrain, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Syria, United Arab Emirates, Yemen",
          "NorthAfrica": "Algeria, Angola, Benin, Burkina Faso, Burundi, Cameroon, Central African Republic, Chad, Comoros, Congo, Ivory Coast, Djibouti, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Congo-Kinshasa, Kenya, Liberia, Mauritania, Mauritius, Morocco, Niger, Nigeria, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, Sudan, Tanzania, Togo, Tunisia, Uganda",
          "CentralSouthAfrica": "Botswana, Lesotho, Madagascar, Malawi, Mozambique, Namibia, Reunion, South Africa, Swaziland, Zambia, Zimbabwe"
          }
airline = united

##### Frontier
frontier = {"US": "United States",
          "Mexico": "Mexico",
          "CostaRica": "Costa Rica",
          }
airline = frontier

##### Alaska
alaska = {"US": "United States",
          "Mexico": "Mexico",
          }
airline = alaska

##### British Airways
british = {"Europe1": "Belgium, France, Germany, Ireland, Luxembourg, Netherlands, Switzerland, United Kingdom",
           "Europe2": "Austria, Croatia, Czech Republic, Denmark, Gibraltar, Hungary, Italy, Norway, Poland, Portugal, Serbia, Spain, Sweden",
           "Europe3": "Albania, Algeria, Bulgaria, Cyprus, Finland, Greece, Israel, Libyan Arab Jamahiriya, Morocco, Romania, Russia, Tunisia, Turkey, Ukraine",
           "MiddleEast": "Bahrain, Egypt, Kuwait, Oman, Qatar, Saudi Arabia, United Arab Emirates",
           "WestAfrica": "Ghana, Nigeria",
           "CentralAfrica": "Angola, Kenya, Mauritius, Namibia, South Africa, Tanzania, Uganda, Zambia, Zimbabwe",
           "SouthAsia": "India, Maldives",
           "FarEast": "China, Hong Kong, Japan, Singapore, Thailand",
           "Pacific": "Australia",
           }
airline = british

DEBUG=False
for header in airline.keys():
    dorun(header, airline[header])

########### American Airlines
# header = "Africa"
# continent = "Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Congo, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Ivory Coast, Kenya, Lesotho, Liberia, Libyan Arab Jamahiriya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Melilla, Morocco, Mozambique, Namibia, Niger, Nigeria, Republic of Congo, Reunion, Rwanda, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# india = "Afghanistan, Bahrain, Bangladesh, Egypt, India, Iran, Iraq, Israel, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon, Maldives, Nepal, Oman, Pakistan, Qatar, Saudi Arabia, Syria, Tajikistan, Turkmenistan, United Arab Emirates, Uzbekistan"
# indialist = india.replace(", ",",").split(',')
# header = "India"
# continentlist = indialist
# getlist(continentlist,data)

# header = "Asia1"
# continent = "Japan, South Korea, Mongolia"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "Asia2"
# continent = "Bhutan, Brunei Darussalam, Cambodia, China, Guam, Hong Kong, Indonesia, Laos, Malaysia, Myanmar, Philippines, Saipan, Singapore, Sri Lanka, Taiwan, Thailand, Vietnam"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "Pacific"
# continent = "Australia, Easter Island, Fiji, French Polynesia, New Caledonia, New Zealand, Papua New Guinea, Tonga, Vanuatu, American Samoa, Samoa"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "Europe"
# continent = "Albania, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia-Herzegovinia, Bulgaria, Canary Islands, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Gibraltar, Greece, Greenland, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Yugoslavia, Bosnia and Herzegovina"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "SouthAmerica1"
# continent = "Belize, Colombia, Costa Rica, Ecuador, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Peru, Venezuela"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "SouthAmerica2"
# continent = "Argentina, Bolivia, Brazil, Chile, Paraguay, Uruguay"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# # header = "NorthAmerica"
# # continent = "United States, Canada, Mexico, Bermuda, Bahamas, Cuba, Trinidad and Tobago, Turks and Caicos Islands, Dominican Republic, Haiti, Jamaica, Cayman Islands, Puerto Rico, Antigua and Barbuda, Anguilla, Saint Kitts and Nevis, Montserrat, Guadeloupe, Dominica, Martinique, Saint Lucia, Saint Vincent and the Grenadines, Grenada, Barbados, Aruba, Bonaire, Curacao, British Virgin Islands, US Virgin Islands"
# # continentlist = continent.replace(", ",",").split(',')
# # getlist(continentlist,data)

# header = "Continental"
# continent = "United States"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# header = "Caribbean"
# continent = "Cuba, Bermuda, Bahamas, Cuba, Trinidad and Tobago, Turks and Caicos Islands, Dominican Republic, Haiti, Jamaica, Cayman Islands, Puerto Rico, Antigua and Barbuda, Anguilla, Saint Kitts and Nevis, Montserrat, Guadeloupe, Dominica, Martinique, Saint Lucia, Saint Vincent and the Grenadines, Grenada, Barbados, Aruba, Bonaire, Curacao, British Virgin Islands, US Virgin Islands"
# continentlist = continent.replace(", ",",").split(',')
# getlist(continentlist,data)

# # What's left
# print data
