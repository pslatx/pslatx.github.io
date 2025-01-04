outline_dict = {
    'The Marxist Understanding of the Roots of LGBTQ Oppression':{
        'date':'June 9, 2015',
        'author':'Liberation School',
        'sections':[
            'REVOLUTIONARY STRUGGLE AND LGBTQ LIBERATION',
            'PATRIARCHY AND CLASS SOCIETY',
            'ENTERING THE CAPITALIST ERA',
            'RESISTANCE TO THE STATUS QUO',
            'LEADING UP TO THE STONEWALL PERIOD',
            'FIGHTING RACISM, SEXISM, HOMOPHOBIA AND TRANSPHOBIA'
        ]
    },
    'Albuquerque Public School Board ‘Parental Rights’ Proposal Part of the National Attack On LGBTQ Rights':{
        'date':'January 20, 2023',
        'author':'Candice Yanez',
        'sections':[
            'WHERE DID KB1 COME FROM?',
            'WHAT’S NEXT IN ALBUQUERQUE?'
        ]
    },
    'A Victory For One Is A Victory For All: Lessons From “Trans Liberation”':{
        'date':'July 27, 2023',
        'author':'Alithia Zamantakis and Aviva Levine',
        'sections':[
            'INTRODUCTION',
            'SOCIAL & POLITICAL CONTEXT OF FEINBERG’S POLITICAL DEVELOPMENT',
            'AN INJURY TO ONE IS AN INJURY TO ALL AND A VICTORY FOR ONE IS A VICTORY FOR ALL',
            'THE ONGOING STRUGGLE FOR TRANS LIBERATION'
        ]
    },
    'The AIDS Fight Back: Reﬂections From A Revolutionary':{
        'date':'May 16, 2014',
        'author': 'Preston Wood',
        'sections':[
            'INTRODUCTION',
            'CAPITALIST GOVERNMENT, MEDIA, AND BIGOTS SPREAD BIGOTRY, HATRED, AND FEAR',
            'THE FIGHT BACK',
            '“ACT UP! FIGHT BACK!”',
            'DENIAL OF EDUCATION AND PREVENTION PROGRAMS',
            'CAPITALIST RULE AND THE AIDS MULTI-FACETED WORLD PANDEMIC'
        ]
    }
}

txt_file = 'class_15_docx.txt'
outputName = 'reading_15.html'




#########DO NOT CHANGE BELOW THIS LINE#########DO NOT CHANGE BELOW THIS LINE#########DO NOT CHANGE BELOW THIS LINE
def get_sections(outline_dict, txt_file):
    # given the outline_dict and the txt_file representing the text from the docx file representation of the origianl pdf
    # returns sections_dict which is structured as {article:[article_intro_section,{sectionTitle:sectionText}]}
    
    def getBetween(string, start, end, author):
        startIndex = string.find(start) + len(start)
        if end != None:
            endIndex = string.find(end)
        else:
            endIndex = len(string)-1
        unedited = string[startIndex: endIndex]
        returnMe = unedited.replace(author,'')
        returnMe = returnMe.strip()
        returnMe = returnMe.replace("‘","'")        
        returnMe = returnMe.replace("’","'")
        returnMe = returnMe.replace("“",'"')
        returnMe = returnMe.replace("”",'"')
        returnMe = returnMe.replace("–",'-')
        returnMe = returnMe.replace('ﬀ','ff')
        returnMe = returnMe.replace('ﬃ','ffi')
        return returnMe

            
    sections_dict = {articleName:['',{sectionName:'' for sectionName in outline_dict[articleName]['sections']}] for articleName in outline_dict}
    allHeaders = []
    for article in outline_dict:
        allHeaders.append(article)
        for section in outline_dict[article]['sections']:
            allHeaders.append(section)
    
    with open(txt_file, 'r', encoding='utf-8') as f:
        allContent = f.read()
    
    for article in sections_dict:
        author = outline_dict[article]['author']
        end = None # acts as a flag to indicate we're on the last article and to read everything until the end
        if allHeaders.index(article) != len(allHeaders)-1:
            end = allHeaders[allHeaders.index(article)+1]
        sections_dict[article][0] = format_section_to_html(getBetween(allContent, article, end, author))
        for section in outline_dict[article]['sections']:
            end = None
            if allHeaders.index(section) != len(allHeaders)-1:
                end = allHeaders[allHeaders.index(section)+1]
            sections_dict[article][1][section] = format_section_to_html(getBetween(allContent, section, end, author))
    return sections_dict

def print_sections_dict(sections_dict):
    # only used for debugging
    for article in sections_dict:
        print (article)
        print('\t'+sections_dict[article][0])
        print('\n')
        for sectionHeader, sectionText in sections_dict[article][1].items():
            print('\t'+sectionHeader)
            print('\t\t'+sectionText)
            print('\n')
        print('\n')

def bulid_html(outline_dict, sections_dict, outputName):
    start = \
"""<!DOCTYPE html>
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

    outline_dynamic_articleName = lambda articleID, articleName: \
f"""
      <li><a href="#{articleID}"><h1>{articleName}</h1></a></li>"""

    outline_dynamic_section_start = \
"""
        <ul>"""
    outline_dynamic_section = lambda sectionID, sectionName: \
f"""
          <li><a href="#{sectionID}"><h2>{sectionName}</h2></a></li>"""
    outline_dynamic_section_end = \
f"""
        </ul>"""


    middle = \
"""
    </ul>
  </div>
  <button id="toggle-btn">☰</button>

  <div id="content">"""


    content_dynamic_articleName_date_author = lambda articleID, articleName, date, author, section_content: \
f"""
    <article id="{articleID}">
      <h1>{articleName}</h1>
      <hr>
      <div class = "publish-date">{date}</div>
      <div class="author">{author}</div>
      <hr>
{section_content}"""

    content_dynamic_section = lambda sectionID, sectionName, section_content: \
f"""
      <section id="{sectionID}">
        <h2>{sectionName}</h2>
{section_content}
      </section>"""

    content_article_end = \
"""
    </article>
"""

    end = \
"""
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
    for articleNum, (articleName, dateAuthorSections) in enumerate(outline_dict.items(), start=1):
        articleID = f'a{articleNum}'
        output += outline_dynamic_articleName(articleID, articleName)
        if len(dateAuthorSections['sections']) > 0: output += outline_dynamic_section_start
        for sectionNum, sectionName in enumerate(dateAuthorSections['sections'], start=1):
            sectionID = f'{articleID}s{sectionNum}'
            output += outline_dynamic_section(sectionID, sectionName)
        if len(dateAuthorSections['sections']) > 0: output += outline_dynamic_section_end

    output += middle

    # create content 
    for articleNum, (articleName, dateAuthorSections) in enumerate(outline_dict.items(), start=1):
        articleID = f'a{articleNum}'
        output += content_dynamic_articleName_date_author(articleID, articleName, dateAuthorSections['date'], dateAuthorSections['author'], sections_dict[articleName][0])
        for sectionNum, sectionName in enumerate(dateAuthorSections['sections'], start=1):
            sectionID = f'{articleID}s{sectionNum}'
            output += content_dynamic_section(sectionID, sectionName, sections_dict[articleName][1][sectionName])
        output += content_article_end

    output += end

    output = output.replace("‘","'")
    output = output.replace("’","'")
    output = output.replace("“",'"')
    output = output.replace("”",'"')
    output = output.replace("–",'-')

    with open(outputName, 'w', encoding='utf-8') as f:
        f.write(output)

def format_section_to_html(original_section):
    paragraphs = original_section.split('\n\n')

    html_section = ""

    for i,paragraph in enumerate(paragraphs):
        if i < len(paragraphs)-1: end = '\n'
        else: end = ''
        html_section += "<p>" + paragraph + "</p>"+end
    
    return html_section


if __name__ == '__main__':
    sections_dict = get_sections(outline_dict, txt_file)
    # print_sections_dict(sections_dict)
    bulid_html(outline_dict, sections_dict, outputName)
    
    