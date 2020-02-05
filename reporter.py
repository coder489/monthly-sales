# reporter.py

import os
import pandas
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


print("READING GRADEBOOK CSV FILE...")
# if CSV file in same dir as this Python script:
# csv_filepath = "gradebook2.csv"
# if CSV file in the data dir:
# csv_filepath = "data/gradebook.csv"


csv_filepath = os.path.join(os.path.dirname(__file__), "data", "gradebook.csv")
print("FILEPATH:", os.path.abspath(csv_filepath))
grades = pandas.read_csv(csv_filepath)
print("GRADES:", type(grades))


#print(dir(grades))
print(grades.tail())
# grades["student_id"]
# grades["final_grade"]



## Objectives

##Find an average grade

average_grade = grades["final_grade"].mean()
print("AVERAGE GRADE: ", average_grade)


##Loop through all rows
#Use for loop



