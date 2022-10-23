from flask import Flask,render_template,request,jsonify
import os
import pandas as pd
from src.controller.prepare_excel_data import PrepareExcelData

app=Flask(__name__)
app.secret_key="123"

app.config["UPLOAD_FOLDER"]="tmp"



def unlink_file(file_path):
    return os.unlink(file_path)

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload_excel']
        if upload_file.filename != '':
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], upload_file.filename)
            upload_file.save(file_path)
            data=pd.read_excel(upload_file)
            p = PrepareExcelData(data)
            p.prepare()
            unlink_file(file_path)
            return render_template("imported-excel-data.html",data=data.to_html(index=False).replace('<th>','<th style="text-align:center">'))
    return render_template("upload-excel.html")


if __name__=='__main__':
    app.run(debug=True)