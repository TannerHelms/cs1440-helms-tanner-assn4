from utils.ImagePainter import ImagePainter
from fractals import Julia, Mandelbrot
from utils import FractalSelection
from tkinter import mainloop

# Set vars for the height, width and background color of the GUI
heightOfWindow = 512
widthOfWindow = 512
backgroundColorOfWindow = '#ffffff'

if __name__ == '__main__':

    # Check the sys.args for valid input before the program continues to run
    image, fractalType, fractal = FractalSelection.getImageFromUserInput()

    # Create an instance of imagePainter that will be used as a GUI for this program
    imagePainter = ImagePainter(widthOfWindow, heightOfWindow, backgroundColorOfWindow)

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)

    size = abs(maxx - minx) / 512

    # Loop through each row in the window
    for row in range(heightOfWindow, 0, -1):

        # Loop through each column in the window
        for column in range(widthOfWindow):
            x = minx + column * size
            y = miny + row * size

            # Get the color of the pixel
            if fractalType == "Julia":
                color = Julia.colorOfThePixel(complex(x, y))
            else:
                color = Mandelbrot.colorOfThePixel(complex(x, y))

            # Print the pixel to the photoImage
            imagePainter.photoImage.put(color, (column, 512 - row))

        # Update the window with the photoImage that we just created
        imagePainter.win.update()

    # Save the fractal
    imagePainter.photoImage.write(image + ".png")

    # Tell the user that we have saved and crated the picture
    print(f"Wrote image {image}.png")

    # Keep the GUI open
    mainloop()
