from flask import Flask,render_template,request,redirect,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
@app.route("/",methods=["GET"])
def func1():
    # return jsonify({"in":"progress"})
    data = Todo.query.all()
    data_list = [{"title": item.title, "desc": item.desc} for item in data]
    size=len(data_list);
    d={}
    i=1
    for temp in data_list:
        d[f"{i}"]=temp
        i=i+1
    json_data = jsonify(d)

    return json_data
    
      
@app.route("/del",methods=["POST"])
def func2():
    a=request.get_json()
    if(request.method=='POST'):
        todo=Todo(title=a["title"],desc=a["desc"])
        db.session.add(todo)
        db.session.commit()
    return a
    
if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0')