from particle import Particle
import math


class Wave:

    def __init__(self, screen, x, y, sector=None, n_particles=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.sector = sector
        self.n_particles = n_particles
        self.particles = []

        # self.create_particles()

    def create_particles(self):

        theta = math.pi / self.n_particles * 2
        for n in range(self.n_particles // 2):
            # FIXME
            p_speed = [math.cos(theta * n), math.sin(theta * n)]
            p = Particle(self.screen, self.x, self.y, p_speed)
            self.particles.append(p)

            p_speed = [-math.cos(theta * n), -math.sin(theta * n)]
            # print(p_speed)
            p = Particle(self.screen, self.x, self.y, p_speed)
            self.particles.append(p)


    def update(self):
        # print("Updating Wave")
        for particle in self.particles:
            particle.update()

        # if time % 4 == 0:
        # self.create_particles()

    def draw(self):
        # print("Drawing Wave")
        for particle in self.particles:
            particle.draw()