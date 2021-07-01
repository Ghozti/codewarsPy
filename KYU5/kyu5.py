class FindDomain:
    def find_dom(self, link):
        dom = ""
        link = link.replace("www.", "")
        link = link.replace("http://", "")
        link = link.replace("https://", "")
        link = link.replace(".com", "")

        for i in link:
            dom += i
        if "." in dom:
            dom = dom.rsplit(".")[0]
        elif "/" in dom:
            dom = dom.rsplit("/")[0]

        return dom


class ROT13:
    def rot13(self, message):
        txt = ""
        word_dic = {
            "a": "n",
            "b": "o",
            "c": "p",
            "d": "q",
            "e": "r",
            "f": "s",
            "g": "t",
            "h": "u",
            "i": "v",
            "j": "w",
            "k": "x",
            "l": "y",
            "m": "z",
            "n": "a",
            "o": "b",
            "p": "c",
            "q": "d",
            "r": "e",
            "s": "f",
            "t": "g",
            "u": "h",
            "v": "i",
            "w": "j",
            "x": "k",
            "y": "l",
            "z": "m",

            "A": "N",
            "B": "O",
            "C": "P",
            "D": "Q",
            "E": "R",
            "F": "S",
            "G": "T",
            "H": "U",
            "I": "V",
            "J": "W",
            "K": "X",
            "L": "Y",
            "M": "Z",
            "N": "A",
            "O": "B",
            "P": "C",
            "Q": "D",
            "R": "E",
            "S": "F",
            "T": "G",
            "U": "H",
            "V": "I",
            "W": "J",
            "X": "K",
            "Y": "L",
            "Z": "M",
        }

        for i in message:
            txt += word_dic.get(i)

        return txt


class Connect4:
