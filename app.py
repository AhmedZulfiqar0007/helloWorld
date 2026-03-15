from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Go to /hello to see the Hello World page.'

@app.route('/hello')
def hello():
    return render_template('hello.html')


# FAVORITE COURSE ROUTE
@app.route('/favorite-course')
def favorite_course():

    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    return render_template(
        'favorite-course.html',
        subject=subject,
        course_number=course_number
    )


# CONTACT PAGE
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        first = request.form.get('first_name')
        last = request.form.get('last_name')
        email = request.form.get('email')
        message = request.form.get('message')

        return render_template(
            'contact.html',
            submitted=True,
            first=first,
            last=last,
            email=email,
            message=message
        )

    return render_template('contact.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True)