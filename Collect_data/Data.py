
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

import pickle


class PickleData:

    def __init__(self):
        self.data = pickle.load(open("immoweb_1", "rb"))

    def get_data(self):
        return self.data


# pickle_data = PickleData().get_data()

class estate():
    


    def __init__(self):
        """valeur par defaut = la valeur n'a pas été trouvée"""

        default = "Not found"

        """ Données de base """
        self.state_of_the_building = default
        self.house_area = default  # living area
        self.price = default

        self.kitchen_type = default
        self.nbr_bedrooms = default
        self.surface_of_the_land = default
        self.terrace_area = default
        self.type_of_property = default
        self.subtype_of_property = default


        """ Données de Localisation """

        self.locality =  default
        self.country = default
        self.region = default
        self.province = default
        self.district = default
        self.postal_code = default
        self.street_name = default
        self.house_number = default
        self.house_box = default
        self.property_name = default
        self.latitude = default
        self.longitude = default
        self.approximated = default  # c'est quoi ???
        self.region_code = default
        self.type = default # c'est quoi ???
        self.has_sea_view = default
        self.points_of_interest = default
        self.place_name = default
        self.net_habitable_surface = default
        self.room_count = default



        """ Description du bien """
        self.construction_year = default
        self.floor = default  # a quel étage se trouve le bien
        self.nbr_floor = default
        self.street_facade_width = default
        self.nbr_facades = default
        self.covered_parking_spaces = default
        self.outdoor_parking_spaces = default
        self.living_room_surface = default
        self.bedroom_1_surface = default
        self.bedroom_2_surface = default
        self.bedroom_3_surface = default
        self.bedroom_4_surface = default
        self.bedroom_5_surface = default
        self.nbr_bathrooms = default
        self.nbr_shower = default
        self.nbr_toilet = default
        self.cellar = default  # la cave
        self.cellar_surface = default
        self.office_surface = default
        self.office = default
        self.work_space_surface = default
        self.attic = default  # le grenier
        self.sewer_network = default  # connection aux égouts
        self.annex_count = default
        self.has_heat_pump = default
        self.has_photovoltaic_panels = default
        self.has_thermic_panels = default

        self.fire_place_count = default
        self.fire_place_exists = default
        self.garden_orientation = default
        self.garden_area = default

        self.habitable_unit_count = default
        self.has_air_conditioning = default
        self.has_armored_door = default
        self.has_balcony = default
        self.has_barbecue = default
        self.has_desabled_access = default
        self.has_door_phone = default
        self.has_dressing_room = default
        self.has_fitness_room = default
        self.has_hammam = default
        self.has_garden = default
        self.has_internet = default
        self.has_jacuzzi = default
        self.has_laundry_room = default
        self.has_lift = default
        self.has_sauna = default
        self.has_alarm = default
        self.has_swimming_pool = default
        self.has_tv_cable = default
        self.has_tennis_court = default
        self.has_visiophone = default
        self.terrace = default

        self.is_first_occupation = default
        self.is_holiday_property = default

        self.kitchen_has_dishwasher = default
        self.kitchen_has_freezer = default
        self.kitchen_has_fridge = default
        self.kitchen_has_micro_wave_oven = default
        self.kitchen_has_oven = default
        self.kitchen_has_steam_oven = default
        self.kitchen_has_washing_machine = default
        self.kitchen_surface = default

        self.land_has_plot_to_rear = default
        self.land_is_facing_street = default
        self.land_is_flat = default
        self.land_is_wooded = default
        self.land_width = default
        self.land_latest_use_designation = default
        self.land_rear_land = default

        self.terrace_orientation = default

        """ Energie """
        self.energy_consumption = default  # kwh/m²
        self.energy_class = default
        self.co2_emission = default
        self.heating_type = default
        self.solar_panels = default
        self.double_glazing = default

        """ Divers """

        self.property_name = default
        self.neighbourhood = default
        self.flood_zone = default
        self.cadastral_income = default
        self.agent = default  # personne qui gére la vente sur immoweb
        self.customer_name = default  # même que agent ?
        self.customer_type = default

        self.min_price = default
        self.max_price = default
        self.min_room = default
        self.max_room = default
        self.min_surface = default
        self.max_surface = default
        self.bedroom_range = default
        self.surface_range = default

        self.constructor = default
        self.groupId = default
        self.phase = default
        self.project_name = default
        self.delivery_date = default
        self.sold_percentage = default
        self.units_display_mode = default

        self.title = default # c'est quoi ?

        self.certificate = default
        self.type_of_sale = default
        self.rental = default
        self.life_annuity = default
        self.has_starting_price = default
        self.old_price = default
        self.price_per_sqm = default
        self.public_sale = default
        self.to_build = default
        self.vat_type = default

        self.price_type = default
        self.has_360_tour = default

        self.transaction_type = default
        self.is_furnished = default

        self.attic_is_isolated = default
        self.attic_surface = default

        """ Suivit et actualisation des données """

        self.available_date = default
        self.removed_from_immoweb = False
        self.immoweb_id = default
        self.immoweb_creation_date = default
        self.immoweb_expiration_date = default
        self.immoweb_last_modification_date = default
        self.update_date = default




