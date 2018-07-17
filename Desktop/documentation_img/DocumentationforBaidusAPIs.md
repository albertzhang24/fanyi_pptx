# Documentation for Baidu's APIs #

### Getting Started with Translate PPTX: ### 

Choose a source to target language option and the powerpoint you want translated, and we will take care of the rest!
****************************************************************************************************
### Walkthrough: ###
Original Powerpoint

![original powerpoint](https://media.giphy.com/media/fCTqxdJtFd1lKrAw3L/giphy.gif)

Translate it!

![translate it](https://media.giphy.com/media/3XDUQmwUppd4NNZ1gb/giphy.gif)

Translated Powerpoint:

![translated powerpoint](https://media.giphy.com/media/1jl4ssrpu8JtgH3QX2/giphy.gif)

****************************************************************************************************
### How it Works: ###

Using python-pptx freeware, the python script can search each slide of a powerpoint for all of its paragraph text runs. 
Then, the scipt's _translate function translates each the powerpoint's text content from a source to a target language 
by sending a GET request to Baidu's free Univeral Translation API for each text run. 

****************************************************************************************************
### FAQ: ###
**Q:** Does this work for ppt files, Microsoft Office documents, web pages and other?

**A:** No, so far this only works for pptx files. However, you can use https://fanyi.baidu.com/?sid=607 for document translation. We are currently working on supporting translation for other file types as well. 


**Q:** Can I set up my own source to target language options?

**A:** Yes, modify our source code and create your own options in the form field of index.html under templates. 


**Q:** Does this work for translating text in pictures?

**A:** Not currently, but getting OCR to work for powerpoint images is next up on our to-do list.
****************************************************************************************************
### Reference Sources: ###
##### Language List #####
![](images/language_list.png "Language List")


##### Error Code List #####
![](images/error_codes.png "Error Codes")

****************************************************************************************************
### Feedback ###

Please make an issue

