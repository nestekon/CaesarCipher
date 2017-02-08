# coding=UTF-8
'''
Модуль позволяет кодировать и декодировать текст Шифром Цезаря. Поддерживаются русский и английский языки.
@author: kos
'''

#заглавные буквы алфавитов
ENG_ALPH = list(unichr(i) for i in range(65,91))
RUS_ALPH = list(unichr(i) for i in range(1040,1072))
AVAILABLE_ALPHS = [ENG_ALPH, RUS_ALPH]

def main():

    test_str = u"""это нека1я пробная строка с
возвратом каретки и some english wor#ds! И это замечательно."""
    test_str = encrypt_string(test_str, 3)
    print(test_str)
    
    test_str2 = u"""ъпл квзэ1ь мнлюкэь опнлзэ о
ялдянэплй зэнвпзе е pljb bkdifpe tlo#ap! Е ъпл дэйвфэпвищкл."""
    test_str2 = decrypt_string(test_str2, -3)
    print(test_str2)

def encrypt_chr(achr, alph, k):
    if achr.upper() not in alph:
        return achr
    
    enc_ord = ((alph.index(achr.upper()) + k) % len(alph) + ord(alph[0]))
    chr = unichr(enc_ord)
    if achr.isupper():
        return chr
    else: 
        return chr.lower() 

def encrypt_word(aword, alph, k):
    return u"".join([encrypt_chr(chr, alph, k) for chr in aword])  

def encrypt_string(astr, k):
    import re
    
    #разобьём на уникальные слова
    the_set = set(re.split(ur"(?u)\W+",astr))
    the_str = astr
    for word in the_set:
        #определим язык слова
        for alph in AVAILABLE_ALPHS:
            if any(c.upper() in alph for c in word):
                #заменим зашифрованое слово во всей строке
                enc_word = encrypt_word(word, alph, k)
                pattern = ur"(?u)\b{}\b".format(word)
                the_str = re.sub(pattern, enc_word, the_str)
                break
        
    return the_str

def decrypt_chr(achr, alph, k):
    if achr.upper() not in alph:
        return achr
    
    dec_ord = ((alph.index(achr.upper()) - k + len(alph)) % len(alph) + ord(alph[0]))
    chr = unichr(dec_ord)
    if achr.isupper():
        return chr
    else: 
        return chr.lower()
    
def decrypt_word(aword, alph, k):
    return u"".join([decrypt_chr(chr, alph, k) for chr in aword])  

def decrypt_string(astr, k):
    import re
    
    #разобьём на уникальные слова
    the_set = set(re.split(ur"(?u)\W+",astr))
    the_str = astr
    for word in the_set:
        #определим язык слова
        for alph in AVAILABLE_ALPHS:
            if any(c.upper() in alph for c in word):
                #заменим зашифрованое слово во всей строке
                enc_word = decrypt_word(word, alph, k)
                pattern = ur"(?u)\b{}\b".format(word)
                the_str = re.sub(pattern, enc_word, the_str)
                break
        
    return the_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
main()
