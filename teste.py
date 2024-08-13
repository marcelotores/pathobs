from pathobs import ObstacleFactory, Node, Scenario, Path, PathAnalyzer
import matplotlib.pyplot as plt
import shapely

cenario_1 = Scenario(grid_size=(60, 60), min_distance=8)
cenario_1.set_start(10, 10)
cenario_1.set_end(50, 50)

cenario_2 = Scenario(grid_size=(60, 60), min_distance=8)
cenario_2.set_start(12, 12)
cenario_2.set_end(45, 45)

L = ObstacleFactory.create_L()
esfera = ObstacleFactory.create_circle(radius=5)
quadrado = ObstacleFactory.create_square(side_length=6)

cenario_1.add_obstacle(L, position=(20, 20))
cenario_1.add_obstacle(esfera, position=(40, 40))
cenario_1.add_obstacle(quadrado, position=(15, 45))

cenario_2.add_obstacle(L, position=(38, 38))
cenario_2.add_obstacle(esfera, position=(30, 20))
cenario_2.add_obstacle(quadrado, position=(20, 45))

#cenario_1.plot_scenario(grid=True)
#cenario_2.plot_scenario()

#plt.show()
path = Path()
path.add_point(shapely.Point(2, 4))
path.add_point(shapely.Point(4, 6))
path.add_point(shapely.Point(6, 8))
print(path.total_distance())
#print(PathAnalyzer.path_smoothness(path))
cenarios_fac = [cenario_1, cenario_2]

print(cenarios_fac[0])