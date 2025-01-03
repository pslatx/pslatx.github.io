This new tool builds the vast majority of the html for you.

1. Convert the pdf to a .docx via adobe https://www.adobe.com/acrobat/online/pdf-to-word.html
    Note: This only allows a limited number of uses before it starts asking for you to sign up. This can be bypassed, to an extent, by using an 
    incognito window, waiting, and/or by using a proxy/viewpoint
2. Open the .docx in google drive.
3. Delete the Title page, and outline page so the first thing in the docx is the header of the first article
4. Go through and add italics html markers around italicsed sections. Make mental note of any special formatting that will have to be done after 
    the fact (adding a left margin for quotes, adding hyperlinks to other articles, videos, etc)
5. Copy and paste the content of the docx into a .txt within the pdf_to_html_converter_tool directory
6. Edit the content so all paragraphs are a single line, and each paragraph is separated from all others by an empty line
7. Edit the top 3 variables in txt_and_dict_to_html.plays
    outline_dict - make sure all article titles and sections show up exactly as they are in the docx txt - you may have to edit the docx txt, 
        especially for sub-titles 
    txt_file - the name of the .txt representation of the docx made in step 5. Depending on where you ran this you may need to give a relative 
        path instead of just a file name
    outputName - "reading_x.html" where x is the class number
8. Run the txt_and_dict_to_html.py - depending on where you ran this from you may need to move the produced "reading_x.html" file into the root 
    directory of the repo
9. edit the index-unrestricted to reference the new file
10. Check how it looks, go back and add any additional things needed, as considered in step 4.