#!/usr/bin/python
print("DNA içinde motif bulma:")
dna = input("Lütfen içinde motif aranacak bir DNA sekansı giriniz:")
motif = input("Lütfen DNA sekansı içinde aranacak bir motif giriniz:")

DNA = dna.upper() #Küçük 'a, t, g, c' girilme ihtimaline karşı 
MOTIF = motif.upper() #Python küçük/büyük harf duyarlı olduğu için büyük harfe dönüştürme

if DNA.count('A')+DNA.count('T')+DNA.count('G')+DNA.count('C') == len(DNA):
#DNA sekansında 'A, T, G, C' nükleotidleri dışında harf ile yanlışlık yapılmadığından emin olmak için
    if MOTIF.count('A')+MOTIF.count('T')+MOTIF.count('G')+MOTIF.count('C') == len(MOTIF):
    #Motif sekansında 'A, T, G, C' nükleotidleri dışında harf ile yanlışlık yapılmadığından emin olmak için
        if len(DNA) >= len(MOTIF):
        #DNA'nın içinde bulunacak motiften uzun veya motif ile aynı uzunlukta olduğuna emin olmak için  
            if MOTIF in DNA:
            #Motifin DNA'da bulunması
                pozisyon = "" #Başlangıç için boş string
                for i in range(len(DNA)):
                #DNA uzunluğu kadar tekrar
                    if DNA[i:i+len(MOTIF)] == MOTIF:
                        #DNA'nın motifi içerdiği index
                        pozisyon = pozisyon+ str(i+1)+" " #Python index '0'dan başladığı için '+1'
                        #DNA'nın motife eşit olduğu başlangıç pozisyonları
                print(pozisyon)
                if DNA == MOTIF: #DNA ile motifin aynı olması durumu
                    print("Motif, DNA ile aynı sekansa sahiptir.")
            else:
                print("Motif DNA sekansında bulunmamaktadır.")
        else:
            print("Girilen motif, DNA'dan daha uzun olamaz! Lütfen buna dikkat ediniz.")
    else:
        print("Hatalı motif sekansı girdiniz. Lütfen motifin sadece 'A, T, G, C'den oluştuğundan emin olunuz.")
else:
    print("Hatalı DNA sekansı girdiniz. Lütfen DNA'nın sadece 'A, T, G, C'den oluştuğundan emin olunuz.")
