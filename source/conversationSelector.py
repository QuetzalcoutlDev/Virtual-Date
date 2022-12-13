
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
from source import config, textbox, tojiko, con_themes

from source.ui_text import con_selector_text

###########################################
# Pantalla de selección de conversaciones #
###########################################

class ConversationSelector():

    """
    La pantalla de conversación es una de la pantallas más complicadas y cuyo
    código es el más largo de todas las partes del juego.
    """
    
    def __init__(self):
        
        self.visible = False

        self.button_con_selector = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/select_button_normal.png", f"{config.images_dir}/buttons/select_button_hover.png", f"{config.images_dir}/buttons/select_button_select.png", True, f"{config.images_dir}/buttons/select_button_disable.png", text_parameters=[con_selector_text, "VarelaRound.ttf", 19, "#000000", True, [22, 4], f"{config.fonts_dir}/"])

        self.cons_box_x = 600
        self.cons_box_y = 80

        self.button_con_selector_clicked = False
        self.con_selector_screen_show = False

        self.make_compliments_section_show = False
        self.make_questions_section_show = False
        self.i_feel_section_show = False
        self.con_themes_section_show = False

        self.current_theme = "art"

        self.antialiasing = False

    def draw_button(self, antialiasing=False):

        self.antialiasing = antialiasing

        # Si los codigos para dibujar los botones son muy largos.

        # self.button_con_selector.draw(config.canvas, 28, 376, 1.0, self.antialiasing)
        
        if not config.current_screen == "conversationselector" and not config.current_screen == "Game":
            self.button_con_selector.disable = True

        elif config.current_screen == "Game":
            self.button_con_selector.disable = False

        # Si, el click de los botones.

        if self.button_con_selector.draw(config.canvas, 28, 376, 1.0, self.antialiasing) and not self.button_con_selector_clicked and not config.current_screen == "conversationselector":

            self.button_con_selector_clicked = True
            self.con_selector_screen_show = True

        elif not self.button_con_selector.draw(config.canvas, 28, 376, 1.0, self.antialiasing) and self.button_con_selector_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_con_selector_clicked = False

        if self.button_con_selector.draw(config.canvas, 28, 376, 1.0, self.antialiasing) and not self.button_con_selector_clicked and self.con_selector_screen_show and config.current_screen == "conversationselector":

            self.button_con_selector_clicked = True
            self.con_selector_screen_show = False
            config.current_screen = config.current_screen_default

        elif not self.button_con_selector.draw(config.canvas, 28, 376, 1.0, self.antialiasing) and self.button_con_selector_clicked and pygame.mouse.get_pressed()[0] == 0:

            self.button_con_selector_clicked = False

        ##
        ## Esto permite mostrar las secciones sin salir de la pantalla de conversación.

        if self.con_selector_screen_show:

            config.current_screen = "conversationselector"
            self.Screen(True)

        elif self.make_compliments_section_show:

            self.Screen(True)
            self.make_compliments()

        elif self.make_questions_section_show:

            self.Screen(True)
            self.make_questions()

        elif self.i_feel_section_show:

            self.Screen(True)
            self.i_feel_section()

        elif self.con_themes_section_show:

            self.Screen(True)
            self.conversation_themes_section()

        else:

            self.Screen(False)

    def Screen(self, visible=False):

        choice_dir = "choice_button2_"

        self.visible = visible
        # print(self.visible)

        elements_y = 0
        label_number = 0

        if self.visible and not getattr(textbox.tbox, "visible_box") and config.current_screen == "conversationselector":

            # Esto son los tipos de conversaciones o las maneras de hablar con Tojiko.
            # No hay mucho porque solo es un prototipo.

            # Pero al menos funciona, ¿no?, jeje.

            for elements in con_themes.types.get("types"):

                set_label = con_themes.types.get("labels")[label_number]

                if lenpy.system.windows:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 13, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                elif lenpy.system.linux:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 10, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y)

                # print(elements)
                # print(set_label)

                ## Cada botón en los tipos de manera de hablar son definidos uno por uno debido a que estos no llaman a la caja de texto
                ## directamente a exceptión del botón de 'Adiós'.
                

                # Hablar de...
                if choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y) and set_label == "0":

                    config.current_screen = "con_themes_section"
                    self.con_selector_screen_show = False
                    self.con_themes_section_show = True

                # Me siento...
                if choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y) and set_label == "2":

                    config.current_screen = "i_feel_section"
                    self.con_selector_screen_show = False
                    self.i_feel_section_show = True

                # Hacer una pregunta...
                elif choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y) and set_label == "3":

                    config.current_screen = "make_question_section"
                    self.con_selector_screen_show = False
                    self.make_questions_section_show = True

                # Hacer un cumplido...
                elif choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y) and set_label == "4":

                    config.current_screen = "make_compliments_section"
                    self.con_selector_screen_show = False
                    self.make_compliments_section_show = True

                ### Este es el botón de 'Adiós' ###

                elif choice_button.draw(config.canvas, self.cons_box_x, self.cons_box_y + elements_y) and set_label == "5":

                    textbox.textbox_visibility = True

                    self.call_textbox(con_themes.types_labels.get("5"), textbox.textbox_visibility)
                    self.con_selector_screen_show = False

                #pygame.draw.rect(config.canvas, config.RED, [self.cons_box_x, self.cons_box_y + elements_y, 380, 30])

                label_number += 1

                if set_label == "4":
                    elements_y += 55

                else:
                    elements_y += 40

            self.move_tojiko_bg("left")

        elif self.visible and not config.current_screen == "conversationselector":

            # Esto permite no regresar a Tojiko a su posición original.

            if config.current_screen == "make_compliments_section":

                self.make_compliments()

            elif config.current_screen == "make_question_section":

                self.make_questions()

            elif config.current_screen == "i_feel_section":

                self.i_feel_section()

            elif config.current_screen == "con_themes_section":

                self.conversation_themes_section()

        else:

            # Esto es lo regresa a Tojiko a su posición original.
            self.move_tojiko_bg("right")

    ##########################
    ## Sección de cumplidos ##
    ##########################

    def make_compliments(self):

        # Entramos en la sección de cumplidos.
        # ¿Que cumplidos le harás a Tojiko?

        choice_dir = "choice_button2_"

        elements_y = 0
        label_number = 0

        if self.visible and config.current_screen == "make_compliments_section" and not self.con_selector_screen_show:

            for elements in con_themes.make_compliments.get("types"):

                if lenpy.system.windows:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 13, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                elif lenpy.system.linux:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 10, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 20)

                set_label = con_themes.make_compliments.get("labels")[label_number]
                # print(set_label)

                if choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 20) and not set_label == "9":

                    textbox.textbox_visibility = True

                    self.call_textbox(con_themes.compliments_labels.get(set_label), textbox.textbox_visibility)
                    self.con_selector_screen_show = False
                    self.make_compliments_section_show = False

                elif choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 20) and set_label == "9":
                    
                    self.make_compliments_section_show = False
                    self.con_selector_screen_show = True
                    config.current_screen = "conversationselector"
                    self.button_con_selector.disable = False

                label_number += 1

                if set_label == "8":

                    elements_y += 60

                else:

                    elements_y += 40

    def make_questions(self):

        # La sección de preguntas.
        # ¿Qué preguntas quieres hacerle a Tojiko?

        choice_dir = "choice_button2_"

        elements_y = 0
        label_number = 0

        if self.visible and config.current_screen == "make_question_section" and not self.con_selector_screen_show:

            """
            Creo que si para futuras versiones, habra que cambiar ciertas formas de pintar estos elementos en pantalla.
            Hablo de los errores que ocurriran si se eliminan los temás de conversación.
            Hubiera que cambiar también la cantidad de labels.
            """

            for elements in con_themes.make_questions.get("types"):

                if lenpy.system.windows:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 13, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                elif lenpy.system.linux:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 10, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38)

                set_label = con_themes.make_questions.get("labels")[label_number]
                # print(set_label)

                """
                Está condiciones me gustan porque no tuve que hacer mucho para llamar a sus ¿Labels?.

                """ 

                if choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38) and not set_label == "13":

                    textbox.textbox_visibility = True

                    self.call_textbox(con_themes.question_labels.get(set_label), textbox.textbox_visibility)
                    self.con_selector_screen_show = False
                    self.make_questions_section_show = False

                # Atrás >>>>

                elif choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38) and set_label == "13":
                    
                    self.make_questions_section_show = False
                    self.con_selector_screen_show = True
                    config.current_screen = "conversationselector"
                    self.button_con_selector.disable = False

                label_number += 1

                # Actualmente el juego no cuenta con barras de desplamiento, por lo que los temás de conversación se limita al pequeño
                # tamaño de la pantalla del juego.

                if set_label == "12":

                    elements_y += 40

                else:

                    elements_y += 34

    def i_feel_section(self):

        choice_dir = "choice_button2_"

        elements_y = 0
        label_number = 0

        if self.visible and config.current_screen == "i_feel_section" and not self.con_selector_screen_show:

            for elements in con_themes.i_feel.get("types"):

                if lenpy.system.windows:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 13, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                elif lenpy.system.linux:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 10, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38)

                set_label = con_themes.i_feel.get("labels")[label_number]
                # print(set_label)

                if choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38) and not set_label == "8":

                    config.textbox_visibility = True
                    
                    self.call_textbox(con_themes.feel_labels.get(set_label), config.textbox_visibility)
                    self.con_selector_screen_show = False
                    self.i_feel_section_show = False

                elif choice_button.draw(config.canvas, self.cons_box_x - 20, self.cons_box_y + elements_y - 38) and set_label == "8":

                    self.i_feel_section_show = False
                    self.con_selector_screen_show = True
                    config.current_screen = "conversationselector"
                    self.button_con_selector.disable = False

                label_number += 1

                if set_label == "7":

                    elements_y += 50

                else:

                    elements_y += 40

        pass

    def conversation_themes_section(self):

        choice_dir = "choice_button2_"

        theme_y = 0
        label_number = 0
        elements_y = 0

        theme_x = 480

        y = 60

        if self.visible and config.current_screen == "con_themes_section" and not self.con_selector_screen_show:

            for theme in con_themes.con_themes.get("types"):

                if lenpy.system.windows:

                    button_theme = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/choice_button1_normal.png", f"{config.images_dir}/buttons/choice_button1_hover.png", f"{config.images_dir}/buttons/choice_button1_select.png", True, text_parameters=[theme, "VarelaRound.ttf", 14, "#000000", True, [3, 6], f"{config.fonts_dir}/"])
               
                elif lenpy.system.linux:

                    button_theme = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/choice_button1_normal.png", f"{config.images_dir}/buttons/choice_button1_hover.png", f"{config.images_dir}/buttons/choice_button1_select.png", True, text_parameters=[theme, "VarelaRound.ttf", 11, "#000000", True, [3, 6], f"{config.fonts_dir}/"])

                button_theme.draw(config.canvas, theme_x, y + theme_y) 

                set_label = con_themes.con_themes.get("labels")[label_number]

                # print(current_theme)

                if button_theme.draw(config.canvas, theme_x, y + theme_y) and not set_label == "9":

                    self.current_theme = con_themes.con_themes.get("theme")[label_number]

                elif button_theme.draw(config.canvas, theme_x, y + theme_y) and set_label == "9":

                    self.con_selector_screen_show = True
                    self.con_themes_section_show = False
                    config.current_screen = "conversationselector"
                    self.button_con_selector.disable = False

                label_number += 1

                if set_label == "8":

                    theme_y += 60

                else:

                    theme_y += 40

            ### Subtemás ###

            if self.current_theme == "art":

                current_subtheme = con_themes.art_subthemes
                current_numbers = con_themes.art_numbers

            elif self.current_theme == "anime":

                current_subtheme = con_themes.anime_subthemes
                current_numbers = con_themes.anime_numbers

            elif self.current_theme == "history":

                current_subtheme = con_themes.history_subthemes
                current_numbers = con_themes.history_numbers

            elif self.current_theme == "music":

                current_subtheme = con_themes.music_subthemes
                current_numbers = con_themes.music_numbers

            elif self.current_theme == "us":

                current_subtheme = con_themes.us_subthemes
                current_numbers = con_themes.us_numbers

            elif self.current_theme == "python":

                current_subtheme = con_themes.python_pygame_subthemes
                current_numbers = con_themes.python_pygame_numbers

            elif self.current_theme == "tojiko":

                current_subtheme = con_themes.tojiko_subthemes
                current_numbers = con_themes.tojiko_numbers

            elif self.current_theme == "videogames":

                current_subtheme = con_themes.videogames_subthemes
                current_numbers = con_themes.videogames_numbers

            elif self.current_theme == "virtual_date":

                current_subtheme = con_themes.virtual_date_subthemes
                current_numbers = con_themes.virtual_date_numbers

            theme_number = 0

            ## Los subtemás ya dibujados ##

            for elements in current_subtheme.get("themes"):

                if "=" in elements:

                    # print(elements.index(":"))

                    element = elements[elements.index("=") + 1:]
                    exp_unlock = int(elements[0:elements.index("=")])
                    
                    # print(exp_unlock)
                    
                else:

                    element = elements
                    exp_unlock = 0

                set_number = current_subtheme.get("numbers")[theme_number]

                if lenpy.system.windows:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 13, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                elif lenpy.system.linux:

                    choice_button = lenpy.ui.ImageButton(f"{config.images_dir}/buttons/{choice_dir}normal.png", f"{config.images_dir}/buttons/{choice_dir}hover.png", f"{config.images_dir}/buttons/{choice_dir}select.png", True, text_parameters=[elements, "VarelaRound.ttf", 10, "#000000", True, [10, 4], f"{config.fonts_dir}/"])
                
                if config.exp_points >= exp_unlock:

                    choice_button.draw(config.canvas, self.cons_box_x + 5, self.cons_box_y + elements_y - 30)

                    if choice_button.draw(config.canvas, self.cons_box_x + 5, self.cons_box_y + elements_y - 30):

                        config.textbox_visibility = True
                    
                        self.call_textbox(current_numbers.get(set_number), config.textbox_visibility)
                        self.con_selector_screen_show = False
                        self.con_themes_section_show = False

                    elements_y += 40

                theme_number += 1

    def move_tojiko_bg(self, direction):

        """
        Tojiko y el BG se moveran a la dirección que colocada(Solo izquierda o derecha(left or right))

        :direction: Permite solo dos opciones:
                    "left"
                    "right"

        Esto solo se usa para la pantalla de conversación.
        """

        counter = 0

        for i in range(80):

            if direction == "left" and not config.tojiko_bg_x <= float(404):

                config.tojiko_bg_x -= counter
                config.bg_x -= counter

            elif direction == "right" and not config.tojiko_bg_x >= float(483):

                config.tojiko_bg_x += counter
                config.bg_x += counter


            # Esto para darle suavidad la movimiento de Tojiko.

            if i < 20:

                counter += 0.008

            elif i > 20:

                counter += 0.002

    def call_textbox(self, set_conversation, visibility=True):

        """
        Se usa para llamar a la caja de texto.
        :set_conversation: Usa la misma manera de colocar texto en la caja de texto: 

                           [la expresión, el texto, la pose, la acción]

        :visibility: Como el nombre lo indica, es para mostrar la caja de texto, 
                     ¿Quizás solo quiera cambiar el texto y no mostrarlo?
        """

        textbox.current_conversation = set_conversation
        textbox.tbox.counter = 0
        textbox.textbox_visibility = visibility

conversationselector = ConversationSelector()