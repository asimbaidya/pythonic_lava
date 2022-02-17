from flask import Flask

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return '''
<head>
    <title>The Pythonic Lava</title>
    <style>
        body{
            text-align: center;
            font-size: 30px;
            color: royalblue;
        }
        .content{
            background-color: lightgreen;
            margin: 30px;    
        }
    </style>
</head>

<body>
    <div class="content">
        <h1>Probable Routes</h1>
        <h3>/reports</h3>
        <h3>/info</h3>
        <h3>/todo</h3>
        <h1>Pythonic Lava💀</h1>
    </div>
</body>
'''
    return app
