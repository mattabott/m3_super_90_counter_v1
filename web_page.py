def web_page(value):
  HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;  /* changed from 'center' */
            height: 100vh;
            margin: 0;
            padding-top: 10vh;  /* increased padding-top to push content down */
            background-color: #F3F4F6;
        }
        h1 {
            font-size: 75px;
            margin-bottom: 50px;
            color: #374151;
        }
        button {
            font-size: 70px;
            width: 600px;
            height: 300px;
            margin-bottom: 20px;
            border: none;
            border-radius: 15px;
            color: #F3F4F6;
            transition: transform 0.1s ease-in-out;
        }
        button:active {
            transform: scale(0.98);
        }
        #increase {
            background-color: #60A5FA;
        }
        #decrease {
            background-color: #FBBF24;
        }
        #start {
            background-color: #34D399;
        }
    </style>
</head>
<body>

<h1>Value: %s</h1>

<button id="increase" onclick="location.href='/increase'">Increase</button>
<button id="decrease" onclick="location.href='/decrease'">Decrease</button>
<button id="start" onclick="location.href='/start'">Start</button>

</body>
</html>

"""
  return HTML % value