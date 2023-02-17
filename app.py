
from flask import Flask, request, redirect, render_template
import requests, json, csv
app = Flask(__name__)

#@app.route("/main_page", methods=["GET", "POST"])
#def main_page():
    #return render_template("index.html")


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
dict_rates=(data[0]['rates'])

#print(rates)

with open ('valuta.csv', 'w', newline='') as csvfile:
    
    writer=csv.writer(csvfile, delimiter=';')
    writer.writerow(dict_rates[0].keys())

    for dict in dict_rates: 
        #writer.writerow(dict.values())
        list1=dict.values()
        #print (list1)
        

@app.route("/main_page", methods=["GET", "POST"])           
def click_calc():
    
    if request.method=="POST":
        data_user=request.form
        currency=data_user.get("select-currency")
        number=data_user.get("number")
        
        for currency in dict_rates[currency]:
            rate=dict_rates[ask]
            print(rate)
            summ_zl=float(rate*number)
            #print(summ_zl)
            return render_template ('index.html', summ_zl=summ_zl)
    else: return redirect("/main_page")
     #response

#click_calc()
          
if __name__=="__main__":
    app.run(debug=True)
    
    