import numpy as np
from flask import Flask,request,render_template
import jsonify
import pickle

app=Flask(__name__,template_folder='templates')
model=pickle.load(open('random_forest_model.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/Predict",methods=['POST'])
def predict():
    if request.method=='POST':
        item_type=request.form['item_type']
        item_fat_content = request.form['item_fat_content']
                
        item_weight = float(request.form['item_weight'])
            
        item_visibility = (float(request.form['item_visibility'])/100)**(1/3)
            
        item_mrp = float(request.form['item_mrp'])
            
        outlet_size = request.form['outlet_size']
                
        outlet_type = request.form['outlet_type']
                
        outlet_location_type = request.form['outlet_location_type']
            
        outlet_age = 2021 - int(request.form['outlet_est_year'])

        breads=0
        breakfast=0
        foods=0
        dairy_foods=0
        frozen_foods=0
        fruits_and_vegetables=0
        hard_drinks=0
        health_and_hygiene=0
        household=0
        meat=0
        others=0
        seafoods=0
        snacks=0
        soft_drinks=0
        starchy_foods=0
        regular=0
        medium=0
        small=0
        supermarket_type1=0
        supermarket_type2=0
        supermarket_type3=0
        tier_2=0
        tier_3=0
        item_type= request.form['item_type']
        if item_type=='breads':
            breads=1
        elif item_type=='breakfast':
            breakfast=1
        elif item_type=='dairy_foods':
            dairy_foods=1
        elif item_type=='frozen_foods':
            frozen_foods=1
        elif item_type=='fruits_and_vegetables':
            fruits_and_vegetables=1
        elif item_type=='hard_drinks':
            hard_drinks=1
        elif item_type=='health_and_hygiene':
            health_and_hygiene=1
        elif item_type=='household':
            household=1
        elif item_type=='meat':
            meat=1
        elif item_type=='others':
            others=1
        elif item_type=='seafoods':
            seafoods=1
        elif item_type=='snacks':
            snacks=1
        elif item_type=='soft_drinks':
            soft_drinks=1
        elif item_type=='starchy_foods':
            starchy_foods=1
        item_fat_content= request.form['item_fat_content']
        if item_fat_content=='regular':
            regular=1
        outlet_size= request.form['outlet_size']
        if outlet_size=='medium':
            medium=1
        elif outlet_size=='small':
            small=1
        outlet_type=request.form['outlet_type']
        if outlet_type=='supermarket_type1':
            supermarket_type1=1
        elif outlet_type=='supermarket_type2':
            supermarket_type2=1
        elif outlet_type=='supermarket_type3':
            supermarket_type3=1

        prediction = (model.predict([[item_weight, item_visibility,  item_mrp,  outlet_age,regular,breads,breakfast,foods,dairy_foods,frozen_foods,fruits_and_vegetables,hard_drinks,health_and_hygiene,household,meat,others,seafoods,snacks,soft_drinks,starchy_foods,medium,small,tier_2,tier_3,supermarket_type1,supermarket_type2,supermarket_type3]]))**8
        
        output = round(prediction[0],2)
        
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this item!")
        else:
            return render_template('index.html',prediction_text="Item-Outlet Sales will be around: ₹{} per day".format(output))
    else:
       return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
