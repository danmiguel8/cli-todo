# cli-todo

Une petite to-do list en ligne de commande, écrite en Python (bibliothèque standard uniquement).

## Utilisation

```bash
python todo.py add Acheter du pain
python todo.py add Finir le README
python todo.py list
python todo.py done 1
python todo.py rm 2
```

Exemple de sortie :

```
1. [x] Acheter du pain
2. [ ] Finir le README
```

Les tâches sont stockées dans `~/.todo.json`.

## Prérequis

Python 3.8 ou plus récent. Aucune dépendance à installer.

## Idées d'amélioration

- [ ] Dates d'échéance
- [ ] Priorités
- [ ] Commande `edit`
- [ ] Tests avec `pytest`
- [ ] Couleurs dans le terminal

## Ce que j'ai appris

- Lire et écrire du JSON
- Créer une CLI avec `argparse` et des sous-commandes
- Manipuler des fichiers avec `pathlib`
