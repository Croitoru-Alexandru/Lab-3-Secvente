"""
    lab 3 - cea mai lunga subsecventa a caror numere au suma cifrelor divizibile cu 10
"""


def generare_lista(x):
    """
    Generare lista
    :param x: Cate numere dorim sa fie
    :return: lista de numere
    """
    lista = []
    for i in range(1, x + 1, 1):
        numar = int(input(f"Introduceti numarul dorit {i}:"))
        lista.append(numar)
    return lista


def generare_lista1(x):
    """
    Generare lista pentru cerinta live
    :param x: Cate numere dorim sa fie
    :return: lista de numere
    """
    lista = []
    for i in range(1, x + 1, 1):
        numar = input(f"Introduceti numarul dorit {i}:")
        lista.append(numar)
    return lista


def secventa_conditi_unu(lista):
    """
    Gasirea secventei de forma x[i] < x[i+1] < ... < x[i+n]
    :param lista: lista de cifre
    :return: lista cu secventa
    """
    lista_rezultat = []
    lungime = 1
    lungime_maxima = 1
    index_final = 0
    for i in range(0, len(lista) - 1, 1):
        if lista[i] < lista[i + 1]:
            lungime = lungime + 1
            if lungime > lungime_maxima:
                lungime_maxima = lungime
                index_final = i + 1
        else:
            lungime = 1
    for i in range(index_final - lungime_maxima + 1, index_final + 1, 1):
        lista_rezultat.append(lista[i])
    return lista_rezultat


def prim(x):
    """
    Numar prim
    :param x: Numar
    :return: Adevarat sau Fals
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1, 1):
        if x % i == 0:
            return False
    return True


def secventa_conditi_doi(lista):
    """
    Gasirea secventei cu numere prime
    :param lista: lista de numere
    :return: lista cu secventa
    """
    lungime = 0
    lungime_maxima = 0
    index_final = 0
    lista_rezultat = []
    for i in range(0, len(lista), 1):
        if prim(lista[i]):
            lungime = lungime + 1
            if lungime > lungime_maxima:
                lungime_maxima = lungime
                index_final = i
        else:
            lungime = 0
    for i in range(index_final - lungime_maxima + 1, index_final + 1, 1):
        lista_rezultat.append(lista[i])
    return lista_rezultat


def secventa_conditi_trei(lista):
    """
    Gasirea secventei cu suma cifrelor
    :param lista: lista de numere
    :return: lista cu secventa
    """
    lista_rezultat = []
    sume = []
    lungime = 1
    lungime_maxima = 1
    index_final = 0
    for m in lista:
        k = 0
        for n in m:
            p = int(n)
            k += p
        sume.append(k)
    for i in range(0, len(lista) - 1, 1):
        if sume[i] % 10 == 0:
            lungime = lungime + 1
            if lungime > lungime_maxima:
                lungime_maxima = lungime
                index_final = i + 1
        else:
            lungime = 1
    for i in range(index_final - lungime_maxima + 1, index_final + 1, 1):
        lista_rezultat.append(lista[i])
    return lista_rezultat


optiune = """
    1. Realizarea unei liste cu numere intregi
    2. Gasirea secventei de lungime maxima avand conditia: x[i] < x[i+1] < ... < x[i+n]
    3. Gasirea secventei de lungime maxima avand conditia: Toate sunt numere prime
    4. Cerinta live
    5. Oprire program 
"""


def main():
    lista = []
    while True:
        optiuni = input(optiune)
        if optiuni == '1':
            numar = int(input("Introduceti cate numere doriti sa fie in lista:"))
            lista = generare_lista(numar)
            print(lista)
        elif optiuni == '2':
            print(secventa_conditi_unu(lista))
        elif optiuni == '3':
            print(secventa_conditi_doi(lista))
        elif optiuni == '4':
            numar = int(input("Introduceti cate numere doriti sa fie in lista:"))
            lista1 = generare_lista1(numar)
            print(secventa_conditi_trei(lista1))
        elif optiuni == '5':
            break
        else:
            print("Ati introdus o cifra invalida!")


def test_secventa_conditi_unu():
    assert secventa_conditi_unu([5, 3, 17, 5, 6, 7, 8, 9, 13, 10, 11]) == [5, 6, 7, 8, 9, 13]


test_secventa_conditi_unu()


def test_secventa_conditi_doi():
    assert secventa_conditi_doi([2, 3, 5, 7, 9, 13, 15, 18, 20]) == [2, 3, 5, 7]


test_secventa_conditi_doi()


def test_secventa_conditi_trei():
    assert secventa_conditi_trei(['46', '22', '19', '28', '37']) == ['19', '28', '37']


test_secventa_conditi_trei()

if __name__ == main():
    main()
