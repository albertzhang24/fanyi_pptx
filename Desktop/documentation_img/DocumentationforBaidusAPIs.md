# Documentation for Baidu's APIs #

#### Getting Started with Translate PPTX: #### 
Choose a source to target language option and the powerpoint you want translated, and we will take care of the rest :)!
****************************************************************************************************
### Walkthrough: ###
****************************************************************************************************
Original Powerpoint

![original powerpoint](https://media.giphy.com/media/fCTqxdJtFd1lKrAw3L/giphy.gif)

****************************************************************************************************
Translate it!

![translate it](https://media.giphy.com/media/3XDUQmwUppd4NNZ1gb/giphy.gif)

****************************************************************************************************
Translated Powerpoint:

![translated powerpoint](https://media.giphy.com/media/1jl4ssrpu8JtgH3QX2/giphy.gif)

****************************************************************************************************
### Set Up: ###
Download or clone this repo.
Run "sh runner.sh". 
Open the link -  http://127.0.0.1:5000/ - provided by Flask in a browser.
Enter your source to target language and choose a powerpoint. You may also use the provided sample powerpoint .
****************************************************************************************************
### FAQ: ###
#### Q: ####  
Does this work for ppt files, Microsoft Office documents, web pages and other ?
#### A: #### 
No, so far this only works for pptx files. However, you can use https://fanyi.baidu.com/?sid=607 for document translation. We are currently working on supporting translation for other file types as well. 

#### Q: ####
Can I set up my own source to target language options?
#### A: ####
Yes, modify our source code and create your own options in the form field of index.html under templates. 

#### Q: ####
Does this work for translating text in pictures?
#### A: ####
Not currently, but getting OCR to work for powerpoint images is next up on our to-do list.
****************************************************************************************************
#### Reference Sources: ####
###### Language List ######
![](images/language_list.png "Language List")


###### Error Code List ######
![](images/error_codes.png "Error Codes")


