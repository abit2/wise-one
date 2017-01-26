import wikiquote, random

def give_quotes(query, number_of_quotes=3, set_lang='en'):
	return wikiquote.quotes(query, max_quotes=number_of_quotes, lang=set_lang)


def quote_of_day(set_lang='en'):
	return wikiquote.quote_of_the_day(lang=set_lang)


def random_quote(query):
	return random.choice(wikiquote.quotes(query))