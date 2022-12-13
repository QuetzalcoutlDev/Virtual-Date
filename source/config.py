
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

# Este archivo contiene la configuración del juego, como la musica por defecto, el zoom por defecto, etc.
# Ciertas configuraciones son criticas por lo que no seria bueno modificarlas sin modificar lo que ellas hacen.
# Se entiende, ¿no?

import pygame, lenpy, os, pathlib, sys
from source import tojiko

#######################################################

# Variables de los directorios del juego

main_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
main_dir = main_dir.replace("\\", "/")

# print(main_dir)

assets_dir = os.path.join(main_dir, "assets")
images_dir = os.path.join(assets_dir, "images")
music_dir =  os.path.join(assets_dir, "music")
sounds_dir = os.path.join(assets_dir, "sounds")
fonts_dir = os.path.join(assets_dir, "fonts")

#######################################

# El tamaño de la pantalla y del lienzo

screen_size = [1000, 520]
canvas_size = [1000, 520]

icon_32_32 = pygame.image.load(f"{images_dir}/icon-32x32.png")

pygame.display.set_icon(icon_32_32)

screen = lenpy.config.set_display(screen_size, resizable=False)
canvas = pygame.Surface(canvas_size, pygame.SRCALPHA)

canvas_pos = [0, 0] # La posición del lienzo, solo se movera cuando las dimensiones de la pantalla no sean iguales

################################

name = "A Virtual Date!"
version = "0.1.0"

pygame.display.set_caption(name)

###############################

# Define el nombre de la carpeta donde se guardara la data del juego y su extensión

data_manager = lenpy.data.Manager("Virtual_Date",".dat")

# El archivo de guardado se llama Tojiko, ¿qué raro, no?

game_data = data_manager.Load_game_data(["tojiko"], [[]])

#######################################

# Colores

WHITE = "#ffffff"
BLACK = "#000000"
RED = "#ff0000"
BLUE = "#0018ff"
GREEN = "#00ff3c"
GRAY = "#cccccc"
GRAY_ALPHA = pygame.Color("#7c7c7c")

####################################

# Esto permite cargar el BG

class background():

    """
    Clase para permitir el Background en el juego.

    :bg: el nombre del archivo BG
    :scale: la escala por defecto(la escala cambia durante el juego)

    """

    def __init__(self, bg, scale):

        self.bg_img = pygame.image.load(f"{images_dir}/{bg}").convert_alpha()  
        self.bg_scale = scale
        self.antialiasing = False
        
    def draw(self, x, y, antialiasing=False):

        """
        Dibuja el fondo en la pantalla.
        """

        self.antialiasing = antialiasing

        if self.antialiasing:

            bg = pygame.transform.smoothscale(self.bg_img, (self.bg_img.get_width() * self.bg_scale, (self.bg_img.get_height() * self.bg_scale)))
        
        else:

            bg = pygame.transform.scale(self.bg_img, (self.bg_img.get_width() * self.bg_scale, (self.bg_img.get_height() * self.bg_scale)))

        canvas.blit(bg, [x, y])

    def get_size(self):

        # Obtiene el tamaño de la imagen del fondo.
        return [self.bg_img.get_width() * self.bg_scale, self.bg_img.get_height() * self.bg_scale]

#######################################

# Variables de configuración por defecto

default_data = {}

default_data["nvl"] = 0
default_data["current_nvl"] = 0
default_data["exp_points"] = 0
default_data["exp_limit"] = 0
default_data["love_points"] = 0
default_data["love_points_acumulated"] = 0
default_data["bought_gifts"] = 0
default_data["current_gifts"] = 0
default_data["compliments_facts"] = 0
default_data["tojiko_questions_makes"] = 0
default_data["tojiko_responses_good"] = 0
default_data["tojiko_responses_bad"] = 0
default_data["zoom_value"] = 3
default_data["game_music"] = "Relation.ogg"
default_data["tojiko_clothing"] = "school"
default_data["music_volume"] = 0.7
default_data["sfx_volume"] = 1.0
default_data["cps_default"] = 2
default_data["screen_type"] = "window"
default_data["language"] = "es"
default_data["antialiasing"] = True
default_data["show_fps_counter"] = True
default_data["firstrun"] = True

bg_name = "bg.jpg"

#########################################

# print(game_data)

## Si, se que está no es la mejor forma de cargar la data del juego.

if not game_data == []:

    default_data = game_data

############################
############################

# BG Variables

bg = background(bg_name, 0.32)

bg_x = -160
bg_y = -38
bg_w = bg.get_size()[0]
bg_h = bg.get_size()[1]

#######################

# Variables de configuración de Tojiko

tojiko_bg_x = bg_w // 2.75
tojiko_bg_y = bg_h // 1.9
tojiko = tojiko.Tojiko(tojiko_bg_x, tojiko_bg_y) # Está es Tojiko

######################

# Variables que permiten cargar los datos

zoom_scale_value_default = default_data.get("zoom_value")
game_music_default = default_data.get("game_music")
nvl = default_data.get("nvl")
current_nvl = nvl
exp_points = default_data.get("exp_points")
exp_limit = default_data.get("exp_limit")
love_points = default_data.get("love_points")
love_points_acumulated = default_data.get("love_points_acumulated")
bought_gifts = default_data.get("bought_gifts")
current_gifts = default_data.get("current_gifts")
compliments_facts = default_data.get("compliments_facts")
tojiko_questions_makes = default_data.get("tojiko_questions_makes")
tojiko_responses_good = default_data.get("tojiko_responses_good")
tojiko_responses_bad = default_data.get("tojiko_responses_bad")
current_tojiko_clothing = default_data.get("tojiko_clothing")
screen_type = default_data.get("screen_type")
music_volume = default_data.get("music_volume")
sfx_volume = default_data.get("sfx_volume")
current_language = default_data.get("language")
set_antialiasing = default_data.get("antialiasing")
show_fps_counter = default_data.get("show_fps_counter")
firstrun = default_data.get("firstrun")

# print(zoom_scale_value_default)

# La velocidad de las letras en la caja de texto, numeros más altos significa esperas más largas
# Aunque realmente la velocidad dependera de los fotogramas a los que se este ejecutando el juego.

cps = default_data.get("cps_default")

fullscreen = False

######################################

# Configura el volumen

pygame.mixer.music.set_volume(music_volume)

sound_channel = pygame.mixer.Channel(2)
sound_channel.set_volume(sfx_volume)

#####################################

if screen_type == "window":

    screen = lenpy.config.set_display(screen_size, resizable=False)
   
elif screen_type == "fullscreen":

    screen = lenpy.config.set_display(screen_size, True, resizable=False)
    
#####################################

# Estás variables permiten el cambio entre las pantallas del juego

current_screen_default = "Game"
current_screen = "splash"


def display_fps(visible=True):

    # Permite tomar la captura de pantalla
    # Notese que primero se analiza si esta una captura de pantalla del mismo nombre

    get_fps = str(int(lenpy.config.clock.get_fps()))
    text_fps = lenpy.Text("FPS: " + get_fps, "LSANS.TTF", 13, f"{fonts_dir}", BLACK, sysfont=False)
    
    if visible:
        text_fps.draw(canvas, 4, 2)



def take_screenshot(take=True):

    # Permite tomar la captura de pantalla
    # Notese que primero se analiza si esta una captura de pantalla del mismo nombre

    num = lenpy.tools.numbers_Count(0, 0, 0, 0)

    for file in os.listdir(main_dir):

        numbers = num.count()

        if f"screenshot{str(numbers)}.png" in os.listdir(main_dir):

            num.d += 1

    if take:

        pygame.image.save(screen, f"{main_dir}/screenshot{str(numbers)}.png")

    else:

        return f"screenshot{str(numbers)}.png"

##################################################################
## La variables de configuración de la pantalla de notificación ##

notify = lenpy.ui.Screen_Notify(screen, 0, 20, "#000000", "LSANS.TTF", "#ffffff", 15, f"{images_dir}/notify_box.png", f"{fonts_dir}")
notify_message = ""
notify_visibility = False
notify_visibility_counter = 0

### Lo que permite desaparecer la pantalla de notificación ####

def notify_counter():

    global notify_visibility, notify_visibility_counter

    # Esto permite desaparecer la pantalla de notificación

    if notify_visibility == True and notify_visibility_counter == 0:
        notify_visibility_counter += 1

    elif notify_visibility == True and notify_visibility_counter >= 0 and notify_visibility_counter < 50:
        notify_visibility_counter +=1

    elif notify_visibility == True and notify_visibility_counter >= 50:
        notify_visibility = False
        notify_visibility_counter = 0


tojiko.antialiasing = set_antialiasing
bg.antialiasing = set_antialiasing

########

black_in_screen = pygame.image.load(f"{images_dir}/black.png").convert_alpha()

welcome_again_text = True
welcome_again_no_more = True

in_game = False