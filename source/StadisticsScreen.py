
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

import pygame, lenpy
from source import config, textbox

# Este archivo es la pantalla de estadisticas, pero en está versión(0.1.0)
# no se usa

###########################
# Pantalla de estadisticas
###########################

class Stadistics_Screen():

    """
    La pantalla de estadisticas en una de las más sencillas que hay en todo
    el juego.
    """

    def __init__(self):

        self.visible = False
        self.stadistics_elements = [f"Nivel: {config.current_nvl}",
                                    f"Puntos de relación y cariño: {config.exp_points}",
                                    f"Puntos de amor: {config.love_points}",
                                    f"Puntos de amor acumulados: {config.love_points_acumulated}",
                                    f"Regalos actuales: {config.current_gifts}",
                                    f"Regalos comprados: {config.bought_gifts}",
                                    f"cumplidos realizados: {config.compliments_facts}",
                                    f"Preguntas realizadas por Tojiko: {config.tojiko_questions_makes}",
                                    f"Respuestas correctas(Preguntas de Tojiko): {config.tojiko_responses_good}",
                                    f"Respuestas incorrectas(Preguntas de Tojiko): {config.tojiko_responses_bad}"
                                    ]

        self.st_box_x = config.canvas_size[0] // 3.8
        self.st_box_y = 40

        self.button_stadistics_screen = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/stadistics_button_normal.png", f"{config.images_dir}/buttons/stadistics_button_hover.png", f"{config.images_dir}/buttons/stadistics_button_select.png", True, f"{config.images_dir}/buttons/stadistics_button_disable.png")
        self.button_stadistics_exit = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/exit_button_normal.png", f"{config.images_dir}/buttons/exit_button_hover.png", f"{config.images_dir}/buttons/exit_button_select.png", True, f"{config.images_dir}/buttons/exit_button_disable.png")

        self.stadistics_screen_button_clicked = False
        self.stadistics_screen_button_clicked_exit = False
        
        self.stadistics_screen_show = False

        self.title = lenpy.Text("Estadisticas", "Varela Round", 40, None, config.BLACK, sysfont=True)

        self.antialiasing = False

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        # self.button_stadistics_screen.draw(config.canvas, 900, 13, 0.7, self.antialiasing)

        # Deshabilita los botones para mostrar la pantalla
        
        if not config.current_screen == "Stadistics_Screen" and not config.current_screen == "Game":
            self.button_stadistics_screen.disable = True

        elif config.current_screen == "Game":
            self.button_stadistics_screen.disable = False

        elif config.current_screen == "Stadistics_Screen" and self.stadistics_screen_show:
            self.button_stadistics_screen.disable = True

        # El botón para mostrar la pantalla de estadisticas (El de circulo)

        if self.button_stadistics_screen.draw(config.canvas, 900, 13, 0.8, self.antialiasing) and not self.stadistics_screen_button_clicked and not config.current_screen == "Stadistics_Screen":

            self.stadistics_screen_show = True
            self.stadistics_screen_button_clicked = True

        elif not self.button_stadistics_screen.draw(config.canvas, 900, 13, 0.8, self.antialiasing) and self.stadistics_screen_button_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.stadistics_screen_button_clicked = False

        if self.stadistics_screen_show:

            config.current_screen = "Stadistics_Screen"
            
            self.Screen(True)

            # Este es el botón para salir de la pantalla de estadisticas
            
            self.button_stadistics_exit.draw(config.canvas, self.st_box_x * 2.8, 10, 0.8, self.antialiasing)

            if self.button_stadistics_exit.draw(config.canvas, self.st_box_x * 2.8, 10, 0.8, self.antialiasing) and not self.stadistics_screen_button_clicked_exit:
                
                self.stadistics_screen_button_clicked_exit = True
                self.stadistics_screen_show = False
                config.current_screen = config.current_screen_default 

            elif not self.button_stadistics_exit.draw(config.canvas, self.st_box_x * 2.8, 10, 0.8, self.antialiasing) and self.stadistics_screen_button_clicked_exit and pygame.mouse.get_pressed()[0] == 0:

                self.stadistics_screen_button_clicked_exit = False

        else:

            self.Screen(False)

    def Screen(self, visible):

        self.visible = visible

        if self.visible and not getattr(textbox.tbox, "visible_box"):

            # config.screen.fill(config.GRAY, [0, 0, config.canvas_size[0], config.canvas_size[1]], pygame.BLEND_RGBA_MIN)

            pygame.draw.rect(config.canvas, config.RED, [self.st_box_x, self.st_box_y, 500, 433.3])

            self.title.draw(config.canvas, self.st_box_x * 1.6, self.st_box_y * 1.4)

            stadistic_element_y = 2.5

            for stadistics in self.stadistics_elements:

                stadistic_element = lenpy.Text(stadistics, "Varela Round", 28, None, config.BLACK, sysfont=True)
                stadistic_element.draw(config.canvas, self.st_box_x * 1.1, self.st_box_y * stadistic_element_y)

                stadistic_element_y += 0.6

stadistics_screen = Stadistics_Screen()