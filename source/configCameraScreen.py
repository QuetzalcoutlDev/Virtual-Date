
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

from source.ui_text import camera_texts

##########################################
## Pantalla de configuración de camara ###
##########################################

class configCamera():

    def __init__(self):
        
        self.visible = False
        self.zoom_scale_value = config.zoom_scale_value_default

        self.zoom_button_plus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_plus_normal.png", f"{config.images_dir}/buttons/button_plus_hover.png", f"{config.images_dir}/buttons/button_plus_select.png", True, f"{config.images_dir}/buttons/button_plus_disable.png")
        self.zoom_button_minus = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/button_minus_normal.png", f"{config.images_dir}/buttons/button_minus_hover.png", f"{config.images_dir}/buttons/button_minus_select.png", True, f"{config.images_dir}/buttons/button_minus_disable.png")

        self.zoom_box = pygame.image.load(f"{config.images_dir}/zoom_box.png").convert_alpha()
        
        self.title = lenpy.Text(camera_texts[0], "ARLRDBD.TTF", 18, f"{config.fonts_dir}", config.BLACK, sysfont=False)

        self.cc_box_x = 160
        self.cc_box_y = 400

        self.cc_w = 109
        self.cc_h = 100

        self.button_camera = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[camera_texts[1], "VarelaRound.ttf", 19, "#000000", True, [19, 4], f"{config.fonts_dir}/"])

        self.clicked = False

        self.button_camera_clicked = False
        self.configcamera_screen_show = False

        self.antialiasing = False

        # Esto permite un control sobre el zoom_scale_value, lo que permitira que otras partes del juego puedan manipular la 
        # variable

        # Todas estas configuraciones de la escala y las posiciones de Tojiko y del BG, fueron calculadas por lo que si la posición
        # de Tojiko o la escala por defecto cambian, entonces hay que recalcular todo de nuevo.

        if self.zoom_scale_value == -1:

            config.tojiko.scale = 0.2799999999999998
            config.tojiko_bg_y = 282.0
            config.bg_x = -100
            config.bg.bg_scale = 0.284

        elif self.zoom_scale_value == 0:

            config.tojiko.scale = 0.30699999999999983
            config.tojiko_bg_y = 306.0
            config.bg_x = -130
            config.bg.bg_scale = 0.302

        elif self.zoom_scale_value == 1:

            config.tojiko.scale = 0.33399999999999985
            config.tojiko_bg_y = 330.0
            config.bg_x = -160
            config.bg.bg_scale = 0.32

        elif self.zoom_scale_value == 2:

            config.tojiko.scale = 0.3609999999999999
            config.tojiko_bg_y = 354.0
            config.bg_x = -190
            config.bg.bg_scale = 0.338

        elif self.zoom_scale_value == 3:

            config.tojiko.scale = 0.3879999999999999
            config.tojiko_bg_y = 378.0
            config.bg_x = -220
            config.bg.bg_scale = 0.35600000000000004

        elif self.zoom_scale_value == 4:

            config.tojiko.scale = 0.4149999999999999
            config.tojiko_bg_y = 402.0
            config.bg_x = -250
            config.bg.bg_scale = 0.37400000000000005

        elif self.zoom_scale_value == 5:

            config.tojiko.scale = 0.44199999999999995
            config.tojiko_bg_y = 426.0
            config.bg_x = -280
            config.bg.bg_scale = 0.39200000000000007

        elif self.zoom_scale_value == 6:

            config.tojiko.scale = 0.469
            config.tojiko_bg_y = 450.0
            config.bg_x = -310
            config.bg.bg_scale = 0.4100000000000001

        elif self.zoom_scale_value == 7:

            config.tojiko.scale = 0.496
            config.tojiko_bg_y = 474.0
            config.bg_x = -340
            config.bg.bg_scale = 0.4280000000000001

        elif self.zoom_scale_value == 8:

            config.tojiko.scale = 0.523
            config.tojiko_bg_y = 498.0
            config.bg_x = -370
            config.bg.bg_scale = 0.4460000000000001

        elif self.zoom_scale_value == 9:

            config.tojiko.scale = 0.55
            config.tojiko_bg_y = 522.0 
            config.bg_x = -400
            config.bg.bg_scale = 0.46400000000000013

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        self.button_camera.draw(config.canvas, 28, 470, 1.0, self.antialiasing)
    
        if not config.current_screen == "configCamera" and not config.current_screen == "Game":
            self.button_camera.disable = True

        elif config.current_screen == "Game":
            self.button_camera.disable = False

        if self.button_camera.draw(config.canvas, 28, 470, 1.0, self.antialiasing) and not self.button_camera_clicked and not self.configcamera_screen_show and not config.current_screen == "configCamera":

            self.button_camera_clicked = True
            self.configcamera_screen_show = True

            # print("click")

        elif not self.button_camera.draw(config.canvas, 28, 470, 1.0, self.antialiasing) and self.button_camera_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_camera_clicked = False
            
        if self.button_camera.draw(config.canvas, 28, 470, 1.0, self.antialiasing) and not self.button_camera_clicked and self.configcamera_screen_show and config.current_screen == "configCamera":

            self.button_camera_clicked = True
            self.configcamera_screen_show = False
            config.current_screen = config.current_screen_default     
            # print("click")

        elif not self.button_camera.draw(config.canvas, 28, 470, 1.0, self.antialiasing) and self.button_camera_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_camera_clicked = False
    
        if self.configcamera_screen_show:

            config.current_screen = "configCamera"
            self.Screen(True)

        else:

            self.Screen(False)

    def Screen(self, visible):

        self.visible = visible
        
        if self.visible and not getattr(textbox.tbox, "visible_box"):

            # config.screen.fill(config.GRAY, [0, 0, config.canvas_size[0], config.canvas_size[1]], pygame.BLEND_RGBA_MIN)
            #pygame.draw.rect(config.canvas, config.RED, [self.cc_box_x, self.cc_box_y, self.cc_w, self.cc_h])

            config.canvas.blit(config.black_in_screen, [0, 0])

            config.canvas.blit(self.zoom_box, [self.cc_box_x, self.cc_box_y])

            self.title.draw(config.canvas, self.cc_w * 1.76, self.cc_h * 4.15)

            # pygame.draw.rect(config.canvas, config.BLACK, [cc_box_x * 1.10, cc_box_y * 1.14, 30, 30])
            # pygame.draw.rect(config.canvas, config.BLACK, [cc_box_x * 1.4, cc_box_y * 1.14, 30, 30])

            self.zoom_button_plus.draw(config.canvas, self.cc_w * 2.03, self.cc_h * 4.5, 1.0, self.antialiasing)
            self.zoom_button_minus.draw(config.canvas, self.cc_w * 1.63, self.cc_h * 4.5, 1.0, self.antialiasing)

            #print("tojiko",config.tojiko.scale, "y", config.tojiko_bg_y, "bg", config.bg.bg_scale, "x", config.bg_x, "zoom_scale_value", self.zoom_scale_value)
        
            if self.zoom_button_plus.draw(config.canvas, self.cc_w * 2.03, self.cc_h * 4.5, 1.0, self.antialiasing) and not self.clicked and self.zoom_scale_value < 9:

                self.clicked = True

                config.tojiko.scale += 0.009 * 3
                config.tojiko_bg_y += 8 * 3
                config.bg_x -= 10 * 3
                config.bg.bg_scale += 0.006 * 3

                self.zoom_scale_value += 1
                config.default_data["zoom_value"] = self.zoom_scale_value

            elif not self.zoom_button_plus.draw(config.canvas, self.cc_w * 2.03, self.cc_h * 4.5, 1.0, self.antialiasing) and self.clicked and pygame.mouse.get_pressed()[0] == 0:

                self.clicked = False

            if self.zoom_scale_value == 9:

                self.zoom_button_plus.disable = True
                self.clicked = False

            else:
                
                self.zoom_button_plus.disable = False

            if self.zoom_scale_value == -1:

                self.zoom_button_minus.disable = True
                self.clicked = False

            else:
                
                self.zoom_button_minus.disable = False


            if self.zoom_button_minus.draw(config.canvas, self.cc_w * 1.63, self.cc_h * 4.5, 1.0, self.antialiasing) and not self.clicked and self.zoom_scale_value != -1:

                self.clicked = True

                config.tojiko.scale -= 0.009 * 3
                config.tojiko_bg_y -= 8 * 3
                config.bg_x += 10 * 3
                config.bg.bg_scale -= 0.006 * 3

                self.zoom_scale_value -= 1
                config.default_data["zoom_value"] = self.zoom_scale_value

            elif self.zoom_button_minus.draw(config.canvas, self.cc_w * 1.63, self.cc_h * 4.5, 1.0, self.antialiasing) and self.clicked and pygame.mouse.get_pressed()[0] == 0:

                self.clicked = False

configcamera = configCamera()