
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

import lenpy, os
from source import config

# Este archivo controla y es Tojiko

# Aquí se definen sus poses y más

class Tojiko():

    """
    Está es Tojiko.

    :x: La posición x por defecto.
    :y: La posición y por defecto.

    Se puede dibujar en pantalla a Tojiko con sus posiciones por defecto al momento
    de cargar la clase en una variable.

    O se puede dibujar con otras posiciones.

    """
    
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.tojiko_sprite_normal = lenpy.spritesheet.SpriteSheet(f"{config.images_dir}/Tojiko_normal.png", f"{config.images_dir}/Tojiko_normal.xml")
        self.tojiko_sprite_hi_date_excuse = lenpy.spritesheet.SpriteSheet(f"{config.images_dir}/Tojiko_hi_date_excuse.png", f"{config.images_dir}/Tojiko_hi_date_excuse.xml")

        self.actual_animation = []
        self.animation_name = ""
        self.scale = 0.32 # Valor por defecto
        self.antialiasing = False

        self.tojiko_clothes = ["school", "github", "monika"] # Si, tengo pensado colocar la ropa de Monika de DDLC
        
        # Las poses
        self.tojiko_poses = ["normal", 
                             "hi", 
                             "date", 
                             "excuse"]
        
        # tipos de estado
        self.tojiko_type_list = ["idle", "talking"]

        # lista de expresiones
        self.tojiko_expressions_list = ["normal", 
                                        "happy", 
                                        "confused", 
                                        "embarrassed", 
                                        "sad", 
                                        "jeje", 
                                        "neutral", 
                                        "angry", 
                                        "hangry", 
                                        "deception",
                                        "ego",
                                        "angry2",
                                        "neutral2",
                                        "happy2",
                                        "oh",
                                        "deception2",
                                        "sad2",
                                        "sad3"]
        
        # variables de control
        self.clothes_number = 0
        self.poses_number = 0
        self.type_number = 0
        self.expression_number = 0

        # Usualmente la cantidad de fotogramas en las animaciones
        # es de 1
        self.frames_amount = 1

        # Inicia con la posición idle
        self.idle()

    def Expressions(self, expression="normal"):

        """
        Se usa para cambiar la expresión de Tojiko

        :expression: Este acepta como opciones los valores dentro de la
                     lista "self.tojiko_expressions_list ".
        """

        if expression == "normal":

            self.expression_number = 0

        elif expression == "happy":

            self.expression_number = 1

        elif expression == "confused":

            self.expression_number = 2

        elif expression == "embarrassed":

            self.expression_number = 3

        elif expression == "sad":

            self.expression_number = 4

        elif expression == "jeje":

            self.expression_number = 5

        elif expression == "neutral":

            self.expression_number = 6

        elif expression == "angry":

            self.expression_number = 7

        elif expression == "hangry":

            self.expression_number = 8

        elif expression == "deception":

            self.expression_number = 9

        elif expression == "ego":

            self.expression_number = 10

        elif expression == "angry2":

            self.expression_number = 11

        elif expression == "neutral2":

            self.expression_number = 12

        elif expression == "happy2":

            self.expression_number = 13

        elif expression == "oh":

            self.expression_number = 14

        elif expression == "deception2":

            self.expression_number = 15

        elif expression == "sad2":

            self.expression_number = 16

        elif expression == "sad3":

            self.expression_number = 17

        return self.expression_number

    def set_pose(self, pose="normal"):

        """
        La posiciones de Tojiko son cambiadas por está función.

        Está función es un poco más complicada que la de las expresiones
        debido a que los nombres de las poses son más especificos y dificiles
        de recordar, :p.

        :pose: Acepta como opciones los elementos en la lista "self.tojiko_poses"

        """

        if pose == "normal":

            self.frames_amount = 1
            self.poses_number = 0

        elif pose == "hi":

            self.frames_amount = 1
            self.poses_number = 1

        elif pose == "date":

            self.frames_amount = 1
            self.poses_number = 2

        elif pose == "excuse":

            self.frames_amount = 1
            self.poses_number = 3

        return self.poses_number
        
    def idle(self, expression="normal", pose="normal"):

        """
        Está función se usa para devolver a Tojiko a su expresión "normal" y pose "idle"

        Si se especifica opciones en "expression" o "pose", podemos devolver a la expresión
        "normal" sin cambiar su pose.

        :expression: Este acepta como opciones los valores dentro de la
                     lista "self.tojiko_expressions_list ".

        :pose: Acepta como opciones los elementos en la lista "self.tojiko_poses"

        """

        self.type_number = 0
        
        self.tojiko_sprite_normal.frame_index = 0
        self.tojiko_sprite_hi_date_excuse.frame_index = 0
        # self.frames_amount = 1
        
        exp = self.Expressions(expression)
        pose = self.set_pose(pose)

        self.animation_name = f"{self.tojiko_clothes[self.clothes_number]} {self.tojiko_poses[pose]} {self.tojiko_type_list[self.type_number]} {self.tojiko_expressions_list[exp]}"

    def talking(self, expression="normal", pose="normal"):

        """
        Está función se usa durante el efecto de "letra por letra"
        y regresa a usar la función "idle" cuando no hay más letras que mostrar.

        """

        # self.frames_amount = 1
        self.type_number = 1

        exp = self.Expressions(expression)
        pose = self.set_pose(pose)

        self.animation_name = f"{self.tojiko_clothes[self.clothes_number]} {self.tojiko_poses[pose]} {self.tojiko_type_list[self.type_number]} {self.tojiko_expressions_list[exp]}"

    def take_animation(self):

        # Debido a que el colocar una función con una variable con el nombre de la animación
        # Y otra variable con el mismo nombre pero con otro nombre de la animación este hacia
        # Que se mostrara la animación de la ultima variable que redefinio a la misma variable.

        # ¿No se si me entiendes?

        if self.poses_number == 0:

            self.actual_animation = self.tojiko_sprite_normal.get_animation_name(f"tojiko {self.animation_name}", self.frames_amount)
    
        elif self.poses_number == 1 or self.poses_number == 2 or self.poses_number == 3:

            self.actual_animation = self.tojiko_sprite_hi_date_excuse.get_animation_name(f"tojiko {self.animation_name}", self.frames_amount)

    def update(self):

        fps = 24

        # Actualiza la animación

        if self.poses_number == 0:

            self.tojiko_sprite_normal.update(fps)

        elif self.poses_number == 2 or self.poses_number == 1 or self.poses_number == 3:

            self.tojiko_sprite_hi_date_excuse.update(fps)

    def draw(self, x_y=[], antialiasing=False):

        self.take_animation() # Toma el nombre de la animación

        self.antialiasing = antialiasing

        """
        Si no se especifica nada en el parametro 'x_y', se usara las posiciones
        por defecto.

        """

        if x_y == []:

            x = self.x
            y = self.y

        else:
            x = x_y[0]
            y = x_y[1]

        # Debido a que las poses no siempre mantienen a Tojiko en su lugar
        # se necesita mover un poco para que parezca que está no se mueve :)

        if self.poses_number == 0:

            self.tojiko_sprite_normal.draw(config.canvas, x, y, self.scale, self.antialiasing)

        elif self.poses_number == 1:

            self.tojiko_sprite_hi_date_excuse.draw(config.canvas, x + 9, y, self.scale, self.antialiasing)

        elif self.poses_number == 2:

            self.tojiko_sprite_hi_date_excuse.draw(config.canvas, x - 3.8, y, self.scale, self.antialiasing)

        elif self.poses_number == 3:

            self.tojiko_sprite_hi_date_excuse.draw(config.canvas, x - 3, y, self.scale, self.antialiasing)

        self.update()