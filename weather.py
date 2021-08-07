import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass
    parsedate = datetime.fromisoformat(iso_string)
    return "{} {:02d} {} {}".format(parsedate.strftime("%A"),parsedate.day,parsedate.strftime("%B"),parsedate.year)

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

    celcius = round((float(temp_in_farenheit) - 32) * 5 / 9,1)

    return celcius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

    total = 0.0
    for num in weather_data:
        total = total + float(num)
    average = float(total)/len(weather_data)

    return average

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

    with open(csv_file) as myCSV:
        reader = csv.reader(myCSV)
        header = next(reader)
        myData = []
        for line in reader:
            if (len(line)>0):
                myData.append([line[0], int(line[1]), int(line[2])])
                #myData.append(line)
    
    return myData

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass

    if (len(weather_data) > 0 ):
        minimum = float(weather_data[0])
        position = 0
        for i in range(1,len(weather_data)):
            #print(weather_data[i])
            if (float(weather_data[i]) <= minimum):
                minimum = float(weather_data[i])
                position = i
        return (minimum,position)
    else:
        return ()

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass

    if (len(weather_data) > 0):
        maximum = float(weather_data[0])
        position = 0
        for i in range(1,len(weather_data)):
            if (float(weather_data[i]) >= maximum):
                maximum = float(weather_data[i])
                position = i
        return (maximum,position)
    else:
        return ()

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
    numDays = len(weather_data)
    lowTempData = []
    highTempData = []
    for row in weather_data:
        lowTempData.append(row[1])
        highTempData.append(row[2])

    lowPos = find_min(lowTempData)
    highPos = find_max(highTempData)

    lowAvg = calculate_mean(lowTempData)
    highAvg = calculate_mean(highTempData)

    mySummary = f"{numDays} Day Overview\n"
    mySummary = mySummary + f"  The lowest temperature will be {format_temperature(convert_f_to_c(lowPos[0]))}, and will occur on {convert_date(weather_data[lowPos[1]][0])}.\n"
    mySummary = mySummary + f"  The highest temperature will be {format_temperature(convert_f_to_c(highPos[0]))}, and will occur on {convert_date(weather_data[highPos[1]][0])}.\n"
    mySummary = mySummary + f"  The average low this week is {format_temperature(convert_f_to_c(lowAvg))}.\n"
    mySummary = mySummary + f"  The average high this week is {format_temperature(convert_f_to_c(highAvg))}.\n"
    
    return (mySummary)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

    mySummary = ""
    for row in weather_data:
        mySummary += f"---- {convert_date(row[0])} ----\n"
        mySummary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n"
        mySummary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n"
        mySummary += "\n"

    return mySummary

        
         

# print (calculate_mean([49, 57, 56, 55, 53])) #54.0
# # print (format_temperature(90)) #90oC

# print (find_min(["49", "57", "56", "55", "53"]))  #(49.0, 0)
# print (find_max(["49", "57", "56", "55", "53", "49"])) #(57.0, 1)
# print (generate_daily_summary(load_data_from_csv(".\\tests\\data\\example_two.csv")))
