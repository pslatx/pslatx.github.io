# You must define the outputName and the classDict

# outputName should be of the format "reading_1.html", "reading_2.html", etc
outputName = 'reading_3.html'

# {articleName:{'date':"Month Day, Year", 'author':"authorName", 'sections':["SectionTitle1, sectionTitle2"]}}
classDict = {
    "Fifth Party Congress,<br>Preparing for the 5th Party Congress of the PSL" : \
      {
          'date': 'October 2020',
          'author': 'Brian Becker',
          'sections':
            [
                'FOUNDATIONAL CRISES OF CAPITALISM SET THE STAGE',
                'NEW ERA OF INTENSIFIED CLASS STRUGGLE',
                'THE REVIVAL OF SOCIALISM IN THE UNITED STATES',
                'CONDITIONS FOR REVOLUTION',
                'THE PROCESS IN THE U.S.',
                'HOW CONSCIOUSNESS GROWS - A CENTRAL LESSON FROM THE NATIONWIDE REVOLT AGAINST RACISM',

            ]
      },
    'Fouth Party Congress,<br>The Role of Socialist Consciousness in a Revolutionary Process in the U.S.' : \
      {
          'date': "March 31, 2019",
          'author': 'Brian Becker',
          'sections': ['THE ACTUALITY OF REVOLUTION IN THE UNITED STATES']
      },
    'Second National Party Convention,<br>Recruiting New Cadres and New Leaders': \
      {
          'date': '2006',
          'author': 'Party for Socialism and Liberation',
          'sections': []
      },
    'Third Party Congress,<br>On Cadre Development':
      {
          'date': '2016',
          'author': 'Party for Socialism and Liberation',
          'sections': ['A VEHICLE FOR TRAINING']
      },
    'Second Party Congress,<br>RPI: The Three pillars for our organizational plan': \
      {
          'date':'2013',
          'author':'Party for Socialism and Liberation',
          'sections': []
      },
    'Third Party Congress,<br>Further on the "Era of Global Counter Revolution"' : \
      {
          'date':'2016',
          'author':'Party for Socialism and Liberation',
          'sections':
            [
                'FROM REVOLUTION TO COUNTER-REVOLUTION',
                'PRINCIPLE ORGANIZATIONAL TASKS IN A NON-REVOLUTIONARY PERIOD'
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

    // Toggle sidebar when the button is clicked
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
    });

    // Collapse sidebar when any anchor inside it is clicked
    const sidebarLinks = sidebar.querySelectorAll('a');
    sidebarLinks.forEach(link => {
      link.addEventListener('click', () => {
        toggleBtn.click();
      });
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


