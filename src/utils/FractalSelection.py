"""
FractalSelection uses the command line arguments to select which fractal
image to use
"""
from Images import juliaImages, mandelbrotImages
import sys

juliaDictionary = juliaImages.Images
mandelDictionary = mandelbrotImages.Images


# Process command-line arguments, allowing the user to select their fractal
def getImageFromUserInput():

    # Check to see if the user provided a fractal
    if not len(sys.argv) < 2:
        userInput = sys.argv[1]

    # Crash the program since no fractal is provided
    else:
        crashProgram()

    # Check if the user input is in the juliaDictionary
    if userInput in juliaDictionary:
        return userInput, "Julia", juliaDictionary[userInput]

    # Check if the user input is in the mandelDictionary
    if userInput in mandelDictionary:
        return userInput, "Mandel", mandelDictionary[userInput]

    # If we got to this point we have invalid user input
    crashProgram()


# crashProgram crashes the program with instructions
def crashProgram():
    print(f"Usage: main.py FRACTALNAME\nWhere FRACTALNAME is one of:")
    for f in juliaDictionary:
        print(f"\t{f}")
    for f in mandelDictionary:
        print(f"\t{f}")
    sys.exit(1)
