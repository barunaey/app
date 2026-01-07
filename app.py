from flask import Flask, render_template_string
from flask import url_for

app = Flask(__name__)

love_letter = """
To kanwxu, 

Every day with you feels lighter, warmer and a little more magical
You make me laugh and somehow you still manage to be
the best part of every single day. Thank you for being honest with me and for listening when I opened up too. 
I really appreciate your strength and your heart. 
 I truly value what we have, and I don’t want to lose it. 
 I want us to keep communicating like this honestly, calmly and with love.

Thank you for your patience, your silly jokes, your soft heart,
and for staying even when things aren’t perfect.

I don't know exactly where life is taking us,
but I do know I am happiest walking there with you.

From,
    Barun shrestha
"""

playlist = [
    ("Perfect", "Ed Sheeran"),
    ("All of Me", "John Legend"),
    ("Until I Found You", "Stephen Sanchez"),
    ("Just The Way You Are", "Bruno Mars"),
    ("Love Story", "Taylor Swift"),
]

photos = [
    # add your image links here
    "static/photos/img 1.jpeg",
    "static/photos/img 2.jpeg",
    "static/photos/img 3.jpeg",
    "static/photos/img 4.jpeg",
]

html = """
<!DOCTYPE html>
<html>
<head>
<title>For You ❤️</title>

<style>
body{
    background: radial-gradient(circle at top, pink, #ffb3c6, #ff9aa2);
    font-family: Arial;
    text-align:center;
    padding: 30px;
    overflow-x:hidden;
}

/* floating hearts */
.heart{
    position: fixed;
    color: red;
    font-size: 22px;
    animation: float 6s linear infinite;
    opacity: 0.7;
}
<img src="{{ url_for('static', filename=photo) }}">

@keyframes float{
    0% { transform: translateY(0); opacity:1; }
    100% { transform: translateY(-800px); opacity:0; }
}

.card{
    background:white;
    border-radius:20px;
    padding:25px;
    max-width:800px;
    margin:auto;
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
}

/* gallery */
.gallery img{
    width:160px;
    height:160px;
    border-radius:20px;
    object-fit:cover;
    margin:8px;
    box-shadow:0 6px 16px rgba(0,0,0,0.2);
}
</style>

<script>
function hearts(){
    let heart = document.createElement("div");
    heart.innerHTML = "❤️";
    heart.className = "heart";
    heart.style.left = Math.random()*100 + "vw";
    heart.style.bottom = "0px";
    document.body.appendChild(heart);
    setTimeout(()=>heart.remove(), 6000);
}
setInterval(hearts, 600);
</script>

</head>

<body>

<h1>Kanwxu❤️</h1>
<p>This small website exists for one reason: to make you smile.</p>

<div class="card">
<h2>💌 Love Letter</h2>
<p style="white-space: pre-line; font-size:17px;">{{ love_letter }}</p>
</div>

<br>

<div class="card">
<h2>🎵 Our Playlist</h2>
<ul style="list-style:none; padding:0;">
{% for song, artist in playlist %}
<li><b>{{ song }}</b> — {{ artist }}</li>
{% endfor %}
</ul>
</div>

<br>

<div class="card">
<h2>📸 Our Little Gallery</h2>
<div class="gallery">
{% for photo in photos %}
<img src="{{ photo }}">
{% endfor %}
</div>
</div>

<p>Made with ❤️ just for you</p>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, love_letter=love_letter, playlist=playlist, photos=photos)

if __name__ == "__main__":
    app.run(debug=True)
