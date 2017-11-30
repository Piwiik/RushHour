====================
 :mod:`board` module
====================

 A module for board representations in a Rush Hour game.
 This module uses from :mod:`vehicle`

Class description
-----------------

.. autoclass:: board.Board

Methods
-------

.. automethod:: board.Board.add_vehicle

.. automethod:: board.Board.get_starting_cell

.. automethod:: board.Board.copy

.. automethod:: board.Board.push_vehicle

.. automethod:: board.Board.clone_and_push

.. automethod:: board.Board.get_possible_moves

.. automethod:: board.Board.get_red_car

Special methods
---------------

.. automethod:: board.Board.__init__

.. automethod:: board.Board.__hash__

.. automethod:: board.Board.__eq__

.. automethod:: board.Board.__repr__

.. automethod:: board.Board.__str__

Exceptions
----------

.. autoclass:: board.CollisionError

.. autoclass:: board.PositionError

.. autoclass:: board.NoVehicleError

.. autoclass:: board.NoRedCarError
