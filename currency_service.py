import requests

class currency_service:

	# Call API to get latest rates - https://currencylayer.com/quickstart 
	def get_rates():

		rates = requests.get('http://www.apilayer.net/api/live?access_key=88b5656f48dc23632ce1e4ce7150bd63&currencies=USD,GBP,EUR&format=1').json()

		return rates

	def get_rate(currency1, currency2):

		try:

			rates = currency_service.get_rates()

			currency1_rate = 0

			if currency1.lower() == 'gbp':
				currency1_rate = rates['quotes']['USDGBP']
			elif currency1.lower() == 'eur':
				currency1_rate = rates['quotes']['USDEUR']
			elif currency1.lower() == 'usd':
				currency1_rate = rates['quotes']['USDUSD']

			currency2_rate = 0

			if currency2.lower() == 'gbp':
				currency2_rate = rates['quotes']['USDGBP']
			elif currency2.lower() == 'eur':
				currency2_rate = rates['quotes']['USDEUR']
			elif currency2.lower() == 'usd':
				currency2_rate = rates['quotes']['USDUSD']

			if currency1_rate < 1 and currency2_rate < 1:
				return 1 / currency1_rate * currency2_rate
			elif currency1_rate > currency2_rate:
				return currency2_rate
			else:
				return 1 / currency1_rate

		except:
			return 0