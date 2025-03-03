Documentation: https://github.com/robinmoisson/staticrypt

What follows is the tl;dr...

When to use staticrypt:
Any time you make an update to index.html we need to rerun staticrypt

How to use:
1. Make your edits to index.html
2. In a CMD terminal open in the root directory of the local repository run `staticrypt index-unrestricted.html -p <OUR_PASSWORD>`
3. Step 2 will generate another index-unrestricted.html within the encrypted directory. Within this generated file, copy 
    the value of the variable `staticryptConfig`
4. Within the index.html in the root directory, replace the value of the `staticryptConfig` variable therein with what
    you copied in step 3.