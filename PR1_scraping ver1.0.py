# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:00:19 2019

@authors: Daura Hernández Díaz; Xiaowei Cai 
"""

#Import the modules which will be used in this script.

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

#Please enter an absolute path where you would like to generate the results of webscraping.
#For Windows users, the format of directory should be 'D:\\XXX\\XXX' or 'D:/XXX/XXX'. 
localdirection = "C:\\Users\\Xiaowei\\Desktop\\UOC学习\\Tipología y ciclo de vida de los datos\\Pr1\\"

#Users are required to in put the type of historical data, initial day, end day, name of station and direction where they want to save the results of webscraping.

#There are four types of historical data, which are Horario, OctoHorario, Diario and Mensual
data_type_input = input("Please enter the type of data:")

#Input initial date.
initial_day_input = input("Please enter the initial day(An integer):")
initial_month_input = input("Please enter the initial month(In Spanish. e.g. Marzo):")
initial_year_input = input("Please enter the initial year(An integer):")

#Input end date.
end_day_input = input("Please enter the end day(An integer):")
end_month_input = input("Please enter the end month(In Spanish. e.g. Marzo):")
end_year_input = input("Please enter the end year(An integer):")

#Input the name of station.
station_name = input("Please enter the station name(In Spanish. e.g. San Isidro):")

#Use headless web navigator is used to reach the targeted page. 
driver = webdriver.Chrome()
driver.get("http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do")

#We set a few seconds delay at each step to circumvent the server blockade.
time.sleep(3)

#The web crawler will input the required information automatically to bypass the barriers of JavaScript.
#Input the type of historical data.
historical_type = Select(driver.find_element_by_id('pinteg'))
historical_type.select_by_visible_text(data_type_input)

#Input the initial date.
time.sleep(2)
initial_data = Select(driver.find_element_by_id('selMesIni'))
initial_data.select_by_visible_text(initial_month_input)
initial_year = Select(driver.find_element_by_id('selAnioIni'))
initial_year.select_by_visible_text(initial_year_input)
time.sleep(2)
driver.find_element_by_id('cal1').find_element_by_link_text(initial_day_input).click()

#Input the end date.
time.sleep(2)
final_data = Select(driver.find_element_by_id('selMesFin'))
final_data.select_by_visible_text(end_month_input)
initial_year = Select(driver.find_element_by_id('selAnioFin'))
initial_year.select_by_visible_text(end_year_input)
time.sleep(2)
driver.find_element_by_id('cal2').find_element_by_link_text(end_day_input).click()

#Input the name of station.
time.sleep(2)
station = Select(driver.find_element_by_id('tbEstaciones'))
station.select_by_visible_text(station_name)

#Acquire all the parameters of air quality.
time.sleep(2)
parameters = Select(driver.find_element_by_id('tbParametros'))
parameters.select_by_visible_text('Todos los parámetros')

#Click the "Agregar" button.
time.sleep(3)
driver.find_element_by_css_selector("[type='button']").click()

#Click the "Enviar consulta" button.
time.sleep(2)
driver.find_element_by_xpath("/html//input[@id='btEnviar']").click()

#Acquire the html code of the page of results.
time.sleep(3)
canarias_source = driver.page_source
canarias_soup = BeautifulSoup(canarias_source,'html.parser')

#Locate all the tables.
tableoriginal = canarias_soup(class_='tablaDisplayTag')

#Scrap all the table one by one and save the results as csv file(s).
for i in range(0,len(tableoriginal)):
    table = tableoriginal[i]

    canariasvariables = ""
    for variables in table.findAll('th'):
        if canariasvariables.find('PM2,5'):
            canariasvariables = canariasvariables.replace('PM2,5','PM2.5')
        canariasvariables = canariasvariables+","+variables.text
    canariasvariables = canariasvariables.replace(",\n", "")

    canariasdatasaved = ''
    for record in table.findAll('tr'):
        canariasdata = ""
        for data in record.findAll('td'):
            canariasdata = canariasdata+","+data.text   
        if len(canariasdata) != 0:
            canariasdatasaved = canariasdatasaved + "\n" +canariasdata[1:]                    
        
    finaldata = canariasvariables +canariasdatasaved
    
    file = open(localdirection+"table"+str(i+1)+".csv","wb")
    file.write(bytes(finaldata,encoding="UTF-8"))
    file.close()

#Print a message to confirm the whole process of webscraping has been completed successfully.
print("\nCongratulations! The dataset(s) you required has already been generated!")