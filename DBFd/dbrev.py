#Cody Brown, Exam 3 Review, Databases!

 # QUESTION, How many different errors may we get while coding in python?
    # 1) syntax errors
    # 2) logic errors
    # 3) exceptions

 # DATABASE INTRO
# a database is a file that is organized for storing data
    # might be organized like a dictionary (map from keys to values)
    # BIGGEST DIFFERENCE BTWN DICTIONARY: database is permanent!

# CREATING A DATABASE
# We can create our database
#-------
import dbm
    # it is another module!
firstdb = dbm.open("data","c")
#-------
    # after running, we have a new file in the DBFd folder, called data.db!

# What is the type of this new database?
#-------
t = type(firstdb)
print(t)
#-------
    # this prints <class '_dbm.dbm'>

 # UPDATED A DATABASE FILE
# import dbm
# firstdb = dbm.open('data','c')
    # these are commented out because they are done above, always remember to import
    # the dbm module!
#-------
firstdb["data_one"] = "my first data point!"
    # creates the 'data_one' with info
dp1 = firstdb['data_one']
print(dp1)
#-------
    # this prints
    # b'my first data point!'
        # the result of this is called a bytes object, which is why it starts with a b

 # REPLACING OLD VALUES
#Replacing old values is as simple as assigning the already existing key to another
#value!
#For example:
# import dbm
# firstdb = dbm.open('data','c')
# firstdb["data_one"] = "my first data point!"
# dp1 = firstdb['data_one']
# print(dp1)
    # commented out because done above
#-------
firstdb['data_one'] = 'actually, this is my first data point'
dp11 = firstdb['data_one']
print(dp11
#------
    # this prints:
    # b'my first data point!'   ##(from previous print line of first value)
    # b'actually, this is my first data point' ##(from the replacing and second print)

 # ADDING MORE ITEMS
# import dbm
import dbm
secdb = dbm.open("mygrades","c")

secdb['calculus'] = 'I currently have an A before the final'
secdb['psychology'] = 'I have an A in the class and will finish with an A'
secdb['physics'] = 'I currently have an A before the final, and the final is not cumulative!'
c = secdb['calculus']
psy = secdb['psychology']
phys = secdb['physics']
print(c)
print(psy)
print(phys)
    # this prints:
        # b'calculus' b'I currently have an A before the final'
        # b'psychology' b'I have an A in the class and will finish with an A'
        # b'physics' b'I currently have an A before the final, and the final is not cumulative!'
        
 # LOOPING OVER ITEMS IN A DATABASE
#We can use a for loop to iterate over items in a database and print them
for item in secdb.keys(): #makaes the for loop iterate, .keys() is necessary for it to work on macs
    print(item, secdb[item])
    # be sure to comment out the print functions from before before running
# this printed:
    # b'calculus' b'I currently have an A before the final'
    # b'psychology' b'I have an A in the class and will finish with an A'
    # b'physics' b'I currently have an A before the final, and the final is not cumulative!'
