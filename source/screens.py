
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

from source import config, ccamera, musicselect, configscreen, screenshot_f, stadistscreen, conversationSelector, exp_screen

def draw_screens():

    ccamera.configcamera.draw_button(config.set_antialiasing)
    musicselect.musicselector.draw_button(config.set_antialiasing)
    screenshot_f.screenshot_button.draw_button(config.set_antialiasing)
    # stadistscreen.stadistics_screen.draw_button(config.set_antialiasing)
    conversationSelector.conversationselector.draw_button(config.set_antialiasing)
    exp_screen.exp_screen.draw(config.set_antialiasing)
    configscreen.configscreen.draw_button(config.set_antialiasing)