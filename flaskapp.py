from htmlparse import getTags, seeMore
from flask import Flask, redirect, url_for, request, render_template
app = Flask (__name__)


# @app.route('/result')
# def resultPage(name):
#   return render_template('result.html', name)
   

@app.route('/main', methods=['GET', 'POST'])
def mainPage():
  if request.method == 'POST':
    tagOne = request.form['tagone']
    tagTwo = request.form['tagtwo']
    pageSource = request.form['source']
    tagSelection = getTags(pageSource, tagOne, tagTwo)
    moreDetails = seeMore(pageSource, tagOne)
    print(tagSelection) # this print is for debugging purposes
    # return redirect(url_for('resultPage', name=tagSelection))
    # if not tagSelection:
      # noResult = 'No results'
      # tagSelection = eval('[' + noResult + ']')
      # tagSelection = noResult.split()
    return render_template('result.html', tagSelection=tagSelection, moreDetails=moreDetails, tagOne=tagOne, tagTwo=tagTwo)
  else:
    return render_template('main.html')

if __name__ == '__main__':
  app.run(debug=True)