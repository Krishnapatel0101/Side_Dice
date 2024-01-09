# import pandas as pd
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from tkinter import Tk, Label, Button, filedialog
# from PIL import Image
# import csv

# class DiceMosaicGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Dice Mosaic Generator")

#         self.root.geometry("600x200")  # Set your desired width and height


#         self.image_path1 = None
#         self.image_path2 = None

#         self.label1 = Label(root, text="Select Image 1:")
#         self.label1.pack()

#         self.button1 = Button(root, text="Browse", command=self.browse_image1)
#         self.button1.pack()

#         self.label2 = Label(root, text="Select Image 2:")
#         self.label2.pack()

#         self.button2 = Button(root, text="Browse", command=self.browse_image2)
#         self.button2.pack()

#         self.convert_button = Button(root, text="Convert to Mosaic", command=self.convert_to_mosaic)
#         self.convert_button.pack()

#     def browse_image1(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#         if file_path:
#             self.image_path1 = file_path
#             self.label1.config(text=f"Selected Image 1: {file_path}")

#     def browse_image2(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#         if file_path:
#             self.image_path2 = file_path
#             self.label2.config(text=f"Selected Image 2: {file_path}")

#     def convert_to_mosaic(self):
#         if self.image_path1 and self.image_path2:
#             numDiceWide = 100
#             numDiceTall = 100

#             source_image1 = Image.open(self.image_path1)
#             source_image2 = Image.open(self.image_path2)
#             die_one = Image.open("DiceImages/1.png")
#             die_two = Image.open("DiceImages/2.png")
#             die_three = Image.open("DiceImages/3.png")
#             die_four = Image.open("DiceImages/4.png")
#             die_five = Image.open("DiceImages/5.png")
#             die_six = Image.open("DiceImages/6.png")

#             resized_image1 = source_image1.resize((numDiceWide, numDiceTall))
#             resized_image2 = source_image2.resize((numDiceWide, numDiceTall))

#             resized_image1 = resized_image1.convert('L')
#             resized_image2 = resized_image2.convert('L')

#             pix_val1 = list(resized_image1.getdata())
#             pix_val2 = list(resized_image2.getdata())

#             def map_to_dice_value(value):
#                 if value < 42:
#                     return 1
#                 elif 42 <= value < 84:
#                     return 2
#                 elif 84 <= value < 126:
#                     return 3
#                 elif 126 <= value < 168:
#                     return 4
#                 elif 168 <= value < 210:
#                     return 5
#                 else:
#                     return 6

#             pix_val1 = [map_to_dice_value(value) for value in pix_val1]
#             pix_val2 = [map_to_dice_value(value) for value in pix_val2]

#         flag = 1
#         for i in range(len(pix_val1)):
#             if pix_val1[i] == pix_val2[i]:
#                 if flag == 1:
#                     flag = 0
#                     if pix_val1[i] == 6:
#                         pix_val1[i] = 5
#                     elif pix_val1[i] == 3:
#                         pix_val1[i] = 2
#                     else:
#                         pix_val1[i] += 1
#                 else:
#                     flag = 1
#                     if pix_val2[i] == 6:
#                         pix_val2[i] = 5
#                     elif pix_val2[i] == 3:
#                         pix_val2[i] = 2
#                     else:
#                         pix_val2[i] += 1

#             elif pix_val1[i] + pix_val2[i] == 7:
#                 if flag == 1:
#                     flag = 0
#                     if pix_val1[i] == 6:
#                         pix_val1[i] = 5
#                     elif pix_val1[i] == 5:
#                         pix_val1[i] = 6
#                     elif pix_val1[i] == 4:
#                         pix_val1[i] = 5
#                     elif pix_val1[i] == 3:
#                         pix_val1[i] = 2
#                     elif pix_val1[i] == 2:
#                         pix_val1[i] = 3
#                     else:
#                         pix_val1[i] = 2
#                 else:
#                     flag = 1
#                     if pix_val2[i] == 6:
#                         pix_val2[i] = 5
#                     elif pix_val2[i] == 5:
#                         pix_val2[i] = 6
#                     elif pix_val2[i] == 4:
#                         pix_val2[i] = 5
#                     elif pix_val2[i] == 3:
#                         pix_val2[i] = 2
#                     elif pix_val2[i] == 2:
#                         pix_val2[i] = 3
#                     else:
#                         pix_val2[i] = 2

#         # Calculate the size of the output image
#         dice_image_width, dice_image_height = die_one.size
#         output_image_size = (dice_image_width * numDiceWide, dice_image_height * numDiceTall)

#         # Create black images the size of the output images
#         output_image1 = Image.new('L', output_image_size, color=0)
#         output_image2 = Image.new('L', output_image_size, color=0)

#         # Iterate over the list and paste the correct value die onto the corresponding pixel location
#         for i in range(len(pix_val1)):
#             # Calculate the x_location of the top left corner of die location
#             x_location = int((int(dice_image_width) * i)) % (dice_image_width * numDiceWide)
#             # Calculate the y_location of the top left corner of the die image
#             y_location = int(i / numDiceWide) * dice_image_height

#             # Paste the die from the first image to output_image1
#             if pix_val1[i] == 1:
#                 output_image1.paste(die_one, (x_location, y_location))
#             elif pix_val1[i] == 2:
#                 output_image1.paste(die_two, (x_location, y_location))
#             elif pix_val1[i] == 3:
#                 output_image1.paste(die_three, (x_location, y_location))
#             elif pix_val1[i] == 4:
#                 output_image1.paste(die_four, (x_location, y_location))
#             elif pix_val1[i] == 5:
#                 output_image1.paste(die_five, (x_location, y_location))
#             elif pix_val1[i] == 6:
#                 output_image1.paste(die_six, (x_location, y_location))

#             # Paste the die from the second image to output_image2
#             if pix_val2[i] == 1:
#                 output_image2.paste(die_one, (x_location, y_location))
#             elif pix_val2[i] == 2:
#                 output_image2.paste(die_two, (x_location , y_location))
#             elif pix_val2[i] == 3:
#                 output_image2.paste(die_three, (x_location , y_location))
#             elif pix_val2[i] == 4:
#                 output_image2.paste(die_four, (x_location , y_location))
#             elif pix_val2[i] == 5:
#                 output_image2.paste(die_five, (x_location , y_location))
#             elif pix_val2[i] == 6:
#                 output_image2.paste(die_six, (x_location , y_location))

#         output_image1.save('mosaic_output1.png')
#         output_image2.save('mosaic_output2.png')

#             # Optional: Display the output images in new windows
#         output_image1.show()
#         output_image2.show()

#         output_pix = [int(str(val1) + str(val2)) for val1, val2 in zip(pix_val1, pix_val2)]
#         print(output_pix)
#         num_rows = 100
#         num_columns = 100
#         pix_val_nested = []
#         for i in range(0, len(output_pix), num_columns):
#             pix_val_nested.append(output_pix[i:i + num_columns])
#         print("Using Nested Loops:")
#         for row in pix_val_nested:
#             print(row)
#         csv_file_path = 'mosaic.csv'
#         with open(csv_file_path, 'w', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerows(pix_val_nested)
#         # Call the function to create the PDF
#         self.create_pdf(csv_file_path)

#     def create_pdf(self, csv_file_path):
#         # Set up PDF
#         pdf_output_path = 'output.pdf'
#         doc = SimpleDocTemplate(pdf_output_path, pagesize=A4)

#         # Create a list to store the tables, spacers, and labels
#         elements = []

#         # Load CSV data into a Pandas DataFrame
#         df = pd.read_csv(csv_file_path, header=None)

#         # Define the number of rows and columns per table
#         rows_per_table = 10
#         cols_per_table = 10

#         # Define a style for the labels
#         styles = getSampleStyleSheet()
#         label_style = styles['Normal']

#         # Split the DataFrame into chunks for each table
#         for start_row in range(0, len(df), rows_per_table):
#             end_row = start_row + rows_per_table
#             for start_col in range(0, len(df.columns), cols_per_table):
#                 end_col = start_col + cols_per_table

#                 # Extract data for the current table
#                 data = df.iloc[start_row:end_row, start_col:end_col].values.tolist()

#                 # Create a table for the current page
#                 table = Table(data)

#                 # Add borders to cells and grid lines
#                 style = TableStyle([
#                     ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
#                     ('BOX', (0, 0), (-1, -1), 1, colors.black)   # Add borders to cells
#                 ])
#                 table.setStyle(style)

#                 # Get the label for the current table
#                 label = chr(ord('A') + (start_col // cols_per_table)) + str((start_row // rows_per_table) + 1)

#                 # Add the label to the list
#                 label_text = Paragraph(f"<b>{label}</b>", label_style)
#                 elements.append(label_text)

#                 # Add the table to the list
#                 elements.append(table)

#                 # Add a spacer for spacing between labels and tables
#                 elements.append(Spacer(1, 35))  # Adjust the vertical spacing as needed

#         # Build PDF document with labels, tables, and spacers
#         doc.build(elements)

# if __name__ == "__main__":
#     root = Tk()
#     app = DiceMosaicGUI(root)
#     root.mainloop()
import streamlit as st
from PIL import Image
import csv
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd  # Import Pandas for DataFrame support

class DiceMosaicApp:
    def __init__(self):
        self.image_path1 = None
        self.image_path2 = None

    def browse_image1(self):
        file_path = st.file_uploader("Select Image 1:", type=["png", "jpg", "jpeg"])
        if file_path:
            self.image_path1 = file_path
            st.write(f"Selected Image 1: {file_path.name}")

    def browse_image2(self):
        file_path = st.file_uploader("Select Image 2:", type=["png", "jpg", "jpeg"])
        if file_path:
            self.image_path2 = file_path
            st.write(f"Selected Image 2: {file_path.name}")

    def convert_to_mosaic(self):
        if self.image_path1 and self.image_path2:
            numDiceWide = 100
            numDiceTall = 100

            source_image1 = Image.open(self.image_path1)
            source_image2 = Image.open(self.image_path2)
            die_one = Image.open("DiceImages/1.png")
            die_two = Image.open("DiceImages/2.png")
            die_three = Image.open("DiceImages/3.png")
            die_four = Image.open("DiceImages/4.png")
            die_five = Image.open("DiceImages/5.png")
            die_six = Image.open("DiceImages/6.png")

            resized_image1 = source_image1.resize((numDiceWide, numDiceTall))
            resized_image2 = source_image2.resize((numDiceWide, numDiceTall))

            resized_image1 = resized_image1.convert('L')
            resized_image2 = resized_image2.convert('L')

            pix_val1 = list(resized_image1.getdata())
            pix_val2 = list(resized_image2.getdata())

            def map_to_dice_value(value):
                if value < 42:
                    return 1
                elif 42 <= value < 84:
                    return 2
                elif 84 <= value < 126:
                    return 3
                elif 126 <= value < 168:
                    return 4
                elif 168 <= value < 210:
                    return 5
                else:
                    return 6

            pix_val1 = [map_to_dice_value(value) for value in pix_val1]
            pix_val2 = [map_to_dice_value(value) for value in pix_val2]

            flag = 1
            for i in range(len(pix_val1)):
                if pix_val1[i] == pix_val2[i]:
                    if flag == 1:
                        flag = 0
                        if pix_val1[i] == 6:
                            pix_val1[i] = 5
                        elif pix_val1[i] == 3:
                            pix_val1[i] = 2
                        else:
                            pix_val1[i] += 1
                    else:
                        flag = 1
                        if pix_val2[i] == 6:
                            pix_val2[i] = 5
                        elif pix_val2[i] == 3:
                            pix_val2[i] = 2
                        else:
                            pix_val2[i] += 1

                elif pix_val1[i] + pix_val2[i] == 7:
                    if flag == 1:
                        flag = 0
                        if pix_val1[i] == 6:
                            pix_val1[i] = 5
                        elif pix_val1[i] == 5:
                            pix_val1[i] = 6
                        elif pix_val1[i] == 4:
                            pix_val1[i] = 5
                        elif pix_val1[i] == 3:
                            pix_val1[i] = 2
                        elif pix_val1[i] == 2:
                            pix_val1[i] = 3
                        else:
                            pix_val1[i] = 2
                    else:
                        flag = 1
                        if pix_val2[i] == 6:
                            pix_val2[i] = 5
                        elif pix_val2[i] == 5:
                            pix_val2[i] = 6
                        elif pix_val2[i] == 4:
                            pix_val2[i] = 5
                        elif pix_val2[i] == 3:
                            pix_val2[i] = 2
                        elif pix_val2[i] == 2:
                            pix_val2[i] = 3
                        else:
                            pix_val2[i] = 2

            # Calculate the size of the output image
            dice_image_width, dice_image_height = die_one.size
            output_image_size = (dice_image_width * numDiceWide, dice_image_height * numDiceTall)

            # Create black images the size of the output images
            output_image1 = Image.new('L', output_image_size, color=0)
            output_image2 = Image.new('L', output_image_size, color=0)

            # Iterate over the list and paste the correct value die onto the corresponding pixel location
            for i in range(len(pix_val1)):
                # Calculate the x_location of the top left corner of die location
                x_location = int((int(dice_image_width) * i)) % (dice_image_width * numDiceWide)
                # Calculate the y_location of the top left corner of the die image
                y_location = int(i / numDiceWide) * dice_image_height

                # Paste the die from the first image to output_image1
                if pix_val1[i] == 1:
                    output_image1.paste(die_one, (x_location, y_location))
                elif pix_val1[i] == 2:
                    output_image1.paste(die_two, (x_location, y_location))
                elif pix_val1[i] == 3:
                    output_image1.paste(die_three, (x_location, y_location))
                elif pix_val1[i] == 4:
                    output_image1.paste(die_four, (x_location, y_location))
                elif pix_val1[i] == 5:
                    output_image1.paste(die_five, (x_location, y_location))
                elif pix_val1[i] == 6:
                    output_image1.paste(die_six, (x_location, y_location))

                # Paste the die from the second image to output_image2
                if pix_val2[i] == 1:
                    output_image2.paste(die_one, (x_location, y_location))
                elif pix_val2[i] == 2:
                    output_image2.paste(die_two, (x_location , y_location))
                elif pix_val2[i] == 3:
                    output_image2.paste(die_three, (x_location , y_location))
                elif pix_val2[i] == 4:
                    output_image2.paste(die_four, (x_location , y_location))
                elif pix_val2[i] == 5:
                    output_image2.paste(die_five, (x_location , y_location))
                elif pix_val2[i] == 6:
                    output_image2.paste(die_six, (x_location , y_location))

            # Display output images in Streamlit
            st.image(output_image1, caption="Mosaic Output 1", use_column_width=True)
            st.image(output_image2, caption="Mosaic Output 2", use_column_width=True)

            # Display CSV download link
            st.markdown(get_csv_download_link([pix_val1]), unsafe_allow_html=True)

            # Create PDF
            self.create_pdf([pix_val1])

    def create_pdf(self, data):
        # Set up PDF
        pdf_output_path = 'output.pdf'
        doc = SimpleDocTemplate(pdf_output_path, pagesize=A4)

        # Create a list to store the tables, spacers, and labels
        elements = []

        # Load CSV data into a Pandas DataFrame
        df = pd.DataFrame(data)

        # Define the number of rows and columns per table
        rows_per_table = 10
        cols_per_table = 10

        # Define a style for the labels
        styles = getSampleStyleSheet()
        label_style = styles['Normal']

        # Split the DataFrame into chunks for each table
        for start_row in range(0, len(df), rows_per_table):
            end_row = start_row + rows_per_table
            for start_col in range(0, len(df.columns), cols_per_table):
                end_col = start_col + cols_per_table

                # Extract data for the current table
                table_data = df.iloc[start_row:end_row, start_col:end_col].values.tolist()

                # Create a table for the current page
                table = Table(table_data)

                # Add borders to cells and grid lines
                style = TableStyle([
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
                    ('BOX', (0, 0), (-1, -1), 1, colors.black)   # Add borders to cells
                ])
                table.setStyle(style)

                # Get the label for the current table
                label = chr(ord('A') + (start_col // cols_per_table)) + str((start_row // rows_per_table) + 1)

                # Add the label to the list
                label_text = Paragraph(f"<b>{label}</b>", label_style)
                elements.append(label_text)

                # Add the table to the list
                elements.append(table)

                # Add a spacer for spacing between labels and tables
                elements.append(Spacer(1, 35))  # Adjust the vertical spacing as needed

        # Build PDF document with labels, tables, and spacers
        doc.build(elements)

def get_csv_download_link(data):
    csv_file_path = 'mosaic.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)

    csv_url = f'<a href="/downloads/{csv_file_path}" download="{csv_file_path}">Download CSV</a>'
    return csv_url

if __name__ == "__main__":
    app = DiceMosaicApp()

    st.title("Dice Mosaic Generator")

    app.browse_image1()
    app.browse_image2()

    if st.button("Convert to Mosaic"):
        app.convert_to_mosaic()

