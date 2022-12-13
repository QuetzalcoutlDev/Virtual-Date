
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

import pygame, lenpy, sys
from source import config, configscreen, screenshot_f

from source.ui_text import MainMenu_text

class MainMenu():

    """
    La clase del menú principal

    El menú principal solo se ve durante el primer inicio del juego
    después del segundo arranque este no volvera a verse (Siempre y cuando
    se haya despedido correctamente de Tojiko.)
    
    """
    
    def __init__(self):
        
        self.bg = pygame.image.load(f"{config.images_dir}/bg_menu.png").convert_alpha()

        self.logo_img = pygame.image.load(f"{config.images_dir}/logo.png").convert_alpha()
        self.logo_scale = 0.3

        self.logo = pygame.transform.scale(self.logo_img, [self.logo_img.get_width() * self.logo_scale, self.logo_img.get_height() * self.logo_scale])
        self.rect = self.logo.get_rect()

        self.white_img = pygame.image.load(f"{config.images_dir}/white.png").convert()
        self.white_img_alpha_value = 255

        self.button_new_game = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[MainMenu_text[0], "VarelaRound.ttf", 20, "#000000", True, [25, 4], f"{config.fonts_dir}/"])
        # self.button_config = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[MainMenu_text[1], "VarelaRound.ttf", 20, "#000000", True, [20, 4], f"{config.fonts_dir}/"])
        self.button_exit = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[MainMenu_text[2], "VarelaRound.ttf", 20, "#000000", True, [30, 4], f"{config.fonts_dir}/"])

        self.pg_version = lenpy.Text(f"Pygame {pygame.version.ver}", "lucon.ttf", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.tojiko_version = lenpy.Text(f"Virtual-Date_{config.version}-alpha", "lucon.ttf", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        
        self.s_pressed = False

        self.to_game = False
        self.counter_to_game = 0

    def Screen(self):

        # antialiasing?

        if config.set_antialiasing:

            self.logo = pygame.transform.smoothscale(self.logo_img, [self.logo_img.get_width() * self.logo_scale, self.logo_img.get_height() * self.logo_scale])
        
        else:

            self.logo = pygame.transform.scale(self.logo_img, [self.logo_img.get_width() * self.logo_scale, self.logo_img.get_height() * self.logo_scale])

        # cambiar valor alpha

        self.white_img.set_alpha(self.white_img_alpha_value)

        # efecto de transición alpha entrada

        if self.white_img_alpha_value > 0 and not self.to_game:

            self.white_img_alpha_value -= 5

        elif self.white_img_alpha_value == 0 and not self.to_game:

            self.white_img_alpha_value = 0

        elif self.white_img_alpha_value == 0 and self.to_game:

            self.white_img_alpha_value += 5

        elif self.white_img_alpha_value < 255 and self.to_game:

            self.white_img_alpha_value += 5

        elif self.white_img_alpha_value == 255 and self.to_game:

            self.counter_to_game += 1
            config.current_screen = "MainMenu"
            configscreen.configscreen_main.button_config.disable = True

        if self.counter_to_game >= 40:

            config.current_screen = "Game"

        # redefine la pantalla

        surf = pygame.transform.scale(config.canvas, config.canvas_size)
        config.screen.fill(config.BLACK)
        config.screen.blit(surf, config.canvas_pos)

        config.canvas.fill(config.WHITE)

        self.rect.center = (500, 80) # configura el centro del logo

        config.canvas.blit(self.bg, [0, 0])
        config.canvas.blit(self.logo, self.rect)

        # print(config.current_screen, self.counter_to_game)
        
        # Botones

        key = pygame.key.get_pressed()

        if key[pygame.K_s] == 1 and not self.s_pressed:

            screenshot_f.take_screenshot_quick()
            self.s_pressed = True

        elif key[pygame.K_s] == 0 and self.s_pressed:

            self.s_pressed = False

        if self.button_new_game.draw(config.canvas, 430, 250, 1.0, config.set_antialiasing) and not self.to_game and config.current_screen == "MainMenu":

            self.to_game = True
            self.button_new_game.disable = True
            self.button_exit.disable = True
            configscreen.configscreen_main.button_config.disable = True

        #self.button_config.draw(config.canvas, 430, 290, 1.0, config.set_antialiasing)
        #self.button_exit.draw(config.canvas, 430, 330, 1.0, config.set_antialiasing)

        if self.button_exit.draw(config.canvas, 430, 330, 1.0, config.set_antialiasing) and config.current_screen == "MainMenu":

            pygame.quit()
            config.data_manager.Save_game_data([config.default_data], ["tojiko"])
            sys.exit()

        ## versiones
        self.pg_version.draw(config.canvas, 5, 470)
        self.tojiko_version.draw(config.canvas, 5, 490)

        #

        configscreen.configscreen_main.draw_button(config.set_antialiasing)

        # otros

        config.notify_counter()
        config.notify.notify(config.notify_message, config.notify_visibility)
        config.display_fps(config.show_fps_counter)

        # Blanco
        config.canvas.blit(self.white_img, [0, 0])

m_menu = MainMenu()
