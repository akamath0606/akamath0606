import numpy as np #import for calculating linear regression
import matplotlib.pyplot as plt #import for plotting data and line of best fit

#this function returns a dictionary that counts the occurrences of each word in the given text
#https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file/
def countWords(filename): 
    text = open(str(filename), "r")
    ret = dict()

    for nl in text:
        nl = nl.strip()
        nl = nl.lower()

        words = nl.split(" ") #split each line by spaces to get all the words

        for word in words: #increment if word already in dictionary, set to one otherwise
            if word in ret:
                ret[word] += 1
            else:
                ret[word] = 1

    return ret

#function for calculating the coefficients of linear regression
#https://www.geeksforgeeks.org/linear-regression-python-implementation/?ref=ml_lbp
def estimate_coefficients(x, y):
    n = np.size(x)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    cross_dev = np.sum(y*x) - n*mean_y*mean_x
    dev = np.sum(x*x) - n*mean_x*mean_x

    reg_coeff1 = cross_dev / dev
    reg_coeff0 = mean_y - reg_coeff1*mean_x

    return (reg_coeff0, reg_coeff1)

#function to plot the line of best fit using data and coefficients calculated in function estimate_coefficients()
def plot_line(x, y, b):
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    predictedy = b[0] + b[1]*x

    plt.plot(x, predictedy, color = "g")

    plt.ylabel("Number of Written Works")
    plt.xlabel("Occurrences of Given Word")

    plt.show()

#code to be executed every run
oncomputable = countWords("turing1.txt")
imitationgame = countWords("turing2.txt")
print("On Computable Dictionary:")
for key in list(oncomputable.keys()):
    print(key + ": " + str(oncomputable[key]))

print("\n\nImitation Game Dictionary:")
for k in list(imitationgame.keys()):
    print(k + ": " + str(imitationgame[k]))
regword = input("Please input the word you would like to predict:\n")
regword = regword.lower()
computeocc = 0
if(regword in oncomputable.keys()):
    computeocc = oncomputable[regword]

print("Occurrences of \"" + regword + "\" in On Computable Numbers: " + str(computeocc))

imitocc = 0
if(regword in imitationgame.keys()):
    imitocc = imitationgame[regword]
print("Occurrences of \"" + regword + "\" in The Imitation Game: " + str(imitocc))

x = np.array([computeocc, imitocc])
y = np.array([1, 2])

b = estimate_coefficients(x, y)

plot_line(x, y, b)