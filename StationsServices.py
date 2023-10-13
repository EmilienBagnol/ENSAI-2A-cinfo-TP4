from Carburants import Carburants
from Horaires import Horaires
from Services import Services


class StationService(Carburants, Horaires, Services):
    def __init__(self, id_station, nom_station, coordonnees_gps, carburants, horaires, services):
        self.id_station = id_station
        self.nom_station = nom_station
        self.coordonnees_gps = coordonnees_gps
        self.carburants = carburants
        self.horaires = horaires
        self.services = services

    def __str__(self):
        return f"Station {self.id_station}: {self.nom_station}, Coordonnées GPS: {self.coordonnees_gps}"
