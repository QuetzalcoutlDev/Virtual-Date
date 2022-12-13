
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

from source.ui_text import music_texts

###################################
# Pantalla de selección de música
###################################

class MusicSelector():
    
    def __init__(self):
        
        self.visible = False
        self.music_list = ["Relation.ogg", "Hikara.ogg", "Sad.ogg"] # Lista de músicas disponibles.

        self.button_music_selector = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[music_texts[0], "VarelaRound.ttf", 19, "#000000", True, [19, 4], f"{config.fonts_dir}/"])
        self.music_selector_box = pygame.image.load(f"{config.images_dir}/music_selector_box.png").convert_alpha()
        
        self.ms_box_x = 160
        self.ms_box_y = 40

        self.button_music_selector_clicked = False
        self.music_selector_screen_show = False

        self.title = lenpy.Text(music_texts[0], "ARLRDBD.TTF", 34, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.music = lenpy.ui.TextButton("Boton", "ARLRDBD.TTF", 24, "#302f2f", "#8a8888", "#000000", True, font_dir=f"{config.fonts_dir}/", sysfont=False)

        self.music_Stop_button = lenpy.ui.TextButton(music_texts[1], "VarelaRound.ttf", 22, "#302f2f", "#8a8888", "#000000", "stop_music", font_dir=f"{config.fonts_dir}/", sysfont=False)
    
        self.antialiasing = False

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        self.button_music_selector.draw(config.canvas, 28, 424, 1.0, self.antialiasing)

        if not config.current_screen == "musicSelector" and not config.current_screen == "Game":
            self.button_music_selector.disable = True

        elif config.current_screen == "Game":
            self.button_music_selector.disable = False

        if self.button_music_selector.draw(config.canvas, 28, 424, 1.0, self.antialiasing) and not self.button_music_selector_clicked and not self.music_selector_screen_show and not config.current_screen == "musicSelector":

            self.button_music_selector_clicked = True
            self.music_selector_screen_show = True

            # print("click")

        elif not self.button_music_selector.draw(config.canvas, 28, 424, 1.0, self.antialiasing) and self.button_music_selector_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_music_selector_clicked = False

        if self.button_music_selector.draw(config.canvas, 28, 424, 1.0, self.antialiasing) and not self.button_music_selector_clicked and self.music_selector_screen_show and config.current_screen == "musicSelector":

            self.button_music_selector_clicked = True
            self.music_selector_screen_show = False
            config.current_screen = config.current_screen_default     
            # print("click")

        elif not self.button_music_selector.draw(config.canvas, 28, 424, 1.0, self.antialiasing) and self.button_music_selector_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_music_selector_clicked = False

        if self.music_selector_screen_show:

            config.current_screen = "musicSelector"
            self.Screen(True)

        else:

            self.Screen(False)

    def Screen(self, visible):
        
        self.visible = visible

        # Solo será permitido cambiar la música si la caja de texto no esta visible.
        # Esto se aplica para todas las pantallas.

        if self.visible and not getattr(textbox.tbox, "visible_box"):

            # config.screen.fill(config.GRAY, [0, 0, config.canvas_size[0], config.canvas_size[1]], pygame.BLEND_RGBA_MIN)
            #pygame.draw.rect(config.canvas, config.RED, [self.ms_box_x, self.ms_box_y, 416, 433])

            config.canvas.blit(config.black_in_screen, [0, 0])

            config.canvas.blit(self.music_selector_box, [self.ms_box_x, self.ms_box_y])

            # print(config.canvas_size[0] / 2.4, config.canvas_size[1] / 1.2)

            self.title.draw(config.canvas, self.ms_box_x * 1.9, self.ms_box_y * 1.45)
            self.music_Stop_button.draw(config.canvas, self.ms_box_x * 2.9, self.ms_box_y * 1.5)

            music_list_y = 2.6

            for files in self.music_list:

                # self.music = lenpy.ui.TextButton(files, "Varela Round", 30, "#302f2f", "#8a8888", "#000000", f"play:{config.music_dir}/{files}", sysfont=True)
                
                name = files.strip(".ogg")

                self.music = lenpy.ui.TextButton(name, "ARLRDBD.TTF", 24, "#302f2f", "#8a8888", "#000000", True, font_dir=f"{config.fonts_dir}/", sysfont=False)

                self.music.draw(config.canvas, self.ms_box_x * 1.2, self.ms_box_y * music_list_y)

                if self.music.draw(config.canvas, self.ms_box_x * 1.2, self.ms_box_y * music_list_y):

                    lenpy.ui.UIaction(f"play:{config.music_dir}/{files}")
                    config.default_data["game_music"] = files

                music_list_y += 0.8

musicselector = MusicSelector()