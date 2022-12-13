
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

################
# Caja de texto
################

class Textbox():

    """
    Está clase es la caja de texto, se que hay muchas cosas basicas en esta clase
    pero es lo mejor que pude hacer.

    La lineas de dialogo aún son bastante primitivas, por lo que no permiten más de 4 lineas de dialogo,
    tampoco permiten efectos de texto, algo así como en Ren'Py.

    :x: posición x
    :y: posición y

    :font: la fuente a usar.
    :font_size: El tamaño de la fuente, si puedes notar no se coloca un tamaño de fuente
                tan grande, esto porque terminaria saliendo de la caja de texto.
    """
    
    def __init__(self, x, y, font, font_size):

        self.x = x
        self.y = y
        self.text = ""

        self.textbox_img = pygame.image.load(f"{config.images_dir}/textbox.png").convert_alpha()
        
        self.font = pygame.font.Font(font, font_size)
        self.counter = 0 # El contador
        self.speed = config.cps
        self.active_dialogs = 0
        self.done = False
        
        self.skip_text = False
        self.change_text = False
        
        self.visible_box = False
        
        # La lineas de texto
        self.snip = self.font.render("", True, config.WHITE)
        self.snip2 = self.font.render("", True, config.WHITE)
        self.snip3 = self.font.render("", True, config.WHITE)
        self.snip4 = self.font.render("", True, config.WHITE)

        self.sound_no_loop = False
        self.sound_actual = ""
        self.actual_dialog = 0

        self.tojiko_talking = True

    def draw(self, text=[["normal", "", "normal", None]], visibilty=False):

        # ¿No hay más dialogos?

        # print(text)

        if visibilty == True:

            config.current_screen = "text_window"

        if self.active_dialogs == len(text):

            self.active_dialogs = 0
            self.visible_box = False
            
        else:

            self.visible_box = visibilty

        # ¿Hay más de un dialogo?

        if len(text) > 1:

            self.text = text[self.active_dialogs][1]

        else:

            self.text = text[1]

        # print(self.text)

        # get_text = ""
        # print(self.visible_box)
        
        if self.visible_box:

            ### La caja de texto ###
            
            # pygame.draw.rect(config.canvas, config.BLACK, [self.x, self.y, 540, 130])
            config.canvas.blit(self.textbox_img, [self.x, self.y])

            # Acciones UI que puede hacer la caja de texto

            if text[self.active_dialogs][3] == None:

                # print("No action")
                self.sound_no_loop = False

                self.tojiko_talking = True

            elif "play:" in text[self.active_dialogs][3]:

                file = text[self.active_dialogs][3].strip("play:")

                lenpy.ui.UIaction(f"play:{config.music_dir}/{file}")

            elif text[self.active_dialogs][3] == "stop_music":

                lenpy.ui.UIaction("stop_music")

            elif "play_sound:" in text[self.active_dialogs][3]:

                file = text[self.active_dialogs][3][11:]

                if self.actual_dialog == self.active_dialogs:

                    self.sound_no_loop = True
                    
                else:

                    self.sound_no_loop = False

                if self.active_dialogs > self.actual_dialog and not self.text == "":

                    lenpy.ui.UIaction("stop_sound")
                    self.actual_dialog = self.active_dialogs

                # Si no se está reproduciendo ningún sonido, entonces...

                if not lenpy.ui.UIaction.get_busy_sound(self) and not self.sound_no_loop:

                    lenpy.ui.UIaction(f"play_sound:{config.sounds_dir}/{file}")

                elif lenpy.ui.UIaction.get_busy_sound(self):

                    self.sound_no_loop = True
                    self.actual_dialog = self.active_dialogs

            elif text[self.active_dialogs][3] == "stop_sound":

                lenpy.ui.UIaction("stop_sound")

            elif text[self.active_dialogs][3] == "quit":

                if config.firstrun:

                    config.welcome_again_text = False
                    config.default_data["firstrun"] = False

                config.data_manager.Save_game_data([config.default_data], ["tojiko"])
                lenpy.ui.UIaction("quit")

            elif text[self.active_dialogs][3] == "firstrun":

                if config.firstrun:

                    config.welcome_again_text = False
                    config.default_data["firstrun"] = False

                elif not config.firstrun:

                    config.welcome_again_text = False

            elif "exp:" in text[self.active_dialogs][3]:

                exp_plus = text[self.active_dialogs][3].strip("exp:")

                # print(exp_plus)
                config.exp_points += int(exp_plus)
                config.default_data["exp_points"] = config.exp_points

            elif text[self.active_dialogs][3] == "no_talk":

                self.tojiko_talking = False

            # El contador permite el mostrar letra por letra mientras que no sea igual a la cantidad de letras del texto.

            if self.counter < self.speed * len(self.text):
                
                self.counter += 2

                # Este código comentado era un intento por colocar efectos de texto en el dialogo, algo así como se hace en Ren'Py
                # Creo que estoy haciendo algo mal, ¿qué puede ser?

                # # get_text = "" + self.text[0:self.counter//self.speed]

                # # if "{i}" in text:
                    
                # #     print(text.index("{i}"))
                # #     print(text.index("{/i}"))

                # #     italic_start = text.index("{i}") + 3
                # #     italic_end = text.index("{/i}") + 4
                    
                # #     if self.counter == italic_start:
                        
                # #         self.font.set_bold(True)

                # #     elif self.counter == italic_end:

                # #         self.font.set_bold(False)

                #### Más abajo se explica el porque las comillas vacias

                if not self.text == "" and self.tojiko_talking:
                
                    config.tojiko.talking(text[self.active_dialogs][0], text[self.active_dialogs][2])

            # ¿No hay más letras?

            elif self.counter >= self.speed * len(self.text):

                self.done = True # Ya puedes cambiar a otro dialogo

                config.tojiko.idle(text[self.active_dialogs][0], text[self.active_dialogs][2])

            # Si el contador aún no se alcanza la cantidad de letras puedes pulsar el botón derecho del mouse para saltarte el efecto
            # de letra por letra.

            key = pygame.key.get_pressed()

            if self.counter != self.speed * len(self.text) and pygame.mouse.get_pressed()[0] == 1 and not self.skip_text or self.counter != self.speed * len(self.text) and key[pygame.K_SPACE] == 1 and not self.skip_text:

                self.counter = self.speed * len(self.text) - 2
                self.skip_text = True

            elif pygame.mouse.get_pressed()[0] == 0 and self.skip_text or key[pygame.K_SPACE] == 0 and self.skip_text:

                self.skip_text = False

            # Salta a otro dialogo
            
            if self.done and pygame.mouse.get_pressed()[0] == 1 and not self.change_text or self.done and key[pygame.K_SPACE] == 1 and not self.change_text:

                self.active_dialogs += 1
            
                self.done = False
                self.counter = 0
                self.change_text = True

            elif pygame.mouse.get_pressed()[0] == 0 and self.change_text or key[pygame.K_SPACE] == 0 and self.change_text:

                self.change_text = False

            # Estás condiciones de aqui permiten el mostrar 4 lineas de texto de una forma un poco... ¿Basica?

            if self.counter < 61 * self.speed:

                self.snip = self.font.render(self.text[0:self.counter//self.speed], True, config.BLACK)
                config.canvas.blit(self.snip, [self.x * 1.05, self.y + 16]) 
            
            elif self.counter >= 61 * self.speed and self.counter < 126 * self.speed:

                self.snip = self.font.render(self.text[0:61], True, config.BLACK)
                config.canvas.blit(self.snip, [self.x * 1.05, self.y + 16])

                self.snip2 = self.font.render(self.text[61:self.counter//self.speed], True, config.BLACK)
                config.canvas.blit(self.snip2, [self.x * 1.05, self.y + self.snip2.get_size()[1] * 2.2])
            
            elif self.counter >= 126 * self.speed and self.counter < 191 * self.speed:

                self.snip = self.font.render(self.text[0:61], True, config.BLACK)
                config.canvas.blit(self.snip, [self.x * 1.05, self.y + 16])

                self.snip2 = self.font.render(self.text[61:126], True, config.BLACK)
                config.canvas.blit(self.snip2, [self.x * 1.05, self.y + self.snip2.get_size()[1] * 2.2])

                self.snip3 = self.font.render(self.text[126:self.counter//self.speed], True, config.BLACK)
                config.canvas.blit(self.snip3, [self.x * 1.05, self.y + self.snip3.get_size()[1] * 3.4])
            
            elif self.counter >= 191 * self.speed and self.counter < 259 * self.speed:

                self.snip = self.font.render(self.text[0:61], True, config.BLACK)
                config.canvas.blit(self.snip, [self.x * 1.05, self.y + 16])

                self.snip2 = self.font.render(self.text[61:126], True, config.BLACK)
                config.canvas.blit(self.snip2, [self.x * 1.05, self.y + self.snip2.get_size()[1] * 2.2])

                self.snip3 = self.font.render(self.text[126:191], True, config.BLACK)
                config.canvas.blit(self.snip3, [self.x * 1.05, self.y + self.snip3.get_size()[1] * 3.4])

                self.snip4 = self.font.render(self.text[191:self.counter//self.speed], True, config.BLACK)
                config.canvas.blit(self.snip4, [self.x * 1.05, self.y + self.snip4.get_size()[1] * 4.25])

            elif self.counter >= 258 * self.speed:

                self.snip = self.font.render(self.text[0:61], True, config.BLACK)
                config.canvas.blit(self.snip, [self.x * 1.05, self.y + 16])

                self.snip2 = self.font.render(self.text[61:127], True, config.BLACK)
                config.canvas.blit(self.snip2, [self.x * 1.05, self.y + self.snip2.get_size()[1] * 2.2])

                self.snip3 = self.font.render(self.text[126:191], True, config.BLACK)
                config.canvas.blit(self.snip3, [self.x * 1.05, self.y + self.snip3.get_size()[1] * 3.4])

                self.snip4 = self.font.render(self.text[191:258], True, config.BLACK)
                config.canvas.blit(self.snip4, [self.x * 1.05, self.y + self.snip4.get_size()[1] * 4.25])

        else:

            self.sound_no_loop = False

            config.tojiko.idle()
            self.counter = 0
            self.active_dialogs = 0
            self.done = False

textbox_visibility = False

not_intro = True

# En Windows no se muestra una fuente como en Linux, en Linux un tamaño de fuente 24 es demasiado grande
# por lo que un tamaño más pequeño es mejor.

if lenpy.system.windows:

    tbox = Textbox(240, 380, f"{config.fonts_dir}/ARLRDBD.TTF", 16)

elif lenpy.system.linux:

    tbox = Textbox(240, 380, f"{config.fonts_dir}/ARLRDBD.TTF", 16)

# test_conversation = [
#                     ["normal", "Hello World!!!", "normal", None], 
#                     ["happy", "My name is Tojiko Merata!!!", "normal", None],
#                     ["normal", "¿How are you in this day?", "normal", None],
#                     ["normal", "", "normal", None]
#                     ]

current_conversation = [["normal", "Hello World!!!", "normal", None],
                        ["normal", "", "normal", None]]


def textbox_show_hide():

    global tbox, textbox_visibility

    ## Las comillas vacias permiten desaparecer la caja de texto 
    
    if tbox.text == "":
        textbox_visibility = False
        config.current_screen = config.current_screen_default

    tbox.draw(current_conversation, textbox_visibility)