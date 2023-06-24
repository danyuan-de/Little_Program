import pygame, sys, random
from math import pi, sin, cos, pow
WIDTH = 600
HEIGHT = 400

class ParticlePrinciple:
    def __init__(self, pos, size, offset) -> None:
        self.ori_pos = pos
        self.cur_pos = pos
        self.size = size
        self.offset = offset # random offset factor for the particle

    def draw_particle(self, screen):
        pos_x = 10 * self.offset * self.cur_pos[0] + 300
        pos_y = -10 * self.offset * self.cur_pos[1] + 180
        size_x = self.size[0]
        size_y = self.size[1]
        pygame.draw.rect(screen, 'pink', (pos_x, pos_y, size_x, size_y))


    def update_pos(self):
        pass

# --------------------------------- change here ---------------------------------
class HeartAnimation:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Heart Beat")
        self.particles = []
        
    def generate_heart_particles(self):
        num_particles = 10000
        t_interval = 2 * pi / num_particles
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
            
            size = (random.uniform(1, 2.5), random.uniform(1, 2.5)) # randomly change the size of every particle
            self.particles.append(ParticlePrinciple((x, y), size, offset))
            theta += t_interval

    def draw_Ani(self, screen):
        screen.fill((0, 0, 0))
        # Draw the heart particles
        for p in self.particles:
            p.draw_particle(screen)

    def update_Ani(self):
        pass 

    def run(self):
        while True:
            self.update_Ani()
            self.draw_Ani(self.screen)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            self.clock.tick(120)

# -------------------------------------------------------------------------------

if __name__ == '__main__':
    pygame.init()
    heart_beat = HeartAnimation()
    heart_beat.run()

    