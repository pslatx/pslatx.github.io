# You must define the outputName and the classDict

# outputName should be of the format "reading_1.html", "reading_2.html", etc
outputName = 'reading_2.html'

# {articleName:{'date':"Month Day, Year", 'author':"authorName", 'sections':["SectionTitle1, sectionTitle2"]}}
classDict = {
    "Proletarians and Communists / Chapter 2 of the Communist Manifesto" : \
        {
            'date': 'February 21, 1848', 
            'author': 'Karl Marx and Friedrich Engels',
            'sections' : []
        },
    "The Weapon of Theory" : \
        {
            'date': 'January 1966',
            'author': 'Amilcar Cabral',
            'sections': []
        },
    "Socialist Reconstruction, Introduction" : \
        {
            'date': 'October 2022',
            'author': 'Party for Socialism and Liberation',
            'sections':
                [
                    "WORKERS MAKE THE WORLD RUN—WORKERS SHOULD RUN THE WORLD",
                    "CLIMATE CHANGE IS CLASS STRUGGLE",
                    "SOCIALISM IS POSSIBLE AND NECESSARY",
                    "MEANINGFUL WORK AND MORE FREE TIME",
                    "A BETTER FUTURE UNDER SOCIALISM"
                ]
        }
}



###### DONT EDIT PAST HERE ###### DONT EDIT PAST HERE ###### DONT EDIT PAST HERE ######

start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Articles with Collapsible Sidebar</title>
  <link rel="stylesheet" href="reading_style.css">
</head>
<body>

  <div id="sidebar" class="collapsed">
    <h2>Outline</h2>
    <ul>"""

outline_dynamic_articleName = lambda articleID, articleName: f"""
      <li><a href="#{articleID}"><h1>{articleName}</h1></a></li>"""

outline_dynamic_section_start = """
        <ul>"""
outline_dynamic_section = lambda sectionID, sectionName: f"""
          <li><a href="#{sectionID}"><h2>{sectionName}</h2></a></li>"""
outline_dynamic_section_end = f"""
        </ul>"""


middle = """
    </ul>
  </div>
  <button id="toggle-btn">☰</button>

  <div id="content">"""


content_dynamic_articleName_date_author = lambda articleID, articleName, date, author: f"""
    <article id="{articleID}">
      <h1>{articleName}</h1>
      <hr>
      <div class = "publish-date">{date}</div>
      <div class="author">{author}</div>
      <hr>
SECTION_CONTENT_HERE"""

content_dynamic_section = lambda sectionID, sectionName: f"""
      <section id="{sectionID}">
        <h2>{sectionName}</h2>
SECTION_CONTENT_HERE
      </section>"""

content_article_end = """
    </article>
"""

end = """
  </div>
  <script>
    // JavaScript for Collapsible Sidebar
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');

    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
    });
  </script>
</body>
</html>"""

output = start

# create outline 
for articleNum, (articleName, dateAuthorSections) in enumerate(classDict.items(), start=1):
    articleID = f'a{articleNum}'
    output += outline_dynamic_articleName(articleID, articleName)
    if len(dateAuthorSections['sections']) > 0: output += outline_dynamic_section_start
    for sectionNum, sectionName in enumerate(dateAuthorSections['sections'], start=1):
        sectionID = f'{articleID}s{sectionNum}'
        output += outline_dynamic_section(sectionID, sectionName)
    if len(dateAuthorSections['sections']) > 0: output += outline_dynamic_section_end

output += middle

# create content 
for articleNum, (articleName, dateAuthorSections) in enumerate(classDict.items(), start=1):
    articleID = f'a{articleNum}'
    output += content_dynamic_articleName_date_author(articleID, articleName, dateAuthorSections['date'], dateAuthorSections['author'])
    for sectionNum, sectionName in enumerate(dateAuthorSections['sections'], start=1):
        sectionID = f'{articleID}s{sectionNum}'
        output += content_dynamic_section(sectionID, sectionName)
    output += content_article_end

output += end

with open(outputName, 'w', encoding='utf-8') as f:
    f.write(output)


