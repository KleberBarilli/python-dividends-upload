from datetime import date
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
from src.controller.prepare_excel_data import PrepareExcelData
from src.database.postgres import Database
from datetime import datetime

load_dotenv(find_dotenv())
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["UPLOAD_FOLDER"] = "tmp"

database = Database(os.environ['DB_HOST'], os.environ['DB'],
                    os.environ['DB_USER'], os.environ['DB_PASSWORD'])
db = database.get_db_connection()


def unlink_file(file_path):
    return os.unlink(file_path)


@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload_excel']
        if upload_file.filename != '':
            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"], upload_file.filename)
            upload_file.save(file_path)
            data = pd.read_excel(upload_file)
            data['Data'] = pd.to_datetime(data['Data']).dt.date
        p = PrepareExcelData(data, db)
        print(p.prepare())
        unlink_file(file_path)
        return render_template("imported-excel-data.html", data=data.to_html(index=False).replace('<th>', '<th style="text-align:center">'))
    return render_template("upload-excel.html")


if __name__ == '__main__':
    app.run(debug=True)
