

class PrinterErrors:

    def printer_error(self, txt):
        errcount = 0

        for char in txt:
            if ord(char) < 97 or ord(char) > 109:
                errcount += 1

        return str(errcount) + "/" + str(len(txt))



