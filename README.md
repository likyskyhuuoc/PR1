# AIR POLLUTION DATA IN CANARY ISLANDS AND QUALITATIVE DATA FROM TWITTER

This is an assignment of the course "Typology and life cycle of the data", belonging to Master of Data Science of the Open University of Catalonia. In this study, we intend to scrap data from a governmental website of the Canary Islands, which provides a variety of air quality indicators across the Canary Islands. Moreover, we implemented the code to reach the Twitter data by using the functions established by Russell & Klassen (2019). 

# Members of the group
This activity is realised collectively by two persons: Daura Hernández Díaz and Xiaowei Cai.

# Contents
<ul>
<li><strong>PR1_scraping ver1.0.py</strong>：It contains the Python code to scrap the data from <a href="url">the governmental website of the Canary Islands </a>.</li>
<li><strong>PR1_twitter ver1.0.py</strong>：It contains the Python code to use the Twitter API</li>
<li><strong>table1.csv</strong>：An output example after conducting PR1_scraping ver1.0.py</li>
<li><strong>table2.csv</strong>：An output example after conducting PR1_scraping ver1.0.py</li>
<li><strong>table3.csv</strong>：An output example after conducting PR1_scraping ver1.0.py</li>
<li><strong>Air pollution.json</strong>：An output example after conducting PR1_twitter ver1.0.py</li>
</ul>

# How to use?
## Crawler
To acquire the results of air quality, users need to input historical data type (per hour, each eight-hour, daily, or monthly), date (initial and end date), air monitoring station, and air index. Be sure you have installed the following modules: time, BeautifulSoup, and selenium. Additionally, make sure that ChromeDriver(a headless explorer) has been installed and added into environmental path.

Please follow the steps below to acquire the results from the governmental website of the Canary Islands:
1. Enter a local directory for the variable 'localdirection'.
2. Run the code.
3. Enter the information that you request.
4. Check the results in your directory. 

The results will be represented in csv files and here are the explanations of the variables:<br>
<strong>Fecha:</strong> Date. The format is Day-Month-Year.<br>
<strong>Hora:</strong> Time. 24-hour system.<br>
<strong>SO2:</strong> Concentration of SO2 - μg / m³.<br>
<strong>NO:</strong> Concentration of NO - μg / m³.<br>
<strong>NO2:</strong> NO2 - Concentration of NO2 - μg / m³.<br>
<strong>NOX:</strong> Concentration of NOX - μg / m³.<br>
<strong>PM10:</strong> Particles in suspension < 10um - μg / m³.<br>
<strong>PM2.5:</strong> Particles in suspension & lt; 2,5um - μg / m³.<br>
<strong>CO:</strong> Concentration of CO - mg / m³.<br>
<strong>O3:</strong> Concentration of O3 - μg / m³.<br>
<strong>VV:</strong> Wind speed (Velocidad del viento)- m / s.<br>
<strong>DD:</strong> Wind direction(Direccion del viento) – Grd.<br>
<strong>TMP:</strong> Average temperature(Temperatura media) - ºC.<br>
<strong>HR:</strong> Relative humidity(Humedad relativa) -%.<br>
<strong>PRB:</strong> Barometric pressure(Presion barometrica) – mb.<br>

table1.csv, table1.csv, and table1.csv form an example with the following information:
<strong>type of historical data:</strong> ‘Horario’
<strong>time period:</strong> from 01/03/2019 to 01/04/2019
<strong>station:</strong> La Grama-Breña Alta

## Twitter API
To acquire the results from Twitter, please assign what you would like to search to the variable 'q' and specify the number of maximum results in the function twitter_search(). Make sure that the following modules have been install: twitter, and json.
Please note that the following functions are developed by Russell & Klassen (2019):
twitter_search()
save_json()
load_json()

Please follow the steps below to acquire the results from the governmental website of the Canary Islands:
1. Enter a local directory for the variable 'localdirection'.
2. Enter your credentials of Twitter API:
CONSUMER_KEY =''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
3. Run the code.
4. Enter the information that you request.
5. Check the results in your directory. 

The results will be represented in JSON format. Air pollution.json is an example of the output, which was acquired by entering 'Air pollution' as the content for searching and the maximum results were 5. 

# Reference
Russell, M. A., & Klassen, M. (2019). Mining the Social Web: Data Mining Facebook, Twitter, LinkedIn, Instagram, GitHub, and More. O’Reilly Media, Inc.
