from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def process_GET_request():
    return render_template('page.html', title='personality', name="top page")

@app.route('/', methods=['POST'])
def process_POST_request():
    print("post request is received")
    result_dictionary = {
        "first_question": 0,
        "second_question": 1,
        "third_question": 2,
    }
    result_type = process_data(result_dictionary)
    if request.method == 'POST':
        selected_items = request.form.getlist('items')
        print(selected_items)
        return render_template('page.html',result_type=result_type)

def process_data(data):
    """
    parse the request data and return the personality type
    """
    result_type = "温厚型"
    # TODO
    return result_type 

if __name__ == "__main__":
    app.run(debug=True, port=4000, threaded=True)
