
import numpy as np
import cv2
import copy
from collections import deque
from object import *

H,W = 600,1000
G = 1
path = deque(maxlen=200)

def attract(obj1, obj2):
    force = obj1.getPosition() - obj2.getPosition()
    dist = np.sqrt(force[0]**2+force[1]**2)
    force = force/dist  # normalize
    strength = (G * obj1.getMass()*obj2.getMass()/(dist**2))
    force *= strength

    return force

def main():
    Sun = object(W//2,H//2)
    Planet = object(W//2,H//4)

    Sun.setMass(250)

    Planet.setVelocity(np.array([1,0], dtype='float64'))
    Planet.setMass(10)
   
    while True:
        img = np.zeros((H,W), np.uint8)

        posS = Sun.getPosition()
        posP = Planet.getPosition()
        
        for j in range(1,len(path)):
            #cv2.circle(img, (int(path[j][0]),int(path[j][1])), 1, (180,180,180),1)
            cv2.line(img,(int(path[j-1][0]),int(path[j-1][1])),(int(path[j][0]),int(path[j][1])),(100,100,100),1)

        path.appendleft(copy.deepcopy(posP))

        cv2.circle(img, (int(posS[0]),int(posS[1])), 20, (255,255,255),1)
        cv2.circle(img, (int(posP[0]),int(posP[1])), 10, (255,255,255),1)

        planetForce = attract(Sun,Planet)
        Planet.applyForce(planetForce)
        Planet.update()


        #SunForce = attract(Planet,Sun)
        #Sun.applyForce(SunForce)
        #Sun.update()

        cv2.imshow('gravity-CrRaul', img)
        ch = cv2.waitKey(1)
        if ch == 27:
            break


if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)