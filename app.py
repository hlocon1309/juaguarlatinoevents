from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/') 
def index(): 
    # Connect to the database 
    conn = psycopg2.connect(database = "testdb",
                        user="haroldo",
                        password="Russi@2021",
                        host="localhost",
                        port="5432")
  
    # create a cursor 
    cur = conn.cursor() 
  
    # Select first three elements from active events to show
    cur.execute('''select events.event_name, to_char(events.start_date, 'DD-MM-YYYY'), event_data.sale_price from events inner join event_data on events.id_event=event_data.id_event limit 3;''') 
  
    # Fetch the data 
    data = cur.fetchall() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return render_template('index.html', data=data)




if __name__ == '__main__': 
    app.run(debug=True) 