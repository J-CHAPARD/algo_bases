from __future__ import annotations


def somme_pairs(nums: list[int]) -> int:
    """calculer la somme de tous les nombres pairs de la liste donnée."""
    res = 0
    for n in nums:
        if n%2==0: res+=n
    return res


def compter_occurrences(items: list[int], valeur: int) -> int:
    """Implémentez la fonction pour compter le nombre d'occurrences de `valeur` dans la liste `items`."""
    return items.count(valeur)

def table_multiplication(n: int) -> list[int]:
    """Implémentez la fonction pour retourner la table de multiplication de `n` (jusqu'à 10 inclus)."""
    return list(range(n, n*11, n))


def trouver_maximum(nums: list[int]) -> int:
    """Implémentez une fonction pour trouver et retourner la valeur maximale dans la liste."""
    return max(nums)


def calculer_moyenne(nums: list[int]) -> float:
    """Implémentez une fonction pour calculer et retourner la moyenne des valeurs dans la liste."""
    if len(nums)==0: 	return 0.0	
    else: 				return sum(nums)/len(nums)


def compter_negatifs(nums: list[int]) -> int:
    """Implémentez une fonction pour compter et retourner le nombre d'entiers négatifs dans la liste."""
    nb = 0
    for n in nums:
        if n<0 : nb += 1
    return nb


def compter_mots(phrase: str) -> int:
    """Implémentez une fonction pour compter le nombre de mots dans une chaîne de caractères donnée."""
    return len(phrase.split())


def trouver_plus_long(items: list[str]) -> str:
    """Implémentez une fonction pour trouver et retourner le mot le plus long dans une liste de chaînes de caractères."""
    if len(items)==0 : return ""
    else:
        long_mot = items[0]
        for mot_courant in items[1:]:
            if len(mot_courant) > len(long_mot):
                long_mot=mot_courant
        return long_mot


def convertir_majuscule(items: str) -> str:
    """Implémentez une fonction pour convertir toute la chaînes en majuscules."""
    return items.upper()


def compter_mots_commencant_par(items: str, lettre: str) -> int:
    """Implémentez une fonction pour compter les mots commençant par une lettre donnée."""
    #if items is None or lettre is None: raise ValueError
    if None in (items, lettre): raise ValueError
    else :
        nb=0
        for mot in items.split():
            if mot[0]==lettre: nb+=1
        return nb


def trouver_mot_finissant_par(items: str, suffixe: str) -> list[str]:
    """Implémentez une fonction pour trouver tous les mots qui se terminent par un suffixe donné dans la liste."""
    if None in (items, suffixe): raise ValueError
    return [mot for mot in items.split() if mot[-len(suffixe) : ] == suffixe]
     


def compter_caracteres(s: str, char: str) -> int:
    """Implémentez une fonction pour compter le nombre d'occurences du caractère char et retourner le nombre total."""
    if None in (s, char): raise ValueError 
    else:
        nb = 0
        c = char.lower()
        for lettre in s: 
        	if lettre.lower() == c: nb+=1
    return nb



def inverser_chaine(s: str) -> str:
    """Implémentez une fonction pour inverser et retourner la chaîne de caractères donnée."""
    if s is None: 
        raise ValueError 
    result = ""
    for char in reversed(s): result += char
    return result


def trouver_occurrences_chaine(s: str, c: str) -> int:
    """Implémentez une fonction pour compter les occurrences d'un caractère donné dans une chaîne."""
    if None in (s, c): 
        raise ValueError
    return s.count(c)


# tuples
def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    """Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un tuple donné."""
    res = 0
    for n in nums:
        if n%2==0: res+=n
    return res


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    """Implémentez la fonction pour compter le nombre d'occurrences d'une valeur dans un tuple donné."""
    return items.count(valeur)


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    """Implémentez la fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de tuple."""
    return tuple(range(n, n*11, n))


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    """Implémentez une fonction pour trouver et retourner le nombre maximum d'un tuple."""
    return max(nums)


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    """Implémentez une fonction pour calculer et retourner la moyenne des nombres dans un tuple."""    
    if len(nums)==0: 	return 0.0	
    else: 				return sum(nums)/len(nums)


# sets

def somme_pairs_sets(nums: set[int]) -> int:
    """Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un set donné."""
    res = 0
    for n in nums:
        if n%2==0: res+=n
    return res


def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    """Cette fonction vérifiera simplement si `valeur` existe puisque les sets ne permettent pas les doublons."""
    return valeur in items


def table_multiplication_sets(n: int) -> set[int]:
    """Implémentez une fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de set."""
    return set(range(n, n*11, n))



def trouver_maximum_sets(nums: set[int]) -> int:
    """Implémentez une fonction pour trouver et retourner le nombre maximum d'un set."""
    """if nums is None or len(nums)==0: 
        raise ValueError 
    max = nums.pop()
    for nb in nums:
        if max < nb: max = nb
    return max"""
    if None is nums:
        raise ValueError 
    return max(nums)


def compter_negatifs_sets(nums: set[int]) -> int:
    """Implémentez une fonction pour compter et retourner le nombre de nombres négatifs dans un set."""
    if None is nums:
        raise ValueError
    #return len(list(filter(lambda x: x<0, nums)))
    return len([x for x in nums if x<0])

# dictionnaires

def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    """Implémentez une fonction pour ajouter une clé et sa valeur dans un dictionnaire."""
    d[cle] = valeur
    return d


def supprimer_element(d: dict, cle: str) -> dict:
    """Implémentez une fonction pour supprimer une clé et sa valeur d'un dictionnaire."""
    del d[cle]
    return d


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    """Implémentez une fonction qui fusionne deux dictionnaires et renvoie le résultat.
    Les valeurs de `d2` remplaceront celles de `d1` en cas de doublons."""
    return d1 | d2


def inverser_dictionnaire(d: dict) -> dict:
    """Implémentez une fonction pour inverser un dictionnaire, échangeant les clés et les valeurs.
    Note: Si des valeurs duplicatées existent, une erreur ou un comportement spécifique doit être défini."""
    return dict(zip(d.values(), d.keys()))


def compter_valeurs(d: dict) -> int:
    """Implémentez une fonction pour compter combien de paires clé-valeur sont dans le dictionnaire."""
    return len(d)


def trouver_valeur_maximale(d: dict) -> any:
    """Implémentez une fonction pour trouver et retourner la valeur la plus grande dans un dictionnaire."""
    return max(d.values())


def trouver_cle_par_valeur(d: dict, valeur: any) -> list[str]:
    """Implémentez une fonction pour retourner une liste de toutes les clés correspondant à une valeur donnée."""
    return [x for (x,y) in d.items() if y==valeur]


def verifier_cle_existe(d: dict, cle: str) -> bool:
    """Implémentez une fonction qui vérifie si une clé existe dans le dictionnaire."""
    return cle in d


def valeurs_uniques(d: dict) -> set:
    """Implémentez une fonction qui retourne toutes les valeurs uniques dans un dictionnaire sous forme de set."""
    return set(d.values())


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    """Implémentez une fonction pour mettre à jour une valeur associée à une clé existante ou en ajouter une nouvelle."""
    d[cle] = nouvelle_valeur
    return d
