import matplotlib.pyplot as plt
import numpy as np

numBars = 15
timer = 0.001

randNums = np.random.randint(0,100,numBars) # generate array of size numBars with values from 0 to 100
x = np.arange(0,numBars,1) # generate array of size numBar from 0 to 15, incrementing by 1 each time

#bubble sort
for i in range(len(randNums)):
    for j in range(0, len(randNums)-i-1):
        plt.title("Bubble Sort")
        barGraph = plt.bar(x, randNums) # create bar plot with positions on x axis given by array x and heights given by array randNums
        barGraph[j].set_color("red")
        barGraph[j+1].set_color("red")
        plt.pause(timer) # used to pause in between animation
        plt.clf() # clears previous plot before next generation
        
        if randNums[j] > randNums[j+1]:
            plt.title("Bubble Sort")
            randNums[j], randNums[j+1] = randNums[j+1], randNums[j]
            barGraph = plt.bar(x, randNums)
            barGraph[j].set_color("red")
            barGraph[j+1].set_color("red")
            plt.pause(timer) 
            plt.clf() 
            
plt.show() # opens visualization