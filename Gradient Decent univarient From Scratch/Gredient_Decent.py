import numpy as np
import matplotlib.pyplot as plt

try:

        def cost_function(inital_theta0,initial_theta1,points):
                cost = 0
                b = initail_theta0
                m= initial_theta1
                for i in range(0,len(points)):
                        x = points[i,0]
                        y = points[i,1]
                        cost+= ((b + m * x) - y)**2
                return cost / float(len(points))    


        def step_gradient(current_theta0,current_theta1,points,alpha):
                theta0_gradient = 0
                theta1_gradient = 0
                b = current_theta0
                m = current_theta1
                H = []
                N = float(len(points))
                for i in range(len(points)):
                        x = points[i,0]
                        y = points[i,1]
                        theta0_gradient += (-(2 / N) * (y - (b + m * x)))
                        theta1_gradient +=  (-(2 / N) * x * (y - ((m * x) + b)))

                        temp0 = b - (alpha * theta0_gradient)
                        temp1 = m - (alpha * theta1_gradient)


                new_theta0 = temp0
                new_theta1 = temp1
                
                for i in range(len(points)):
                        h = new_theta0 + (new_theta1  * points[i,0])
                        H.append(h)
                return [new_theta0, new_theta1,H]




        def gradient_decent(points,initial_theta0,initial_theta1,alpha):
                theta0 = initial_theta0
                theta1 = initial_theta1
                number_of_iteration = 1500
                for i in range(number_of_iteration):
                        theta0, theta1, H= step_gradient(theta0, theta1, points, alpha)

                return [theta0, theta1,H]

        def run():
                points = np.genfromtxt('data.txt' ,delimiter=',')
                #points = np.array(points)
                #points = points[[1:,0],[1:,1]]
                x = points [:,0]
                y = points [:,1]

                alpha = 0.01
                initial_theta0 = 0
                initial_theta1 = 0
                print("starting main operation")
                print("data: ",points)
                [theta0,theta1, H] = gradient_decent(points, initial_theta0,initial_theta1,alpha)


                print("Optimal Theta0 and Theta1 Values Are:", theta0,theta1)


                print("X values are: ", x)
                print("Predicted Values are", H)
                plt.scatter(x,y)
                plt.xlabel("X Values")
                plt.ylabel("H Values")

                plt.plot(x,H)
                plt.show()


except ValueError:
        print("error")


if __name__=='__main__':
        run()

