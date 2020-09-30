from bs4 import BeautifulSoup
import requests
import json
import Functions
import Data
import pprint





url = "https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=350000&minPrice=250000&orderBy=relevance"

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

result = soup.find_all('div')

data = json.loads(soup.find('iw-search')[':results'])

if Functions.debug:
    for d in data:
        print(d)

        url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

        print(url)

for d in data:

    maison = Data.estate()

    maison.immoweb_id = d.get("id", "Not found")

    if d.get("cluster", "Not found") != "Not found":
        maison.min_price = d["cluster"].get("minPrice", "Not found")
        maison.max_price = d["cluster"].get("maxPrice", "Not found")
        maison.min_room = d["cluster"].get("minRoom", "Not found")
        maison.max_room = d["cluster"].get("maxRoom", "Not found")
        maison.min_surface = d["cluster"].get("minSurface", "Not found")
        maison.max_surface = d["cluster"].get("maxSurface", "Not found")

        if d["cluster"].get("projectInfo", "Not found") != "Not found" \
                and d["cluster"].get("projectInfo", "Not found") is not None:
            maison.constructor = d["cluster"]["projectInfo"].get("constructor", "Not found")
            maison.groupId = d["cluster"]["projectInfo"].get("groupId", "Not found")
            maison.phase = d["cluster"]["projectInfo"].get("phase", "Not found")
            maison.project_name = d["cluster"]["projectInfo"].get("projectName", "Not found")
            maison.delivery_date = d["cluster"]["projectInfo"].get("deliveryDate", "Not found")
            maison.sold_percentage = d["cluster"]["projectInfo"].get("soldPercentage", "Not found")
            maison.units_display_mode = d["cluster"]["projectInfo"].get("unitsDisplayMode", "Not found")

    maison.bedroom_range = d.get("bedroomRange", "Not found")
    maison.surface_range = d.get("surfaceRange", "Not found")
    maison.customer_name = d.get("customerName", "Not found")

    if d.get("property", "Not found") != "Not found":
        maison.type_of_property = d["property"].get("type", "Not found")
        maison.subtype_of_property = d["property"].get("subtype", "Not found")
        maison.nbr_bedrooms = d["property"].get("bedroomCount", "Not found")
        maison.title = d["property"].get("title", "Not found")

        if d["property"].get("location", "Not found") != "Not found" \
                and d["property"].get("location", "Not found") is not None:
            maison.country = d["property"]["location"].get("country", "Not found")
            maison.region = d["property"]["location"].get("region", "Not found")
            maison.province = d["property"]["location"].get("province", "Not found")
            maison.district = d["property"]["location"].get("district", "Not found")
            maison.locality = d["property"]["location"].get("postalCode", "Not found")
            maison.postal_code = d["property"]["location"].get("postalCode", "Not found")
            maison.street_name = d["property"]["location"].get("street", "Not found")
            maison.house_number = d["property"]["location"].get("number", "Not found")
            maison.house_box = d["property"]["location"].get("box", "Not found")
            maison.property_name = d["property"]["location"].get("propertyName", "Not found")
            maison.floor = d["property"]["location"].get("floor", "Not found")
            maison.latitude = d["property"]["location"].get("latitude", "Not found")
            maison.longitude = d["property"]["location"].get("longitude", "Not found")
            maison.approximated = d["property"]["location"].get("approximated", "Not found")
            maison.region_code = d["property"]["location"].get("regionCode", "Not found")
            maison.type = d["property"]["location"].get("type", "Not found")
            maison.has_sea_view = d["property"]["location"].get("hasSeaView", "Not found")
            maison.points_of_interest = d["property"]["location"].get("pointsOfInterest", "Not found")
            maison.place_name = d["property"]["location"].get("placeName", "Not found")

        maison.net_habitable_surface = d["property"].get("netHabitableSurface", "Not found")
        maison.room_count = d["property"].get("roomCount", "Not found")
        maison.surface_of_the_land = d["property"].get("landSurface", "Not found")

    if d.get("transaction", "Not found") != "not found":
        maison.certificate = d["transaction"].get("certificate", "Not found")
        maison.type_of_sale = d["transaction"].get("type", "Not found")
        maison.rental = d["transaction"].get("rental", "Not found")

        if d["transaction"].get("sale", "Not found") != "Not found" \
                and d["transaction"].get("sale", "Not found") is not None:
            maison.life_annuity = d["transaction"]["sale"].get("lifeAnnuity", "Not found")
            maison.has_starting_price = d["transaction"]["sale"].get("hasStartingPrice", "Not found")
            maison.old_price = d["transaction"]["sale"].get("oldPrice", "Not found")
            maison.price = d["transaction"]["sale"].get("price", "Not found")
            maison.price_per_sqm = d["transaction"]["sale"].get("pricePerSqm", "Not found")
            maison.public_sale = d["transaction"]["sale"].get("publicSale", "Not found")
            maison.to_build = d["transaction"]["sale"].get("toBuild", "Not found")
            maison.vat_type = d["transaction"]["sale"].get("vatType", "Not found")

    maison.price_type = d.get("priceType", "Not found")
    maison.has_360_tour = d.get("has360Tour", "Not found")

    if Functions.debug:

        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

        remove_not_found = vars(maison).copy()
        for i in vars(maison):
            if vars(maison)[i] == "Not found" or vars(maison)[i] is None:
                del remove_not_found[i]

        pprint.pprint(remove_not_found)
        """for f in d:
             pprint.pprint(d[f])"""

