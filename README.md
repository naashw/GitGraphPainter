# Git Graph Painter

Dessinez du texte et des symboles sur votre graphe de contributions GitHub.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Description

Git Graph Painter est un script Python qui génère des commits Git antidatés pour afficher du texte personnalisé sur votre graphe de contributions GitHub. Le script convertit votre texte en une grille de pixels puis crée les commits nécessaires aux dates appropriées.

## Fonctionnalités

- Alphabet complet (A-Z) et chiffres (0-9)
- Caractères spéciaux : `! . - _ : ; ( ) < > / ? * + =`
- Symboles : `☺` `♥`
- Prévisualisation ASCII avant création des commits
- Contrôle de l'intensité (couleur plus ou moins foncée)
- Mode simulation (dry-run)

## Installation

```bash
git clone https://github.com/votre-username/GitGraphPainter.git
cd GitGraphPainter
```

Aucune dépendance externe requise. Python 3.6+ suffit.

## Utilisation

### Prévisualisation

Voir à quoi ressemblera votre texte sans créer de commits :

```bash
python git_graph_painter.py "HELLO" --preview
```

Résultat :
```
=== Git Graph Painter ===
Text: HELLO
Grid size: 24 weeks x 5 days

Preview:
Tue #..##.####.#...#....
Wed #..#..#....#...#....
Thu ####..###..#...#....
Fri #..#..#....#...#....
Sat #..#..####.####.####
```

### Création des commits

```bash
python git_graph_painter.py "HI"
```

Le script demandera confirmation avant de créer les commits.

### Options

| Option | Court | Description |
|--------|-------|-------------|
| `--preview` | `-p` | Prévisualiser sans créer de commits |
| `--offset` | `-o` | Décalage en semaines depuis le début (défaut: 1) |
| `--intensity` | `-i` | Commits par jour, 1-4 (défaut: 1) |
| `--year` | `-y` | Année cible (défaut: année courante) |
| `--dry-run` | `-d` | Afficher les actions sans les exécuter |

### Exemples

```bash
# Texte simple
python git_graph_painter.py "DEV"

# Décaler le texte de 5 semaines
python git_graph_painter.py "CODE" --offset 5

# Couleur plus intense (plus de commits par jour)
python git_graph_painter.py "2024" --intensity 3

# Simuler sans créer de commits
python git_graph_painter.py "TEST" --dry-run

# Combiner plusieurs options
python git_graph_painter.py "NAASH" -o 2 -i 2
```

## Publication sur GitHub

Après avoir créé les commits :

```bash
git push origin main
```

Les contributions apparaîtront sur votre profil GitHub dans les minutes qui suivent.

## Limitations

- Le graphe GitHub affiche environ 52 semaines
- Chaque caractère occupe 4-5 colonnes + 1 espace
- Seules les dates passées peuvent recevoir des commits
- Les contributions sont limitées à 5 lignes (Mardi à Samedi)

## Avertissement

Ce script crée de vrais commits dans votre historique Git. Utilisez-le de préférence sur un dépôt dédié pour éviter de polluer l'historique de vos projets.

## License

MIT License - Libre d'utilisation et de modification.
