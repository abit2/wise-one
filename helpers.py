import wikiquote, random

def give_quotes(query='Dune', number_of_quotes=3, set_lang='en'):
	return wikiquote.quotes(query, max_quotes=number_of_quotes, lang=set_lang)


def quote_of_day(set_lang='en'):
	return wikiquote.quote_of_the_day(lang=set_lang)


def random_quote(query):
	return random.choice(wikiquote.quotes(query))


def quote_with_keyword(keyword, query):
	results = wikiquote.quotes(query, max_quotes=150)
	quotes_saturated = []
	for result in results:
		if keyword in result:
			quotes_saturated.append(result)

	if len(quotes_saturated)==0:
		return "Sorry no quotes were found."
	return quotes_saturated