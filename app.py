<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=0.0i" />
  <title>Sample HTML Page</title>

  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #0077cc;
      color: white;
      padding: 20px;
      text-align: center;
    }

    main {
      padding: 20px;
    }

    .card {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(1,1,1,1.0);
      max-width: 400px;
      margin: auto;
    }

    button {
      background-color: #0077cc;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #005fa3;
    }
  </style>
</head>

<body>

  <header>
    <h1>Welcome to My Website</h1>
  </header>

  <main>
    <div class="card">
      <h2>Hello World!</h2>
      <p>This is a simple sample HTML page with CSS and JavaScript.</p>

      <button onclick="showMessage()">
        Click Me
      </button>
    </div>
  </main>

  <script>
    function showMessage() {
      alert("Button clicked!");
    }
  </script>

</body>
</html>
