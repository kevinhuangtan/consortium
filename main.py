from flask import Flask, render_template
from bs4 import BeautifulSoup 
import urllib2
from apscheduler.scheduler import Scheduler

app = Flask(__name__)
app.debug = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# class Blog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)\
#     person = db.Column(db.String(80), unique=True)
#     title = db.Column(db.String(80), unique=True)
#     date = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username

blogs = {'p_title':'title', 'p_date':'date', 'd_title':'title', 'd_date':'date', 's_title':'title', 's_date':'date', 'f_title':'title', 'f_date':'date', 'j_title':'title', 'j_date':'date', 'k_title':'title', 'k_date':'date'}
variable = 1
dictionary = {'name': 'kevin'}
def job():
	with app.app_context():

		#Pat
		req = urllib2.Request('https://pwilz.wordpress.com/', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())
		blogs['p_title'] = soup.findAll('h1')[1].a.string
		blogs['p_date'] = soup.findAll('time')[0].string
		# print blogs['d_title']
		# print blogs['p_date']

		#Donald
		req = urllib2.Request('http://donaldwoodson.tumblr.com', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())
		# print soup.findAll('h2')[0]
		blogs['d_title'] = soup.findAll('h2')[0].string
		blogs['d_title'] = blogs['d_title'][2:]
		blogs['d_date'] = soup.findAll("li", { "class" : "date" })[0].a.text
		# print blogs['d_date']
		# blogs['d_date'] = soup.findAll('span')[5]
		# print blogs['d_title']

		# steven
		req = urllib2.Request('https://kangexpress.wordpress.com', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())
		blogs['s_title'] = soup.findAll('h1')[1].a.string
		blogs['s_date'] = soup.time.string
		# print blogs['s_title']
		# print blogs['s_date']

		# frank
		req = urllib2.Request('http://www.frankjwu.com', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())
		blogs['f_title'] = soup.section.div.a.string
		blogs['f_date'] = soup.section.section.string
		# print title
		# print date

		# jonathan
		req = urllib2.Request('http://jchang.me/posts.html', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())
		blogs['j_title'] = soup.section.a.string
		blogs['j_date'] = soup.section.small.string

		#ktizzel
		req = urllib2.Request('http://www.ktizzel.com/blog', headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		soup=BeautifulSoup(con.read())

		blogs['k_date'] = soup.find_all("p")[-3].string
		if (len(soup.find_all("div")[-4].find_all("h1"))>0):
			blogs['k_title'] = soup.find_all("div")[-4].find_all("h1")[-1].string
		else:
			blogs['k_title'] = ""
		# print kt_title
		# print kblogs['t_date']
		return


@app.before_first_request
def initialize():
    apsched = Scheduler()
    apsched.start()

    apsched.add_interval_job(job, seconds=3600)
    #43200

@app.route('/')
def hello_world():
	return render_template('consortium.html', f_title = blogs['f_title'], f_date = blogs['f_date'], j_title = blogs['j_title'], j_date =blogs['j_date'], k_title =blogs['k_title'], k_date = blogs['k_date'], s_title=blogs['s_title'], s_date=blogs['s_date'], d_title = blogs['d_title'], d_date = blogs['d_date'], p_title = blogs['p_title'], p_date = blogs['p_date'])



if __name__ == '__main__':
	job()
	app.run()


