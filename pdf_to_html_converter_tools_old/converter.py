# each line below is a paragraph and each paragraph is separated by an empty line
original_section=""""""

if original_section == "":
    with open('original_section.txt', 'r', encoding='utf-8') as f:
        original_section = f.read()

original_section = original_section.replace("‘","'")
original_section = original_section.replace("’","'")
original_section = original_section.replace("“",'"')
original_section = original_section.replace("”",'"')
original_section = original_section.replace("–",'-')
paragraphs = original_section.split('\n\n')

html_section = ""

for paragraph in paragraphs:
    html_section += "<p>" + paragraph + "</p>"+'\n'

print(html_section)