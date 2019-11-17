#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= harrington1

all: PutCGI PutHTML

PutCGI:
	chmod 757 search.py
	cp search.py /usr/lib/cgi-bin/$(USER)_search.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp artmedia.html /var/www/html/class/softdev/$(USER)/artmedia/
	cp artmedia.css /var/www/html/class/softdev/$(USER)/artmedia/
	cp artmedia.js /var/www/html/class/softdev/$(USER)/artmedia/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(USER)/artmedia/
