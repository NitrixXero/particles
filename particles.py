# Copyright 2024 Elijah Gordon (NitrixXero) <nitrixxero@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from sys import exit
from random import randint, uniform
from math import pi, cos, sin
from pygame import init, display, FULLSCREEN, event, QUIT, KEYDOWN, K_ESCAPE, draw, time, image

init()

screen_info = display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

screen = display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
display.set_caption("Particles")

icon = image.load('icon/icon.jpeg')
display.set_icon(icon)

class Particle:
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
        self.radius = randint(1, 3)
        self.color = (0, 0, 255)

        self.speed = uniform(0.1, 2)
        self.angle = uniform(0, pi * 2)

    def move(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0


def draw_particles(particles):
    for particle in particles:
        draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)


def generate_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        particles.append(Particle())
    return particles


running = True
particles = generate_particles(500)

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            running = False

    screen.fill((0, 0, 0))

    for particle in particles:
        particle.move()
    draw_particles(particles)

    display.flip()
    time.delay(30)

quit()
exit()
