from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aditya'
app.config['MYSQL_DATABASE_DB'] = 'Metro'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/info/')
def info():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT distinct sname from metro_facility")
	data = cursor.fetchall()
	return render_template('info.html',data=data)

@app.route('/directions/')
def directions():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT distinct sname from metro_facility")
	data = cursor.fetchall()
	return render_template('directions.html',data=data)

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/review/')
def review():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT distinct sname from metro_facility")
	data = cursor.fetchall()
	return render_template('review.html',data=data)

@app.route('/review2/')
def review2():
	name = request.args.get('stat_name')
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT title,author,timest,bodytext from reviews where sname = '"+ name +"'")
	review = cursor.fetchall()
	return render_template('review2.html',review=review)

'''@app.review('/add_rev') #ISSSSSSUE
def add():
	msg = "Error, please try again"
	if request.method == 'POST':
		stat = request.form['stat']
		title = request.form['title']
		desc = request.form['desc']
		author = request.form['author']
		cursor = mysql.connect().cursor()
		#cursor.execute("INSERT into reviews values ("'+ stat + '","' + title + '","' + author + '", now() ,"'+desc +'")
		msg = "Review has been added"
		return render_template('/added',msg=msg)'''



@app.route('/authenticate', methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		user = request.form['InputEmail']
		passw = request.form['InputPassword']
		cursor = mysql.connect().cursor()
		cursor.execute("SELECT count(*) from metro_admin where username='" + user + "' and password='" + passw + "'")
		count = cursor.fetchone()
		if count == 1:
			return render_template('admin.html')
		else:
			error = 'Invalid username/password'
			return render_template('error.html', error=error)

@app.route('/directions2', methods=['POST', 'GET'])
def dir_actual():
	if request.method == 'POST':
		source = request.form['source']
		dest = request.form['dest']
		cursor = mysql.connect().cursor()
		cursor.execute("CALL find_path('"+ source +"','"+ dest +"')")
		data = cursor.fetchall()
		return render_template('directions2.html',data=data,source=source,dest=dest)
	else:
		return redirect(url_for('directions'))

@app.route('/info2', methods=['POST','GET'])
def info_actual():
	if request.method == 'POST':
		name = request.form['stat_name']
		cursor = mysql.connect().cursor()
		cursor.execute("SELECT * from metro_facility where sname = '" + name + "'")
		infor = cursor.fetchone()
		cursor.execute("SELECT * from metro_stations where sname = '" + name + "'")
		inform = cursor.fetchall()
		cursor.execute("SELECT pname from metro_places where sname = '" + name + "'")
		informa = cursor.fetchall()
		return render_template('info2.html',infor=infor,inform=inform,informa=informa)
	else:
		return redirect(url_for('info'))

@app.route('/nearest/<info>')
def closer(info):
	if info == 'pin':
		pincode = request.args.get('code')
		cursor = mysql.connect().cursor()
		cursor.execute("SELECT sname from metro_facility where pincode = '"+ pincode +"'")
		stations = cursor.fetchall()
		return render_template('nearest2.html',stations=stations)
	if info == 'near':
		place = request.args.get('by')
		cursor = mysql.connect().cursor()
		cursor.execute("SELECT sname from metro_places where pname = '" + place +"'")
		stations = cursor.fetchall()
		return render_template('nearest2.html',stations=stations)
	return render_template('nearest.html')


@app.route('/nearest/')
def trial():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT distinct pincode from metro_facility")
	data = cursor.fetchall()
	cursor.execute("SELECT distinct pname from metro_places order by sname")
	names = cursor.fetchall()
	return render_template('nearest.html',data=data, names=names )

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
