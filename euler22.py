import csv
import string


def get_names():
    returnlist = []
    with open('p022_names.txt', 'rb') as csvfile:
        content = csv.reader(csvfile, delimiter=",")
        for line in content:
            for i in line:
                returnlist.append(i)
    return returnlist

#print get_names()

def sort_names(names):
    return sorted(names)

def char_worth(char):
    return string.uppercase.index(char) + 1

def name_worth(name):
    return sum(map(char_worth, name))

def calculate_score(name, pos):
    return name_worth(name)*pos

print calculate_score("COLIN",938)

def get_sum_of_scores(names):
    sum_num = 0
    for i in range(0,len(names)):
        if names[i] == "COLIN":
            print i
        sum_num = calculate_score(names[i],i+1) + sum_num
    return sum_num

print get_sum_of_scores(sort_names(get_names()))
