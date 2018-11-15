#Project 1: Logs Analysis

##Summary:

####This program will output the following information regarding data from a news psql DB*	
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

	Example:
		"Princess Shellfish Marries Prince Handsome" — 1201 views
		"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
		"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

	Example:
		Ursula La Multa — 2304 views
		Rudolf von Treppenwitz — 1985 views
		Markoff Chaney — 1723 views
		Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

	Example:
		July 29, 2016 — 2.5% errors
		
##How to run
* If Vagrant and VirtualBox are not already installed, install them from:
** https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
** https://www.vagrantup.com/downloads.html

*Download Udacity's VM configuration:
** https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

* Downlod the news DB:
** https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

*   "From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
    
    When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!" -Udacity

* Move the newsdata.sql file into the shared vagrant directory (FSDN-Virtual-Machine/vagrant) You may need to unzip the newsdata.sql file.

*   "To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
    Here's what this command does:

        `psql` — the PostgreSQL command line program
        `-d news` — connect to the database named news which has been set up for you
        `-f newsdata.sql` — run the SQL statements in the file newsdata.sql
        Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data." -Udacity

####Make sure you are in the parent directory of the logsAnalysisProject.py file

enter:
	`python logsAnalysisProject.py`
	
The console should output the information 

##Sources
Some text used directly from Udacty'd course materials.'

##Author
###Mallory Robertson
	