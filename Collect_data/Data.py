
# utile pour plus tard

# class data():
#
#     def __init__(self):
#         self.immoweb_file = 'immoweb.csv'
#
#         self.immoweb_list = []
#
#     def load_db(self):
#         pass
#
#     def save_db(self):
#         pass


class estate():

    def __init__(self):
        """Constructor our class"""

        """ Données de base """
        self.state_of_the_building = "Not found"
        self.house_area = "Not found"  # living area
        self.price = "Not found"

        self.kitchen_type = "Not found"
        self.nbr_bedrooms = "Not found"
        self.surface_of_the_land = "Not found"
        self.terrace_area = "Not found"
        self.type_of_property = "Not found"
        self.subtype_of_property = "Not found"


        """ Données de Localisation """

        self.country = "Not found"
        self.region = "Not found"
        self.province = "Not found"
        self.district = "Not found"
        self.postal_code = "Not found"
        self.street_name = "Not found"
        self.house_number = "Not found"
        self.house_box = "Not found"
        self.property_name = "Not found"
        self.latitude = "Not found"
        self.longitude = "Not found"
        self.approximated = "Not found"  # c'est quoi ???
        self.region_code = "Not found"
        self.type = "Not found" # c'est quoi ???
        self.has_sea_view = "Not found"
        self.points_of_interest = "Not found"
        self.place_name = "Not found"
        self.net_habitable_surface = "Not found"
        self.room_count = "Not found"



        """ Description du bien """
        self.construction_year = "Not found"
        self.floor = "Not found"  # a quel étage se trouve le bien
        self.nbr_floor = "Not found"
        self.street_facade_width = "Not found"
        self.nbr_facades = "Not found"
        self.covered_parking_spaces = "Not found"
        self.outdoor_parking_spaces = "Not found"
        self.living_room_surface = "Not found"
        self.bedroom_1_surface = "Not found"
        self.bedroom_2_surface = "Not found"
        self.bedroom_3_surface = "Not found"
        self.bedroom_4_surface = "Not found"
        self.bedroom_5_surface = "Not found"
        self.nbr_bathrooms = "Not found"
        self.nbr_shower = "Not found"
        self.nbr_toilet = "Not found"
        self.cellar = "Not found"  # la cave
        self.office_surface = "Not found"
        self.office = "Not found"
        self.work_space_surface = "Not found"
        self.attic = "Not found"  # le grenier
        self.sewer_network = "Not found"  # connection aux égouts

        """ Energie """
        self.energy_consumption = "Not found"  # kwh/m²
        self.energy_class = "Not found"
        self.co2_emission = "Not found"
        self.heating_type = "Not found"
        self.solar_panels = "Not found"
        self.double_glazing = "Not found"

        """ Divers """

        self.property_name = "Not found"
        self.neighbourhood = "Not found"
        self.flood_zone = "Not found"
        self.cadastral_income = "Not found"
        self.agent = "Not found"  # personne qui gére la vente sur immoweb
        self.customer_name = "Not found"  # même que agent ?

        self.min_price = "Not found"
        self.max_price = "Not found"
        self.min_room = "Not found"
        self.max_room = "Not found"
        self.min_surface = "Not found"
        self.max_surface = "Not found"
        self.bedroom_range = "Not found"
        self.surface_range = "Not found"

        self.constructor = "Not found"
        self.groupId = "Not found"
        self.phase = "Not found"
        self.project_name = "Not found"
        self.delivery_date = "Not found"
        self.sold_percentage = "Not found"
        self.units_display_mode = "Not found"

        self.title = "Not found"

        """ Suivit et actualisation des données """

        self.available_date = "Not found"
        self.removed_from_immoweb = False
        self.immoweb_id = "Not found"

        """ a classer et trouver """

        self.type_of_sale = "Not found"
        self.furnished = str(None)
        self.open_fire = "Not found"
        self.terrace = "Not found"
        self.garden = "Not found"
        self.garden_area = "Not found"
        self.surface_of_the_plot_of_land = str(None)
        self.swimming_pool = "Not found"
