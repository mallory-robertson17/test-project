#!/usr/bin/env python
import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()

print("1. What are the most popular three articles of all time?")
cursor.execute(
    "select articles.title, count(*) as number from authors, articles \
join log on log.path LIKE ('%' || (articles.slug)) where \
authors.id=articles.author group by articles.title order by number \
desc limit 3;"
)
for x in cursor.fetchall():
    print("\"" + x[0].title() + "\"" + " - " + str(x[1]))
print

print("2. Who are the most popular article authors of all time?")
cursor.execute(
    "select authors.name, count(*) as number from authors, articles \
join log on log.path ~~ ('%' || (articles.slug)) where \
authors.id=articles.author group by authors.name order by number desc;"
)
for x in cursor.fetchall():
    print(x[0] + " - " + str(x[1]) + " views")
print

print("3. On which days did more than 1% of requests lead to errors?")
cursor.execute(
    "select * from (select okay.date2, round(sum((error.num *100) ::\
numeric/(error.num+okay.num)), 2) as p from \
(select substr(CAST(time AS text),0,11) as date2, status, \
COUNT(*) as num from log where status like '2%' group by date2, \
status) as okay, (select substr(CAST(time AS text),0,11) as date1,\
status,COUNT(*) as num from log where status like '4%' group by \
date1, status) as error where okay.date2=error.date1 group by \
okay.date2) as totals where p>2;"
)
for x in cursor.fetchall():
    datetimeobject = datetime.strptime(x[0], '%Y-%m-%d')
    newformat = datetimeobject.strftime('%B %d, %Y')
    print(str(newformat) + " - " + str(x[1]) + "% errors")

conn.close()
