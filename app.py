from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/hello')
def hello():
    """Simple example of an API endpoint"""
    return jsonify({'message': 'ohai'})


@app.route('/hello/<string:name>')
def hello_name(name):
    """Simple example using an URL parameter"""
    return jsonify({'message': 'ohai {}'.format(name)})

# Discogs Marketplace Squad - currency conversion endpoints

# GET /rate/currency1/to/currency2
@app.route('/rate/<string:currency1>/to/<string:currency2>')
def currency_rate(currency1, currency2):

	rate = get_rate(currency1, currency2)

	return jsonify(
		{	
			'from': '{}'.format(currency1), 
			'to': '{}'.format(currency2),
			'rate': '{}'.format(rate)
		})

# GET /convert/currency1/amount/to/currency2
@app.route('/convert/<string:currency1>/<float:amount>/to/<string:currency2>')
def currency_convert(currency1, amount, currency2):

	rate = get_rate(currency1, currency2)

	converted_amount = round(amount * rate, 2)

	return jsonify(
		{	
			'from': '{}'.format(currency1), 
			'from_amount':'{}'.format(amount),
			'to': '{}'.format(currency2),
			'converted_amount': '{}'.format(converted_amount),
			'rate': '{}'.format(rate)
		})

# Call API to get latest rates - https://currencylayer.com/quickstart 
def get_rate(currency1, currency2):

	data = requests.get('http://www.apilayer.net/api/live?access_key=88b5656f48dc23632ce1e4ce7150bd63&currencies=USD,GBP,EUR&format=1').json()

	currency1_rate = 0

	if currency1.lower() == 'gbp':
		currency1_rate = data['quotes']['USDGBP']
	elif currency1.lower() == 'eur':
		currency1_rate = data['quotes']['USDEUR']
	elif currency1.lower() == 'usd':
		currency1_rate = data['quotes']['USDUSD']

	currency2_rate = 0

	if currency2.lower() == 'gbp':
		currency2_rate = data['quotes']['USDGBP']
	elif currency2.lower() == 'eur':
		currency2_rate = data['quotes']['USDEUR']
	elif currency2.lower() == 'usd':
		currency2_rate = data['quotes']['USDUSD']

	if currency1_rate > currency2_rate:
		return currency2_rate;
	else:
		return 1 / currency1_rate;

