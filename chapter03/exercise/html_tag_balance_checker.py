from structures.stack import Stack


def validate_html_tags(html_code: str):
    tags = Stack()
    balanced = True
    start_index = int(html_code.find('<')) + 1
    end_index = int(html_code.find('>'))

    while balanced and start_index > 0 and end_index > 0:
        tag = html_code[start_index:end_index]
        # print("start -> {} , End -> {} ; Tag -> {}".format(str(start_index), str(end_index), tag))
        if not tag.startswith('/'):
            tags.push(tag)
        else:
            if tags.is_empty():
                balanced = False
                break
            peek_tag = '/' + tags.pop()
            if peek_tag != tag:
                balanced = False

        start_index = int(html_code.find('<', end_index)) + 1
        end_index = int(html_code.find('>', start_index))

    return balanced


html = '''
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
'''

print(validate_html_tags(html))
