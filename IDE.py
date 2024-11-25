import tkinter as tk
from tkinter import scrolledtext
import re  # pour les expressions régulières
import subprocess  # Pour exécuter le texte dans un terminal bash

# Dictionnaire de mots spécifiques
var = {
    "important": "gray",  # Les mots "important" seront en gris
    "urgent": "#d3d3d3",  # Le mot "urgent" sera en gris très clair
}

# Liste de mots dans la "fonction famille" (en gras)
funcFamilly = ["def", "class", "lambda", "return"]

# Liste de mots dans la "fonction liste" (en bleu)
funcList = ["print", "input", "str", "int"]

def get_word_color(word):
    """
    Retourne la couleur du mot en fonction des conditions :
    - Gris foncé si le mot est une clé dans 'var'
    - Bleu si le mot est dans 'funcList'
    - Gras si le mot est dans 'funcFamilly'
    """
    # Vérification si le mot est dans le dictionnaire 'var'
    if word in var:
        return var[word], False  # Retourne la couleur spécifiée dans 'var'
    # Vérification si le mot est dans la liste 'funcFamilly'
    elif word in funcFamilly:
        return "black", True   # Texte normal (noir) mais en gras
    # Vérification si le mot est dans la liste 'funcList'
    elif word in funcList:
        return "blue", False   # Bleu et pas de gras
    return "white", False      # Si le mot n'est dans aucune des listes, couleur blanche (par défaut)

def apply_syntax_highlighting(event=None):
    """
    Applique les styles (gris, bleu, gras) aux mots en fonction des critères définis.
    """
    # Récupérer tout le texte
    text_content = text_area.get("1.0", tk.END)

    # Supprimer les anciennes balises de style
    text_area.tag_remove("gray", "1.0", tk.END)
    text_area.tag_remove("bold", "1.0", tk.END)
    text_area.tag_remove("blue", "1.0", tk.END)

    # Recherche et application de style pour chaque mot
    idx = "1.0"
    word_regex = r'\b\w+\b'  # Expression régulière pour trouver les mots

    for match in re.finditer(word_regex, text_content):
        start_idx = match.start()  # Position du début du mot
        end_idx = match.end()      # Position de la fin du mot
        word = match.group()        # Le mot trouvé

        # Obtenir la couleur et le style pour le mot
        color, bold = get_word_color(word)

        # Appliquer les styles
        start_tag = f"1.0 + {start_idx}c"
        end_tag = f"1.0 + {end_idx}c"

        if color == "gray":
            text_area.tag_add("gray", start_tag, end_tag)
        elif color == "blue":
            text_area.tag_add("blue", start_tag, end_tag)

        if bold:
            text_area.tag_add("bold", start_tag, end_tag)

    # Ajouter les styles (définir les couleurs et les styles de texte)
    text_area.tag_config("gray", foreground="gray")  # Gris foncé
    text_area.tag_config("bold", font=("Arial", 12, "bold"))  # Gras
    text_area.tag_config("blue", foreground="blue")  # Bleu
    text_area.tag_config("default", foreground="white")  # Texte par défaut en blanc

def run_text_in_bash():
    """
    Envoie le texte écrit dans la zone de texte à une fenêtre bash.
    """
    text_content = text_area.get("1.0", tk.END).strip()  # Récupère le texte sans les sauts de ligne finaux
    if text_content:  # Vérifie si le texte n'est pas vide
        # Exécuter le texte dans le terminal bash
        subprocess.run(['C:\\Program Files\\Git\\bin\\bash.exe', '-c', text_content])


# Création de la fenêtre principale
root = tk.Tk()
root.title("Éditeur de texte coloré")

# Fenêtre avec un fond gris très foncé
root.configure(bg="#2c2c2c")  # Gris très foncé

# Zone de texte avec défilement
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#2c2c2c", fg="white")
text_area.pack(fill=tk.BOTH, expand=True)

# Création du bouton pour exécuter le texte dans bash
run_button = tk.Button(root, text="Run", command=run_text_in_bash, width=4, height=2, bg="lightgray")
run_button.pack(pady=10)

# Lier un événement pour appliquer la coloration après chaque frappe
text_area.bind("<KeyRelease>", apply_syntax_highlighting)

# Lancer la boucle principale
root.mainloop()
