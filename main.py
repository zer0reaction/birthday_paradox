import datetime as d
import random as r


# generating an array of birthdays of given length
def generate_birthdays(number):
    birthdays = []
    date = d.date(2000, 1, 1)
    for i in range(int(number)):
        birthdays.append(date + d.timedelta(r.randint(0, 364)))
    return birthdays


# finding the birthdays which are on the same date
# returns the date if there is a match
# returns false if there is none
def find_match(birthdays):
    for a, dateA in enumerate(birthdays):
        for b, dateB in enumerate(birthdays):
            if not a == b and dateA == dateB:
                return dateA


# here is the part of user input and analyzing the statistics

# making a sample to analyze
sample = []  # the sample data (100 000 bday arrays)
num = input("Input the group size:\n> ")
for i in range(100_000):
    if i % 1000 == 0:
        print("{}% of generating samples".format(int(i / 1000)))
    sample.append(generate_birthdays(num))

# actually analyzing it
counter = 0  # a counter for matched birthdays in group (out of 100000)
for i in range(100_000):
    if i % 1000 == 0:
        print("{}% of analyzing samples".format(int(i / 1000)))
    if not find_match(sample[i]) is None:
        counter += 1

print("The possibility of having a birthday match in a {} people group is {}%".format(num, counter / 1000))
