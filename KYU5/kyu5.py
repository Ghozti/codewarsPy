class FindDomain:
    def find_dom(self, link):
        dom = ""
        if link.contains("www."):
            for i in range(link.index("."),len(link)):
                if i is not '.':
                    dom += link[i]
        else:
            for i in range(link.index("/"),len(link)):
                if i is not '.' or i is not '/':
                    dom += link[i]