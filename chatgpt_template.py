import zipfile
import os

# Create HTML content with dark mode toggle
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Deque Enterprise Proposal — Hypervanse</title>
  <style id="theme-style">
    body {
      background: black;
      color: #00ff00;
      font-family: 'Courier New', monospace;
      padding: 2em;
    }
    h1, h2, h3 {
      color: #00ff99;
      border-bottom: 1px solid #00ff99;
      padding-bottom: 0.2em;
    }
    a { color: #00ccff; text-decoration: underline; }
    .code-block {
      background: #111;
      padding: 1em;
      margin: 1em 0;
      border-left: 3px solid #00ff00;
      overflow-x: auto;
      white-space: pre-wrap;
    }
    .glow { animation: pulse 2s infinite; }
    @keyframes pulse {
      0% { text-shadow: 0 0 5px #00ff00; }
      50% { text-shadow: 0 0 20px #00ff00; }
      100% { text-shadow: 0 0 5px #00ff00; }
    }
    audio {
      width: 100%;
      margin-top: 20px;
    }
    .toggle-btn {
      position: fixed;
      top: 1em;
      right: 1em;
      background: #222;
      color: #00ff00;
      padding: 0.5em 1em;
      border: 1px solid #00ff00;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <button class="toggle-btn" onclick="toggleTheme()">Toggle Theme</button>
  <h1 class="glow">🧠 Deque Enterprise Partnership Proposal</h1>

  <h2>🔍 From</h2>
  <p><strong>Frederico Correia Moreira</strong><br/>
  <em>aka <span class="glow">Hypervanse</span></em><br/>
  Email: frederico-moreira@ceca-ufal.br<br/>
  Affiliation: UFAL – Universidade Federal de Alagoas</p>

  <h2>📌 Context</h2>
  <p>Unauthorized CSS metadata injections were found in Microsoft's 'Semantic Kernel' output during audits of AI platforms such as Gemini using axe DevTools Pro.</p>
  <p><a href="https://axe.deque.com/axe-devtools/user-flows/2a55bb67-20eb-4254-bc67-830841ac3237/issues?pageStateKey=1744182000089-https%3A%2F%2Fgemini.google.com%2Fapp%2Fec095b7906ae3b49" target="_blank">Gemini Violation Report</a></p>

  <h2>🧪 Proposal Summary</h2>
  <ul>
    <li>Extend access to axe DevTools Enterprise</li>
    <li>Conduct accessibility CI/CD red-teaming</li>
    <li>Co-author research output / technical blog</li>
  </ul>

  <h2>💾 Metadata Summary</h2>
  <div class="code-block">
    Proposal includes deep dive into accessibility violations<br/>
    Triggered by metadata-injected CSS<br/>
    Crossed threshold into deceptive AI UI practices
  </div>

  <h2>🎵 Soundtrack</h2>
  <audio controls>
    <source src="soundtrack.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>

  <script>
    function toggleTheme() {
      const style = document.getElementById("theme-style");
      const isDark = style.innerHTML.includes("background: black");
      style.innerHTML = isDark ?
        \`body { background: white; color: black; font-family: 'Courier New', monospace; padding: 2em; }
         h1, h2, h3 { color: black; border-bottom: 1px solid black; }\` :
        \`body { background: black; color: #00ff00; font-family: 'Courier New', monospace; padding: 2em; }
         h1, h2, h3 { color: #00ff99; border-bottom: 1px solid #00ff99; }\`;
    }
  </script>
</body>
</html>
"""

# Write to a local HTML file
html_filename = "/mnt/data/deque_proposal.html"
with open(html_filename, "w") as f:
    f.write(html_content)

# Create a ZIP archive including the HTML file and placeholder for soundtrack
zip_filename = "/mnt/data/deque_proposal_package.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(html_filename, arcname="index.html")
    # Add a placeholder soundtrack file (empty)
    open("/mnt/data/soundtrack.mp3", "wb").close()
    zipf.write("/mnt/data/soundtrack.mp3", arcname="soundtrack.mp3")

zip_filename