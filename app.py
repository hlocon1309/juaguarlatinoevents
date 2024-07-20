from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'jaguarlatinoevents'

@app.route('/') 
def index(): 
    # Connect to the database 
    conn = psycopg2.connect(database="testdb",
                        user="haroldo",
                        password="Russi@2021",
                        host="localhost",
                        port="5432")
  
    # create a cursor 
    cur = conn.cursor() 
  
    # Select first three elements from active events to show
    cur.execute('''select events.event_name, to_char(events.start_date, 'DD-MM-YYYY'), event_data.sale_price from events inner join event_data on events.id_event=event_data.id_event limit 3;''') 
  
    # Fetch the data from events
    evnt = cur.fetchall() 
    print(evnt)
  
    # close the cursor and connection 
    cur.close() 
    conn.close()

    if 'username' in session:
        return render_template('index.html', data=evnt, username=session['username'])
    else:
        return render_template('index.html', data=evnt)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #return '<h1>Page Found but not Implemented</h1>'
        username = request.form['demail']
        pwd = request.form['dpassword']

        # Connect to the database 
        conn = psycopg2.connect(database="testdb",
                    user="haroldo",
                    password="Russi@2021",
                    host="localhost",
                    port="5432")
        # create a cursor 
        cur = conn.cursor() 
        
        cur.execute('''select user_name, user_mail, user_passw from users where user_mail = %s; ''', (username,) )
        
        # Fetch the data from events
        user = cur.fetchone()
        print(user)

        # close the cursor and connection 
        cur.close() 
        conn.close()

        if user and pwd == user[2]:
            session['username'] = user[0]
            return redirect("/#home")
        else:
            return render_template('login.html', error='Invalid usermail and password')
     
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #return '<h1>Page Found but not Implemented</h1>'
        uname = request.form['duser']
        username = request.form['demail']
        pwd = request.form['dpassword']

        # Connect to the database 
        conn = psycopg2.connect(database="testdb",
                    user="haroldo",
                    password="Russi@2021",
                    host="localhost",
                    port="5432")
        # create a cursor 
        cur = conn.cursor() 
        
        cur.execute('''insert into users (user_name, user_surname, user_mail, user_passw, user_phone, date_created, user_type) values \
                    (%s, ' ', %s, %s, '+', '2024-07-20 08:00:00', 3);''', (uname, username, pwd) )
        
        # Fetch the data from events
        # commit the changes 
        conn.commit() 

        # close the cursor and connection 
        cur.close() 
        conn.close()

        return redirect("/#home")
      
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/#home')
    



if __name__ == '__main__': 
    app.run(debug=True) 