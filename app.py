from flask import Flask, request, redirect, render_template
import requests, json, csv
app = Flask(__name__)


 
def get_rate(currency) -> float:
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    rates = data[0]['rates']
    for rate in rates:
        print(currency)
        print(rate)
        if rate['currency'] == currency:
            return rate['ask']
    else:
        raise ValueError('wrong currency')


@app.route("/", methods=["GET", "POST"])           
def main():
    
    if request.method=="POST":
        data_user=request.form
        currency=data_user.get("select-currency")
        amount=float(data_user.get("amount"))
        rate = get_rate(currency=currency)
        result = rate * amount  
        return render_template ('index.html', result=result)
 
    return render_template ('index.html', result=0)

          
if __name__=="__main__":
    app.run(debug=True)
    