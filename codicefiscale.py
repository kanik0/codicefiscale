import csv

dict_mesi = {'A':'Gennaio', 'B':'Febbraio', 'C':'Marzo', 'D':'Aprile', 'E':'Maggio', 'H':'Giugno', 'L':'Luglio', 'M':'Agosto', 'P':'Settembre', 'R':'Ottobre', 'S':'Novembre', 'T':'Dicembre'}

def get_city(codice):
    with open('comuni.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        found = False
        for row in reader:
            if(row[0] == codice):
                found = True
                return {"Comune":row[1], "Provincia":row[2]}
        if(found == False):
            return {"Comune":"ERR", "Provincia":"ERR"}


def get_stuff(codicefiscale):
    cognome = codicefiscale[0:3]
    nome = codicefiscale[3:6]
    anno = codicefiscale[6:8]
    mese = codicefiscale[8]
    giorno = int(codicefiscale[9:11])
    comune = get_city(codicefiscale[11:15])

    if(giorno > 32):
        giorno = giorno - 40
        sesso = 'F'
    else:
        sesso = 'M'
    
    mese = dict_mesi[mese]


    return {"Nome":nome, "Cognome":cognome, "Giorno":giorno, "Mese":mese, "Anno":anno, "Sesso":sesso, "Comune":comune['Comune'], "Provincia":comune['Provincia']}


if __name__ == '__main__':
    print("Hi.")
