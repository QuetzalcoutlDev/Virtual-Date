
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

from source import config

# Cámara

camera_texts_es = ["Zoom", "Cámara"]

camera_texts_en = ["Zoom", "Camera"]

# Pantalla de configuración

config_screen_texts_es = ["Configuración", 
						  "Pantalla", 
						  "P.Completa", 
						  "Antialiasing", 
						  "Lenguaje", 
						  "Español", 
						  "English",
						  "Sonido & Música",
						  "Vol.Música",
						  "Vol.Sonido",
						  "Gameplay",
						  "Contador FPS",
						  "Silenciar Todo",
						  ]

config_screen_texts_en = ["Settings",
						  "Screen",
						  "Full Screen",
						  "Antialiasing",
						  "Language",
						  "Spanish",
						  "English",
						  "Sound and Music",
						  "Music volume",
						  "Sound volume",
						  "Gameplay",
						  "FPS Counter",
						  "Mute all"]

# Conversación

con_selector_text_es = "Hablar"

con_selector_text_en = "Talk"

# Menú principal 

MainMenu_text_es = ["Iniciar", "Config...", "Salir"]
MainMenu_text_en = ["Start", "Settings", "Exit"]

# Pantalla de música

music_texts_es = ["Música", "Detener"]
music_texts_en = ["Music", "Stop"]

# Captura de pantalla

screenshot_text_es  = "Captura de pantalla: "
screenshot_text_en  = "Screenshot: "

# Pantalla de diálogos

bye_dialog_es = "Di 'Adiós' para cerrar el juego."
bye_dialog_en = "Say 'Goodbye' to close the game"

change_language_es = "Se cerrará el juego para que los cambios hagan efecto."
change_language_en = "The game will be closed for the changes to take effect."


####################################
# Función para el cambio de lenguaje

def change_languages(language="es"):

	"""
	:language: el lenguaje a usar, "es" o "en"
	"""

	global camera_texts, config_screen_texts, con_selector_text, MainMenu_text, music_texts, screenshot_text, bye_dialog, change_language

	if language == "es":

		camera_texts = camera_texts_es
		config_screen_texts = config_screen_texts_es
		con_selector_text = con_selector_text_es
		MainMenu_text = MainMenu_text_es
		music_texts = music_texts_es
		screenshot_text = screenshot_text_es
		bye_dialog = bye_dialog_es
		change_language = change_language_es

	elif language == "en":

		camera_texts = camera_texts_en
		config_screen_texts = config_screen_texts_en
		con_selector_text = con_selector_text_en
		MainMenu_text = MainMenu_text_en
		music_texts = music_texts_en
		screenshot_text = screenshot_text_en
		bye_dialog = bye_dialog_en
		change_language = change_language_en

# Idioma al cargar el juego

if config.current_language == "es":

	change_languages("es")

elif config.current_language == "en":

	change_languages("en")