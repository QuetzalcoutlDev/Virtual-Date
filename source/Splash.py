
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

class Splash(object):
    
    def __init__(self):

        self.splash1 = pygame.image.load(f"{config.images_dir}/splash1.png").convert_alpha()
        self.splash2 = pygame.image.load(f"{config.images_dir}/splash2.png").convert_alpha()

        self.white_img = pygame.image.load(f"{config.images_dir}/white.png").convert()

        self.white_img_alpha_value = 255

        self.number_img = 0

        self.counter = 0

        self.hide = False

    def Screen(self):

        # config.screen.fill(config.BLACK)
        # config.canvas.fill(config.WHITE)

        surf = pygame.transform.scale(config.canvas, config.canvas_size)
        config.screen.fill(config.BLACK)
        config.screen.blit(surf, config.canvas_pos)

        config.canvas.fill(config.WHITE)

        if self.number_img == 0:

            config.canvas.blit(self.splash1, [0, 0])

        elif self.number_img == 1:
            config.canvas.blit(self.splash2, [0, 0])

    def update(self):

        # Contador y valor alpha

        #print(self.counter)

        self.white_img.set_alpha(self.white_img_alpha_value)

        if self.counter < 255 and not self.hide:
            
            self.counter += 10
            self.white_img_alpha_value -= 10

        elif self.counter >= 255 and not self.hide:

            self.counter += 5
            self.white_img_alpha_value = 0

        if self.counter >= 355 and not self.hide:

            self.counter = 255
            self.counter -= 10

            self.white_img_alpha_value += 10

            self.hide = True

        if self.counter > 0 and self.hide:

            self.counter -= 10
            self.white_img_alpha_value += 10

        elif self.counter <= 0 and self.hide:

            self.counter = 0
            self.white_img_alpha_value = 255
            self.hide = False
            self.number_img += 1

        if self.counter < 255 and not self.hide and self.number_img == 2:
            
            self.counter += 5

        elif self.counter >= 255 and not self.hide and self.number_img == 2:

            self.number_img = 3

        config.canvas.blit(self.white_img, [0, 0])

    def splashscreen_complete(self, boolean:bool):

        return boolean

splashscreen = Splash()