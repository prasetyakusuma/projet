#!/usr/bin/env python
# coding: utf-8

# In[203]:


#4.1.1
def nb_points_carte(carte):
    if carte % 55 == 0:
        return 7
    if carte % 11 == 0:
        return 5
    if carte % 10 == 0:
        return 3
    if carte % 5 == 0:
        return 2
    return 1
nb_points_carte(20)


# In[204]:


#4.1.2
def nb_points_tas(list):
    res=0
    for i in list:
        a=nb_points_carte(i)
        res=res+a
    return res

nb_points_tas([44, 1, 20])


# In[205]:


#4.1.3
def texte_carte(carte):
    b=str(carte)
    a=str(nb_points_carte(carte))
    return b+" "+'('+a+')'
texte_carte(25)
    


# In[206]:


#4.1.4
def afficher_liste_cartes(liste):
    res=""
    for number in liste:
        c=texte_carte(number)
        res=res+c+'   '
    print(res)
afficher_liste_cartes([1, 20, 44]) 


# In[207]:


#4.1.5
def afficher_plateau(d):
    for i in range(1, len(d)+1):
        print("Lig",i,":", end='\t')
        a=afficher_liste_cartes(d[i])
    return a
        
afficher_plateau({1: [27], 2: [2, 5, 25], 3: [93], 4: [30,41]})


# In[208]:


#4.1.6
def afficher_scores(liste,nature):
   print("Scores"+" "+nature+":")
   for i , j  in liste.items():
       print("\t"+ i + " :" + " " + str(j) + " point(s)")
afficher_scores({'tata' : 3,'titi' : 12,'toto' : 0}, "manche")


# In[209]:


#4.2.1
import random
def generer_pioche():
    mylist=[]
    for i in range (1,105):
        a = random.randint(1,104)
        while a in mylist :
            a = random.randint(1,104)
        mylist.append(a)    
    return(mylist)
print(generer_pioche())


# In[ ]:


#4.2.2
def demander_nb_joueurs():
    a=int(input("Entrez le nombre de jouer "))
    while a<2 or a>10:
        a=int(input("Entrez le nombre de jouer"))
    return a
demander_nb_joueurs()


# In[ ]:


#4.2.3 
def saisie_noms(n):
    drapeau=True
    nom_liste_joueur = []
    for i in range(n):
        while drapeau :
            nom = input("\nEntrez le nom de joueur " + str(i+1) + " : ")
            if nom not in nom_liste_joueur:
                nom_liste_joueur.append(nom)
                break
            else:
                drapeau
            
    return nom_liste_joueur
saisie_noms(3)


# In[ ]:


#4.2.4
def init_scores(ljouer):
    ljouer_dict = { nom : 0 for nom in ljouer }
    return ljouer_dict
init_scores(['rara', 'riri', 'ruru', 'roro', 'rere'])


# In[ ]:


def distribute_cartes(card,players,nb_card=10):
    dictionary={}
    for nom in players:
        dictionary[nom]=[]
        for j in range(nb_card):
            # adding 10 values to the list
            dictionary[nom].append(card.pop(0))
    return dictionary
def sortDictionary(dict):
    keys = list(dict.keys())
    for value in keys:
        dict[value].sort() 
    return dict

card = [74, 72, 59, 82, 44, 77, 17, 11, 62, 97, 83, 69, 100, 22, 4, 51, 55, 50, 103, 52, 13, 25, 38, 37, 29, 104, 47, 23, 39, 80, 
49, 98, 8, 78, 26, 46, 86, 18, 93, 31, 27, 34, 85, 84, 76, 87, 65, 35, 81, 79, 101, 66, 20, 91, 73, 16, 102, 42, 40, 70, 90, 7, 6,
64, 14, 67, 43, 12, 58, 1, 63, 2, 75, 32, 48, 96, 3, 15, 99, 68, 53, 61, 56, 92, 36, 28, 19, 5, 24, 45, 57, 94, 21, 54, 88, 33, 10, 
71, 30, 95, 9, 41, 60, 89]
players = ['rara', 'riri', 'rere']

dict=distribute_cartes(card,players,nb_card=10)
sortDictionary(dict)


# In[ ]:


def distribuer_cartes(pioche, ljoueurs, nb_cartes=10):
    djoueurs = {}
    for joueur in ljoueurs:
        tmp = [] # to stock a player's cards
        for i in range(nb_cartes):
            tmp.append(pioche.pop())
        tmp.sort()
        djoueurs[joueur] = tmp
    print(djoueurs)
pioche = [74, 72, 59, 82, 44, 77, 17, 11, 62, 97, 83, 69, 100, 22, 4, 51, 55, 50, 103, 52, 13, 25, 38, 37, 29, 104, 47, 23, 39, 80, 
49, 98, 8, 78, 26, 46, 86, 18, 93, 31, 27, 34, 85, 84, 76, 87, 65, 35, 81, 79, 101, 66, 20, 91, 73, 16, 102, 42, 40, 70, 90, 7, 6,
64, 14, 67, 43, 12, 58, 1, 63, 2, 75, 32, 48, 96, 3, 15, 99, 68, 53, 61, 56, 92, 36, 28, 19, 5, 24, 45, 57, 94, 21, 54, 88, 33, 10, 
71, 30, 95, 9, 41, 60, 89]
ljoueurs = ['rara', 'riri', 'rere']
distribuer_cartes(pioche, ljoueurs, nb_cartes=10)


# In[ ]:


#4.2.6
def init_line(pioche):
    #data = {1: card[0], 2: card[1], 3: card[2], 4: card[3]}
    data={}
    for i in range(1,5):        
        data[i]=[pioche.pop(0)]
    # remove first 4 cards from list
    # return dictionary result
    return data
pioche=[20, 72, 59, 82, 44, 77, 17, 11, 62, 97, 83, 69, 100, 22, 4, 51, 55, 50, 103, 52, 13, 25, 38, 37, 29, 104, 47, 23, 39, 80, 49, 98, 8, 78, 26, 46, 86, 18, 93, 31, 27, 34, 85, 84, 76, 87, 65, 35, 81, 79, 101, 66, 20, 91, 73, 16, 102, 42, 40, 70, 90, 7, 6, 64, 14, 67, 43, 12, 58, 1, 63, 2, 75, 32, 48, 96, 3, 15, 99, 68, 53, 61, 56, 92, 36, 28, 19, 5, 24, 45, 57, 94, 21, 54, 88, 33, 10, 71, 30, 95, 9, 41, 60, 89]
data=init_line(pioche)
print(data)

afficher_plateau(data)


# In[ ]:


#4.3.1
def demander_choix(nom,jeu):
    print("Joueur ",nom, "votre jeu :")
    afficher_liste_cartes(jeu)
    n=int(input("Valeur de la carte a jouer :"))
    while n not in jeu:
        print("Cette carte n'est pas dans votre jeu !",end="")
        n=int(input("recommencez"))
    return n  


demander_choix('toto',[5, 17, 65, 97])
    


# In[ ]:


#4.3.2 trouver ligne

def trouver_ligne(card,dligne):
    numligne=None
    mini=9999
    for i in range(1,5):
        last = dligne[i][-1]
        dif= card-last
        if card > last and dif<mini  :
            mini=dif
            numligne=i
    return numligne

#test
card=43
dligne={1: [17], 2: [20], 3: [26,42], 4: [46]}
trouver_ligne(card,dligne)


# In[ ]:


#4.3.3 ramasser ligne

def ramasser_ligne(dlignes,num_ligne,carte):
    som=nb_points_tas(dlignes[num_ligne])
    dlignes[num_ligne]=[carte]
    return som
#test 
carte=43
dlignes={1: [17], 2: [20], 3: [26,42], 4: [42]}
print(ramasser_ligne(dlignes,4,carte),dlignes[4],dlignes)


# In[218]:


#4.3.4
def jouer_carte(carte,nom,dlignes):
    point = 0
    lig=trouver_ligne(carte,dlignes)
    if lig==None:
        print(nom,"vous ramassez une ligne.")
        inp=int(input("Quelle ligne choisissez-vous ?"))
        while inp<1 or inp>4:
            inp=int(input("Quelle ligne choisissez-vous ?"))
        point=ramasser_ligne(dlignes,inp,carte)
        print(nom,"vous ramassez",point,"point(s).")
    else:
        if len(dlignes[lig]) == 5:
            print(nom,"vous ramassez une ligne.")
            inp=int(input("Quelle ligne choisissez-vous ?"))
            while inp<1 or inp>4:
                inp=int(input("Quelle ligne choisissez-vous ?"))
            print(nom,"joue la carte",carte,"sur la ligne",inp)
            point=ramasser_ligne(dlignes,inp,carte)
            print(nom,"vous ramassez",point,"point(s).")
        else:
            print(nom,"joue la carte",carte,"sur la ligne",lig)
            dlignes[lig].append(carte)
        
    return point

    
jouer_carte(5,'titi',{1: [5], 2: [88,90,102], 3: [10], 4: [15,32,44,45,47]})
        
    


# In[ ]:


#4.3.5
def jouer_tour(djeux,dligne):
    score=init_scores(djeux.keys()) #key of dictionary
    liste_carte=[]
    for joueur,jeu in djeux.items(): #to change from dictionary to the list
        carte=demander_choix(joueur,jeu)
        liste_carte.append((joueur,carte))
        jeu.remove(carte)
    liste_carte.sort(key= lambda x:x[1])
    for joueur, carte in liste_carte:
        point = jouer_carte(carte,joueur,dlignes)
        score[joueur] = score[joueur]+point
    return score

dligne={1: [5], 2: [88,90,102], 3: [10], 4: [15,32,44,45,47]}
djeux={'rara': [11, 17, 44, 59, 62, 72, 74, 77, 82, 97],'riri': [4, 22, 50, 51, 52, 55, 69, 83, 100, 103],'rere': [13, 23, 25, 29, 37, 38, 39, 47, 80, 104]}
jouer_tour(djeux,dligne)


# In[ ]:


#4.4.1
def incrementer_scores(score_total, score_partiel):
    
    for key, value in score_total.items():
        
        score_total[key] = score_total[key] + score_partiel[key]

#Testing
dscores = {'tata': 0, 'titi': 0, 'toto': 0}

score_partiel = {'titi': 1, 'toto': 0, 'tata': 11}

incrementer_scores(dscores,score_partiel)
print(dscores)


# In[ ]:


#4.4.2
def joueur_manche(ljoueurs,nb_cartes=10):
    score_total=init_scores(ljoueurs)
    print(score_total)
    pioche=generer_pioche()
    distribuer_cartes(pioche, ljoueurs, nb_cartes=10)
    data=init_line(pioche)
    print(data)
    afficher_plateau(data)
    for i in range(1,nb_cartes):
        print("manche",i)
        x=jouer_tour(djeux,dligne)
        incrementer_scores(score_total,x)
        print("manche",i,"le score est",score_total)
    print("Terminé en",i,"maanche")
    return score_total
ljoueurs = ['rara', 'riri', 'rere']
joueur_manche(ljoueurs,nb_cartes=10)


# In[214]:


#4.4.3
def fin_partie(dict_score,score_final=66):
    for joueur,score in dict_score.items():
        if score>=score_final:
            return True
    return False
dict_score={'rara': 8, 'riri': 46, 'rere': 66}
fin_partie(dict_score,score_final=66)


# In[ ]:


#4.4.4
def afficher_gagnants(dictonary):
    smallest = 99999
    for point in dictonary.values():
        if smallest > point:
            smallest = point
    lst = []
    for joueur, score in dictonary.items():
        if score == smallest:
            lst.append(joueur)
    return lst


print(afficher_gagnants({'rara': 43, 'riri': 62, 'rere': 23}))
print(afficher_gagnants({'rara': 32, 'riri': 42, 'rere': 32}))


# In[215]:


#4.4.5
def jouer_partie(nb_cartes=10,score_final=66):
    n=demander_nb_joueurs()
    ljoueurs=saisie_noms(n)
    x=joueur_manche(ljoueurs,nb_cartes=10)
    fin_partie(x,score_final=66)
    print(afficher_gagnants(x))
    
jouer_partie(nb_cartes=10,score_final=66)


# In[ ]:


#4.5.1

import turtle

turtle.speed(100)

turtle.hideturtle()

turtle.setup(1000,1000)

turtle.title('Round Rectangle')

turtle.speed(0)  

turtle.up()

turtle.hideturtle()

def rectangle(x,y, width, height, radius):

    turtle.up()

    turtle.goto(x-width/2+radius,y-height/2)

    turtle.down()

    for _ in range(2):

        turtle.fd(width-2*radius)

        turtle.circle(radius,90)

        turtle.fd(height-2*radius)

        turtle.circle(radius, 90)

rectangle(100,50,25,75,5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




