import math
import numpy as np
import matplotlib.pyplot as plt

class PathAnalyzer:
  @staticmethod
  def total_distance(path):
    """Calcula a distância total do caminho."""
    total_dist = 0
    for i in range(1, len(path.points)):
      total_dist += path.points[i-1].distance(path.points[i])
    return total_dist

  @staticmethod
  def path_smoothness(path):
    """Calcula o nível de suavidade do caminho (baseado na mudança de ângulo)."""
    total_angle_change = 0
    for i in range(1, len(path.points) - 1):
      v1 = (path.points[i].x - path.points[i-1].x, path.points[i].y - path.points[i-1].y)
      v2 = (path.points[i+1].x - path.points[i].x, path.points[i+1].y - path.points[i].y)
      angle_change = math.atan2(v2[1], v2[0]) - math.atan2(v1[1], v1[0])
      total_angle_change += abs(angle_change)
    return total_angle_change
  
  @staticmethod
  def inverse_kinematics(path):
    """Calcula a posição inversa dos pontos do caminho."""
    links_len = (35,30)
    L1,L2 = links_len

    x = np.array([node.x for node in path])
    y = np.array([node.y for node in path])

    cos_theta2 = (x**2+y**2-(L1**2+L2**2))/(2*L1*L2)
    sin_theta2 = np.sqrt(abs(1-cos_theta2**2))

    theta2 = np.arctan2(sin_theta2,cos_theta2)

    k1 = L1+L2*cos_theta2
    k2 = L2*sin_theta2
    theta1 = np.arctan2(y,x) - np.arctan2(k2,k1)

    return np.rad2deg((theta1,theta2))

  @staticmethod
  def acc_jerk(path):
    """Calcula a posição inversa dos pontos do caminho."""
    theta = PathAnalyzer.inverse_kinematics(path)
    dtheta = np.diff(theta,axis=1)
    d2theta = np.diff(dtheta,axis=1)
    d3theta = np.diff(d2theta,axis=1)
    std_acc = d2theta.std()
    max_jerk = d3theta.max()

    return std_acc, max_jerk

class Path:
  def __init__(self):
    self.points = []

  def add_point(self, point):
    """Adiciona um ponto ao caminho."""
    self.points.append(point)

  def get_path(self):
    """Retorna a lista de pontos do caminho."""
    return self.points

  def get_path_xy(self):
    """Retorna as coordenadas x e y do caminho."""
    return zip(*[(p.x, p.y) for p in self.points])

  def length(self):
    """Retorna o comprimento do caminho."""
    return len(self.points)

  def plot_path(self, ax=None):
    """Plota o caminho no gráfico."""
    if ax is None:
      fig, ax = plt.subplots()
        
    x, y = zip(*[(p.x, p.y) for p in self.points])
    ax.plot(x, y, color='blue', linewidth=2, label='Path')
  
  def total_distance(self):
    """Calcula a distância total do caminho."""
    return PathAnalyzer.total_distance(self)

  def path_smoothness(self):
    """Calcula o nível de suavidade do caminho (baseado na mudança de ângulo)."""
    return PathAnalyzer.path_smoothness(self)
  
  def acc_jerk(self):
    """Calcula a posição inversa dos pontos do caminho."""
    return PathAnalyzer.acc_jerk(self.get_path())