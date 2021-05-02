from flask import Flask
app Flask(__name__)

@app.route('/')
def quests():
  return 'The Test'