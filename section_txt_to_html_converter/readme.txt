1. Download the class pdf you're trying to convert sections in
2. use https://www.pdf2go.com/pdf-to-word to convert it to a word document (this will make copying and pasting sections easier so we avoid missing characters, which happens frequently when copy/pasting directly from pdfs)
3. If you don't have word, upload the new .docx to your google drive so you can view it therein. Otherwise just view it in word.
4. Open the .docx
5. Copy and paste the complete content of a section (taking care to omit page numbers, headers/footers, etc) into the variable `original_section` in the converter.py
6. Open a cmd and navigate to the section_txt_to_html_converter directory then run `python converter.py`. This will produce output.
7. Copy and paste the output into the reading_x.html section you were converting. *TIP: at least in VSCODE, pasting at the very beginning of the line (before any whitespace) will automatically respsect indentation.
8. Repeat steps 5 through 7 until you've finished all sections of the reading. *TIP: you can use `clear` in cmd to get rid of old lines to reduce clutter and eye-strain.
9. Repeat steps 1 through 8 for all class pdfs you're converting.