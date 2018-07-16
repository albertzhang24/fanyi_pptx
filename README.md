Documentation for Baidu's APIs
****************************************************************************************************
Getting Started with Translate PPTX: 
Choose a source to target language option and the powerpoint you want translated, and we will take care of the rest :)!
****************************************************************************************************
Walkthrough: 
<iframe src="https://giphy.com/embed/3XDUQmwUppd4NNZ1gb" width="480" height="300" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/3XDUQmwUppd4NNZ1gb">via GIPHY</a></p>
****************************************************************************************************
Set Up:
Download or clone this repo.
Run "sh runner.sh". 
Open the link -  http://127.0.0.1:5000/ - provided by Flask in a browser.
Enter your source to target language and choose a powerpoint. You may also use the provided sample powerpoint .
****************************************************************************************************
FAQ:
Q: Does this work for ppt files, Microsoft Office documents, web pages and other ?
A: No, so far this only works for pptx files. However, use https://fanyi.baidu.com/?sid=607 for document translation.

Q: Can I set up my own source to target language options?
A: Yes, modify our source code and create your own options in the form field of index.html under templates. 

Q: Does this work for translating text in pictures?
A: Not currently, but getting OCR to work for powerpoint images is next up on our to-do list.
****************************************************************************************************
Reference Sources: 
Language List

Error Code List


