import sqlite3

# Connect to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('./Database/coffeeshop.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL statement to create a new table
create_table_query = '''
CREATE TABLE IF NOT EXISTS Profit (
    total_profit FLOAT PRIMARY KEY,
    total FLOAT
);
'''

# Execute the SQL statement
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

#*****************************************************************
# Connect to the SQLite database
conn = sqlite3.connect('./Database/coffeeshop.db')
cursor = conn.cursor()

# Example: Update the total_profit for a specific record
update_query = '''
UPDATE Profit
SET total_profit = 1500.0  -- Set the new total_profit value
WHERE total = 500.0;  -- Specify the condition to identify the record to be updated
'''

# Execute the UPDATE statement
cursor.execute(update_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#**********************************************************************


# Connect to the SQLite database
conn = sqlite3.connect('./Database/coffeeshop.db')
cursor = conn.cursor()

# Example: Select all data from the Profit table
select_query = '''
SELECT * FROM Profit;
'''

# Execute the SELECT statement
cursor.execute(select_query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()

