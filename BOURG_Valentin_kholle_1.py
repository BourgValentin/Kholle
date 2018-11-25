#!/usr/bin/python3.7

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Affiche le contenu de la liste", action="store_true")
parser.add_argument("-a", help="Ajoute les elements dans liste.csv", type=int, nargs='+')
parser.add_argument("-c", help="Supprime tous les elements dans liste.csv", action="store_true")
parser.add_argument("-s", help="Plusieurs options sont disponible : --max  --min  --moy  --sum", action="store_true")
parser.add_argument("--max", help="Affiche la valeur maximum dans la liste", action="store_true")
parser.add_argument("--min", help="Affiche la valeur minimum dans la liste", action="store_true")
parser.add_argument("--moy", help="Affiche la moyenne des éléments de la liste", action="store_true")
parser.add_argument("--sum", help="Affiche la somme des éléments de la liste", action="store_true")
parser.add_argument("-t", help="Trie les éléments de la liste dans l'ordre croissant, option --desc disponible ", action="store_true")
parser.add_argument("--desc", help="Trie les éléments de la liste dans l'ordre decroissant", action="store_true")

args = parser.parse_args()


if args.l:
    with open('liste.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            print(' '.join(row))

elif args.a:
    with open('liste.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([[a] for a in args.a])
 
elif args.c:
    delete_list = open("liste.csv", "w+")
    delete_list.close()

elif args.s:
    if args.max:
        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)
            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            max = max(liste)
            print('La valeur maximale dans la liste est : ', max)

    elif args.min:
        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)
            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            min = min(liste)
            print('La valeur minimale dans la liste est : ', min)

elif args.moy:
    with open('liste.csv', 'r') as csvfile:
        
        reader = csv.reader(csvfile)
        liste = []

        for row in reader:
            
            for x in row:
            
                x = int(x)
                liste.append(x)

        moy = sum(liste)/len(liste)        
        print('La moyenne de cette liste est : ', moy)

elif args.sum:
    with open('liste.csv', 'r') as csvfile:
        
        reader = csv.reader(csvfile)
        liste = []

        for row in reader:
            
            for x in row:
            
                x = int(x)
                liste.append(x)

        summ = sum(liste)      
        print('La somme de cette liste est : ', summ)
            
elif args.t:
    if args.desc:
        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)
            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)
            
            liste.sort(reverse=True)
            print('Le tri par ordre décroissant de cette liste est : ', liste)
    
    else:
        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)
            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)
            
            liste.sort()
            print('Le tri par ordre croissant de cette liste est : ', liste)