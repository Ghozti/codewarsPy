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
    player1Go = True

    gameChart = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    def play(self, col):

        i = 5

        while i != 0:

            if self.gameChart[i][col] == 0:
                if self.player1Go:
                    self.gameChart[i][col] = 1
                    break
                else:
                    self[i][col] = 2
                    break
            else:
                i -= 1
        else:
            return "Collum full!"

        print(self.gameChart[0])
        print(self.gameChart[1])
        print(self.gameChart[2])
        print(self.gameChart[3])
        print(self.gameChart[4])
        print(self.gameChart[5])

        self.checkForWin(self.gameChart)

    def checkForWin(self, table):

        # vertical win

        v_same_num_count = 0
        v_win = False

        for row in range(6):
            for i in range(len(table)-1):
                if table[row][i] == 1:
                    v_same_num_count += 1

            if v_same_num_count == 4:
                print("***")

        # horizontal win

        h_same_num_count = 0
        h_win = False

        for row in range(6):
            for i in range(len(table)-1):
                if table[row][i] == 1:
                    v_same_num_count += 1

            if v_same_num_count == 4:
                print("***")