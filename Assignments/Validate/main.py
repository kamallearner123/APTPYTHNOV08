# Get the list of folders from the parent of this path except "Validate" folder
from os import listdir
from os.path import isdir, join
from datetime import datetime
import importlib.util
from time import time
import run_solution
import sqlite3
import pandas as pd

# Configure the base folder path
base_folder = join('./', '../')


# Register adapter and converter for datetime
sqlite3.register_adapter(datetime, lambda dt: dt.isoformat())  # Store as ISO format
sqlite3.register_converter("timestamp", lambda s: datetime.fromisoformat(s.decode("utf-8")))


# if command line argument is given then use that as the folder name or collect all the folders from the parent directory
import sys
if len(sys.argv) > 1:
    folders = [sys.argv[1]]
    print(f"\n\nChecking the solution for {folders}\n")
else:
    folders = [f for f in listdir(base_folder) if isdir(join(base_folder, f)) and f != 'Validate']

print(folders)
# open a data base file for sql and create table with Folder name, Program name, time executed, status and time taken to execute
conn = sqlite3.connect('assignments_updated.db')
c = conn.cursor()

# Create table if not exists with Name and program as primary key column, program, time_executed, status and time_taken as columns in the table assignments 
c.execute('''CREATE TABLE IF NOT EXISTS assignments (
    Name VARCHAR(255),
    Program VARCHAR(255),
    Time_Executed TIMESTAMP,
    Status VARCHAR(50),
    Time_Taken FLOAT,
    UNIQUE (Name, Program)
);''') 


# From each folder get files "program1.py", "program2.py", "program3.py" import those as modules and run solution function from each file
# and store the time taken to execute the function and status of the function in the database and time when it ran in the database
def run_programs(folders):
    for folder in folders:
        for i in range(1, 4):
            AssignmentName = f'Assignment{i}'
            spec = importlib.util.spec_from_file_location(f'{folder}.program{i}', f'{base_folder}/{folder}/{AssignmentName}.py')
            module = importlib.util.module_from_spec(spec)
            # what is module_from_spec and spec_from_file_location 
            start = time()

            try:
                spec.loader.exec_module(module)
                # pass module to function test_solution which is there in run_solution.py in current directory and collect the result
                status = run_solution.test_solution(module)
                if status == 0:
                    status = 'Passed'
                else:
                    status = 'Failed'

            except Exception as e:
                print(e)
                status = 'Failed'
                print(f"Error in running {folder}/{AssignmentName}.py")

            if status == 'Failed':
                #print with red color
                print(f"\033[91m{folder}/{AssignmentName}.py failed\033[0m")
            else:
                #print with green color
                print(f"\033[92m{folder}/{AssignmentName}.py passed\033[0m")

            end = time()
            time_taken = end - start
            # update the data if the folder text is already there or create a new row with folder name, program name, time executed, status and time taken
            c.execute("INSERT OR REPLACE INTO assignments (Name, Program, Time_Executed, Status, Time_Taken) VALUES (?, ?, ?, ?, ?)", (folder, f'{AssignmentName}', datetime.now(), status, time_taken))

            conn.commit()



# Write a function to get the table from the database and print the table
def get_table():
    conn = sqlite3.connect('assignments_updated.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assignments")
    # fetch all the details and generate an image and save it in the current directory
    rows = c.fetchall()
    # dump rows to a csv file 
    
    with open('assignments.csv', 'w') as f:
        # write the header
        f.write(','.join(map(str, ['Name', 'Program', 'Time_Executed', 'Status', 'Time_Taken'])) + '\n')
        for row in rows:
            f.write(','.join(map(str, row)) + '\n')

    conn.close()

    # Read the csv file and print the table without index
    df = pd.read_csv('assignments.csv')
    # Create a html file from the data frame
    df.to_html('assignments.html')
    
    print(df.to_string(index=False))
    print("\n\n")

if __name__ == "__main__":
    run_programs(folders)
    conn.close()
    get_table()