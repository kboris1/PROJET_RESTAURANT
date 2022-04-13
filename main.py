"""
"""
import random

##########################################################################################
                             #DEBUT FONCTIONS
    
##########################################################################################

###################PERMET DE LIRE LA LISTE DES PLATS D'UN MENU#######################################

def lire_menu(type_menu):
    tab1, tab2, taille_doc = decomposer_ligne(type_menu)
    for i in range(0,taille_doc):
        print(i+1,"-",tab1[i],"                   ",tab2[i],"Fcfa")
    return taille_doc
    

###### DECOMPOSER LES CHAINES DES PLATS DU MENU SI TYPE = 0 OU LA CHAINE CONTENANT LE USERNAME ET MOT DE PASSE SI TYPE =1###
def decomposer_ligne(type_menu,type = 0):
    ###### DECOMPOSER LES CHAINES DES PLATS DU MENU SI TYPE = 0
    if type == 0:
        #Ouvrir les fichiers de menus et leurs prix
        fichier_menu = open(type_menu,"r")
        fichier_prix_menu = open(f"prix_{type_menu}","r")
        #Transformer les fichier en tableau
        liste_menu = fichier_menu.readlines()
        liste_prix_menu = fichier_prix_menu.readlines()
        #Prendre la taille de l'un des tableau car ils ont la même taille
        taille_liste = len(liste_menu)
        tableau_menu_final = []
        tableau_prix_menu_final = []
        #On décompose chaque ligne pour extraire les donnée souhaité
        for i in range(0,taille_liste):
            #On sépare le nom du plat à receuillir de sont numero la même chose pour le prix
            l1,l2 = liste_menu[i].split(".")
            m1,m2 = liste_prix_menu[i].split(".")
            #On supprime l'espace dans les chianes recoltées
            l2 = l2.strip()
            m2 = m2.strip()
            #On met le nom du plat dans le tableau
            tableau_menu_final.append(l2)
            #On met le prix du plat dans le tableau
            tableau_prix_menu_final.append(m2)
        return tableau_menu_final, tableau_prix_menu_final, taille_liste
    ##################DECOMPOSER LES IDENTIFIANTS SI TYPE = 1
    if type == 1:
        #Ouvrir le fichier contenant les identifiants des utilisateurs
        fichier_id = open(type_menu,"r")
        #Transformer le fichier en tableaux
        liste_id = fichier_id.readlines()
        #Prendre la taille du tableau
        taille_liste = len(liste_id)
        tableau_username = []
        tableau_mot_de_passe = []
        #On décompose chaque ligne pour extraire les donnée souhaité
        for i in range(0,taille_liste):
            #On sépare le nom d'utilisateur de son mot de passe
            username,mot_de_passe = liste_id[i].split(":")
            #On supprime l'espace dans les chianes recoltées
            username = username.strip()
            username = username.strip()
            mot_de_passe = mot_de_passe.strip()
            #On met le username du plat dans le tableau
            tableau_username.append(username)
            #On met le mot de passe dans le tableau
            tableau_mot_de_passe.append(mot_de_passe)
        return tableau_username, tableau_mot_de_passe, taille_liste
        
        

############PERMET DE PASSER LA COMMANDE GRACE AU NUMERO DU PLAT,DE LA QUANTITE ET DU NOM DU MENU#######################3
def commande(num,nombre, type_menu):
    tab1, tab2, taille_doc = decomposer_ligne(type_menu)
    ma_commande = [tab1[num-1],nombre,int(tab2[num-1])]
    facture(ma_commande)

############### APRES AVOIR COMMANDE UN PLAT ON PEUT OBTENIR UNE FACTURE INSTANTEE ##################
def facture(ma_commande):
    global tableau_facture
    global total_facture
    total_facture = 0
    tableau_facture.append(ma_commande)
    taille_facture = len(tableau_facture)
    for commande in tableau_facture:
        total_facture = total_facture + commande[1]*commande[2]
    
    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|Article                                         |  Nombre |         prix unitaire |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    i = 0      
    for commande in tableau_facture:
        print(i+1,"-",commande[0],"                 ",commande[1],"         ",commande[2] )
        i +=1
    print()
    print("""+++++++++++++++++++++++
|   TOTAL : """+str(total_facture)+"""   |
+++++++++++++++++++++++""")
        
####PERMET DE SUPRIMER UN PLAT CHOISI DE SA FACTURE EN CAS D'ERREUR DE CHANGEMENT D'AVIS#######
def suppression_choix_commande(indice):
    tableau_facture.pop(indice)
    
    facture_finale()

##########3######### PERMET DE CHOISIR LE MENU ###########################
def choix_menu_principal():
    valeurs = [1,2,3,4]
    
    print("""1-Entrées
2-Menu principal
3-Desserts
4-Boissons""")
    saisie = saisir_un_nombre(":",4)
        
    return saisie

########### PERMET DE SAISIR UN NOMBRE ET VERIFIER EN MEME TEMPS LA SAISIE
def saisir_un_nombre(message,nombre_elements = 0,tableau_de_valeurs = []):
    while True:
        try:
            nombre = int(input(message))
        except ValueError:
            print("Vous avez saisie une valeur incorrecte.Veuillez recommencer")
        else:
            if len(tableau_de_valeurs) != 0 and nombre_elements == 0:
                if nombre not in tableau_de_valeurs:
                    print("Vous avez saisie une valeur incorrecte.Veuillez recommencer")
                else:
                    break
            elif len(tableau_de_valeurs) == 0 and nombre_elements != 0:
                if nombre <= 0 and nombre >nombre_elements:
                    print("Vous avez saisie une valeur incorrecte.Veuillez recommencer")
                else:
                    break
            else:
                break
 
    return nombre

################## PERMET DE SAISIR UNE CHAINE ET VERIFIER QU'ELLE EST NON VIDE #######################
def saisir_une_chaine_non_vide(message):

    while True:
        chaine = input(message)
        if len(chaine) !=0:
            break
        else:
            print("Saisie non valide")
            
    return chaine
############## PERMET D'ECRIRE DANS UN FICHIER LES IDENTIFIANT SAISIS PAS L'UTILISATEUR ###############
def imprimer_id(username,mot_de_passe):
    fichier = open("identifiants.txt","a")
    fichier.write(f"{username}:{mot_de_passe} \n")

############## PERMET DE FAIRE L'INSCRIPTION D'UN NOUVEL UTILISATEUR EN VERIFANT QUE LE COMPTE N'EXISTE PAS DEJA
def inscription():
    while True:
        username = saisir_une_chaine_non_vide("Choisissez un username: ")
        mot_de_passe = saisir_une_chaine_non_vide("Choisissez un mot de passe: ")
        valider = verifier_id(username,mot_de_passe)
        connecter = 0
        
    # Si le nom d'utilisateur n'existe pas déjà
        if valider == 0:
            imprimer_id(username,mot_de_passe)
            print("Félicitation, votre compte a été créé")
            connecter =1
            break
        else :
            print("Ce compte existe déja")
            valeurs = [1,2]
            choix = saisir_un_nombre("Tapez 1 pour se connecter, Tapez 2 pour ressayer: ",0,valeurs)
            if choix == 1:
                connexion()
                break

    return connecter


############## PERMET DE CONNECTER UN UTILISATEUR EN VERIFANT QUE LE COMPTE EST EXISTANT.#####################
####################### SI CE N'EST PAS LE CAS IL POUR POURRA S'INSCRIRE 
def connexion():
    aff_mdp = 0
    while True:
        #Si le username est correcte et le mot de passe faut, plus besoin de redemandé le username 
        if aff_mdp == 0:
            username = saisir_une_chaine_non_vide("Saisissez un username: ")
        mot_de_passe = saisir_une_chaine_non_vide("Saisissez votre mot de passe: ")
        valider = verifier_id(username,mot_de_passe)
        # Par défaut  on n'a pas la possibilé de se connecter à l'appli, il faut que les infos saisies sont validé avant que connceter prenne la valeur 1
        connecter = 0
    #Si le nom d'utilisateur existe
        if valider == 2 :
            print("Mot de passe incorrect !")
            valeurs = [1,2]
            choix = saisir_un_nombre("Tapez 1 pour ressaisir le mot de passe, 2 pour changer de nom d'utilisateur: ",0,valeurs)
            if choix ==1:
                aff_mdp = 1
            else:
                aff_mdp = 0
    #Si le nom d'utilisateur et le mot de passe sont corrrectes 
        if valider == 3 :
            print(f"Vous êtes connectés {username}")
            connecter = 1
            break
        if valider == 0:
            print("Cet utilisateur n'existe pas")
            valeurs = [1,2]
            choix = saisir_un_nombre("Tapez 1 pour réessayer, 2 pour s'incrire :",0,valeurs)
            if choix == 1:
                aff_mdp = 0
            else:
                inscription()
                connecter =1
                break
        
    return connecter


##### PERMET DE VERIFIER QUE LES IDENTIFAINT DE INSCRIPTION/CONNEXION EXISTE DANS LE FICHIER D'IDENTIFIANT AVANT DE SE CONNECTER OU DE S'INSCRIRE ######   
def verifier_id(username,mot_de_passe):
    fichier = open("identifiants.txt","r")
    tab_username,tab_mdp,taille_tab = decomposer_ligne("identifiants.txt",1)
    #Si le nom d'utilisateur n'existe pas
    valider =0
    for i in range(0,taille_tab):
        # 1 si le nom d'utilisateur existe déjà
        if tab_username[i] == username :
            valider = 1
        # 2 si le mot de passe est incorrect
            if tab_mdp[i] != mot_de_passe:
                valider = 2
        # 3 si le nom d'utilisateur et le mot de passe existent déjà
        if tab_username[i] == username and tab_mdp[i] == mot_de_passe:
            valider = 3
    fichier.close()
    return valider 

###################### PERMET DE CHOISIR UN PLAT #############################
def choix_du_plat (type_menu):
    while True:
        #On affiche la liste du menu choisi en prenant en même temps la taille de la liste du menu dont le fichier peut être mofifié à tout moment
        taille_liste = lire_menu(type_menu)
        #On invite l'utilisateur à choisir un des plat. La saisie est déjà testée par la fonction saisir_un_nombre()
        choix = saisir_un_nombre("Choisissez un plat: ")
        #On invite l'utilisateur à saisir la quantitité qu'il veut pour le plat choisi
        nombre_de_plats =saisir_un_nombre("Nombre de plats: ",taille_liste)
        #Une fois les informations saisies, on passe la commande grâce à la fonction commande()
        print("____________________________________________________________________________________")
        print()
        commande(choix,nombre_de_plats,type_menu)
        print("____________________________________________________________________________________")
        while True:
            continuer = saisir_un_nombre("""1-Pour ajouter un autre plat de ce menu
2-Pour aller vers d'autre menu
3-Pour payer la facture
4-Pour supprimer un choix
:""",4)
            if continuer == 4:
                indice = saisir_un_nombre("Saissir l'indice de plat à supprimer :",taille_liste)
                suppression_choix_commande(indice-1)
            if continuer != 4 :
                break
            
        if continuer !=1:
                break
    return continuer

####################### PERMET D'ETABLIR LA FACTURE FINALE ######################
def facture_finale():
    global tableau_facture
    global total_facture
    total_facture = 0
    taille_facture = len(tableau_facture)
    for commande in tableau_facture:
        total_facture = total_facture + commande[1]*commande[2]

    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|Article                                         |  Nombre |         prix unitaire |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    i=0
    for commande in tableau_facture:
        print(i+1,"-",commande[0],"                 ",commande[1],"         ",commande[2] )
        i +=1
    print()
    print("""+++++++++++++++++++++++
|   TOTAL : """+str(total_facture)+"""   |
+++++++++++++++++++++++""")

############################## PERMET DE SIMULER UN PARYEMENT PAR CARTE BANCAIRE ########################       
def paiement():
    print("Numero de la carte")
    print("XXXX_XXXX_XXXX_XXXX")
    numero_carte = saisir_un_nombre(":")
    print("Date d'expiration")
    print("MM / AA")
    date_expiration = input()
    print("TRANSACTION FAITE AVEC SUCCES!!!")
    
    code_de_caisse = random.randint(1000, 9999999)
    print("NUMERO DE CAISSE :",code_de_caisse)
    
    
        
def wellcome(bienvenu_message):
    bv_m=""
    es=" "
    l= len(bienvenu_message)
    
    for i in bienvenu_message:
        espace=es*l
        bv_m= bv_m + i 
        l-=1
    print("""+==========================================================+
|              {}{}             |
+==========================================================+
                """.format(bv_m,espace))


    
##########################################################################################
                             #FIN FONCTIONS
    
##########################################################################################


while True:
    choix = saisir_un_nombre("""1-Se connceter
2-S'inscrire
3-Quitter
""",3)
    if choix == 1:
       connexion()
    elif choix == 2 :
        inscription()
    else:
       break
    
    tableau_facture =[]
    total_facture = 0
    wellcome("BIENVENU CHEZ K'BORIS RESTO!!!")
    
    while True:
        #Choix du menu
        saisie = choix_menu_principal()
        #On veut selectionner un plat parmi les entrées
        if saisie == 1:
            continuer = choix_du_plat("entrees.txt")
        if saisie == 2:
            continuer = choix_du_plat("menu_principal.txt")
        if saisie == 3:
            continuer = choix_du_plat("desserts.txt")
        if saisie == 4:
            continuer = choix_du_plat("boissons.txt")
        if continuer == 3:
            break
    print("FACRTURE")
    facture_finale()
    valeurs = [0,1]
    payer = saisir_un_nombre("Taper 1 pour payer et 0 pour annuler la commande: ")
    if payer == 1:
        paiement()
        print()
    quitter = saisir_un_nombre("""Tapez 1 pour refaire une autre commande
Tapez 0 pour quitter :""",0,valeurs)
    if quitter == 0:
        break
    
print("A BINETOT!!!")




