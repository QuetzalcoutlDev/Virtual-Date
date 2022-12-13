
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
from source import config

from source.ui_text import screenshot_text

################################
# Boton de captura de pantalla
################################

screenshot_message = "" # Mensaje al capturar la pantalla

class Screenshot_button():

    """
    Clase para la captura de pantalla, más bien para capturar la pantalla
    mediante el boton.
    """
    
    def __init__(self):
        
        self.button_screenshot = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/screenshot_button_normal.png", f"{config.images_dir}/buttons/screenshot_button_hover.png", f"{config.images_dir}/buttons/screenshot_button_select.png", True, f"{config.images_dir}/buttons/screenshot_button_disable.png")
        self.button_screenshot_clicked = False

        self.s_pressed = False

        self.antialiasing = False
            
    def draw_button(self, antialiasing=False):

        key = pygame.key.get_pressed()

        self.antialiasing = antialiasing

        # self.button_screenshot.draw(config.canvas, 860, 13, 0.7, self.antialiasing)

        if self.button_screenshot.draw(config.canvas, 900, 13, 0.95, self.antialiasing) and not self.button_screenshot_clicked:

            self.button_screenshot_clicked = True
            screenshot_message = screenshot_text + f"{config.main_dir}/{config.take_screenshot(False)}"
            config.notify_message = screenshot_message
            config.notify_visibility = True
            config.take_screenshot()
  
        elif not self.button_screenshot.draw(config.canvas, 900, 13, 0.95, self.antialiasing) and self.button_screenshot_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_screenshot_clicked = False

        # Captura de pantalla pero tocando la tecla S

        if key[pygame.K_s] == 1 and not self.s_pressed:

            take_screenshot_quick()
            self.s_pressed = True

        elif key[pygame.K_s] == 0 and self.s_pressed:

            self.s_pressed = False

screenshot_button = Screenshot_button()

def take_screenshot_quick():

    # Función para capturar la pantalla de manera...¿rápida?

    screenshot_message = screenshot_text + f"{config.main_dir}/{config.take_screenshot(False)}"
    config.notify_message = screenshot_message
    config.notify_visibility = True
    config.take_screenshot()