
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
from source import config, textbox, con_themes

from source import ui_text
from source.ui_text import config_screen_texts, MainMenu_text, change_language

from source.dialog_box import dialog

###############################
## Pantalla de Configuración ##
###############################

class configScreen():
    
    """
    Está es la clase de la pantalla de configuración durante el juego
    Quizas el código es demasiado largo para tener tan pocas opciones.

    El check de pantalla completa está deshabilitado por defecto debido
    a que el juego no cuenta con el redimensionado de los graficos y recalculado 
    de las posiciones(No habia tiempo).
    """

    def __init__(self):

        self.visible = False

        self.cs_box_x = config.canvas_size[0] // 4.5
        self.cs_box_y = 40

        self.button_configscreen = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/config_button_normal.png", f"{config.images_dir}/buttons/config_button_hover.png", f"{config.images_dir}/buttons/config_button_select.png", True, f"{config.images_dir}/buttons/config_button_disable.png")
        self.button_configscreen_exit = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/exit_button_normal.png", f"{config.images_dir}/buttons/exit_button_hover.png", f"{config.images_dir}/buttons/exit_button_select.png", True, f"{config.images_dir}/buttons/exit_button_disable.png")

        self.config_box = pygame.image.load(f"{config.images_dir}/config_box.png").convert_alpha()
        
        self.configscreen_button_clicked = False
        self.configscreen_button_clicked_exit = False
        
        self.configscreen_show = False

        self.title = lenpy.Text(config_screen_texts[0], "VarelaRound.ttf", 30, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        ### Titulos pantalla

        self.screen_title = lenpy.Text(config_screen_texts[1], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.fullscreen_title = lenpy.Text(config_screen_texts[2], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.antialiasing_title = lenpy.Text(config_screen_texts[3], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        ### Titulos lenguaje
        
        self.language = lenpy.Text(config_screen_texts[4], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        #self.available_languages = ["Español", "English"]
        self.available_languages = [config_screen_texts[5], config_screen_texts[6]]

        self.available_languages_codes = ["es", "en"]

        ### Titulos sonido

        self.sound_title = lenpy.Text(config_screen_texts[7], "ARLRDBD.TTF", 23, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        self.music_volume_title = lenpy.Text(config_screen_texts[8], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.music_volume_value = lenpy.Text(str(config.music_volume), "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        
        self.sfx_volume_title = lenpy.Text(config_screen_texts[9], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.sfx_volume_value = lenpy.Text(str(config.sfx_volume), "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        
        ### Titulos gameplay

        self.gameplay_title = lenpy.Text(config_screen_texts[10], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.fps_counter_title = lenpy.Text(config_screen_texts[11], "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        ##############
        ### Checks ###
        ##############

        self.dci = f"{config.images_dir}/buttons/check_button_"
        self.dcoi = f"{config.images_dir}/buttons/check_on_button_"

        ##########################
        ### Checks de pantalla ###
        ##########################

        self.fullscreen_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        self.fullscreen_check_on = False

        self.antialiasing_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        self.antialiasing_check_on = False

        ### Habilitar los check según.... ###

        # Pantalla completa

        if config.screen_type == "window":

            self.fullscreen_check.check = False

        elif config.screen_type == "fullscreen":

            self.fullscreen_check.check = True

        # Antialiasing

        if not config.set_antialiasing:

            self.antialiasing_check.check = False

        elif config.set_antialiasing:

            self.antialiasing_check.check = True

        ##########################################
        ### Botones de configuración de sonido ###
        ##########################################

        self.music_volume_button_plus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_plus_normal.png", f"{config.images_dir}/buttons/button_plus_hover.png", f"{config.images_dir}/buttons/button_plus_select.png", True, f"{config.images_dir}/buttons/button_plus_disable.png")
        self.music_volume_button_minus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_minus_normal.png", f"{config.images_dir}/buttons/button_minus_hover.png", f"{config.images_dir}/buttons/button_minus_select.png", True, f"{config.images_dir}/buttons/button_minus_disable.png")

        self.music_volume_buttons_clicked = False
        
        self.sfx_volume_button_plus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_plus_normal.png", f"{config.images_dir}/buttons/button_plus_hover.png", f"{config.images_dir}/buttons/button_plus_select.png", True, f"{config.images_dir}/buttons/button_plus_disable.png")
        self.sfx_volume_button_minus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_minus_normal.png", f"{config.images_dir}/buttons/button_minus_hover.png", f"{config.images_dir}/buttons/button_minus_select.png", True, f"{config.images_dir}/buttons/button_minus_disable.png")

        self.sfx_volume_buttons_clicked = False
        
        self.music_value = config.music_volume
        self.sfx_value = config.sfx_volume
        
        self.sound_channel = pygame.mixer.Channel(2)

        self.mute_all = lenpy.ui.TextButton(config_screen_texts[12], "VarelaRound.ttf", 20, "#302f2f", "#8a8888", "#000000", True, font_dir=f"{config.fonts_dir}/", sysfont=False)

        ##########################
        ### Checks de pantalla ###
        ##########################

        self.fps_counter_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        
        ### Habilitar los check según.... ###

        # Pantalla completa

        if not config.show_fps_counter:

            self.fps_counter_check.check = False

        elif config.show_fps_counter:

            self.fps_counter_check.check = True

        self.antialiasing = False

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        # self.button_configscreen.draw(config.canvas, 940, 13, 0.7, self.antialiasing)

        # Deshabilita los botones para mostrar la pantalla de configuración si...
        
        if not config.current_screen == "ConfigScreen" and not config.current_screen == "Game":
            self.button_configscreen.disable = True

        elif config.current_screen == "Game":
            self.button_configscreen.disable = False

        elif config.current_screen == "ConfigScreen" and self.configscreen_show:
            self.button_configscreen.disable = True

        # Estas condiciones son para poder mostrar la pantalla de configuración si se hace clic.

        if self.button_configscreen.draw(config.canvas, 950, 13, 0.9, self.antialiasing) and not self.configscreen_button_clicked and not config.current_screen == "ConfigScreen":

            self.configscreen_show = True
            self.configscreen_button_clicked = True

        elif not self.button_configscreen.draw(config.canvas, 950, 13, 0.9, self.antialiasing) and self.configscreen_button_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.configscreen_button_clicked = False

        ##############################################################
        ## Cuando la pantalla de configuración es visible, entonces...

        if self.configscreen_show:

            config.current_screen = "ConfigScreen"
            
            self.Screen(True)
            
            # self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 10, 0.7, self.antialiasing)

            # Este es el botón de salida de la pantalla

            if self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 3, 0.95, self.antialiasing) and not self.configscreen_button_clicked_exit:
                
                self.configscreen_button_clicked_exit = True
                self.configscreen_show = False
                config.current_screen = config.current_screen_default 

            elif not self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 3, 0.95, self.antialiasing) and self.configscreen_button_clicked_exit and pygame.mouse.get_pressed()[0] == 0:

                self.configscreen_button_clicked_exit = False

        else:

            self.Screen(False)

    #################################
    ### Pantalla de configuración ###
    #################################

    def Screen(self, visible):

        self.visible = visible

        if self.visible and not getattr(textbox.tbox, "visible_box"):

            # config.screen.fill(config.GRAY, [0, 0, config.canvas_size[0], config.canvas_size[1]], pygame.BLEND_RGBA_MIN)
            #pygame.draw.rect(config.canvas, config.RED, [self.cs_box_x, self.cs_box_y, 560, 433.3])

            config.canvas.blit(config.black_in_screen, [0, 0])

            config.canvas.blit(self.config_box, [self.cs_box_x, self.cs_box_y])

            self.title.draw(config.canvas, self.cs_box_x * 1.8, self.cs_box_y * 1.5)

            ###################################
            #### Configuración de pantalla ####
            ###################################

            self.screen_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 2.6)

            self.fullscreen_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 4.2)
            self.antialiasing_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 5.0)
            
            self.fullscreen_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 4.1, 0.7, self.antialiasing)
            self.fullscreen_check.disable = True
            self.antialiasing_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 4.9, 0.7, self.antialiasing)

            ## Check pantalla completa

            if self.fullscreen_check.check == True:

                config.screen_type = "fullscreen"
                config.default_data["screen_type"] = "fullscreen"
                
                if self.fullscreen_check_on:

                    config.screen = lenpy.config.set_display(config.screen_size, True, False)
                    self.fullscreen_check_on = False

            elif self.fullscreen_check.check == False:

                config.screen_type = "window"
                config.default_data["screen_type"] = "window"
                
                if not self.fullscreen_check_on:

                    config.screen = lenpy.config.set_display(config.screen_size, resizable=False)
                    self.fullscreen_check_on = True

            ## Check antialiasing

            if self.antialiasing_check.check == True:

                config.set_antialiasing = True
                config.default_data["antialiasing"] = True

            elif self.antialiasing_check.check == False:

                config.set_antialiasing = False
                config.default_data["antialiasing"] = False
                
            ###################################
            #### Configuración de lenguaje ####
            ###################################

            self.language.draw(config.canvas, self.cs_box_x * 1.9, self.cs_box_y * 2.6)

            language_title_y = 4.15

            lan_index = 0

            for lan in self.available_languages:

                language_button = lenpy.ui.TextButton(lan, "ARLRDBD.TTF", 20, "#302f2f", "#8a8888", "#000000", True, font_dir=f"{config.fonts_dir}/", sysfont=False)
                
                if language_button.draw(config.canvas, self.cs_box_x * 1.9, self.cs_box_y * language_title_y):

                    config.default_data["language"] = self.available_languages_codes[lan_index]
                    
                    if config.default_data["language"] == self.available_languages_codes[lan_index] and config.current_language != self.available_languages_codes[lan_index]:

                        dialog(change_language, "quit")

                    else:
                        
                        pass

                language_title_y += 0.85

                if not lan_index == 1:
                    
                    lan_index += 1

            ###################################
            #### Configuración de sonido   ####
            ###################################

            #### Dibujar botones y titulos ####

            """
            Si es demasiado código para solo subir y bajar volumen.

            """

            self.sound_title.draw(config.canvas, self.cs_box_x * 2.6, self.cs_box_y * 2.6)
            self.music_volume_title.draw(config.canvas, self.cs_box_x * 2.6, self.cs_box_y * 4.2)
            self.sfx_volume_title.draw(config.canvas, self.cs_box_x * 2.6, self.cs_box_y * 5.0)

            self.music_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 4.2, 0.7, self.antialiasing)
            self.music_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 4.2, 0.7, self.antialiasing)

            self.sfx_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 5.0, 0.7, self.antialiasing)
            self.sfx_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 5.0, 0.7, self.antialiasing)

            self.music_volume_value.draw(config.canvas, self.cs_box_x * 3.23, self.cs_box_y * 4.32)
            self.sfx_volume_value.draw(config.canvas, self.cs_box_x * 3.23, self.cs_box_y * 5.08)

            ### Subir-bajar volumen de música

            if self.music_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 4.2, 0.7, self.antialiasing) and not self.music_volume_buttons_clicked and self.music_value < 1.0:

                self.music_value += 0.1

                pygame.mixer.music.set_volume(self.music_value)
                config.default_data["music_volume"] = self.music_value
                self.music_volume_buttons_clicked = True

            elif not self.music_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 4.2, 0.7, self.antialiasing) and self.music_volume_buttons_clicked and pygame.mouse.get_pressed()[0] == 0:

                self.music_volume_buttons_clicked = False

            if self.music_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 4.2, 0.7, self.antialiasing) and not self.music_volume_buttons_clicked and self.music_value > 0.0:

                self.music_value -= 0.1
                
                pygame.mixer.music.set_volume(self.music_value)
                config.default_data["music_volume"] = self.music_value
                self.music_volume_buttons_clicked = True

            elif not self.music_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 4.2, 0.7, self.antialiasing) and self.music_volume_buttons_clicked and pygame.mouse.get_pressed()[0] == 0:

                self.music_volume_buttons_clicked = False

            if self.music_value >= 1.0:

                self.music_value = 1.0
                self.music_volume_button_plus.disable = True
                
                pygame.mixer.music.set_volume(1.0)
                config.default_data["music_volume"] = 1.0
                self.music_volume_buttons_clicked = False

            else:

                self.music_volume_button_plus.disable = False

            if self.music_value < 0.1:

                self.music_value = 0.0
                self.music_volume_button_minus.disable = True
                config.music_volume = 0.0
                
                pygame.mixer.music.set_volume(0.0)
                config.default_data["music_volume"] = 0.0
                self.music_volume_buttons_clicked = False

            else:

                self.music_volume_button_minus.disable = False


            ### Subir-bajar volumen de sonido

            if self.sfx_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 5.0, 0.7, self.antialiasing) and not self.sfx_volume_buttons_clicked and self.sfx_value < 1.0:

                self.sfx_value += 0.1

                self.sound_channel.set_volume(self.sfx_value)

                config.default_data["sfx_volume"] = self.sfx_value
                self.sfx_volume_buttons_clicked = True

            elif not self.sfx_volume_button_plus.draw(config.canvas, self.cs_box_x * 3.35, self.cs_box_y * 5.0, 0.7, self.antialiasing) and self.sfx_volume_buttons_clicked and pygame.mouse.get_pressed()[0] == 0:

                self.sfx_volume_buttons_clicked = False

            if self.sfx_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 5.0, 0.7, self.antialiasing) and not self.sfx_volume_buttons_clicked and self.sfx_value > 0.0:

                self.sfx_value -= 0.1
                
                self.sound_channel.set_volume(self.sfx_value)

                config.default_data["sfx_volume"] = self.sfx_value
                self.sfx_volume_buttons_clicked = True

            elif not self.sfx_volume_button_minus.draw(config.canvas, self.cs_box_x * 3.10, self.cs_box_y * 5.0, 0.7, self.antialiasing) and self.sfx_volume_buttons_clicked and pygame.mouse.get_pressed()[0] == 0:

                self.sfx_volume_buttons_clicked = False

            if self.sfx_value >= 1.0:

                self.sfx_value = 1.0
                self.sfx_volume_button_plus.disable = True
                
                self.sound_channel.set_volume(1.0)

                config.default_data["sfx_volume"] = 1.0
                self.sfx_volume_buttons_clicked = False

            else:

                self.sfx_volume_button_plus.disable = False

            if self.sfx_value < 0.1:

                self.sfx_value = 0.0
                self.sfx_volume_button_minus.disable = True
                config.sfx_volume = 0.0
                
                self.sound_channel.set_volume(0.0)

                config.default_data["sfx_volume"] = 0.0
                self.sfx_volume_buttons_clicked = False

            else:

                self.sfx_volume_button_minus.disable = False

            ## Mutear todo ##

            self.mute_all.draw(config.canvas, self.cs_box_x * 2.6, self.cs_box_y * 6.0)

            if self.mute_all.draw(config.canvas, self.cs_box_x * 2.6, self.cs_box_y * 6.0):

                self.music_value = 0.0
                self.sfx_value = 0.0
                pygame.mixer.music.set_volume(0.0)

                self.sound_channel.set_volume(0.0)

                config.default_data["music_volume"] = 0.0
                config.default_data["sfx_volume"] = 0.0

            # Este código es para que la cantidad de digitos mostrada en el volumen de la música sea 0.0, no 0.000, osea solo 3
            # digitos.

            music_value_str = str(self.music_value)
            sfx_value_str = str(self.sfx_value)

            # Que los digitos del medidor de volumen de la música no sean más de 3 digitos

            if len(music_value_str) > 3:

                music_value_str_3_digits = music_value_str[0:3]

            else:

                music_value_str_3_digits = music_value_str[0:3]

            # Lo mismo pero con el sonido

            if len(sfx_value_str) > 3:

                sfx_value_str_3_digits = sfx_value_str[0:3]

            else:

                sfx_value_str_3_digits = sfx_value_str[0:3]

            config.music_volume = music_value_str_3_digits
            config.sfx_volume = sfx_value_str_3_digits

            self.music_volume_value = lenpy.Text(str(config.music_volume), "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
            self.sfx_volume_value = lenpy.Text(str(config.sfx_volume), "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

            # print(self.music_value)

            ###################################
            #### Configuración de gameplay ####
            ###################################

            # Esto iba a ir en su propio apartado pero se coloco en el de pantalla

            #### self.gameplay_title.draw(config.canvas, self.cs_box_x * 4.2, self.cs_box_y * 2.6)

            #### self.fps_counter_title.draw(config.canvas, self.cs_box_x * 4.2, self.cs_box_y * 4.2)
            #### self.fps_counter_check.draw(config.canvas, self.cs_box_x * 4.85, self.cs_box_y * 4.08, 0.7, self.antialiasing)

            self.fps_counter_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 6.0)
            self.fps_counter_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 5.75, 0.7, self.antialiasing)

            ## Check contador de FPS

            if self.fps_counter_check.check == True:

                config.show_fps_counter = True
                config.default_data["show_fps_counter"] = True

            elif self.fps_counter_check.check == False:

                config.show_fps_counter = False
                config.default_data["show_fps_counter"] = False

class configScreenMain():
    """
    La clase para la configuración en el menú principal
    Es basicamente lo mismo que en el juego en sí.

    Pero solo se ve una vez.
    """
    
    def __init__(self):
        
        self.visible = False

        self.cs_box_x = config.canvas_size[0] // 4.5
        self.cs_box_y = 40

        self.button_config = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[MainMenu_text[1], "VarelaRound.ttf", 20, "#000000", True, [20, 4], f"{config.fonts_dir}/"])
        self.button_configscreen_exit = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/exit_button_normal.png", f"{config.images_dir}/buttons/exit_button_hover.png", f"{config.images_dir}/buttons/exit_button_select.png", True, f"{config.images_dir}/buttons/exit_button_disable.png")

        self.config_box = pygame.image.load(f"{config.images_dir}/config_box.png").convert_alpha()
        
        self.configscreen_button_clicked = False
        self.configscreen_button_clicked_exit = False
        
        self.configscreen_show = False

        self.title = lenpy.Text(config_screen_texts[0], "VarelaRound.ttf", 30, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        ### Titulos pantalla

        self.screen_title = lenpy.Text(config_screen_texts[1], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.fullscreen_title = lenpy.Text(config_screen_texts[2], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.antialiasing_title = lenpy.Text(config_screen_texts[3], "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        ### Titulos lenguaje
        
        self.language = lenpy.Text(config_screen_texts[4], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        #self.available_languages = ["Español", "English"]
        self.available_languages = [config_screen_texts[5], config_screen_texts[6]]
        self.available_languages_codes = ["es", "en"]

        ###

        self.gameplay_title = lenpy.Text(config_screen_texts[10], "ARLRDBD.TTF", 25, f"{config.fonts_dir}/", config.BLACK, sysfont=False)
        self.fps_counter_title = lenpy.Text(config_screen_texts[11], "ARLRDBD.TTF", 15, f"{config.fonts_dir}/", config.BLACK, sysfont=False)

        self.dci = f"{config.images_dir}/buttons/check_button_"
        self.dcoi = f"{config.images_dir}/buttons/check_on_button_"

        ##########################
        ### Checks de pantalla ###
        ##########################

        self.fullscreen_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        self.fullscreen_check_on = False

        self.antialiasing_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        self.antialiasing_check_on = False

        ### Habilitar los check según.... ###

        # Pantalla completa

        if config.screen_type == "window":

            self.fullscreen_check.check = False

        elif config.screen_type == "fullscreen":

            self.fullscreen_check.check = True

        # Antialiasing

        if not config.set_antialiasing:

            self.antialiasing_check.check = False

        elif config.set_antialiasing:

            self.antialiasing_check.check = True
        
        ##########################
        ### Checks de pantalla ###
        ##########################

        self.fps_counter_check = lenpy.ui.CheckButton(self.dci + "normal.png", self.dci + "hover.png", self.dci + "select.png", self.dcoi + "normal.png", self.dcoi + "hover.png", self.dcoi + "select.png", self.dci + "disable.png", self.dcoi + "disable.png")
        
        ### Habilitar los check según.... ###

        # Pantalla completa

        if not config.show_fps_counter:

            self.fps_counter_check.check = False

        elif config.show_fps_counter:

            self.fps_counter_check.check = True

        self.antialiasing = False

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        # self.button_configscreen.draw(config.canvas, 940, 13, 0.7, self.antialiasing)

        # Deshabilita los botones para mostrar la pantalla de configuración si...
        
        if not config.current_screen == "ConfigScreenMain" and not config.current_screen == "MainMenu":
            self.button_config.disable = True

        elif config.current_screen == "MainMenu":
            self.button_config.disable = False

        elif config.current_screen == "ConfigScreenMain" and self.configscreen_show:
            self.button_config.disable = True

        # Estas condiciones son para poder mostrar la pantalla de configuración si se hace clic.

        if self.button_config.draw(config.canvas, 430, 290, 1.0, config.set_antialiasing) and not self.configscreen_button_clicked and not config.current_screen == "ConfigScreen":

            self.configscreen_show = True
            self.configscreen_button_clicked = True

        elif not self.button_config.draw(config.canvas, 430, 290, 1.0, config.set_antialiasing) and self.configscreen_button_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.configscreen_button_clicked = False

        ##############################################################
        ## Cuando la pantalla de configuración es visible, entonces...

        if self.configscreen_show:

            config.current_screen = "ConfigScreenMain"
            
            self.Screen(True)
            
            # self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 10, 0.7, self.antialiasing)

            # Este es el botón de salida de la pantalla

            if self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 3, 0.95, self.antialiasing) and not self.configscreen_button_clicked_exit:
                
                self.configscreen_button_clicked_exit = True
                self.configscreen_show = False
                config.current_screen = "MainMenu"

            elif not self.button_configscreen_exit.draw(config.canvas, self.cs_box_x * 3.35, 3, 0.95, self.antialiasing) and self.configscreen_button_clicked_exit and pygame.mouse.get_pressed()[0] == 0:

                self.configscreen_button_clicked_exit = False

        else:

            self.Screen(False)

    ###########################################
    ### Pantalla de configuración principal ###
    ###########################################

    def Screen(self, visible):

        self.visible = visible

        if self.visible:

            # config.screen.fill(config.GRAY, [0, 0, config.canvas_size[0], config.canvas_size[1]], pygame.BLEND_RGBA_MIN)
            #pygame.draw.rect(config.canvas, config.RED, [self.cs_box_x, self.cs_box_y, 560, 433.3])

            config.canvas.blit(config.black_in_screen, [0, 0])

            config.canvas.blit(self.config_box, [self.cs_box_x, self.cs_box_y])

            self.title.draw(config.canvas, self.cs_box_x * 1.8, self.cs_box_y * 1.5)

            ###################################
            #### Configuración de pantalla ####
            ###################################

            self.screen_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 2.6)

            self.fullscreen_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 4.2)
            self.antialiasing_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 5.0)
            
            self.fullscreen_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 4.1, 0.7, self.antialiasing)
            self.fullscreen_check.disable = True
            self.antialiasing_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 4.9, 0.7, self.antialiasing)

            ## Check pantalla completa

            if self.fullscreen_check.check == True:

                config.screen_type = "fullscreen"
                config.default_data["screen_type"] = "fullscreen"
                
                if self.fullscreen_check_on:

                    config.screen = lenpy.config.set_display(config.screen_size, True, False)
                    self.fullscreen_check_on = False

            elif self.fullscreen_check.check == False:

                config.screen_type = "window"
                config.default_data["screen_type"] = "window"
                
                if not self.fullscreen_check_on:

                    config.screen = lenpy.config.set_display(config.screen_size, resizable=False)
                    self.fullscreen_check_on = True

            ## Check antialiasing

            if self.antialiasing_check.check == True:

                config.set_antialiasing = True
                config.default_data["antialiasing"] = True

            elif self.antialiasing_check.check == False:

                config.set_antialiasing = False
                config.default_data["antialiasing"] = False
                
            ###################################
            #### Configuración de lenguaje ####
            ###################################

            self.language.draw(config.canvas, self.cs_box_x * 1.9, self.cs_box_y * 2.6)

            language_title_y = 4.15

            lan_index = 0

            for lan in self.available_languages:

                language_button = lenpy.ui.TextButton(lan, "ARLRDBD.TTF", 20, "#302f2f", "#8a8888", "#000000", True, font_dir=f"{config.fonts_dir}/", sysfont=False)
                
                if language_button.draw(config.canvas, self.cs_box_x * 1.9, self.cs_box_y * language_title_y):

                    config.default_data["language"] = self.available_languages_codes[lan_index]
                    
                    if config.default_data["language"] == self.available_languages_codes[lan_index] and config.current_language != self.available_languages_codes[lan_index]:

                        dialog(change_language, "quit")

                    else:
                        
                        pass

                language_title_y += 0.85

                if not lan_index == 1:
                    
                    lan_index += 1

            ###################################
            #### Configuración de gameplay ####
            ###################################

            # Esto iba a ir en su propio apartado pero se coloco en el de pantalla

            #### self.gameplay_title.draw(config.canvas, self.cs_box_x * 4.2, self.cs_box_y * 2.6)

            #### self.fps_counter_title.draw(config.canvas, self.cs_box_x * 4.2, self.cs_box_y * 4.2)
            #### self.fps_counter_check.draw(config.canvas, self.cs_box_x * 4.85, self.cs_box_y * 4.08, 0.7, self.antialiasing)

            self.fps_counter_title.draw(config.canvas, self.cs_box_x * 1.1, self.cs_box_y * 6.0)
            self.fps_counter_check.draw(config.canvas, self.cs_box_x * 1.6, self.cs_box_y * 5.75, 0.7, self.antialiasing)

            ## Check contador de FPS

            if self.fps_counter_check.check == True:

                config.show_fps_counter = True
                config.default_data["show_fps_counter"] = True

            elif self.fps_counter_check.check == False:

                config.show_fps_counter = False
                config.default_data["show_fps_counter"] = False

configscreen = configScreen()
configscreen_main = configScreenMain()