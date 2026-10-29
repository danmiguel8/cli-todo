#!/usr/bin/env python3
"""Petite to-do list en ligne de commande."""

import argparse
import json
from pathlib import Path

FICHIER = Path.home() / ".todo.json"


def charger():
    """Lit les tâches depuis le fichier JSON (liste vide si absent)."""
    if FICHIER.exists():
        return json.loads(FICHIER.read_text(encoding="utf-8"))
    return []


def sauvegarder(taches):
    """Écrit les tâches dans le fichier JSON."""
    FICHIER.write_text(
        json.dumps(taches, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def numero_valide(taches, numero):
    if 1 <= numero <= len(taches):
        return True
    print(f"Tâche n°{numero} introuvable.")
    return False


def ajouter(args):
    taches = charger()
    taches.append({"texte": " ".join(args.texte), "fait": False})
    sauvegarder(taches)
    print(f"Ajouté : {taches[-1]['texte']}")


def lister(args):
    taches = charger()
    if not taches:
        print("Aucune tâche.")
        return
    for i, tache in enumerate(taches, start=1):
        case = "x" if tache["fait"] else " "
        print(f"{i}. [{case}] {tache['texte']}")


def terminer(args):
    taches = charger()
    if numero_valide(taches, args.numero):
        taches[args.numero - 1]["fait"] = True
        sauvegarder(taches)
        print(f"Terminé : {taches[args.numero - 1]['texte']}")


def supprimer(args):
    taches = charger()
    if numero_valide(taches, args.numero):
        retiree = taches.pop(args.numero - 1)
        sauvegarder(taches)
        print(f"Supprimé : {retiree['texte']}")


def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de tâches simple")
    sous = parser.add_subparsers(dest="commande", required=True)

    p = sous.add_parser("add", help="ajouter une tâche")
    p.add_argument("texte", nargs="+")
    p.set_defaults(func=ajouter)

    p = sous.add_parser("list", help="afficher les tâches")
    p.set_defaults(func=lister)

    p = sous.add_parser("done", help="marquer une tâche comme faite")
    p.add_argument("numero", type=int)
    p.set_defaults(func=terminer)

    p = sous.add_parser("rm", help="supprimer une tâche")
    p.add_argument("numero", type=int)
    p.set_defaults(func=supprimer)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
