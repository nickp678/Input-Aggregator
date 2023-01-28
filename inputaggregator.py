#build Menu
# options 1. Aggregate input in url 2. Check last website input number 3. Total Input number so far 4. List of Urls visited 5. Quit

import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

total = 0 #Total number of inputs aggregated for all websites
urls = [] #List of urls visited so far
temp1 = 0 #Temp holder for number of inputs in a website
urltemp = "" #Temp holder for last website url


def main():
	
	menu()


def menu():
	print("Hello, Welcome to the Input Aggregator...")
	print()
	
	choice = input("""
                      1: Aggregate inputs of a website
                      2: Check last website's information
                      3: Check total number of inputs
                      4: Check list of urls visited
                      5. Print data into a CSV file output
                      6. Quit

                      Please enter your choice: """)
	if choice == "1":
		search()
	elif choice == "2":
		lastwebsite()
	elif choice == "3":
		print("Total number of inputs so far is: " + str(total))
		menu()
	elif choice == "4":
		urlist()
	elif choice == "5":
		printtocsv()
	elif choice == "6":
		quit()
	else:
		print("Please provide a valid option.")
		menu()


def search():
	url = input("Enter the url you would like to search: ")
	global total
	global urls
	global urltemp
	global temp1
	driver = webdriver.Chrome()

	try:
		driver.get(url)
		input_elements = driver.find_elements(By.TAG_NAME, "input")
		urltemp = url
		
		print("The url you are searching for is: " + urltemp)
		print("The number of inputs in this website is: " + str(len(input_elements)))
		
		urls.append(url)
		temp1 = len(input_elements)
		total += len(input_elements)
		driver.quit()
	except:
		print("No Input Found :(")
		print("Please try again")
		menu()

	

	menu()

def lastwebsite():
	global temp1
	global urltemp
	print("Last visited website is: " + urltemp)
	print("Last visited website's number of inputs are: " + str(temp1))
	menu()

def urlist():
	global urls
	print("Here is the list of URLs you have visited: ")
	for i in urls:
		print(i)
	menu()


def printtocsv():
	global total
	global urls

	if len(urls) == 0:
		print("Please search some websites first")
		menu()
	elif len(urls) == 1:
		with open("inputaggregatoroutput.csv", 'w') as csvfile: 
			csvwriter = csv.writer(csvfile) 
        
    
			csvwriter.writerow(['Total Number of Inputs', str(total)]) 
			csvwriter.writerow(['Websites', urls[0]])

		print("Output to csv file complete! Please check directory :)")
		menu()
	else:		

		with open("inputaggregatoroutput.csv", 'w') as csvfile: 
			csvwriter = csv.writer(csvfile) 
        
    
			csvwriter.writerow(['Total Number of Inputs', str(total)]) 
			csvwriter.writerow(['Websites', urls[0]])
			for i in range(1,len(urls)):
				csvwriter.writerow(['', urls[i]])

		print("Output to csv file complete! Please check directory :)")
		menu()
        
    
    

main()