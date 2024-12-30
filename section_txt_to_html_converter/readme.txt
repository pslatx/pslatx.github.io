Intro:
There are two tools in this folder, template_generator.py and converter.py.
template_generator is used to create the reading_x.html template (where x represents the class number) at the beginning
of each pdf to html conversion. The produced file will have sections labeled SECTION_CONTENT_HERE which are then filled
in via the converter.

To use the template_generator you will have to define two variables at the start of the file. A more detailed
description of those variables is in the comments of the file itself. Running the program, with filled out variables, will
produce a reading_x.html file in the section_txt_to_html_converter directory, then move it to the root directory, and replace
the appropriate
`<iframe class='classreadingdoc' src="https://drive.google.com/file/d/10yHEk0YFm-cAxCs6x7auXP8qKLi0Xd8v/preview" width="640" height="480" allow="autoplay"></iframe><br>
<br>`
lines with 
`<a href = "reading_x.html"> INSERT_TITLE Reading</a>
<br><br>`
Where reading_x is updated and so is INSERT_TITLE to match the specific reading.

Now we have to update the SECTION_CONTENT_HERE entries, which is facilitated by the converter.py.

To use the converter:
1. Go to https://drive.google.com/drive/folders/1rhQQtZgDNP75ChfdCVQ2oTkNOK5QdHqC?usp=sharing and view the .docx representation
    of the class pdf you're trying to convert. (You may have to request access from Arno)
2. Scan each section for any highlighted typos and fix them (lots of extra hyphens in the midd-le of wor-ds)
3. Copy and paste the complete content of a section (taking care to omit page numbers, headers/footers, etc) into the
    variable `original_section` in the converter.py. Alternatively, leave the variable set to an empty string and paste the
    content into the original_section.txt
4. Open a cmd and navigate to the section_txt_to_html_converter directory then run `python converter.py`. This will
    produce output.
5. Copy and paste the output into the reading_x.html section you were converting. *TIP: at least in VSCODE, pasting at
    the very beginning of the line (before any whitespace) will automatically respsect indentation.
6. Repeat steps 3 through 5 until you've finished all sections of the reading. *TIP: you can use `clear` in cmd to get
    rid of old lines to reduce clutter and eye-strain.
7. Repeat steps 1 through 6 for all class pdfs you're converting.