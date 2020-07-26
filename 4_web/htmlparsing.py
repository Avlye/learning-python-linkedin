from html.parser import HTMLParser


class AvlyeParser(HTMLParser):
    def handle_comment(self, data):
        print('Encountered comment: ', data)
        pos = self.getpos()
        print('\t At line: ', pos[0], 'position', pos[1])

    def handle_data(self, data):
        if data.isspace(): return

        print('Encountered data: ', data)
        pos = self.getpos()
        print('\t At line:', pos[0], 'position', pos[1])


parser = AvlyeParser()

with open('sample.html', 'r') as file:
    contents = file.read()
    parser.feed(contents)