You can create a html form like this 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.metroui.org.ua/current/metro.css">
    <title>Document</title>
</head>
<body style="margin: 10px;">
    <div style="width: 80%;margin: auto;">
        <form action="http://127.0.0.1:5000/api/signup" style="padding:5px;margin: auto;width:60%" method="POST">
            <input type="text" name="name" id="name" data-role="input" placeholder="Enter name"  > <br>
            <input type="email" name="email" id="email" data-role="input"><br>
            <input type="password" name="paswd" id="pass" data-role="input" placeholder="Password"><br>
            <input type="password" name="cPaswd" id="pass" data-role="input" placeholder="Confirm Password"><br>
            <button type="submit" class="button warning">Register</button>
        </form>
    </div>
    <script src="https://cdn.metroui.org.ua/current/metro.js"></script>
</body>
</html>
