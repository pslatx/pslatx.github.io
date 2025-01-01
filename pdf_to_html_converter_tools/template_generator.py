# You must define the outputName and the classDict

# outputName should be of the format "reading_1.html", "reading_2.html", etc
outputName = 'reading_8.html'

# {articleName:{'date':"Month Day, Year", 'author':"authorName", 'sections':["SectionTitle1, sectionTitle2"]}}
classDict = {
  'What is imperialism? An introduction':\
    {
      'date': 'September 20, 2021',
      'author': 'Summer Pappachen',
      'sections':
        [
            'MARX ON COLONIALISM AND ANTI-COLONIAL STRUGGLES',
            'FROM COLONIALISM TO IMPERIALISM',
            'IMPERIALISM: CAPITALIST WARS AND REVOLUTIONARY SOLUTION',
            'CONCLUSION: PROLETARIAN INTERNATIONALISM'
        ]
    },
 'From inter-imperialist war to global class war: Understanding distinct stages of imperialism' :\
    {
        'date': 'July 20, 2018',
        'author' : 'Brian Becker',
        'sections':
          [
              'ENDLESS WAR AND MILITARISM IN THE MODERN ERA',
              'THE DEBATE ABOUT WAR AND MILITARISM',
              'WHAT MADE WAR INEVITABLE UNDER CAPITALISM',
              'THE CENTRALITY OF COLONIALISM TO LENIN’S THESIS',
              'IMPERIALISM: FROM POLICY TO SYSTEM',
              'SOVIET UNION CHANGES THE EQUATION',
              'GLOBAL CLASS WAR PUTS A CAP ON INTER-IMPERIALIST CONFLICT',
              'IMPERIALIST ENEMIES BECOME FRIENDS',
              'NO WWIII, BUT SOME CLOSE CALLS',
              'NUCLEAR WEAPONS AND THE ORIGIN OF THE COLD WAR',
              'HOW ALLIES BECOME FRIENDS: BACKGROUND TO THE NEW GLOBAL CONFRONTATION',
              'THE KOREAN WAR: A CLASS WAR DISGUISED AS A WAR BETWEEN NATIONS',
              'CHURCHILL FAVORED NUCLEAR ANNIHILATION, US FAVORED ‘CONTAINMENT’',
              '‘CONTAINMENT’ WAS A WAR AGAINST OPPRESSED PEOPLE FIGHTING FOR FREEDOM',
              'IMPERIALIST WAR DRIVE CONTINUES IN NEW FORMS'
          ]
    },
  "International Peoples' Assembly Political Platform":\
    {
        'date': 'current',
        'author': "International Peoples' Assembly",
        'sections':
          [
            'FOR ANTI-CAPITALIST STRUGGLE AND NEW FORMS OF ORGANIZING SOCIETY',
            'FOR ANTI-IMPERIALIST, ANTI-COLONIAL AND ANTI-ZIONIST STRUGGLE AND IN DEFENSE OF NATIONAL AND POPULAR SOVEREIGNTY',
            'FOR ANTI-CAPITALIST AND PEOPLE’S FEMINISM',
            'FOR THE ANTI-RACIST STRUGGLE AND AGAINST RACIAL DISCRIMINATION',
            'FOR AN END TO THE FAILED BOURGEOIS STATE',
            'FOR A NEW PEOPLE’S DEMOCRACY',
            'FOR THE DEFENSE OF NATURAL RESOURCES AS COMMON GOODS',
            'FOR A PEOPLE’S LAND REFORM',
            'FOR CONTROL AND NATIONALIZATION OF THE FINANCIAL SYSTEM, TAX HAVENS, AND TRANSNATIONAL CORPORATIONS',
            'FOR THE RIGHT TO WORK FOR ALL WITH RIGHTS AND WAGES WITH DIGNITY',
            'FOR SOCIAL AND HUMAN RIGHTS',
            'FOR THE RIGHT TO EDUCATION AND ACCESS TO KNOWLEDGE',
            'FOR THE RIGHTS OF LGBT PEOPLE',
            'FOR OUR RIGHTS AS MIGRANTS, REFUGEES, POPULATIONS IN DIASPORAS, INDIGENOUS AND AFRO DESCENDENT PEOPLES, AND ALL THOSE WHO ARE ESPECIALLY VULNERABLE IN OUR SOCIETIES',
            'FOR THE FREEDOM OF ALL POLITICAL PRISONERS IN THE WORLD',
            'FOR STRUGGLE WITH POLITICAL POWER',
            'FIGHT AGAINST FUNDAMENTALISM, SECTARIANISM, AND RELIGIOUS INTOLERANCE'
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

output = output.replace("‘","'")
output = output.replace("’","'")
output = output.replace("“",'"')
output = output.replace("”",'"')
output = output.replace("–",'-')

with open(outputName, 'w', encoding='utf-8') as f:
    f.write(output)


