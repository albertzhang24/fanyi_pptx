# GET URL: #

**FORMAT**: 
'http://api.fanyi.baidu.com/api/trans/vip/translate?appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s' % (appid, urllib.parse.quote(q), sourceLang, targetLang, str(salt), sign)

**EXAMPLE**:
http://api.fanyi.baidu.com/api/trans/vip/translate?appid=20151113000005349&q=banana&from=en&to=zh&salt=60374&sign=f452655dd6a5e80570020358ecf11f94
    
## Path Params ##
Parameter     | Type          | Defintion                   
------------- | ------------- | -------------
appid         | String        | Your developer APP ID, get it from your application information in Baidu Cloud.
secretkey    | String        | Your developer Secret Key, get it from your application information in Baidu Cloud.
q    | String        | The input word/phrase to be translated. By default, it is a text run in the input powerpoint.
salt          | Integer       | A random integer between 32768 and 65536 that is used in creating the unique URL for the GET HTTP request. It will be parsed into a String for signature creation. No user input needed. 
sourceLang   | String        | The source language of the powerpoint. 
targetLang   | String        | The target language for the translated powerpoint
sign     | String        | The signature that is used for making the url. No user input needed. 

## Returns ##
Sends a GET request to the Baidu Universal Translation API, gets back the response, and prints out user's input query and the translated request query. 


# Error Code List #
Error Code    | Meaning       | Solution                    
------------- | ------------- | -------------
52000         | Success       | None, it worked! 
52001         | Time out error| Make your request smaller.
52002         | System error  | Try again or with a different request. 
52003         | User information not recognized | Check that you entered your APPID and Secret Key correctly and the API is being called. 
54000         | Not all parameters were passed in  | Make sure that you entered all the required parameters - APP ID, Secret Key, string input, salt and signature - corrently. The string input, salt, and signature should be there by default. Please check if they were deleted if they aren't. 
54001         | Incorrect signature  | Make sure that you entered the APP ID, Secret Key, string input, and salt corrently, and that you are parsing the salt variable as a string when you encode it in utf-8. 
54003         | Limited access frequency  | Please lower your calling frequency 
54004         | Insufficient account balance  | Please go to the management control platform and pay to add more credits for future translation requests. 
54005         | Sending long queries too often  | Make your queries shorter or wait for at least 3 seconds before sending another long query. 
58000         | Illegal Client IP  | Make sure your IP address information is correct. You may also change the IP limit or set it to none via the management control platform. 
58001         | Source to Target Languages not supported  | Check the language list document to see if your selected source and target language abbreviations are entered in correctly. 
