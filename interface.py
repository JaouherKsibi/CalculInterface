
#Fonction calcul sphere
def sphere (): 
    #Récupération des variables
    A=float(rayon.get()) 
    #Calcul 
    surface=4*pi*A**2
    volume=4*pi*(A**3) / 3
    print("\n   Surface de la sphere de rayon {:.1f} = {:.3f}".format(A,surface))
    print("\n   Volume de la sphere de rayon {:.1f} = {:.3f}".format(A,volume))
    chaine.configure(text = surface)
    chaine1.configure(text= volume)
    #***************************************

    #############################################"""
    #################################################
    #Fonction calcul cercle
def cercle (): 
    #Récupération des variables
    A=float(rayonCercle.get()) 
    #Calcul 
    perimetre=2*pi*A
    aire=pi*(A**2) 
    print("\n   perimetre du cercle de rayon {:.1f} = {:.3f}".format(A,perimetre))
    print("\n   aire du cercle de rayon {:.1f} = {:.3f}".format(A,aire))
    perimetreCercle.configure(text = perimetre)
    aireCercle.configure(text= aire)
    #***************************************

    #############################################"""
    #################################################
#Fonction calcul carre
def carre (): 
    #Récupération des variables
    A=float(coteCarre.get()) 
    #Calcul 
    perimetre=4*A
    aire=A**2
    print("\n   perimetre du carre de cote {:.1f} = {:.3f}".format(A,perimetre))
    print("\n   aire du carre de cote {:.1f} = {:.3f}".format(A,aire))
    perimetreCarre.configure(text = perimetre)
    aireCarre.configure(text= aire)
    #***************************************

    #############################################"""
    #################################################
#Fonction calcul parallelogramme
def parallelogramme (): 
    #Récupération des variables
    A=float(aParallelogramme.get()) 
    B=float(bParallelogramme.get()) 
    H=float(hParallelogramme.get()) 
    #Calcul 
    perimetre=2*A+2*B
    aire=B*H
    print("\n   perimetre du parallelogramme de a: {:.1f} b:{:.1f} et h:{:.1f} = {:.3f}".format(A,B,H,perimetre))
    print("\n   aire du parallelogramme de de a: {:.1f} b:{:.1f} et h:{:.1f} = {:.3f}".format(A,B,H,aire))
    perimetreParallelogramme.configure(text = perimetre)
    surfaceParallelogramme.configure(text= aire)
    #***************************************

    #############################################"""
    #################################################

from tkinter import * 
from math import *

fenetre = Tk()
fenetre.title("Calcul des surfaces et des périmètres ")
fenetre.geometry("1000x1000") 

#Creation du widget contenant l'image sphere
can1=Canvas(fenetre, width =200, height =150, bg ='white')
can1.grid(row =0, column =20, rowspan =5, padx =5, pady =5)
photo = PhotoImage(file ='sphere.png')
item = can1.create_image(100, 80, image =photo)
#Creation du widget contenant l'image cercle
can2=Canvas(fenetre, width =200, height =150, bg ='blue')
can2.grid(row =0, column =350, rowspan =5, padx =5, pady =5)
photo2 = PhotoImage(file ='cercle.png')
item = can2.create_image(100, 80, image =photo2)
#Creation du widget contenant l'image carre
can3=Canvas(fenetre, width =200, height =150, bg ='green')
can3.grid(row =50, column =20, rowspan =5, padx =5, pady =5)
photo3 = PhotoImage(file ='parallelogramme2.png')
item = can3.create_image(100, 80, image =photo3)
#Creation du widget contenant l'image parallelogramme
can4=Canvas(fenetre, width =200, height =150, bg ='red')
can4.grid(row =50, column =350, rowspan =5, padx =5, pady =5)
photo4 = PhotoImage(file ='carre.png')
item = can4.create_image(100, 80, image =photo4)

#Mise en page avec la methode de grid

#*************************************************

#*************************************************
#les labels de sphere
txt1=Label(fenetre, text="rayon:").grid(row=1, column=1) 
txt2=Label(fenetre, text="Surface Sphere=").grid(row=2, column=1) 
txt3=Label(fenetre, text="Volume Sphere=").grid(row=3, column=1) 
#les labels de cercle 
rayonCercleLabel=Label(fenetre, text="rayon:").grid(row=1, column=150) 
aireCercleLabel=Label(fenetre, text="aire du cercle=").grid(row=2, column=150) 
surfaceCercleLabel=Label(fenetre, text="surface sphere=").grid(row=3, column=150) 
#les labels de parallelogrammes
parallelogrammeALabel=Label(fenetre, text="a:").grid(row=51, column=1)
parallelogrammeALabel=Label(fenetre, text="b:").grid(row=52, column=1)
parallelogrammeALabel=Label(fenetre, text="h:").grid(row=53, column=1) 
perimetreParallelogrammeLabel=Label(fenetre, text="perimetre Parallelogramme=").grid(row=54, column=1) 
surfaceParallelogrammeLabel=Label(fenetre, text="surface parallelogramme=").grid(row=55, column=1) 
#les labels de carre
carreSLabel=Label(fenetre, text="s:").grid(row=51, column=150) 
perimetreCarreLabel=Label(fenetre, text="perimetre carre=").grid(row=52, column=150) 
aireCarreLabel=Label(fenetre, text="surface carre=").grid(row=53, column=150) 
#les buttons
Button(fenetre,text='Calculer',command=sphere).grid(row=4 , column=1) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=5, column=1) 
Button(fenetre,text='Calculer',command=cercle).grid(row=4 , column=150) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=5, column=150) 
Button(fenetre,text='Calculer',command=parallelogramme).grid(row=56 , column=1) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=57, column=1) 
Button(fenetre,text='Calculer',command=carre).grid(row=54 , column=150) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=55, column=150) 


rayon=Entry(fenetre) 
chaine = Label(fenetre) 
chaine1 = Label(fenetre) 
rayon.grid(row=1, column=2) 
chaine.grid(row=2, column=2) 
chaine1.grid(row=3, column=2)


#cercle
rayonCercle=Entry(fenetre) 
perimetreCercle = Label(fenetre) 
aireCercle = Label(fenetre) 
rayonCercle.grid(row=1, column=160) 
perimetreCercle.grid(row=2, column=160) 
aireCercle.grid(row=3, column=160)

#Carre
coteCarre=Entry(fenetre) 
perimetreCarre = Label(fenetre) 
aireCarre = Label(fenetre) 
coteCarre.grid(row=51, column=160) 
perimetreCarre.grid(row=52, column=160) 
aireCarre.grid(row=53, column=160)


#parallelogramme
aParallelogramme=Entry(fenetre) 
bParallelogramme=Entry(fenetre) 
hParallelogramme=Entry(fenetre) 
perimetreParallelogramme = Label(fenetre) 
surfaceParallelogramme= Label(fenetre) 
aParallelogramme.grid(row=51, column=2) 
bParallelogramme.grid(row=52, column=2) 
hParallelogramme.grid(row=53, column=2) 
perimetreParallelogramme.grid(row=54, column=2) 
surfaceParallelogramme.grid(row=55, column=2)
#*************************************************
 
fenetre.mainloop()



