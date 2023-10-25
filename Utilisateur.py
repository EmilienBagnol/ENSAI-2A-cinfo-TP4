def créer_compte():
    identifiant = input("Entrez votre identifiant :")
    if not isinstance(identifiant, str):
        raise ValueError("L'identifiant doit être une chaîne de caractères")
