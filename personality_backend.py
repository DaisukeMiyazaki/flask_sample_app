from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/', methods=['GET'])
def process_GET_request():
    # personality_type 
    render_template('page.html', title='personality', name="top page")

@app.route('/', methods=['POST'])
def process_POST_request():
    print("post request is received")
    # result_dictionary = {
    #     "first_question": 0,
    #     "second_question": 1,
    #     "third_question": 2,
    # }
    # result_type = process_data(result_dictionary)
    # if request.method == 'POST':
    #     selected_items = request.form.getlist('items')
    #     print(selected_items)
    #     personality_type render_template('page.html',result_type=result_type)

def result():
    total = 0

    for i in range(1,11):
        answer = request.form.get('q{}'.format(i))
        total += int(answer)
    
    if total >= 40:
        personality_type = 'type A'
    elif 30 <= total <40:
        personality_type = 'type B'
    elif 20 <= total <30:
        personality_type = 'type C'
    elif total >=0:
        personality_type = 'type D'
    
    return render_template('page.html', total = total)

# def process_data(data):
#     """
#     parse the request data and personality_type the personality type
#     """
#     result_type = "温厚型"
#     # TODO
#     personality_type result_type 

if __name__ == "__main__":
    app.run(debug=True, port=4000, threaded=True)
