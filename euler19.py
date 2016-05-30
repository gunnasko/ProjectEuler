class Month:
    def __init__(self, name, numOfDays):
        self.name = name
        self.numOfDays = numOfDays

    def __eq__(self, other):
        return self.name == other.name


Months = [
Month("January",31),
Month("February",28),
Month("March",31),
Month("April",30),
Month("May",31),
Month("June",30),
Month("July",31),
Month("August",31),
Month("September",30),
Month("October",31),
Month("November",30),
Month("December",31)
]


Weeks = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
]

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

def incrementWeek(weekNum):
    if(weekNum >= 6):
        weekNum = 0
    else:
        weekNum = weekNum + 1
    return weekNum

def incrementDate(Date, Month, Year):
    numOfDaysInMonth =  Months[Month].numOfDays
    if isLeapYear(Year) and Months[Month].name == "February":
        numOfDaysInMonth = 29
        #print( Date, Months[Month].name, Year )


    if(Date >= numOfDaysInMonth):
        if(Month == len(Months) - 1):
            Year = Year+1
            Month = 0
        else:
            Month = Month+1
        Date = 1
    else:
        Date = Date+1

    return Date, Month, Year


Date = 1
Week = 0
Month = 0
Year = 1900

num = 0
while Year < 2001:
    Week = incrementWeek(Week)
    Date, Month, Year = incrementDate(Date, Month, Year)
    if Year > 1900 and Year < 2001:
        if Weeks[Week] == "Sunday" and Date == 1:
            num = num+1
            #print(Weeks[Week], Date, Months[Month].name, Year )

    #print(Weeks[Week], Date, Months[Month].name, Year )

print num
