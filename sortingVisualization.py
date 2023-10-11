import matplotlib.pyplot as plt
import numpy as np

sortNum = input("Which sort would you like to see? \n 1) Bubble Sort \n 2) Insertion Sort \n 3) Selection Sort \n 4) Merge Sort \n 5) Quick Sort \n 0) Quit \n")
delay = input("What delay in between sorts would you like to see? (Recommended: 0.5) \n")

numBars = 15
timer = float(delay)

randNums = np.random.randint(0,100,numBars) # generate array of size numBars with values from 0 to 100
x = np.arange(0,numBars,1) # generate array of size numBar from 0 to 15, incrementing by 1 each time

#bubble sort
match int(sortNum):
    case 0:
        print("Bye Bye!")
    case 1:
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
    case 2:
        for i in range(1,len(randNums)):
            curr = randNums[i]
            j = i-1
            while(j >= 0 and randNums[j] > curr):
                plt.title("Insertion Sort")
                barGraph = plt.bar(x, randNums)
                barGraph[j+1].set_color("red")
                barGraph[j].set_color("red")
                plt.pause(timer) 
                plt.clf()
                
                randNums[j+1] = randNums[j]
                randNums[j] = curr # this is added only for visualization purposes
                
                plt.title("Insertion Sort")
                barGraph = plt.bar(x, randNums)
                barGraph[j+1].set_color("red")
                barGraph[j].set_color("red")
                plt.pause(timer) 
                plt.clf()
                j -= 1
                
            randNums[j+1] = curr
        print(randNums)
            
plt.show() # opens visua1lization