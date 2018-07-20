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

