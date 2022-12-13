
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

import pygame, sys

from source import config

from lenpy import Text
from lenpy.ui import TextButton

# Pantalla de dialogo

def dialog(message, action=None):

    """
    La pantalla de dialogo, por ahora solo permite una linea de dialogo
    por lo que por ahora se evita colocar mensajes muy largos.

    :message: el mensaje a mostrar.
    """
    
    img = pygame.image.load(f"{config.images_dir}/dialog_box.png").convert_alpha()

    text = Text(message, "VarelaRound.ttf", 20, f"{config.fonts_dir}/", config.BLACK)
    button = TextButton("Ok", "LSANS.TTF", 30, "#990b8e", "#65085e", "#cb11bd", True, f"{config.fonts_dir}/")

    run = True

    config.screen.blit(config.black_in_screen, [0, 0])

    while run:

        # Procesar los eventos

        for event in pygame.event.get():

            # Cerrar la caja de dialogo

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    run = False

            if event.type == pygame.QUIT and not config.in_game:
                pygame.quit()
                config.data_manager.Save_game_data([config.default_data], ["tojiko"])
                sys.exit()

        config.screen.blit(img, [232.2, 129])

        # print(text.get_text_rect())

        text.draw(config.screen, 488 - (text.get_text_rect()[2] / 2.1), 238)

        # Esto permite cerrar la pantalla de dialogo
        if button.draw(config.screen, 467, 328):

            if action == None:

                run = False

            elif action == "quit":
                
                pygame.quit()
                config.data_manager.Save_game_data([config.default_data], ["tojiko"])
                sys.exit()

        # Actualiza solo una porción de la pantalla
        pygame.display.update()