# University admission prediction model:

## Description of the project:

Build a Model which is able to predict chances of students to get the admission from the university using Admission_prediction dataset.


## Description of dataset:

The dataset contains several parameters which are considered important during the application for Masters Programs. The parameters included are :

- GRE Scores ( out of 340 )
- TOEFL Scores ( out of 120 )
- University Rating ( out of 5 )
- Statement of Purpose ( out of 5 )
- Letter of Recommendation Strength ( out of 5 )
- Undergraduate GPA ( out of 10 )
- Research Experience ( either 0 or 1 )
- Chance of Admit ( ranging from 0 to 1 

## Installation and Usage steps:

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt.

```bash
pip install -r requirements.txt
```

2. Now the run the app.py, it will generate a url

```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5006
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 699-533-116
```

3. Output tests

```bash
 * Debugger is active!
 * Debugger PIN: 699-533-116
127.0.0.1 - - [30/Aug/2022 03:27:55] "GET / HTTP/1.1" 200 -
prediction is  [[0.70477029]]
127.0.0.1 - - [30/Aug/2022 03:28:18] "POST /predict HTTP/1.1" 200 -
```


## [Heroku](https://www.heroku.com) Deployment steps:

1. Install the heroku cli

```bash
$ heroku login
```

2. Deploy the application 

```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## MIT License 

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) [2022] [Babu Jayaraman]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
