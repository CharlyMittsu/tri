# ______Déclaration
import random
stop = False
manip = 0
n = 0
taille = int(input("entrez la taille du tableau : "))
valeurMin = 0
valeurMax = int(input("entrez une valeur max pour les éléments du tableau : "))


# ______Création du tableau
tableau = []
for i in range(taille) :
    tableau.append(random.randint(valeurMin,valeurMax))
print ("taille du tableau : ",len(tableau))
print (tableau)

# ______Fonction
def swap(x,y):
    stock=tableau[x]
    tableau[x]=tableau[y]
    tableau[y]=stock

def petit(x,y):
    mini=tableau[x]
    b=x
    for i in range(x+1,y):
        if tableau[i]<mini:
            mini=tableau[i]
            b=i
    return b

# ______Tri du tableau

print(petit(0,taille))