#ile = "file_name.txt"
#####print(split_data)


#  data_list = temp.readlines()
#  print(data_list)

#Write a function write_file(filename, a_string, mode) that takes the three parameters, as shown, and creates a new file, of the name given as a parameter, and writes the string parameter to that file. 
#  We’ll use this function to create the .txt files for the next 6 exercises.
1
#def write_file(filename, a_string,mode):
  #  filename.write(a_string)
 


#def open_file(filename, option = "read"):
#if user puts nothing in 2nd position, it defaults to read


# a = append , w = write
# MAKE NEW TEXT DOC
#PROBLEM 1
def write_file(filename, a_string, mode):
  with open(filename, mode) as f:
     f.write(a_string)


#PROBLEM 2
def open_file(filename, mode):
    with open(filename, 'r') as f:
        if mode == 'read':
            return f.read()
        elif mode == 'readlines':
            return f.readlines()

      

#Write a function, printFile(file), that prints the contents of the file named “filename” to screen. 
def printFile(file):
  with open(file, "r") as f:
    print(f.read())

printFile("file_name.txt")

#PROBLEM 4
def sumColumn(filename):
 counter = 0 
 with open(filename, "r") as f:
  for line in f:
    counter += int(line)

  print(counter)
sumColumn("sum_col.txt")

#Problem 5
def sumAll(filename):
  total = 0
  with open(filename, "r") as f:
    for line in f:
      num = line.split()
      for n in num:
        total += int(n)
  print(total)
sumAll("sumAllExample.txt")

#Problem 6
def readColumn(filename, columnNo):
  columnNo = columnNo -1 
  columnnum = []
  with open(filename, "r") as f:
    
    for line in f:
      numList = line.strip()
      splitLine = numList.split()
    #  for num in enumerate(splitLine):
      columnnum.append(splitLine[columnNo])
  print(columnnum)
        
readColumn("readColumnExample.txt", 1)

# Problem 7

def countWord(filename, words):
  counter = 0
  with open(filename, "r") as f:
    readtext = f.read()
    text = readtext.lower()
  wordcounts = text.split()
  word_count_dict = {}
  for word in words:
    word_lower = word.lower()
    count = wordcounts.count(word_lower)
    word_count_dict[word_lower] = count
  output = "Word    Number of Times It Appears"
  for word, count in word_count_dict.items():
    output += f"\n{word}      {count}"
  
  write_file("wordcount.txt", output, "w")
    

countWord("zenofPython.txt", ["if", "better", "simple"])


#EXTRA CREDIT
#make dictionaries for each pres
def make_pres_dict(filename = "presidents.txt"):
  
  president_names = {}
  president_year = {}
  president_num = {}
  with open (filename, "r") as f:
    for line in f:
      linesplit = line.split()
      for char in linesplit:

        no_comma = char.strip(",")
    pres_idenfication = no_comma[0]
    name = no_comma[1]
    party = no_comma[2]
    term = no_comma[3]

  president_num[pres_idenfication] = (name, party, term)
  
  last_name_upper = name[-1]
  last_name = last_name_upper.lower()
  president_names[last_name] = (president_num, name, party, term)

  if "-" in term:
    years = term.split("-")
    first_year = years[0]
    last_year = years[-1]
    for year in range(first_year, last_year + 1):
      president_year[year] = name
  else: 
    president_year[term] = name
  
  
  return president_names, president_year, president_num

  
def user_input ():
  print("Type 1 for \"I know the president’s last name and want information about him.\" \n" \
  "Type 2 for \"I know the year the president was in office and want to know the president.\" \n"\
  "Type 3 for \"I know the presidents number (1-44) and want to know the president.\" ")
  int(input("Enter choice (1-3): "))






def pres_name(president_names):
  last = input("Enter the president's last name: ")
  return last
          
def pres_year(president_year):
  year = input("Enter the president's first year in office: ")
  return year
 

def pres_number(president_num):
  pres_num = input("Enter the president's number: ")
  return president_num
  


def main(): 
  president_names, president_year, president_num = make_pres_dict()
  choice = user_input()
  if choice == 1:
    result = pres_name(president_names)
    print(result)
  elif choice == 2:
    result = pres_year(president_year)
    print(result)
  elif choice == 3:
    result = pres_number(president_num)
    print(result)
  else:
    print("Sorry! Enter a digit 1-3.")
  


main()








