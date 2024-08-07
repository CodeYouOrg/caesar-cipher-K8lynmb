# add your code here
#python is fun!
#udymts nx kzs!

def caesar(sentence):
    ciphered_sentence = ""
    cipher = {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e':'j', 'f':'k','g':'l', 'h':'m', 'i':'n', 'j':'o','k':'p','l':'q','m':'r','n':'s','o':'t','p':'u','q':'v','r':'w','s':'x','t':'y','u':'z', 'v':'a', 'w':'b','x':'c','y':'d','z':'e' }
    for letter in sentence:
        for value in cipher.values():
            match(letter):
                case ' ':
                    ciphered_sentence += ' '
                    break
                case '!':
                    ciphered_sentence += '!'
                    break
                case '?':
                    ciphered_sentence += '?'
                    break
                # #$%^&*()
                case '#':
                    ciphered_sentence += '#'
                    break
                case '$':
                    ciphered_sentence += '$'
                    break
                case '%':
                    ciphered_sentence += '%'
                    break
                case '^':
                    ciphered_sentence += '^'
                    break
                case '&':
                    ciphered_sentence += '&'
                    break
                case '*':
                    ciphered_sentence += '*'
                    break
                case '(':
                    ciphered_sentence += '('
                    break
                case ')':
                    ciphered_sentence += ')'
                    break
                case _:
                    ciphered_sentence += cipher[letter.lower()]
                    break

    return ciphered_sentence

sentence = input("Please enter a sentence: ")

print("The encrypted sentence is:", caesar(sentence))