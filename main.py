# Thomas Parent
# 12 septembre 2023
# TP1

def nombre_mots(chaine):
   # Divise la chaîne en mots en utilisant l'espace comme séparateur
   mots = chaine.split()
   # Compte le nombre de mots
   nombre_de_mots = len(mots)
   return nombre_de_mots

# dans la variable phrase tu ecrit la
phrase = input("Tapez votre phrase : ")
résultat = nombre_mots(phrase)
print("Il y a",résultat,"mot dans la phrase")
