from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode import generate
from barcode.writer import ImageWriter
import os
    
# Create a directory to store the images if it doesn't exist
output_directory = "output_images"
os.makedirs(output_directory, exist_ok=True)

# Load the template image
template_image = Image.open('SUPPER OF THE SENT.png')

# Load the font
font = ImageFont.truetype('arial.ttf', size=10)


# Open the text file in read mode
with open('names.txt', 'r') as file:
    # Read the lines of the file and remove leading/trailing whitespace
    names = [line.strip() for line in file.readlines()]

for name in names:
    # Generate a unique ticket number using names

    # Create a copy of the template image to work with
    ticket = template_image.copy()

    # Create a drawing context
    draw = ImageDraw.Draw(ticket)



    # Generate the barcode for the ticket number
    barcode_value = barcode.Code128(name, writer=ImageWriter())
    barcode_image = barcode_value.render(
        writer_options={
            "module_height": 5, 
            "module_width": 0.25,  
            "background": "#992703",
            "foreground": "black",
        }
    )
    
    # Paste the barcode onto the ticket image
    ticket.paste(barcode_image, (800,450))

    # Save the individual ticket image with the name and barcode

    # Save the individual ticket image with the name and barcode in the output directory
    output_filename = os.path.join(output_directory, f'{name}.png')
    ticket.save(output_filename)


print("Ticket generation completed.")
