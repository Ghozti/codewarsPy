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
    def rot13(self,message):
        txt = ""
        for i in message:
            txt += chr(ord(i)+13)
        return txt