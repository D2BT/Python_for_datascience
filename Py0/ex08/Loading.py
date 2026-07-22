import os
import time


# Récupérer les dimensions du terminal actuel
taille = os.get_terminal_size()
largeur_totale = os.get_terminal_size().columns


def ft_tqdm(lst: range) -> None:
    start = time.time()
    for elem in lst:
        pourcentage = (elem + 1) / len(lst) * 100
        now = time.time()
        passed = now - start
        vitesse = (elem + 1) / passed if (passed > 0 and elem > 0) else 0
        largeur_barre = largeur_totale - 40
        temps_restant = (len(lst) - (elem + 1)) / vitesse if vitesse > 0 else 0

        passed_min = int(passed//60)
        passed_sec = int(passed % 60)
        eta_min = int(temps_restant//60)
        eta_sec = int(temps_restant % 60)

        proportion = (elem + 1) / len(lst)
        nb_egal = int(proportion * largeur_barre)

        if pourcentage >= 100:
            barre = "=" * nb_egal
        else:
            nb_espaces = largeur_barre - nb_egal - 1
            barre = ("=" * nb_egal) + ">" + (" " * nb_espaces)

        print(f"{pourcentage:>3.0f}%|{barre}| {elem + 1:>3}/{len(lst):>3}",
              f"[{passed_min:02d}:{passed_sec:02d}<{eta_min:02d}:{eta_sec:02d}"
              f", {vitesse:>6.02f}it/s]", "\r", sep="", end="")
        yield elem
