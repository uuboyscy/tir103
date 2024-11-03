from flask import Flask, request, render_template
from custom_utils import testfun

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello!</h1><h2>hello</h2>"
    # return "Hello"

# url/get_parameters?username=Allen&age=22
@app.route("/get_parameters")
def get_parameters():
    username = request.args.get("username")  # "Allen"
    age = request.args.get("age")  # "22"
    if not username:
        return "What's your name?"
    if not age:
        return f"Hello {username}!"
    return f"Hello {username}! You are {age} years old."

# url/get_employee_info/business_id/<bu_id: str>/department_id/<dep_id: int>
@app.route("/get_employee_info/business_id/<string:bu_id>/department_id/<int:dep_id>")
def get_employee_info(bu_id: str, dep_id: int) -> dict | list:
    # ' OR '1' = '1
    print(
        f"""
            select * from employee
            where bu_id = '{bu_id}'
            and dep_id = {dep_id}
        """
    )
    # cursor.execute(sql, params={"bu_id": bu_id})
    print(type(bu_id))
    print(type(dep_id))
    return {"employee_name": "Allen"}

# [POST] url/get_form_data
@app.route("/get_form_data", methods=["GET", "POST"])
def get_form_data():
    html = """
    <form method='post'>
        <input name='username'>
        <button type='submit'>SUBMIT</button>
    </form>
    """

    # requests.post(url, data={"username": "Allen"})
    request_method = request.method
    print(request_method)
    if request_method == "POST":
        username = request.form.get("username")
        html += f"<h1>{username}</h1>"

    return html


@app.route("/get_form_data_2", methods=["GET", "POST"])
def get_form_data_2():
    request_method = request.method
    username = request.form.get("username")
    return render_template(
        "get_form_data.html",
        request_method=request_method,
        username=username,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
