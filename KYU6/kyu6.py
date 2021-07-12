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

        valid_chars_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2",
                            "3", "4", "5", "6", "7", "8", "9", "0", 1, 2,
                            3, 4, 5, 6, 7, 8, 9, 0
                            ]

        num_dic = {"1": 1,
                   "2": 2,
                   "3": 3,
                   "4": 4,
                   "5": 5,
                   "6": 6,
                   "7": 7,
                   "8": 8,
                   "9": 9,
                   "0": 0,
                   }
        ntxt = []

        for i in txt:
            ntxt.append(i)

        for char in ntxt:
            if len(ordered_list) == 0:
                if char in valid_chars_list:
                    if char in num_dic:
                        ordered_list.append(num_dic.get(char))
                    else:
                        ordered_list.append(char)
            else:
                if char in valid_chars_list:
                    if char in num_dic:

                        if num_dic.get(ordered_list[len(ordered_list) - 1]) != num_dic.get(char):
                            ordered_list.append(num_dic.get(char))
                    else:
                        if ordered_list[len(ordered_list) - 1] != char:
                            print(len(ntxt))
                            print(char)
                            print(ordered_list[len(ordered_list) - 1])
                            ordered_list.append(char)
        return ordered_list


class FindOdd:

    def find_odd(self, seq):
        for i in seq:
            if seq.count(i) % 2 != 0:
                return i


class Highest_Rank:

    def get_highest_rank(self, lst):
        highest_num = 0

        for i in lst:
            if lst.count(i) > lst.count(highest_num):
                highest_num = i
            elif lst.count(i) == lst.count(highest_num):
                if i > highest_num:
                    highest_num = i

        return highest_num


class MazeRunner:
    def maze_run(self, lst, moves):

        move_dic = {
            "N": -1,
            "S": 1,
            "E": 1,
            "W": -1
        }

        current_status = ""
        start_pos = []
        current_pos = []

        for i in range(len(lst)):
            for o in range(len(lst[i])):
                if lst[i][o] == 2:
                    start_pos.append(i)
                    start_pos.append(o)

        current_pos = start_pos

        for i in moves:
            if i == "N" or i == "S":
                current_pos[0] += move_dic.get(i)
            elif i == "E" or i == "W":
                current_pos[1] += move_dic.get(i)

            if current_pos[0] < 0 or current_pos[0] > len(lst[0])-1 or current_pos[1] < 0 or current_pos[1] > len(lst[0])-1:
                current_status = "Dead"
                break
            elif lst[current_pos[0]][current_pos[1]] == 1:
                current_status = "Dead"
                break
            elif lst[current_pos[0]][current_pos[1]] == 3:
                current_status = "Finish"
                break
            else:
                current_status = "Lost"

        return current_status


class Vowel_Coder:

    vowel_dic = {
        "a":"1",
        "e":"2",
        "i": "3",
        "o": "4",
        "u": "5",
    }

    decode_vowel_dic = {
        "1":"a",
        "2":"e",
        "3": "i",
        "4": "o",
        "5": "u",
    }

    def encode(self,txt):
        sentence = ""
        for i in txt:
            if i.lower() in self.vowel_dic:
                sentence += self.vowel_dic.get(i.lower())
            else:
                sentence += i
        return sentence

    def decoded(self,txt):
        senetnce = ""
        for i in txt:
            if i in self.decode_vowel_dic:
                senetnce += self.decode_vowel_dic.get(i)
            else:
                senetnce += i

class Duplicate_Encoder:

    def dupe_encoder(self,txt):
        ntxt = ""
        for i in txt:
            if txt.count(i) > 1:
                ntxt += ")"
            else:
                ntxt += "("

        return ntxt


class NewCashier:

    # Menu order:
    # 1. Burger
    # 2. Fries
    # 3. Chicken
    # 4. Pizza
    # 5. Sandwich
    # 6. Onionrings
    # 7. Milkshake
    # 8. Coke

    def get_order(self,order):

        menu = ["burger","fries","chicken","pizza","sandwich","onionrings","milkshake","coke"]

        lst = []

        orderedList = []

        current_word = []

        for i in order:
            current_word.append(i)
            word = ""
            for j in current_word:
                word += j

            if word in menu:
                lst.append(word)
                current_word = []

        for i in range(len(lst)):
            if

        return orderedList