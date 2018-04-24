from flask import Flask, render_template, request

import json


w = json.load(open("worldl.json"))
lota=sorted(list(set([c['name'][0] for c in w])))

print(lota)
for c in w:
	c['tld'] = c['tld'][1:]
page_size = 20
app = Flask(__name__)

@app.route('/')
def mainPage():
	return render_template('index.html',
		page_number=0,
		page_size=page_size,
		w = w[0:page_size],lota=lota)
		

@app.route('/begin/<b>')
def beginPage(b):
	bn = int(b)
	return render_template('index.html',
		w = w[bn:bn+page_size],
		page_number = bn,
		page_size = page_size,
		lota=lota
		)

@app.route('/continent/<a>')
def continentPage(a):
	cl = [c for c in w if c['continent']==a]
	return render_template(
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a
		)
@app.route('/startWithAlphabetic/<a>')
def startWithAlphabetic(a):
	cl = [c for c in w if c['name'][0]==a]
	return render_template(
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a,
		lota=lota
		)
@app.route('/country/<i>')
def countryPage(i):
	return render_template(
		'country.html',
		c = w[int(i)])

@app.route('/countryByName/<n>')
def countryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country.html',
		c = c)

@app.route('/delete/<n>')

def deleteCountryPage(n):
	i=0
	for c in w:
		if c['name'] == n:
			break

		i+=1

	del w[i]
	return render_template('index.html',
		page_number=0,
		page_size=page_size,
		w = w[0:page_size])
#all deleted country will be back on the list after restarting the server

@app.route('/editcountryByName/<n>')
def editcountryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country-edit.html',
		c = c)


@app.route('/updatecountrybyname')
def updatecountryByNamePage():
	c=None
	n=request.args.get('name')
	c={}
	for x in w:
		if x['name'] == n:
			c = x
	#c['name']=request.args.get('name')
	c['capital']=request.args.get('capital')
	c['continent']=request.args.get('continent')
	c['area']=int(request.args.get('area'))
	c['population']=int(request.args.get('population'))
	c['gdp']=int(request.args.get('gdp'))
	c['tld']=request.args.get('tld')
	#w.append(c)
	return render_template(
		'country.html',
		c = c)



@app.route('/savecountrybyname')
def savecountryByNamePage():
	c={}
	c['name']=request.args.get('name')
	c['capital']=request.args.get('capital')
	c['continent']=request.args.get('continent')
	c['area']=int(request.args.get('area'))
	c['population']=int(request.args.get('population'))
	c['gdp']=int(request.args.get('gdp'))
	c['tld']=request.args.get('tld')
	w.append(c)
	return render_template(
		'country.html',
		c = c)

@app.route('/createcountrybyname')
def createcountryByNamePage():
	c=None
	return render_template(
		'createcountrybyname.html',c=c)

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5623, debug=True)




