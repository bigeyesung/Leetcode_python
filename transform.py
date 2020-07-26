import numpy as np
from math import cos, sin, radians

def trig(angle):
  r = radians(angle)
  return cos(r), sin(r)

def matrix(rotation, translation):
  xC, xS = trig(rotation[0])
  yC, yS = trig(rotation[1])
  zC, zS = trig(rotation[2])
  dX = translation[0]
  dY = translation[1]
  dZ = translation[2]
  Translate_matrix = np.array([[1, 0, 0, dX],
                               [0, 1, 0, dY],
                               [0, 0, 1, dZ],
                               [0, 0, 0, 1]])
  Rotate_X_matrix = np.array([[1, 0, 0, 0],
                              [0, xC, -xS, 0],
                              [0, xS, xC, 0],
                              [0, 0, 0, 1]])
  Rotate_Y_matrix = np.array([[yC, 0, yS, 0],
                              [0, 1, 0, 0],
                              [-yS, 0, yC, 0],
                              [0, 0, 0, 1]])
  Rotate_Z_matrix = np.array([[zC, -zS, 0, 0],
                              [zS, zC, 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])
# new coordinte = Z*Y*X*T*old_coor
  return np.dot(Rotate_Z_matrix,np.dot(Rotate_Y_matrix,np.dot(Rotate_X_matrix,Translate_matrix)))



if __name__ == "__main__":
    rotation = (0, 0, 0)
    translation = (15, 10, 0)
    matrix = matrix(rotation, translation)
    pos = np.array([[10],
                    [0],
                    [0],
                    [1]])
    print(matrix)
    ret = np.dot(matrix,pos)
    # scale = np.array([[2, 0, 0, 0],
    #                     [0, 2, 0, 0],
    #                     [0, 0, 1, 0],
    #                     [0, 0, 0, 1]])
    print(ret)
