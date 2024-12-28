original_section="""We are convinced that we have now entered a new phase. Capitalist economic globalization and its attendant assault on the working class at home is combining with the rapid global march of the U.S. military machine to create new social and class contradictions that will lead to a revival of the socialist and workers movement inside the United States.

Most of the people in the world today are suﬀering from economic depression and recession. The U.S. ruling class is holding it breath, well aware that when the U.S. capitalist economy is seized by the next severe crisis or downturn, it is likely to precipitate a global economic crisis of historic proportions. Under those circumstances, the rule of capitalism must face the inevitable challenge of a revived movement for socialism. That is our Party’s orientation. Marx’s prognosis and theory of revolution in the advanced capitalist societies will be validated by the revival of revolutionary socialism in the very center of imperialism.

At the same time as we aim for revolution in the United States, we stand for defense of the existing workers’ states, the national liberation movements and for oppressed people around the world who stand in the crosshairs of U.S. imperialism. Only a party steeled in working-class internationalism can hope to lead a revolution in the United States, the 21st Century prisonhouse of nations.

The magnitude of our tasks will be matched by our determination to win. Workers and oppressed people of the world, unite!"""

original_section = original_section.replace("‘","'")
original_section = original_section.replace("’","'")
original_section = original_section.replace("“",'"')
original_section = original_section.replace("”",'"')
paragraphs = original_section.split('\n\n')

html_section = ""

for paragraph in paragraphs:
    html_section += "<p>" + paragraph + "</p>"+'\n'

print(html_section)