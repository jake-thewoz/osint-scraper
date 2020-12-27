#!/usr/bin/python3
import sys, requests, webbrowser

# Check to see if the user used the command correctly
if len(sys.argv)!=2:
	sys.exit("Usage: osint-scraper <email>")

# Checking available email searches in browser
webbrowser.open('https://thatsthem.com/email/' + sys.argv[1])
webbrowser.open('https://www.skymem.info/srch?q=' + sys.argv[1] + '&ss=home')
webbrowser.open('https://www.google.com/search?q="' + sys.argv[1] + '"+filetype%3Apdf')
