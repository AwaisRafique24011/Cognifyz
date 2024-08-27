import os
import shutil
import pandas as pd
from fpdf import FPDF

# Function to organize files into folders based on their type
def organize_files(directory):
    folders = {
        'images': ['jpg', 'jpeg', 'png', 'gif'],
        'documents': ['pdf', 'docx', 'txt', 'xlsx'],
        'videos': ['mp4', 'mkv', 'avi'],
        'archives': ['zip', 'rar', 'tar']
    }

    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(directory):
        file_extension = filename.split('.')[-1].lower()
        file_path = os.path.join(directory, filename)

        for folder, extensions in folders.items():
            if file_extension in extensions:
                destination = os.path.join(directory, folder, filename)
                shutil.move(file_path, destination)
                break

# Function to clean data by removing NaNs, standardizing column names, and formatting dates
def clean_data(file_path, output_path):
    try:
        # Skip bad lines (inconsistent rows)
        df = pd.read_csv(file_path, on_bad_lines='skip')
        df.dropna(inplace=True)  # Remove rows with missing values
        df.columns = df.columns.str.lower()  # Standardize column names

        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])  # Format date column

        df.to_csv(output_path, index=False)
        print(f"Data cleaned and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



# Function to generate a PDF report from a CSV file
def generate_report(data_file, report_file):
    try:
        # Read the CSV file, skipping bad lines
        df = pd.read_csv(data_file, on_bad_lines='skip')
        
        # Create a PDF object
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Add a title
        pdf.cell(200, 10, txt="Monthly Report", ln=True, align='C')
        pdf.ln(10)
        
        # Check if the required columns exist in the DataFrame
        if 'first_name' in df.columns and 'price' in df.columns:
            for index, row in df.iterrows():
                pdf.cell(200, 10, txt=f"{row['first_name']}: ${row['price']}", ln=True)
        else:
            print("The CSV file does not contain the required 'name' and 'sales' columns.")
        
        # Save the PDF
        pdf.output(report_file)
        print(f"Report saved to {report_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function to ask the user which task to run
def main():
    print("Select a task to run:")
    print("1. Organize Files")
    print("2. Clean Data")
    print("3. Generate Report")
    print("4. Run All Tasks")
    
    choice = input("Enter the number of the task you want to run: ")

    if choice == '1':
        directory = input("Enter the directory to organize: ")
        organize_files(directory)
    elif choice == '2':
        input_file = input("Enter the path to the CSV file to clean: ")
        output_file = input("Enter the path to save the cleaned file: ")
        clean_data(input_file, output_file)
    elif choice == '3':
        data_file = input("Enter the path to the data file: ")
        report_file = input("Enter the path to save the PDF report: ")
        generate_report(data_file, report_file)
    elif choice == '4':
        directory = input("Enter the directory to organize: ")
        organize_files(directory)
        
        input_file = input("Enter the path to the CSV file to clean: ")
        output_file = input("Enter the path to save the cleaned file: ")
        clean_data(input_file, output_file)
        
        data_file = output_file
        report_file = input("Enter the path to save the PDF report: ")
        generate_report(data_file, report_file)
    else:
        print("Invalid choice. Please try again.")

main()
