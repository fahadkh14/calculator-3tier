from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from datetime import datetime


app = Flask(__name__)

CORS(app)


# Database Configuration

db_config = {

    "host": os.getenv("DB_HOST", "db"),

    "user": os.getenv("DB_USER", "root"),

    "password": os.getenv("DB_PASSWORD", "password"),

    "database": os.getenv("DB_NAME", "calculator")

}



# Database Connection

def get_db():

    return mysql.connector.connect(**db_config)




# Home API

@app.route("/")
def home():

    return jsonify({

        "message":"🚀 Calculator Backend Running",

        "status":"success"

    })





# Calculate API

@app.route("/calculate", methods=["POST"])

def calculate():


    data = request.json


    num1 = data.get("num1")

    num2 = data.get("num2")

    operation = data.get("operation")



    result = None



    if operation == "add":

        result = num1 + num2



    elif operation == "sub":

        result = num1 - num2



    elif operation == "mul":

        result = num1 * num2



    elif operation == "div":


        if num2 == 0:

            return jsonify({

                "error":"Cannot divide by zero"

            }),400


        result = num1 / num2



    else:

        return jsonify({

            "error":"Invalid operation"

        }),400





    # Save History

    try:


        conn = get_db()

        cursor = conn.cursor()



        query = """

        INSERT INTO history

        (num1,num2,operation,result)

        VALUES(%s,%s,%s,%s)

        """



        cursor.execute(

            query,

            (

                num1,

                num2,

                operation,

                result

            )

        )



        conn.commit()



        cursor.close()

        conn.close()



    except Exception as e:


        print("Database Error:",e)




    return jsonify({

        "result":result,

        "operation":operation

    })







# History API

@app.route("/history", methods=["GET"])

def history():


    try:


        conn = get_db()

        cursor = conn.cursor(dictionary=True)



        cursor.execute(

            """

            SELECT *

            FROM history

            ORDER BY id DESC

            LIMIT 10

            """

        )


        data = cursor.fetchall()



        cursor.close()

        conn.close()



        return jsonify(data)



    except Exception as e:


        return jsonify({

            "error":str(e)

        }),500







if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
