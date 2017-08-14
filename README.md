# ZeppelinTwitterAnalysis
parse streaming tweets into a TSV, then analyze with zeppelin

## A. Preparing the tweets
Acquiring the tweets and parsing the results was done in Python but there are many other choices. An important note to consider when running any of these scripts is that you will need to point your script to your python executable. Any of these scripts will need to be modified. <BR>
If you are interested in starting from scratch and acquiring the data, follow these steps:
* Get a twitter developer key here: https://dev.twitter.com
* Grab the secret key info and modify the file <b>stream.py</b>
* Run the streaming python script in the background: <b> ./stream.py & </b>
* Tweets will go to a file called <b>resmed.json</b>
* Wait...wait...wait...for tweets to collect
* The format of the output file will be one line of JSON per tweet
* To prepare the data to be read by Spark, we can parse it into a TSV with a Python script
* Create the TSV by applying the parsing script to output file: <b>cat resmed.json | ./parse.py > t.out</b>
* Adjust the parsing script as needed to extract additional fields

If you want to skip ahead to the parsing only:
* Use the existing file tweets.json and run the parse script: <b>cat tweets.json | ./parse.py > t.out</b>
* Or, the the file <b>twitter.out</b> can be used directly in Zeppelin since it is already parsed


## B. Getting started with zeppelin
Zeppelin is a notebook where you can use a variety of interpreters to run code and share output.
If you do not already have Zeppelin installed and running, here are some suggestions:
* Download and install Zeppelin: https://zeppelin.apache.org
* Once installed, start Zeppelin from the command line: <b>bin/zeppelin-daemon.sh start</b> (give it a minute to get started)
* Open this URL in a browser: http://localhost:8080 (you may need to configure ports or resolve the host)


## C. Analyzing the data with zeppelin
Using notebooks provides an effective visual record of your analysis that can be easily edited and shared with others. This example uses the Spark Scala commands to read the TSV file, create a date field and generate a Spark dataframe. Then SparkSQL commands are used to query and analyze the data; you could also build models and create graph frames and streaming apps as well. There are many other interpreters available in Zeppelin.
* Once Zeppelin is installed, running and accessible, click on the <b>"Import Note"</b> option on the main Zeppelin page
* Browse to the file and select <b>ZepNotebook.json</b>
* The interpreter should be set to default
* You should be able to interact with the notebook by running the commands and interacting with the output (play with the table and various graphing options
* <b>Important:</b> You will need to change the location of the TSV file containing the parsed tweets
* <b>Important:</b> You must run the first section of code without error to run any of the subsequent code sections because the data frame must be created. After that, the others can be run in any order.
