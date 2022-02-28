import datetime 
from  flask import Flask, jsonify
import json

from config import PORT
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home_page():
    time_list = []
    def home_time():

        Time = current_time = datetime.datetime.now() 
        Year = current_time.year
        Month = current_time.month       
        Day = current_time.day        
        Hour = current_time.hour        
        Minute = current_time.minute   
        Second = current_time.second 
        Microsecond = current_time.microsecond

        value = {
                'Time': Time,
                'Year': Year,
                'Month' : Month,
                'Day' : Day,
                'Hour': Hour,
                'Minute': Minute,
                'Second' : Second,
                'Microsecond' : Microsecond
        }
        time_list.append(value)
        New_List = json.dumps(time_list, indent =2, sort_keys=True, default=str)
        
        with open("data.json", "w", encoding="utf-8") as file:
            file.write(str(New_List))
    home_time()
    return jsonify(time_list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
