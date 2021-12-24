facebook pages and groups to rss 


dependices 
-facebook scraber 

 https://github.com/kevinzg/facebook-scraper
 to install 
 pip install facebook-scraper
-rfeed 
 file included in reboo 
 original rebo ->> https://github.com/svpino/rfeed

configuration 

there is to lists in fbrss.py on for groups and another for pages

the output for this program is xml text that should be written in 
rss file
 so use this 
python fbrss.py > rss.xml
 then rss could be hosted in local or remote server 


for rss reading iam using feeder in android 

==to do 
	- limit num of post that is colected with day or count
	- add saving to file outomatically so it could be outomated
	  with cron jop
	- clean rfeed.py from unnessecer class
	- make seperate file for lists or json file 
	- add remote hosting for feeds
