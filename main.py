
# Virtual Date! 
# Copyright (C) 2022 QuetzalcoutlDev

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame, sys, lenpy
from source import config, Game

# Este función recopila, todo el juego en una sola función.
# Ya debes saber eso, pero igual hay que explicarlo :) .

def main():

    # Inicializar Pygame
    pygame.init()

    game = Game.Game() # Variable del juego

    run = False

    # Bucle principal
    while not run:

        # Procesar eventos
        run = game.process_events() 

        # Configura los FPS
        lenpy.config.clock.tick(60)

        game.draw_screen() # <<<< Esto es todo el juego, el splashscreen, el menú principal, etc.

    # Cierra Pygame
    pygame.quit()

    # Esto permite guardar los cambios mientras no se este en el juego
    # Los datos no se guardaran si se está en el juego(Al menos que se diga 'Adiós')
    if not config.in_game:
        config.data_manager.Save_game_data([config.default_data], ["tojiko"])

    # Finaliza la ejecución del juego
    sys.exit()

if __name__ == '__main__':
    main()