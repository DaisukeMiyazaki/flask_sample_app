from flask import Flask, render_template, request, redirect, url_for
import code

# 以下をデバッグしたいところに差し込む
# code.interact(local=locals())

app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

"""htmlページをサーバーで取得する為"""
@app.route('/', methods=['GET'])
def process_GET_request():
    return render_template('page.html', title='personality', name="top page")

"""POSTリクエストがあった場合に処理する環境を整える"""
"""POSTリクエストの中身を実際に処理して返す"""

@app.route('/', methods=['POST'])
def process_POST_request():
    print("post request is received")
    apple = "banana"
    result_type = get_personality_type(request,apple)

    if request.method == 'POST':
        # personality_type = result_type
        print("Daisuke")
        return render_template('page.html', result = result_type )






def get_personality_type(request,apple):
    
    """requestの内容を判断して、返す"""
    print(apple) 
    
    total = 0

    for i in range(1,11):
        answer = request.form.get('item{}'.format(i))
        # code.interact(local=locals())
        print(answer)
        if answer:
            total += int(answer)
    print(total)

    if total >= 40:
        personality_type = 'type A'
        return redirect(url_for("result_a"))
    elif 30 <= total <40:
        personality_type = 'type B'
        return redirect(url_for("result_b"))
    elif 20 <= total <30:
        personality_type = 'type C'
        return redirect(url_for("result_c"))
    elif total >=0:
        personality_type = 'type D'
        return redirect(url_for("result_d"))


@app.route('/result_a.html')
def result_a():
    return render_template("result_a.html")

@app.route('/result_b.html')
def result_b():
    return render_template("result_b.html")

@app.route('/result_c.html')
def result_c():
    return render_template("result_c.html")

@app.route('/result_d.html')
def result_d():
    return render_template("result_d.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000, threaded=True)
