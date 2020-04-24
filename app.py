#!/usr/bin/env python
# coding: utf-8

# In[11]:


#from google.colab import drive
#drive.mount('/content/drive')


# In[ ]:


#!cp -r /content/drive/My\ Drive/30_th_april_submission/* ./


# In[13]:


#!pip install flask-ngrok


# Flask Modules : <br>
# -------------------------------------------------------------------------------------------

# In[ ]:


from flask import Flask,render_template,redirect,url_for,request,flash
#from content_management import Content
from flask_ngrok import run_with_ngrok
import os
import time
from werkzeug.utils import secure_filename
#--------------------------------------------------------------------------------------------


# TF Modules<br>
# ===========================================================================================<br>
# reprocessing libraries

# In[ ]:


from pmd_module import *
# ------------------------------------------------------------------------------------------- 


# -------------------------------------------------------------------------------------

# In[ ]:


app = Flask(__name__)															#     |
app.secret_key = "abcd_1234_@2441139"
#run_with_ngrok(app)  # Start ngrok when app is run 							#     |
var = None 
global model 	
model = load_PMD_model()
t1=0																	#     |
app.config['UPLOAD_FOLDER']=os.path.join(os.getcwd(),'static','uploads')        #     |
#--------------------------------------------------------------------------------------


# ___________________________STARTING_POINT____________________________________________

# In[ ]:


@app.route("/") 																#     |
def home():	 																	#     |
	return render_template("index.html") 										#     |
#======================================================================================


# _________________________Upload_Point________________________________________________

# In[ ]:


@app.route("/upload",methods=['GET','POST']) 									#     |
def upload():                           
	#t1=0																		#	  |																		#     |
	if request.method=='GET': 													#     |
		global var 															    #     |
		if var!= None: 															#     |
			os.remove(var) 														#     |
			var =None 															#     |
		else:	 																#     |
			var = None 															#     |
		return render_template("upload.html") 									#     |
	#_________________________________________________________________________________|
	
	#____________________IN_POST_Part____________________________________________________________
	else:
		t1 = time.perf_counter()														  #     |
		print('in post part') 															  #     |
		fileObj = request.files['my_file']                                                #     |
		print(fileObj)                                                                    #     |
		fname=os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(fileObj.filename)) #     |
		fileObj.save(fname)                                                               #     |
		
		#flash(f"File saved at {app.config['UPLOAD_FOLDER']}")                             #     |
		var = fname
		predicted_result = predict_the_class(get_image(fname)) 
		print(f"Result : {predicted_result}")
		flash(f'This picture belong to {predicted_result}')
		
		tf = round(time.perf_counter()- t1,2)
		flash(f'Time Taken to predict : {tf} sec.')                                                                     #     |
		return render_template('result.html')                     						  #     |
#===============================================================================================|


# ===============================MAIN_call==========================================

# In[ ]:


if __name__ == '__main__':													#     |
	#app.run(debug=True) 													#     |
	app.run()																#     |
#----------------------------------------------------------------------------------		
	


# In[ ]:




