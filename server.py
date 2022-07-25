from flask import Flask, render_template
import subprocess  
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html') 
@app.route('/contact')
def contact():
  return render_template('about.html')

@app.route('/my-link/')
def my_link():
  subprocess.Popen(['python', 'Run_exit_sound.py']) 
  return index() 
  return 'Camera is starting...'  

if __name__ == '__main__':
  app.run()