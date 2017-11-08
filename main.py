# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import os

def run():

	response = requests.get("https://platzi.com/cursos/")
	soup = BeautifulSoup(response.content, "html.parser")

	careers_names = getCareers(html=soup)
	saveFile("careers.txt", careers_names)

	courses_names = getCourses(html=soup)
	saveFile("courses.txt", courses_names)

	getCoursesImages(html=soup)


def getCareers(html):

	careers_titles = html.find_all(class_="Career-name")

	file_content = ""

	for career in careers_titles:
		file_content += "{0} \n".format(career.text.encode('utf-8'))

	return file_content		

def getCourses(html):

	courses_titles = html.find_all(class_="CareerCourse-name")

	file_content = ""

	for course in courses_titles:		
		file_content += "{0} \n".format(course.text.encode("utf-8"))

	return file_content

def getCoursesImages(html):

	courses_containers = html.find_all(class_="CareerCourse-primary")

	file_content = ""

	if not os.path.exists("img"):
		os.mkdir("img")

	for course in courses_containers:
		image_url = course.find("img")["src"]
		file_extension = image_url.split(".")[-1]

		course_container = course.find(class_="CareerCourse-name")
		course_name = course_container.text.encode('utf-8')
		course_name = course_name.strip()
		course_name = course_name.replace(" ", "_")

		file_name = "{0}.{1}".format(course_name, file_extension)
		
		print("Downloading {0}".format(file_name))

		urllib.urlretrieve(image_url, "img/{0}".format(file_name))

def saveFile(fileName, content):
	
	with open(fileName, "w") as file:
		file.write(content)

	print("File created: {0}".format(fileName))


if __name__ == "__main__":
	run()