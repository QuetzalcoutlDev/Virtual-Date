
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

import pygame

from source import config
from lenpy import Text

class Exp():

	"""
	Está clase es la que permite ver en la pantalla los puntos de experiencia
	que esta ubicada en la parte superior izquierda de la pantalla.
	"""
	
	def __init__(self):
		
		self.exp_img = pygame.image.load(f"{config.images_dir}/exp_icon.png").convert_alpha()

		self.scale = 0.7
		self.exp_icon = pygame.transform.scale(self.exp_img, (self.exp_img.get_width() * self.scale, self.exp_img.get_height() * self.scale))

		self.text = Text(str(config.exp_points), "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK)

	def draw(self, antialiasing=False):

		if antialiasing:
			self.exp_icon = pygame.transform.smoothscale(self.exp_img, (self.exp_img.get_width() * self.scale, self.exp_img.get_height() * self.scale))

		else:
			self.exp_icon = pygame.transform.scale(self.exp_img, (self.exp_img.get_width() * self.scale, self.exp_img.get_height() * self.scale))

		self.text = Text(str(config.exp_points), "ARLRDBD.TTF", 18, f"{config.fonts_dir}/", config.BLACK)

		config.canvas.blit(self.exp_icon, [3, 22])
		self.text.draw(config.canvas, 40, 22)

exp_screen = Exp()