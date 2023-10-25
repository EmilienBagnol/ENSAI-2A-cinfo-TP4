import requests
import zipfile
import xml.etree.ElementTree as ET


class Importation:
    def importer_xml():
        # Téléchargez le fichier ZIP à partir du serveur distant
        url = "https://donnees.roulez-eco.fr/opendata/instantane"
        response = requests.get(url)

        # Décompressez le fichier ZIP
        with zipfile.ZipFile(response.content, "r") as zipfile:
            zipfile.extractall("data")

        # Accédez au fichier XML dans le dossier décompressé
        filename = "PrixCarburants_instantane.xml"
        with open(filename, "r") as f:
            data = f.read()

        # Créez un arbre XML à partir du contenu du fichier XML
        tree = ET.fromstring(data)

        # Accédez aux éléments du fichier XML
        for child in tree:
            print(child.tag, child.attrib)
