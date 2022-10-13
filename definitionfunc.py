import requests



#shoutout to Liu Zuo Lin who wrote this code to easily extract certain keys from a messy json response
#source ~ https://python.plainenglish.io/extracting-specific-keys-values-from-a-messed-up-json-file-python-dfb671482681
def extract(data, keys):
    out = []
    queue = [data]
    while len(queue) > 0:
        current = queue.pop(0)
        if type(current) == dict:
            for key in keys:
                if key in current:
                    out.append({key:current[key]})
            
            for val in current.values():
                if type(val) in [list, dict]:
                    queue.append(val)
        elif type(current) == list:
            queue.extend(current)
    return out


class definition:
    def __init__(self):
        #set > lists all day
        self.valid_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    def format_word(self,word):
        fail = False
        for i in range(len(word)):
            if word[i] in self.valid_chars:
                if fail:
                    return word[i-1::]
                else:
                    return word
            fail = True

    def word(self,word_to_define,max_definitions = 3):
        word = self.format_word(word_to_define)
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        x = extract(response.json(),["definition"])
        print(bool(x))
        if x:
            output = [x[i]["definition"] for i in range(max_definitions if len(x) > max_definitions else len(x))]
            output.insert(0,True)
        else:
            output = [False,f"https://www.google.com/search?client=opera-gx&q=definition+of+{word}"]

        #outputs 1st 3 definitions or all definitions if less than 3
        return output

define = definition()




