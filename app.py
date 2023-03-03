from flask import Flask, request, redirect, render_template
import requests, json, csv
app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']
#print(rates)

def get_rate(currency) -> float:
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

#друк значень словарів для перевірки
for rate in rates:
    fieldrows=rate.values()
    print(fieldrows)

#запис заголовків
#with open ('valuta.csv', 'w', newline='') as csvfile:
 #writer=csv.writer(csvfile, delimiter=';')
 #writer.writerow(rates[0].keys())

 #writer.writerow(fieldrows)
 #print(writer.writerow(fieldrows))

#запис строк через відкриття файлу в "append"
#with open ('valuta.csv', 'a', newline='') as csvfile:
    #for f in fieldrows:
        #writer.writerow(f)
        ##print(writer.writerow(f))



#запис через Dict
#with open('valuta.csv', 'w') as csvfile:
        #writer = csv.DictWriter(csvfile, fieldnames=rates[0].keys())
        #writer.writeheader()
        #for rate in rates:
            #writer.writerow(rate)



if __name__=="__main__":
    app.run(debug=True)





#мій перший код
# response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
# data = response.json()
# dict_rates = data[0]['rates']

# with open('valuta.csv', 'w', newline='') as csvfile:
    
#     writer=csv.writer(csvfile, delimiter=';')
#     writer.writerow(dict_rates[0].keys())

#     for dict in dict_rates: 
#         #writer.writerow(dict.values())
#         list1=dict.values()
#         #print (list1)