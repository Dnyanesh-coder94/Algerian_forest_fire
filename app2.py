from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/postman_data', methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
    if (ops == 'add'):
            r = num1+num2
            result = 'the sum of'+ str(num1) + 'and' + str(num2) + 'is' + str(r)
    if (ops == 'sub'):
            r = num1-num2
            result = 'the sub of'+ str(num1) + 'and' + str(num2) + 'is' + str(r)
    if (ops == 'mult'):
            r = num1*num2
            result = 'the multiplication of'+ str(num1) + 'and' + str(num2) + 'is' + str(r)
    if (ops == 'division'):
            r = num1/num2
            result = 'the division of'+ str(num1) + 'and' + str(num2) + 'is' + str(r)
        return jsonify(result)



if __name__=="__main__":
    app.run(host="0.0.0.0")