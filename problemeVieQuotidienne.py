ProdBase = float(input("Quel est le prix (€) du produit ? ")) #Le prix du produit.
Pourcent = float(input("Quel est le pourcentage (%) de réduction ? ")) #Le pourcentage de la solde.
Argent = float(input("Quel est votre somme (€) sur vous ?")) #L'argent que vous avez actuellement.

ProdPromo = ProdBase*(100-Pourcent)/100 #Ici, nous trouvons le prix en solde de l'article.
RendBase = Argent-ProdBase #Là, c'est l'argent qui nous aurais été rendu du base.
RendSolde = Argent-ProdPromo #Maintenant, c'est l'argent rendu avec le pris soldé.
Economie = ProdBase-ProdPromo  #Ça indique la somme économisé grâce à la solde.
ManqueSolde = ProdPromo-Argent #Si jamais vous n'aviez pas assez d'argent malgré les soldes.
ManqueBase = ProdBase-Argent #L'argent qui vous manquais avec le prix de base.

print(f"\nLe prix de votre produit avec cette solde est de {ProdPromo}€")
print(f"Grâce à cette solde, le produit coûte {Economie}€ de moins.\n")

if Argent > ProdPromo and Argent > ProdBase :
    print(f"Avec cette solde, on vous rendra {RendSolde}€ au lieu de {RendBase}€")
    #Vous avez assez d'argent dans les deux cas.

elif Argent > ProdPromo and Argent == ProdBase :
    print(f"Avec cette solde, on vous rendra {RendSolde}€, vous aviez pile ce qu'il fallait pour le prix à plein tarif.")
    #Vous aviez l'argent du prix de base.

elif Argent == ProdPromo:
    print(f"Vous avez pile la bonne somme pour l'acheter en solde.\nSinon, il vous manquais {Economie}€")
    #La somme que vous aviez était égale à la somme de la solde, l'argent qui manquais pour le tarif complet sera donc l'argent économisé.

elif Argent > ProdPromo and Argent < ProdBase :
    print(f"Avec cette solde, on vous rendra {RendSolde}€, heureusement qu'il y'a la solde car vous n'aurez pas eu assez sinon. \nSinon, vous auriez eu besoin {ManqueBase}€ en plus pour l'avoir à son prix de base.")
    #Vous aviez un peu plus que l'argent requis pour acheter le produit soldé.
    
elif Argent < ProdPromo and Argent < ProdBase :
    print(f"Vous n'avez pas assez d'argent sur vous pour acheter ce produit, même soldé. \nIl vous manque {ManqueSolde}€ pour l'avoir en solde et {ManqueBase}€ pour l'avoir plein pot.")
    #Là, vous n'avez aucune des deux sommes, c'est donc ce message qui s'affichera disant ce qu'il manque pour les deux.
