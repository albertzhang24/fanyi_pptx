import json
import sys, os
from hashlib import md5
import sys, hashlib, random, json, string
#import http.client
#import urllib.request, urllib.parse, urllib.error
#from pathlib import Path


libraries = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'libs')
# sys.path.append(os.path.join(libraries, "../"))
sys.path.append(libraries)

# from flask import Flask, flash, request, render_template, redirect, url_for, send_from_directory
from pptx import Presentation
from werkzeug.utils import secure_filename

__author__ = 'albertzhang'


appid = '20180531000169614'
secretKey = 'IRP4F_z0fxRscAU5aMt_'
httpClient = None
salt = random.randint(32768, 65536)
count = 0

UPLOAD_FOLDER = 'uploads/'

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def home(event, context):
    index_content = ''
    # Get index file and show to user.
    with open('templates/index.html', 'r') as index_file:
        index_content = index_file.read()

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': index_content
    }


def upload_file(event, context):
    print("event method name" ,event.get("httpMethod"))
    if event.get("httpMethod") == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        translated_filename = secure_filename(translate_powerpoint(filename, file))
        return redirect(url_for('uploaded_file',
                                filename=translated_filename))
    return render_template('index.html')

def uploaded_file(filename, event, context):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def translate_powerpoint(input_filename, file):
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    source_target = request.form['source_target']
    if source_target[:source_target.find("_")] == 'en':
        sourceLang = 'en'
        targetLang = 'zh'
    else:
        sourceLang = 'zh'
        targetLang = 'en'
    source_ppt_str = input_filename
    ppt = Presentation(Path(UPLOAD_FOLDER + input_filename).absolute())
    targetppt = source_ppt_str[:source_ppt_str.find('.pptx')]+"_"+targetLang+".pptx"
    def translate(q):
        m1 = hashlib.md5()
        m1.update((appid+q+str(salt)+secretKey).encode('utf-8'))
        sign = m1.hexdigest()
        url='/api/trans/vip/translate?appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s' %(appid, urllib.parse.quote(q), sourceLang, targetLang, str(salt), sign)
        global count
        try:
            httpClient.request('GET', url)
            response = httpClient.getresponse()
            r = str(response.read())[2:-1]
            j = json.loads(r)
            if 'trans_result' in j:
                return j['trans_result'][-1]['dst'].encode('ascii').decode('unicode-escape')
            elif 'error_msg' in j:
                count += 1
                return '***Error (%s:%s): %s' % (j['error_code'], j['error_msg'], q)
            else:
                count += 1
                return '***Unexpected response for %s: %s' %(q, r)
        except Exception as e:
            count += 1
            return '***Exception (%s): %s' % (e,q)

    for slide in ppt.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.text = translate(run.text)

    translated_path = os.path.join(app.config['UPLOAD_FOLDER'], targetppt)
    ppt.save(translated_path)
    return targetppt
