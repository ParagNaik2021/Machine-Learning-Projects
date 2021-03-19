from flask import Flask,render_template,request,Response
import pickle
app=Flask(__name__)



@app.route("/",methods=['GET'])
def index():
    return render_template('Crop_Recommendation.html')


@app.route("/predict",methods=["GET","POST"])
def prediction():
    if request.method=='POST':
        try:
            nitrogen=float(request.form['nitrogen'])
            phosphorus=float(request.form['phosphorus'])
            potassium=float(request.form['potassium'])
            temperature=float(request.form['temperature'])
            humidity=float(request.form['humidity'])
            ph=float(request.form['ph'])
            rainfall=float(request.form['rainfall'])

            filename='modelForPrediction.sav'
            load_model=pickle.load(open(filename,'rb'))
            prediction=load_model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
            print(prediction[0])
            if prediction[0]=='cotton':
                return render_template('cotton.html',prediction=prediction[0])
            elif prediction[0]=='mungbean':
                return  render_template("mungbean.html",prediction=prediction[0])
            elif prediction[0]=="coconut":
                return render_template("coconut.html",prediction=prediction[0])
            elif prediction[0]=="banana":
                return render_template("banana.html",prediction=prediction[0])
            elif prediction[0]=="apple":
                return render_template("apple.html",prediction=prediction[0])
            elif prediction[0]=='pomegranate':
                return render_template("pomegranate.html",prediction=prediction[0])
            elif prediction[0] == 'chickpea':
                return render_template("chickpea.html",prediction=prediction[0])
            elif prediction[0] == 'coffee':
                return render_template("coffee.html",prediction=prediction[0])
            elif prediction[0] == 'lentil':
                return render_template("lentil.html",prediction=prediction[0])
            elif prediction[0] == 'jute':
                return render_template("jute.html",prediction=prediction[0])
            elif prediction[0] == 'orange':
                return render_template("orange.html",prediction=prediction[0])
            elif prediction[0] == 'blackgram':
                return render_template("blackgram.html",prediction=prediction[0])
            elif prediction[0] == 'mothbeans':
                return render_template("mothbeans.html",prediction=prediction[0])
            elif prediction[0] == 'kidneybeans':
                return render_template("kidneybeans.html",prediction=prediction[0])
            elif prediction[0] == 'rice':
                return render_template("rice.html",prediction=prediction[0])
            elif prediction[0] == 'pigeonpeas':
                return render_template("pigeonpeas.html",prediction=prediction[0])
            elif prediction[0] == 'papaya':
                return render_template("papaya.html",prediction=prediction[0])
            elif prediction[0] == 'watermelon':
                return render_template("watermelon.html",prediction=prediction[0])
            elif prediction[0] == 'maize':
                return render_template("maize.html",prediction=prediction[0])
            elif prediction[0] == 'muskmelon':
                return render_template("muskmelon.html",prediction=prediction[0])
            elif prediction[0] == 'grapes':
                return render_template("grapes.html",prediction=prediction[0])
            elif prediction[0] == 'mango':
                return render_template("mango.html",prediction=prediction[0])
            else:
                return render_template('Crop_Recommendation.html')
        except ValueError:
            return Response("value not found")
        except Exception as e:
            print("Exception is ",e)
            return Response(e)
    else:
        return render_template("Crop_Recommendation.html")

if __name__=='__main__':
    app.run(debug=True)


