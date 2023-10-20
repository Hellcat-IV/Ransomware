# Hellcat Ransomware 🇫🇷
 
Ce projet est un mini ransomware de démonstration pour comprendre le fonctionnement de ce type de malware. Il a été réalisé dans le cadre d'un projet scolaire, pour le présenter lors d'une Journée Portes Ouvertes.

Les principales caractéristiques du script incluent :

1. **Génération d'une paire de clés RSA** : Le script génère une paire de clés RSA (clé publique et clé privée) pour chiffrer et déchiffrer les fichiers.

2. **Chiffrement des fichiers** : Le script chiffre tous les fichiers du répertoire "ransom_directory" (à la racine du projet) en utilisant la clé publique générée précédemment.

3. **Déchiffrement des fichiers** : Le script déchiffre tous les fichiers du répertoire "ransom_directory" (à la racine du projet) en utilisant la clé privée générée précédemment.

4. **Affichage d'une fenêtre tkinter** : Le script affiche une fenêtre tkinter avec un message de demande de rançon.

⚠️ **Disclaimer** : Ce projet a été réalisé dans un but éducatif et ne doit pas être utilisé dans un but malveillant. Les auteurs ne seront pas tenu responsable de tout dommage causé par les utilisateurs de ce script.

English version [here](README_EN.md) 🇬🇧

## Installation

Vous pouvez installer le projet en clonant le dépôt, en exécutant la commande suivante :
    
```
git clone https://github.com/Hellcat-IV/Ransomware.git
```
N'oubliez pas d'installer les dépendances :    
```
pip install -r requirements.txt
```

## Utilisation

Pour utiliser le script, exécutez la commande suivante :    

```
python3 ransom.py -h
```

## Contributeurs

- [@Kenoor](https://github.com/bxsic-fr) 
- [@Valmar](https://www.github.com/CalValmar) 

## Licence

Ce projet est sous licence GNU General Public License v3.0 - consultez le fichier [LICENSE](LICENSE) pour plus de détails.

GNU General Public License v3.0 © [HellCat-IV](https://github.com/Hellcat-IV)
