from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        if request.method == 'POST':
            gre_score=float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research == "yes"):
                research = 1
            else:
                research = 0
            pre_process_data = 'Pre_processed_transform_data'
            model_file = 'finalized_linear_model'
            scaler = pickle.load(open(pre_process_data,'rb'))
            model = pickle.load(open(model_file,'rb'))
            test = scaler.transform([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            prediction = model.predict(test)
            print("prediction is ", prediction)
            return render_template("results.html",prediction=int(100*prediction[0]))
    except Exception as e:
        print("The Error is ",str(e))

if __name__ == "__main__" :
    app.run(debug=True,port=5006)
