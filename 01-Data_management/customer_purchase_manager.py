#  1. să solicite într-un singur mesaj numele și prenumele utilizatorului și să verifice dacă textul introdus conține cel puțin două cuvinte. Dacă condiția nu este îndeplinită, programul afișează un mesaj că numele nu a fost introdus corect și solicită din nou numele utilizatorului, până când se introduce o valoare care îndeplinește condiția;


def verificare():
    while True:
        nume_complet = str(input("Nume si prenume: ")).strip()
        lista = nume_complet.split()

        if len(lista) >= 2:
            return nume_complet
        else: 
            print("Trebuie sa introduci numele si prenumele. Ex: Ghita Ionut.")


nume_complet = verificare()

# 2. să stocheze datele despre utilizator separate în două variabile: nume și prenume;
lista = nume_complet.split()
nume = lista[0]
prenume = lista[1]

# 3. să solicite numărul total de achiziții efectuate de utilizator în ultimul an. Pentru fiecare achiziție, solicită suma (în lei);
numar_de_achizitii = int(input("Numar de achizitii in ultimul an: "))
suma_achizitii = []

achizitii_peste_zece_mii = []
for i in range(numar_de_achizitii):
    suma = float(input(f'Suma pentru achizitia {i + 1} (RON):'))
    suma_achizitii.append(suma)
    if suma >= 10000:
        achizitii_peste_zece_mii.append(suma)
# 4. să calculeze suma totală cheltuită;
total_cheltuit = sum(suma_achizitii)

# 5. să numere achiziţiile cu o sumă peste 10.000 de lei;
numar_achizitii_peste_zece_mii = 0
for i in achizitii_peste_zece_mii:
    if i >= 10000:
        numar_achizitii_peste_zece_mii += 1
print(f'Ati efectuat {numar_achizitii_peste_zece_mii} achizitii peste suma de 10000 RON.')
        
        
        
# 6. pe baza sumei totale cheltuite, să atribuie statutul utilizatorului:
# dacă suma totală cheltuită este mai mare de 100.000 de lei și utilizatorul a efectuat mai mult de 10 achiziții în ultimul an, utilizatorul primește statut VIP;
# dacă suma totală cheltuită este mai mică sau egală cu 100.000 de lei sau utilizatorul nu a avut 10 achiziții, acesta primește statut STANDARD;
statut_client = ""
if total_cheltuit > 100000 and numar_de_achizitii >= 10:
    statut_client = "VIP"
    print(f'Ai achizitii in valoare de {total_cheltuit}, iar numarul tau de achizitii este {numar_de_achizitii}. Esti client {statut_client}.')
else:
    statut_client = "Standard"
    print(f'Ai achizitii in valoare de {total_cheltuit}, iar numarul tau de achizitii este {numar_de_achizitii}. Esti client {statut_client}.')


#  7. după ce este determinat statutul utilizatorului, clientul va avea o reducere aprobată pentru următoarele achiziții: 5% pentru utilizatorii STANDARD și 10% pentru utilizatorii VIP;
#  8. să solicite utilizatorului să introducă prețul articolului pe care dorește să-l cumpere și calculează și să afișeze prețul cu reducere.
if statut_client == "VIP":
    print("Ai o reducere de 10% pentru urmatoarele achizitii.")
    valoare_achizitie = float(
        input("Introdu valoarea unei viitoare achizitii la pret intreg: ")
    )
    valoare_reducere = valoare_achizitie * 0.10
    valoare_cu_reducere = valoare_achizitie - valoare_reducere
    print(f"Pretul achizitiei dupa aplicarea reducerii este {valoare_cu_reducere}.")
elif statut_client == "Standard":
    print("Ai o reducere de 5% pentru urmatoarele achizitii.")
    valoare_achizitie = float(
        input("Introdu valoarea unei viitoare achizitii la pret intreg: ")
    )
    valoare_reducere = valoare_achizitie * 0.05
    valoare_cu_reducere = valoare_achizitie - valoare_reducere
    print(f'Pretul achizitiei dupa aplicarea reducerii este {valoare_cu_reducere}.')
