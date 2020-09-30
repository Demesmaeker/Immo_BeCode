import re
import requests
import lxml.html as lh
import pprint



# pour afficher ce qui se passe lors du dev

debug = True


def get_str_from_req_content(pattern, fct_content):
    """
    permet d'utiliser les regex pour sortir des données
    """
    if not pattern:
        return None

    print(str(pattern))

    prog = re.compile(pattern)
    fstr = prog.search(str(fct_content))

    return fstr

def recuperer_tr_tag(immmoweb_id):
    """
    permet de récupérer les informations contenue dans le tableau d'une page immoweb à partir de l'id du bien
    """

    url = "https://www.immoweb.be/en/classified/" + str(immmoweb_id)

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url)

    if page.status_code == 200:

        # Store the contents of the website under doc
        doc = lh.fromstring(page.content)

        # Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')

        el = []

        for tr in tr_elements:
            name = tr.text_content()
            el.append(name)

        dico = {}

        for item in el:

            items = list(filter(None, map(str.strip, item.split("\n"))))

            try:
                dico[items[0]] = items[1]

            except IndexError:

                continue

        return dico

    else:
        return "url not reachable"

pprint.pprint(recuperer_tr_tag(8899851))

def collect_data_1_tr_collect(immmoweb_id, maison):
    """
    Récupère les données sur immoweb à partir des tableaux de la page
    """
    dico = recuperer_tr_tag(immmoweb_id)

    if dico == "url not reachable":
        maison.removed_from_immoweb = True
        if debug:
            print("la page n'est pas accessible")
            print(dico)

    else:
        maison.available_date = dico.get("Available date", "Not found")
        maison.property_name = dico.get("Property name", "Not found")
        maison.neighbourhood = dico.get("Neighbourhood or locality", "Not found")
        maison.construction_year = dico.get("Construction year", "Not found")
        maison.floor = dico.get("Floor", "Not found")
        maison.nbr_floor = dico.get("Number of floors", "Not found")
        maison.state_of_the_building = dico.get("Building condition", "Not found")
        maison.street_facade_width = dico.get("Street facade width", "Not found")
        maison.nbr_facades = dico.get("Facades", "Not found")
        maison.covered_parking_spaces = dico.get("Covered parking spaces", "Not found")
        maison.outdoor_parking_spaces = dico.get("Outdoor parking spaces", "Not found")
        maison.house_area = dico.get("Living area", "Not found")
        maison.living_room_surface = dico.get("Living room surface", "Not found")
        maison.kitchen_type = dico.get("Kitchen type", "Not found")
        maison.nbr_bedrooms = dico.get("Bedrooms", "Not found")
        maison.bedroom_1_surface = dico.get("Bedroom 1 surface", "Not found")
        maison.bedroom_2_surface = dico.get("Bedroom 2 surface", "Not found")
        maison.bedroom_3_surface = dico.get("Bedroom 3 surface", "Not found")
        maison.bedroom_4_surface = dico.get("Bedroom 4 surface", "Not found")
        maison.bedroom_5_surface = dico.get("Bedroom 5 surface", "Not found")
        maison.nbr_bathrooms = dico.get("Bathrooms", "Not found")
        maison.nbr_shower = dico.get("Shower rooms", "Not found")
        maison.nbr_toilet = dico.get("Toilets", "Not found")
        maison.office_surface = dico.get("Office surface", "Not found")
        maison.office = dico.get("Office", "Not found")
        maison.work_space_surface = dico.get("Work space surface", "Not found")
        maison.cellar = dico.get("Basement", "Not found")
        maison.attic = dico.get("Attic", "Not found")
        maison.surface_of_the_land = dico.get("Surface of the plot", "Not found")
        maison.sewer_network = dico.get("Connection to sewer network", "Not found")
        maison.terrace_area = dico.get("Terrace surface", "Not found")
        maison.energy_consumption = dico.get("Primary energy consumption", "Not found")
        maison.energy_class = dico.get("Energy class", "Not found")
        maison.co2_emission = dico.get("CO² emission", "Not found")
        maison.heating_type = dico.get("Heating type", "Not found")
        maison.solar_panels = dico.get("Thermic solar panels", "Not found")
        maison.double_glazing = dico.get("Double glazing", "Not found")
        maison.flood_zone = dico.get("Flood zone type", "Not found")
        maison.price = dico.get("Price", "Not found")
        maison.cadastral_income = dico.get("Cadastral income", "Not found")
        maison.agent = dico.get("Website", "Not found")

    if debug:
        print("*******************************************************")
        print("Ce qui a été trouvé sur immoweb : ")
        print("")
        print(dico)
        print("")
        print("*******************************************************")
        print("Résultat du scrapping : ")
        print("")
        remove_not_found = vars(maison).copy()
        for i in vars(maison):
            if vars(maison)[i] == "Not found":
                del remove_not_found[i]

        pprint.pprint(remove_not_found)

