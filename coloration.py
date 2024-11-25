colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",        # Réinitialiser le style
    "bold": "\033[1m",         # Texte en gras
    "underline": "\033[4m",    # Texte souligné
    "dim": "\033[2m",          # Texte atténué
    "reverse": "\033[7m"       # Inversion des couleurs (texte/fond)
}


def color(text, color):
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
