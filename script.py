from countryinfo import CountryInfo

country_name = input("Enter Country Name: ")
country = CountryInfo(country_name)

print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in square kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currency:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
