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

    def draw_particle(self):
        pos_x = 10 * self.offset * self.cur_pos[0] + 300
        pos_y = -10 * self.offset * self.cur_pos[1] + 180
        size_x = self.size[0]
        size_y = self.size[1]
        pygame.draw.rect(screen, 'pink', (pos_x, pos_y, size_x, size_y))


    def update_pos(self):
        pass

# --------------------------------- change here ---------------------------------
class heart:
    def __init__(self) -> None:
        self.particles = []
        
    def heart_curve(self, num_particles=20000, theta=0):
        t_interval = 2 * pi / num_particles # 2 * pi = 1 T cycle, divided by num of particles to calculate time interval of each particle
        
        # c = 0

        # Generate particles on the heart curve
        while theta < 2 * pi:
            # c += 1 
            # sigma = 0.15 if c % 5 else 0.3
            # f = 1 - abs(random.gauss(1, sigma) - 1)
            offset = 1

            # -------------------------------- heart curve --------------------------------
            x = 16 * pow(sin(theta), 3)
            y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
            # -----------------------------------------------------------------------------
            
            size = (random.uniform(0.9, 2.5), random.uniform(0.9, 2.5)) # randomly change the size of every particle
            self.particles.append(ParticlePrinciple((x, y), size, offset))
            theta += t_interval

    def draw(self):
        screen.fill((0, 0, 0))
        # Draw the heart particles
        for p in self.particles:
            p.draw_particle()

# -------------------------------------------------------------------------------

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    TITLE = "Heart Beat"
    pygame.display.set_caption(TITLE)
    pygame.display.get_surface
    
    # particle = ParticlePrinciple()

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # ------ change here ------
        particles = ParticlePrinciple()

        particles.draw()
        # -------------------------
        pygame.display.update()
        clock.tick(120)
