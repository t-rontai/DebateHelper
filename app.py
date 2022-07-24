from flask import Flask, render_template, request

app = Flask(__name__)

# GET method
@app.route("/", methods=['GET'])
def get():
    return render_template('index.html')

# POST method
@app.route("/debate_detail", methods=['POST'])
def post():
    time, people, agenda = request.form['time'], request.form['people'], request.form['agenda']
    return render_template('detail.html', time='時間は{}分です'.format(time)\
                                            , people='{}人です'.format(people)\
                                            , agenda='{}です'.format(agenda))

if __name__ == '__main__':
    app.run()