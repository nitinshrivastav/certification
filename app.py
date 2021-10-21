#!/usr/bin/env python
# coding: utf-8

# In[81]:


from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def jkjksdf():
    return render_template('info.html')
@app.route('/details',methods=['POST'])
def jkhkj():
    if request.method=='POST':
        url1=request.files['a']
        url1.save(url1.filename) 
        url2=request.files['b']
        url2.save(url2.filename)
        df = pd.read_excel(url2.filename)
        font = ImageFont.truetype('arial.ttf', 30)
        for index, j in df.iterrows():
            img = Image.open(url1.filename)
            draw = ImageDraw.Draw(img)
            draw.text(xy=(440, 412),
                text='{}'.format(j['name'].title()),
            fill=(0, 0, 0),
            font=font)
            img.save('{}.jpeg'.format(j['name']))
        return render_template('info.html')

if __name__=='__main__':
    app.run()


# In[ ]:




