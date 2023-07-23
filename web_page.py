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
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #F3F4F6;
        }
        .container {
            display: flex;
            justify-content: space-around;
            width: 100%%;
            max-width: 1200px;
            padding: 10vh 0;
        }
        .group {
            display: flex;
            flex-direction: column;
            align-items: center;
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
        #set-time {
            background-color: #2563EB;
        }
        input {
            margin-bottom: 20px;
            font-size: 70px;
            width: 600px;
            height: 100px;
            text-align: center;
        }
    </style>
    <script>
        function setTime() {
            var time = document.getElementById("time").value;
            window.location.href = "/set_time?time=" + time;
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="group">
            <h1>Set Time</h1>
            <input type="number" id="time" min="0" placeholder="Set Time">
            <button id="set-time" onclick="setTime()">Set Time</button>
        </div>
        <div class="group">
            <h1>Value: %s</h1>
            <button id="increase" onclick="location.href='/increase'">Increase</button>
            <button id="decrease" onclick="location.href='/decrease'">Decrease</button>
            <button id="start" onclick="location.href='/start'">Start</button>
        </div>
    </div>
</body>
</html>
"""
    return HTML % value
