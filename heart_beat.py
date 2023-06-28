import pygame, sys, random
from pygame.locals import *
from math import pi, sin, cos, pow

WIDTH = 1000
HEIGHT = 800
scale = 2 # modify the size of the heart

class ParticlePrinciple:
    def __init__(self, pos, size, offset) -> None:
        self.ori_pos = pos
        self.cur_pos = pos
        self.size = size
        self.offset = offset # random offset factor for the particle

    def draw_particle(self, screen, L):
        pos_x = 10 * self.offset * self.cur_pos[0] + 500
        pos_y = -10 * self.offset * self.cur_pos[1] + 400
        size_x = self.size[0]
        size_y = self.size[1]
        pygame.draw.rect(screen, 'hot pink', (pos_x, pos_y, *self.size))

    def update_pos(self, theta):
        # can change the coefficient in "sin" (e.g. 3, 4, etc.) and denominator (e.g. 8, 10, 12, etc.)
        # to get different heart beat frequency
        freq = 1 + (4 - 3 * self.offset) * sin(theta * 3.5)/10 # Increase heart beat frequency
        self.cur_pos = self.ori_pos[0] * freq * scale, self.ori_pos[1] * freq * scale

# --------------------------------- change here ---------------------------------
class HeartAnimation:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Heart Beat")
        self.particles = []
        self.elapsed = 0
        self.status = 0
        self.L = 100
        self.generate_heart_particles()

    def generate_heart_particles(self):
        num_particles = 20000
        delta_time = 2 * pi / num_particles
        theta = 0
        i = 0

        # Generate particles on the heart curve
        while theta < 2 * pi:
            i += 1
            sigma = 0.15 if i % 5 else 0.3
            f = 1 - abs(random.gauss(1, sigma) - 1) # stochastic shifting proportion
            offset = 1

            # -------------------------------- heart curve --------------------------------
            x = 16 * pow(sin(theta), 3)
            y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
            # -----------------------------------------------------------------------------
            
            size = (random.uniform(0.5, 2.5), random.uniform(0.5, 2.5)) # randomly change the size of every particle
            self.particles.append(ParticlePrinciple((x, y), size, offset))
            theta += delta_time

    def draw_Ani(self):
        self.screen.fill((0, 0, 0))
        # Draw the heart particles 
        for p in self.particles:
            p.draw_particle(self.screen, self.L)

    def update_Ani(self, delta_time):
        self.elapsed += delta_time
        # if self.status == 0:
        #     # For the initial gathering effect, use a large multiplier L and gradually reduce it to normal value
        #     self.L -= delta_time * 200
        #     if self.L <= 10:
        #         self.status = 1
        #         self.L = 10

        # Update particle positions based on time
        for p in self.particles:
            p.update_pos(self.elapsed)

    def run(self):
        while True:
            delta_time = self.clock.tick(60) / 1000 # self.clock.tick(60) limits the frame rate to 60 FPS,
            # divided by 1000 means millisecond -> second
            self.update_Ani(delta_time)
            self.draw_Ani()
            pygame.display.flip()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

# -------------------------------------------------------------------------------

if __name__ == '__main__':
    pygame.init()
    heart_beat = HeartAnimation()
    heart_beat.run()

    