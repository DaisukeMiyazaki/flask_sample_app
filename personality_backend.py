from flask import Flask, render_template, request, redirect, url_for
import code


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
        print(result_type)
        print(type(result_type))
        if result_type == 'type A':
            return redirect(url_for("result_a"))
        elif result_type == 'type B':
            return redirect(url_for("result_b"))
        elif result_type == 'type C':
            return redirect(url_for("result_c"))
        elif result_type == 'type D':
            return redirect(url_for("result_d"))


# def get_group_list(request):
#     group1 = ["1","4","8","10","13","17"]
#     group2 = ["2","6","9","12","15","18"]
#     group3 = ["3","5","7","11","14","16"]

    # return my_list

def get_personality_type(request,apple):
    group1 = ["1","4","8","10","13","17"]
    group2 = ["2","6","9","12","15","18"]
    group3 = ["3","5","7","11","14","16"]

    """group1(=タイプA),group2(=タイプB),group3(=タイプC)にはそれぞれHTMLのitem名に当たる数値を入れてリスト化
    forinを連続することで、それぞれのタイプ別の質問Valueの合算をしている"""
    print(apple) 

    total = 0
    for i in group1:
        answer = request.form.get('item{}'.format(i))
        print(answer)
        if answer:
            total += int(answer)
    print(total)
    print("kanako")

    total2 = 0
    for i in group2:
        answer = request.form.get('item{}'.format(i))
        print(answer)
        if answer:
            total2 += int(answer)

    print(total2)
    print("kana")

    total3 = 0
    for i in group3:
        answer = request.form.get('item{}'.format(i))
        print(answer)
        if answer:
            total3 += int(answer)
    print(total3)
    print("ka")

    # for i in range(1,11):
    #     answer = request.form.get('item{}'.format(i))
    #     # code.interact(local=locals())
    #     print(answer)
    #     if answer:
    #         total += int(answer)
    # print(total)
    print(max(total,total2,total3))

    """total=タイプA,total2=タイプB,total3=タイプC
    -それぞれが最も高い数値の時は、それぞれのタイプを返す
    -数値が同一になってしまった場合は、強いタイプを優先して返す
    （タイプＡ＞タイプＣ＞タイプＢ）"""
    if total >= total2 and total3:
        personality_type = "A"
    elif total2 > total and total3:
        personality_type = "B"
    elif total3 > total and total2:
        personality_type = "C"
    elif total == total2 > total3 or total == total3 > total2:
        personality_type = "A"
    elif total2 == total3 >total:
        personality_type = "C"
    personality_type = "type " + personality_type
    return personality_type


    # if total >= 40:
    #     personality_type = "A"
    # elif 30 <= total <40:
    #     personality_type = "B"
    # elif 20 <= total <30:
    #     personality_type = "C"
    # elif total >=0:
    #     personality_type = "D"
    # personality_type = "type " + personality_type

    # return personality_type




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
    print("Flask server has started")
