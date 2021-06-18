

class PrinterErrors:

    def printer_error(self, txt):
        errcount = 0

        for char in txt:
            if ord(char) < 97 or ord(char) > 109:
                errcount += 1

        return str(errcount) + "/" + str(len(txt))


class FriendOrFoe:

    def friend_or_foe(self,lst):

        friend_list = []

        for item in lst:
            if len(item) == 4:
                friend_list.append(item)
        return friend_list