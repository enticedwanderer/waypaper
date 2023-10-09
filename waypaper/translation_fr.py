"""Traductions en français de l'interface du programme"""

MSG_DESC = "Sélecteur de papier peint graphique pour Wayland et X11. Il fonctionne comme une interface pour feh, swaybg, wallutils et swww."
MSG_INFO = "Pour plus d'informations, visitez :\nhttps://github.com/anufrievroman/waypaper"

MSG_ARG_HELP = "afficher la version du programme"
MSG_ARG_FILL = "spécifier comment remplir l'écran avec l'image choisie"
MSG_ARG_REST = "restaurer le dernier papier peint"
MSG_ARG_BACK = "spécifier quel backend utiliser pour définir le papier peint"
MSG_ARG_RAND = "définir un papier peint aléatoire"

MSG_PATH = "Chemin de l'image sélectionnée :"
MSG_SELECT = "Sélectionner"
MSG_REFRESH = "Actualiser"
MSG_RANDOM = "Aléatoire"
MSG_EXIT = "Quitter"
MSG_SUBFOLDERS = "Sous-dossiers"
MSG_CHANGEFOLDER = "Changer de dossier de papier peint"
MSG_CHOOSEFOLDER = "Veuillez choisir un dossier"
MSG_CACHING = "Mise en cache des papiers peints..."
MSG_SETWITH = "La commande envoyée pour définir le papier peint a été définie avec"

MSG_HELP = "Raccourcis clavier de Waypaper :\n\nhjkl - Navigation (←↓↑→)\nf - Changer de dossier de papier peint\n"
MSG_HELP += "g - Faire défiler vers le haut\nG - Faire défiler vers le bas\nR - Définir un papier peint aléatoire\nr - Recréer le cache des papiers peints\n"
MSG_HELP += "s - Inclure/exclure les images des sous-dossiers\n? - Aide\nq - Quitter\n\n"
MSG_HELP += MSG_INFO

ERR_CACHE = "Erreur lors de la suppression du cache"
ERR_BACKEND = "Il semble qu'aucun des backends de papier peint ne soit installé sur le système.\n"
ERR_BACKEND += "Utilisez votre gestionnaire de paquets pour installer au moins l'un de ces backends :\n\n"
ERR_BACKEND += "- swaybg (pour Wayland)\n- swww (pour Wayland)\n"
ERR_BACKEND += "- feh (pour Xorg)\n- wallutils (pour Xorg & Wayland)\n\n"
ERR_BACKEND += MSG_INFO
ERR_WALL = "Erreur lors du changement de papier peint :"
ERR_NOTSUP = "Le backend n'est pas pris en charge :"
ERR_DISP = "Erreur lors de la détermination des noms des moniteurs :"
ERR_KILL = "Avertissement lié à killall :"

TIP_SUBFOLDER = "Inclure/exclure les images des sous-dossiers"
TIP_REFRESH = "Recréer le dossier d'images"
TIP_FILL = "Choisir le type de remplissage"
TIP_BACKEND = "Choisir le backend"
TIP_SORTING = "Choisir le type de tri"
TIP_DISPLAY = "Choisir l'affichage"
TIP_COLOR = "Choisir la couleur de fond"
TIP_RANDOM = "Définir un papier peint aléatoire"
TIP_EXIT = "Quitter l'application"
