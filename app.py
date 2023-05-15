from flask import Flask, request, render_template
import requests, sys

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['POST', 'GET'])
def index():
    # # Update the content of the output div
    # output_div = '<div id="output">' + response.text + '</div>'
    # return render_template('index.html', output=output_div)
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    print('submit button pressed', file=sys.stderr)
    namespace_id = request.form['namespace_id']
    data = request.form['data']
    url = request.form['url'] + '/submit_pfb'

    payload = {
        "namespace_id": namespace_id,
        "data": data,
        "gas_limit": 80000,
        "fee": 2000
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            result = str(response.text)
        else:
            result = f"There was an error with the POST request: {response.text}"
    except Exception as err:
        result = str(err)

    return render_template('index.html', pfb_output=result)


@app.route('/get_namespaced_share', methods=['GET', 'POST'])
def get_namespaced_share():
    try:
        namespace_id = request.form['share_namespace_id']
        block_height = request.form['height']
        url = request.form['share_url'] + f'/namespaced_shares/{namespace_id}/height/{block_height}'
        print(f'sending POST request to {url}')
    except Exception as err:
        result = 'Error reading variables, you are supposed to submit the PFB first!'
        return render_template('index.html', share_output=result)

    try:
        response = requests.post(url)
        result = response.text
    except Exception as err:
        result = str(err)

    return render_template('index.html', share_output=result)


if __name__ == '__main__':
    app.run(port=8000)
