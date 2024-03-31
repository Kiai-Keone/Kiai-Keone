import string

Poem = """ It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat. """

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

Poem_without_punct = remove_punctuation(Poem)

def count_e(Poem):
    count = 0
    for word in Poem.split():
        if 'e' in word.lower():
            count += 1
    return count

e_count = count_e(Poem_without_punct)

total_words = len(Poem_without_punct.split())

e_percentage = (e_count/total_words) * 100

final = "Your text contains {} words, of which {} ({}%) contain an e.".format(total_words, e_count, e_percentage)

print(final)
