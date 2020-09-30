from bs4 import BeautifulSoup
import requests
import json

import Data


maison = Data.estate()


url = "https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=350000&minPrice=250000&orderBy=relevance"

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

print(" 1 ****************************************")

print(soup.find("search-results__header"))

print(" 2 ****************************************")


result = soup.find_all('div')
print(result)

print(" 4 ****************************************")


print(soup.find('iw-search')[':results'])

data = json.loads(soup.find('iw-search')[':results'])

for d in data:
    print(d)

    url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

    print(url)

print(" 3 ****************************************")


for d in data:


    maison.immoweb_id = d["id"]
    maison.min_price = d["cluster"]["minPrice"]
    maison.max_price = d["cluster"]["maxPrice"]
    maison.min_room = d["cluster"]["minRoom"]
    maison.max_room = d["cluster"]["maxRoom"]
    maison.min_surface = d["cluster"]["minSurface"]
    maison.max_surface = d["cluster"]["maxSurface"]

    try:
        maison.constructor = d["cluster"]["projectInfo"]["constructor"]
        maison.groupId = d["cluster"]["projectInfo"]["groupId"]
        maison.phase = d["cluster"]["projectInfo"]["phase"]
        maison.project_name = d["cluster"]["projectInfo"]["projectName"]
        maison.delivery_date = d["cluster"]["projectInfo"]["deliveryDate"]
        maison.sold_percentage = d["cluster"]["projectInfo"]["soldPercentage"]
        maison.units_display_mode = d["cluster"]["projectInfo"]["unitsDisplayMode"]
        maison.bedroom_range = d["bedroomRange"]
        maison.surface_range = d["surfaceRange"]
        maison.customer_name = d["customerName"]

    except :
        pass

    maison.type_of_property = d["property"]["type"]
    maison.subtype_of_property = d["property"]["subtype"]
    maison.nbr_bedrooms = d["property"]["bedroomCount"]
    maison.title = d["property"]["title"]

    maison.country = d["property"]["location"]["country"]
    maison.region = d["property"]["location"]["region"]
    maison.province = d["property"]["location"]["province"]
    maison.district = d["property"]["location"]["district"]
    maison.locality = d["property"]["location"]["postalCode"]
    maison.postal_code = d["property"]["location"]["postalCode"]
    maison.street_name = d["property"]["location"]["y"]
    maison.house_number = d["property"]["location"]["y"]
    maison.house_box = d["property"]["location"]["y"]
    maison.property_name = d["property"]["location"]["y"]
    maison.floor = d["property"]["location"]["y"]
    maison.latitude = d["property"]["location"]["y"]
    maison.longitude = d["property"]["location"]["y"]
    maison.approximated = d["property"]["location"]["y"]
    maison.region_code = d["property"]["location"]["y"]
    maison.type = d["property"]["location"]["y"]
    maison.has_sea_view = d["property"]["location"]["y"]
    maison.points_of_interest = d["property"]["location"]["y"]
    maison.place_name = d["property"]["location"]["y"]
    maison.net_habitable_surface = d["property"]["location"]["y"]
    maison.room_count = d["property"]["location"]["y"]
    maison.surface_of_the_land = d["property"]["location"]["y"]

    d["property"]["location"][y]


    print("++++++++++++++++++++++++")

    print("immoweb_id")
    print(d["id"])
    print(d.get("cluster").get("minPrice"))

    print("++++++++++++++++++++++++")


    for f in d:
        print(f)
        print(d[f])

        if f == "cluster":
            for i in d[f]:
                print(i)
                print(d[f][i])


                if i == "projectInfo" and d[f][i] != None:
                    for y in d[f][i]:
                        print(y)
                        print(d["cluster"]["projectInfo"][y])

        if f == "property":
            for i in d[f]:
                print(i)
                print(d[f][i])

                if i == "location" and d[f][i] != None:
                    for y in d[f][i]:
                        print(y)
                        print(d["property"]["location"][y])


    print("vl price")
    for t in d["price"]:
        print(t)
        print(d["price"][t])
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")