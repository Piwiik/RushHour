================
 Journal de bord
================

 Par Pierrick Uro, Luqman Ferdjani, Manon Devaux

Semaine 1
=========

 Conceptualisation du problème, saisie d'une configuration, liste des mouvements possibles

 1. Fichier vehicle.py:

 * définition de la classe Vehicle avec son erreur VehicleError:

  * méthodes de classe:

   * **constructeur:** __init__
   * **sélecteur:** get_orientation, get_size, get_name
   * **comparaisons:** __eq__
   * **imprimeur:** __str__

 2. Fichier board.py:

 * définition des erreurs: CollisionError, PositionError, NoVehicleError, NoRedCarError
 * définition de la classe board:

  * méthodes de la classe:

   * **constructeur:** __init__ utilisant la méthode add_vehicle
   * **comparaisons:** __eq__
   * **imprimeurs:** __str__ et __repr__
   * **hachage:** __hash__ (utilisé dans life_uh_finds_a_way)
   * get_starting_cell
   * get_red_car
   * **modificateur:** push_vehicle
   * get_possible_moves utilisé pour la résolution du casse-tête
   * **méthodes en développement:** life_uh_finds_a_way et welcome_to_jurassic_park

 3. Fichier test.py: fichier de test, à ignorer

 **Objectif pour la semaine prochaine:** avancer dans la résolution du casse-tête

Semaines 2 et 3
================

 Exploration de pistes pour la résolution du problème, exploration de la mutabilité des boards

 * méthodes liées à la copie du board:

  * copy
  * clone_and_push

 * méthodes et fonctions utilisées pour la résolution du problème:

  * is_ended
  * get_path
  * get_new_boards

 * move

Semaine 4
==========

Finalisation de la résolution du problème, et options bonus

 1. Fichier main.py:

 * Personnalisation du board:

  * get_input_initialization

 * Résolution du problème:

  * find_solution

 * Fonctions liées au jeu:

  * input_move
  * is_game_ended
  * find_car
  * save_game
  * load_board
  * textual_game
  * main

 2. Fichier boards.py:

 * variable BOARDS qui permet de stocker 40 boards utilisés dans le jeu original

 3. Fichier graphical.py:

 * main
 * board_display
 * board_solver
 * next_step
