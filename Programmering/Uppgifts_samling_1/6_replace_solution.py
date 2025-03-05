# Skriv en funktion som tar en text i forma av en sträng och en ordlista i form av en dict.
# Funktionen ska byta ut de ord i texten som finns som nycklar i ordlistan mot deras definierade värde.
# För enkelhets skull byter vi endast ut exakta matchningar, och gör alltså skillnad mellan stora och
# små bokstäver. Vi byter ut alla exakta matchningar, även om det handlar om delar av ord.
def search_and_replace(text, replacements):
    for word in replacements:
        text = text.replace(word, replacements[word])
    return text


if __name__ == '__main__':
    sentence = 'We have had cold weather. It is bad for my skin.'
    newspeak = {'cold': 'unwarm', 'bad': 'ungood'}
    print(search_and_replace(sentence, newspeak))  # We have had unwarm weather. It is ungood for my skin.
    phrase = 'The weather is bad: Cold and rainy!'
    print(search_and_replace(phrase, newspeak))  # The weather is ungood: Cold and rainy!

    phrase = 'In January, the weather is usually cold. It makes me feel bad.'
    print(search_and_replace(phrase, newspeak))  # The weather is ungood: Cold and rainy!
    phrase = 'Cold, cold heart and an even badder spelling.'
    print(search_and_replace(phrase, newspeak))
    conlang = {'fast': 'speedful', 'slow': 'unspeedful', 'great': 'plusgood', 'completely': 'fullwise'}
    print(search_and_replace('The cold is getting worse fast. Slowly, the seasons are getting completely out of control.', conlang))
