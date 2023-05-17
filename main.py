class _utils:
    ALPHABET = list("abcdefghijklmnopqrstuvwxyz".upper())


class _key_encode(Exception):
    pass


class vigenere:
    """a class that contains all method of vigenere such as encode/decode a plain texts or getting a key to transform a
    word into another"""

    @staticmethod
    def cipher_to_plain(key: str = "a", *args: str, ascii_alphabet: bool = False, keep_chars: bool = False,
                        dict_solo_result: bool = False) -> dict or str:  # same as the other but we change all operator
        """
        this function use vigenere algorithme to decode words encoded in vigenere.
        note: we limit ascii table from 33 to 126 (ords)

        :param key: Key for encoding
        :param args: the word to encode
        :param ascii_alphabet: use latin alphabet or ascii table to encode
        :param keep_chars: keeping integer and non-letter from the word
        :param dict_solo_result: getting a result like {"word":"cipher"}
        :return: dict or str
        """
        for k in key:
            if k.isdigit():
                raise _key_encode('Keys for vigenere can\' have number in it')
        res = {}
        for w in args:
            if not ascii_alphabet:

                k = [_utils.ALPHABET.index(key[k % len(key)].upper()) for k in range(len(w))]  # getting key
                word = ''.join(i.upper() for i in w if i.upper() in _utils.ALPHABET)  # removing numbers
                word = [_utils.ALPHABET.index(c.upper()) for c in word]

                r = [_utils.ALPHABET[x[0] - x[1]] if x[0] - x[1] > 0 else _utils.ALPHABET[
                    (x[0] - x[1]) + len(_utils.ALPHABET)] for x in zip(word, k)]

                if keep_chars:  # reinserting ints if the user want
                    for x in w.upper():
                        if x not in _utils.ALPHABET:
                            r.insert(w.index(x), x)

            elif ascii_alphabet:
                word=w
                r = [chr(w - k) if w - k > 33 else chr(w - k + 93) for w, k in
                     zip(bytearray(word.encode()), [ord(key[k % len(key)]) for k in range(len(word))])]


            else:
                raise Exception("Invalid")

            res[w] = "".join(r)
        if len(res) == 1 and not dict_solo_result:
            return res[list(res)[0]]
        return res

    @staticmethod
    def plain_to_cipher(key: str = "a", *args: str, ascii_alphabet: bool = False, keep_chars: bool = False,
                        dict_solo_result: bool = False):
        """
        this function use vigenere algorithme to encode words encoded in vigenere.
        note: we limit ascii table from 33 to 126 (ords)

        :param key: Key for encoding
        :param args: the word to encode
        :param ascii_alphabet: use latin alphabet or ascii table to encode
        :param keep_chars: keeping integer or non-letter from the word
        :param dict_solo_result: getting a result like {"word":"cipher"}
        :return: dict or str

        """
        for k in key:
            if ascii_alphabet:
                break
            if k.isdigit():
                raise _key_encode('Keys for vigenere can\' have number in it')  # raise error if number in key
        res = {}
        for w in args:  # for each words
            if not ascii_alphabet:
                k = [_utils.ALPHABET.index(key[k % len(key)].upper()) for k in range(len(w))]  # getting each key ints
                word = ''.join(i for i in w if i.upper() in _utils.ALPHABET)  # removing numbers from the word
                word = [_utils.ALPHABET.index(c.upper()) if 65 <= ord(c.upper()) <= 90 else 0 for c in
                        word]  # getting int from word
                r = [_utils.ALPHABET[x[0] + x[1]] if x[0] + x[1] < 0 else _utils.ALPHABET[
                    (x[0] + x[1]) - len(_utils.ALPHABET)] for x in
                     zip(word, k)]  # adding each int of each word and key, if the result < 0 add the alphabet size

                if keep_chars:  # reinserting ints if the user want
                    for x in w.upper():
                        if x not in _utils.ALPHABET:
                            r.insert(w.index(x), x)


            elif ascii_alphabet:  # using ascii
                word=w
                r = [chr((w + k)) if w + k < 126 else chr(w + k - 93) for w, k in zip(bytearray(word.encode()),
                                                                                      [ord(key[k % len(key)]) for k
                                                                                       in range(
                                                                                          len(word))])]  # getting bytearray = ord for each word as a list, we add it and keep it the size of ascii table from 33 to 126



            else:
                raise Exception("Invalid")

            res[w] = "".join(r)

        if len(res) == 1 and not dict_solo_result:
            return res[list(res)[0]]  # get the only key
        return res  # return the dict

    @staticmethod
    def key_by_transform(original: str, into: str, ascii_alphabet: bool = False, keep_int: bool = False) -> str:
        """
            with this function you can get the key that transform a word into another, the condition is the second
            word has to be same lenght
            :param original:
            :param into: into what the original word should be transfomred with vignere
            :return: str

            a=> b ; 1 -> 2+x
            z => a ; 26 -> 1+x
            z => a ; 26-1=x

            """
        print(len(original),len(into))
        if len(original) != len(into):
            raise Exception("words have to be same lenght")
        original_list, into_list = [ord(w) for w in original.upper()], [
            ord(w)
            for w in into.upper()]  # ords list
        result = []
        if ascii_alphabet:  # checking with the ascii alphabet
            for a, b in zip(original_list, into_list):
                res = b - a  # such as operation in docstring
                if res < 33:  # limiting ascii table
                    res += 93
                elif res > 126:
                    res -= 93
                result.append(chr(res))  # add character of the result to result list


        else:
            original_list, into_list = [_utils.ALPHABET.index(w) for w in original.upper() if w in _utils.ALPHABET], [
                _utils.ALPHABET.index(w)
                for w in into.upper() if w in _utils.ALPHABET]  # create int list of each character using latin alphabet
            for a, b in zip(original_list, into_list):  # looping through 2 list at the same time

                res = b - a  # subtracting result to get the key letter
                if res < 0:  # checking for his value
                    res += len(_utils.ALPHABET)
                elif res > len(_utils.ALPHABET):
                    res -= len(_utils.ALPHABET)

                result.append(_utils.ALPHABET[res])
            if keep_int:  # reinserting ints if the user want
                for x in original:
                    if x.isdigit():
                        result.insert(original.index(x), x)
        return "".join(result)  # return result

    @staticmethod
    def plain_to_cipher_phrase(key: str = "a", phrase: str = "", ascii_alphabet: bool = False,
                               keep_chars: bool = False) -> str:
        result = []
        for w in phrase.split(" "):
            result.append(vigenere.plain_to_cipher(key, w, ascii_alphabet=ascii_alphabet, keep_chars=keep_chars))
        return " ".join(result)

    @staticmethod
    def cipher_to_plain_phrase(key: str = "a", phrase: str = "", ascii_alphabet: bool = False,
                               keep_chars: bool = False) -> str:
        result = []
        for w in phrase.split(" "):
            result.append(vigenere.cipher_to_plain(key, w, ascii_alphabet=ascii_alphabet, keep_chars=keep_chars))
        return " ".join(result)

    @staticmethod
    def key_by_transform_phrase(original: str, into: str, ascii_alphabet: bool = False, keep_int: bool = False,
                                spaced_key=False) -> str:
        """

        :param original: the original phrase to transform
        :param into: into what the new phrase would be transform with key
        :param ascii_alphabet: if you use an ascii alphabet, useful to keep number and etc...
        :param keep_int: to keep intergers or special chars
        :param spaced_key: if you want the key to specify the spaces of the new word
        :return: str
        """
        if not spaced_key:
            original = original.split(" ")
            into = into.split(" ")
            result = []
            for a, b in zip(original, into):
                result.append(vigenere.key_by_transform(a, b, ascii_alphabet, keep_int))
            return " ".join(result)
        else:
            a = "".join(original.split(" "))
            b="".join(into.split(" "))
            print(a,b)
            k = list(vigenere.key_by_transform(a, b, ascii_alphabet,
                                               keep_int))
            for i, char in enumerate(into):
                if char == " ":
                    k.insert(i, char)
            return "".join(k)



    @staticmethod
    def cipher_phrase_custom_key(key:str, phrase, ascii_alphabet:bool=False, keep_chars:bool = False, spaced_key=False ) -> str:
        """If you use the key_by_transform_phrase method, you can use this function to apply the key in one way
              (it automatically keeps spaces)
              :param spaced_key: if you use the key by transform phrase 2, the space of the new word is given by the key.
              :param phrase: the phrase you want to decode
              :param key: Key for encoding
              :param ascii_alphabet: use latin alphabet or ascii table to encode
              :param keep_chars: keeping integer and non-letter from the word
              :return: str
              """

        phrase_ = "".join(phrase.split(" "))
        key_ = "".join(key.split(" "))
        x = list(
            vigenere.cipher_to_plain(key_, phrase_, ascii_alphabet=ascii_alphabet, keep_chars=keep_chars))  # apply key
        if not spaced_key:
            for i, char in enumerate(phrase):

                if char == " ":
                    x.insert(i, char)
        else:
            for i, char in enumerate(key):

                if char == " ":
                    x.insert(i, char)
        return "".join(x)
    @staticmethod
    def plain_phrase_custom_key(key:str, phrase, ascii_alphabet:bool=False, keep_chars:bool = False , spaced_key=False) -> str:
        """If you use the key_by_transform_phrase method, you can use this function to apply the key in one way
        (it automatically keeps spaces)
        :param spaced_key: if you use the key by transform phrase 2, the space of the new word is given by the key.
        :param phrase: the phrase you want to decode
        :param key: Key for encoding
        :param ascii_alphabet: use latin alphabet or ascii table to encode
        :param keep_chars: keeping integer and non-letter from the word
        :return: str
        """

        phrase_ = "".join(phrase.split(" "))
        key_ = "".join(key.split(" "))
        x= list(vigenere.plain_to_cipher(key_,phrase_,ascii_alphabet=ascii_alphabet,keep_chars=keep_chars)) # apply key
        if not spaced_key:
            for i,char in enumerate(phrase):

                if char == " ":
                    x.insert(i,char)
        else:
            for i, char in enumerate(key):

                if char == " ":
                    x.insert(i, char)
        return "".join(x)
    #@staticmethod
    #def cipher_paragraphe():