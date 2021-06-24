class alphabetPos:

    def alphabet_position(self, text):
        txt = text.lower()
        num = ""

        dic = {
            "a": "1",
            "b": "2",
            "c": "3",
            "d": "4",
            "e": "5",
            "f": "6",
            "g": "7",
            "h": "8",
            "i": "9",
            "j": "10",
            "k": "11",
            "l": "12",
            "m": "13",
            "n": "14",
            "o": "15",
            "p": "16",
            "q": "17",
            "r": "18",
            "s": "19",
            "t": "20",
            "u": "21",
            "v": "22",
            "w": "23",
            "x": "24",
            "y": "25"
        }

        for char in txt:
            dic.setdefault(char, " ")
            dic.setdefault(" ", "")
            num += dic[char]
            num.replace("  ", " ")

        return num


class FormatNameList:

    def format_List(self, lst):
        nameCount = 0
        nameList = []

        for dic in lst:
            nameCount += 1
            nameList.append(dic.get("name"))

        if nameCount == 2:
            return nameList[0] + " & " + nameList[1]
        elif nameCount == 1:
            return nameList[0]
        elif nameCount == 0:
            return ""
        elif nameCount > 2:
            txt = ""
            for i in range(len(nameList)):
                if i == (len(nameList) - 1):
                    txt += " & " + nameList[i]
                elif i == 0:
                    txt += nameList[i]
                else:
                    txt += ", " + nameList[i]
            return txt


class BreakCamelCase:

    def break_camel(self, txt):

        lst = []
        indlst = []

        for char in txt:
            lst.append(char)

        num_of_camels = 0

        for char in range(len(lst)):
            if ord(lst[char]) >= 65 and ord(lst[char]) <= 90:
                num_of_camels += 1
                if num_of_camels > 1:
                    indlst.append(char + num_of_camels - 1)
                else:
                    indlst.append(char)

        for ind in indlst:
            lst.insert(ind, " ")

        fstr = ""

        for i in lst:
            fstr += i

        return fstr


class CountString:

    def count(self, txt):

        chars = []
        dic = {}

        for char in txt:
            if char not in chars:
                chars.append(char)
                dic[char] = txt.count(char)

        return dic


class StreetFighter:

    def street_fighter_selection(self, fighters, init_pos, moves):
        fighters = [
            ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
            ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
        ]  # 2d array containing the fighters

        init_pos = [0, 0]  # x,y

        move_dicX = {
            "left": -1,
            "right": 1
        }

        move_dicY = {
            "up": -1,
            "down": 1,
        }

        fighters_passed = []

        for move in moves:

            if move not in move_dicX:
                move_dicX.setdefault(move, 0)
            else:

                init_pos[1] += move_dicX.get(move)

                if init_pos[1] > 5:
                    init_pos[1] = 0
                elif init_pos[1] < -5:
                    init_pos[1] = 0

            if move not in move_dicY:
                move_dicY.setdefault(move, 0)
            else:

                init_pos[0] += move_dicY.get(move)

                if init_pos[0] > 0:
                    init_pos[0] = 1
                elif init_pos[0] < 0:
                    init_pos[0] = 0
            fighters_passed.append(fighters[init_pos[0]][init_pos[1]])

        return fighters_passed


class Unique_order:
    def order(self, txt):

        ordered_list = []
        stxt = str(txt)

        valid_chars_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2",
                            "3", "4", "5", "6", "7", "8", "9", "0"
                            ]

        for char in stxt:
            if len(ordered_list) == 0:
                ordered_list.append(char)
            elif len(ordered_list) != 0 and ordered_list[
                len(ordered_list) - 1] is not char and char in valid_chars_list:
                ordered_list.append(char)

        return ordered_list
