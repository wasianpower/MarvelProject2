#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= harrington1

all: PutCGI PutHTML

PutCGI:
	chmod 757 marvelsearchproxy.py
	cp marvelclient.py /usr/lib/cgi-bin/$(USER)_marvelclient.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp marvelsearch.html /var/www/html/class/softdev/$(USER)/marvelsearch2/
	cp marvelsearch.css /var/www/html/class/softdev/$(USER)/marvelsearch2/
	cp marvelsearch2.js /var/www/html/class/softdev/$(USER)/marvelsearch2/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(USER)/marvelsearch2/
