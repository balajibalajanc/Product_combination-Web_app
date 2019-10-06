import os
import csv
import new
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
field_names_list = []
@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'dataset/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        file_name_val=filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".csv") or (ext == ".xlsx"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    with open('dataset/'+file_name_val, 'r') as csvfile:
        readers = csv.reader(csvfile)
        for row in readers:
            field_names_list=row
            break
    field_names_list=field_names_list[1:]
    print(field_names_list)
    return render_template("test.html", resultf=field_names_list)

@app.route('/finalfunction/<string:name>', methods=['GET','POST'])
def para(name):
    dic={}
    dic = new.print_value(name)
    name = dic.keys()
    val = dic.values()
    results = list(map(str, name))
    items = [x * 100 for x in val]
    results2 = list(map(int, items))
    print(results)
    return render_template("main.html", result=results, result1=results2)


if __name__ == "__main__":
    app.run()