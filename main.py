from flask import Flask, render_template
from bs4 import BeautifulSoup 
import urllib2

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():


	#Donald
	req = urllib2.Request('http://donaldwoodson.tumblr.com', headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )
	soup=BeautifulSoup(con.read())
	d_title = soup.findAll('h2')[0].a.string
	d_title = d_title[2:]
	d_date = soup.findAll("div", { "class" : "column left" })[1].a.string
	# print d_title
	print d_date

	# steven
	req = urllib2.Request('https://kangexpress.wordpress.com', headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )
	soup=BeautifulSoup(con.read())
	s_title = soup.findAll('h1')[1].a.string
	s_date = soup.time.string
	# print s_title
	# print s_date

	# frank
	req = urllib2.Request('http://www.frankjwu.com', headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )
	soup=BeautifulSoup(con.read())
	f_title = soup.section.div.a.string
	f_date = soup.section.section.string
	# print title
	# print date

	# jonathan
	req = urllib2.Request('http://jchang.me/posts.html', headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )
	soup=BeautifulSoup(con.read())
	j_title = soup.section.a.string
	j_date = soup.section.small.string

	#ktizzel
	req = urllib2.Request('http://www.ktizzel.com/blog', headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )
	soup=BeautifulSoup(con.read())

	k_date = soup.find_all("p")[-1].string
	if (len(soup.find_all("div")[-2].find_all("h1"))>0):
		k_title = soup.find_all("div")[-2].find_all("h1")[-1].string
	else:
		k_title = ""

	# print kt_title
	# print kt_date


	return render_template('consortium.html', f_title = f_title, f_date = f_date, j_title = j_title, j_date =j_date, k_title =k_title, k_date = k_date, s_title=s_title, s_date=s_date, d_title = d_title, d_date = d_date)

if __name__ == '__main__':
    app.run()