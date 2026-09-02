import sys

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="550" height="433" viewBox="0 0 550 433">
<defs>
  <style>
    .key    { font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: #22D3EE; font-weight: bold; }
    .value  { font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: #E5E7EB; }
    .cc     { font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: #475569; }
    .head   { font-family: 'Courier New', Consolas, monospace; font-size: 17px; fill: #7C3AED; font-weight: bold; }
    .accent { font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: #10B981; font-weight: bold; }
    text, tspan { white-space: pre; }
    
    .term-label { font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: #64748B; letter-spacing: 0.5px; }
    .cursor-blink { fill: #22D3EE; }
  </style>
</defs>

<rect width="550" height="433" rx="12" fill="#050816" stroke="#30363d" stroke-width="1"/>

<g id="titlebar">
  <rect x="0" y="0" width="550" height="34" rx="12" fill="#0B1120"/>
  <rect x="0" y="17" width="550" height="17" fill="#0B1120"/>
  <circle cx="24" cy="17" r="5" fill="#EF4444"/>
  <circle cx="42" cy="17" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="17" r="5" fill="#10B981"/>
  <text x="275" y="21" text-anchor="middle" class="term-label">wormav@devos ~ % ./profile.sh</text>
  <line x1="0" y1="34" x2="550" y2="34" stroke="#30363d"/>
</g>

<g transform="translate(20, 70)">
  <text x="0" y="0" fill="#dbeafe">
    <tspan x="0" y="0" class="head">wormav@devos</tspan><tspan class="cc"> -——————————————————————————————-—-</tspan>
    
    <tspan x="0" y="28" class="cc">. </tspan><tspan class="key">Subject</tspan><tspan class="cc">: ....................... </tspan><tspan class="value">Jérémy Lorette</tspan>
    <tspan x="0" y="52" class="cc">. </tspan><tspan class="key">Role</tspan><tspan class="cc">: .......................... </tspan><tspan class="value">Web Developer</tspan>
    <tspan x="0" y="76" class="cc">. </tspan><tspan class="key">Education</tspan><tspan class="cc">: ..................... </tspan><tspan class="value">42 Student</tspan>
    <tspan x="0" y="100" class="cc">. </tspan><tspan class="key">Status</tspan><tspan class="cc">: ........................ </tspan><tspan class="value">Building &amp; Learning</tspan>
    <tspan x="0" y="124" class="cc">. </tspan><tspan class="key">ToolChain</tspan><tspan class="cc">: ..................... </tspan><tspan class="value">VS Code, Git, Docker</tspan>
    
    <tspan x="0" y="166" class="cc">. </tspan><tspan class="key">Core</tspan><tspan class="cc">.</tspan><tspan class="key">Lang</tspan><tspan class="cc">: .................. </tspan><tspan class="value">C, C++, JS, TS, Python</tspan>
    <tspan x="0" y="190" class="cc">. </tspan><tspan class="key">Core</tspan><tspan class="cc">.</tspan><tspan class="key">Frontend</tspan><tspan class="cc">: .............. </tspan><tspan class="value">React, Next.js, Tailwind</tspan>
    <tspan x="0" y="214" class="cc">. </tspan><tspan class="key">Core</tspan><tspan class="cc">.</tspan><tspan class="key">Backend</tspan><tspan class="cc">: ............... </tspan><tspan class="value">Node.js, PostgreSQL</tspan>
    <tspan x="0" y="238" class="cc">. </tspan><tspan class="key">Core</tspan><tspan class="cc">.</tspan><tspan class="key">Mobile</tspan><tspan class="cc">: ................ </tspan><tspan class="value">Flutter, React Native</tspan>
    
    <tspan x="0" y="284" class="accent">- Contact</tspan><tspan class="cc"> -————————————————————————————————-—-</tspan>
    <tspan x="0" y="312" class="cc">. </tspan><tspan class="key">Grid</tspan><tspan class="cc">.</tspan><tspan class="key">Github</tspan><tspan class="cc">: ................. </tspan><tspan class="value">github.com/Wormav</tspan>
    <tspan x="0" y="336" class="cc">. </tspan><tspan class="key">Grid</tspan><tspan class="cc">.</tspan><tspan class="key">LinkedIn</tspan><tspan class="cc">: ............... </tspan><tspan class="value">jeremy-lorette</tspan>
  </text>
  
  <rect x="0" y="348" width="9" height="16" class="cursor-blink">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</g>
</svg>
"""

with open("cv-noir.svg", "w") as f:
    f.write(svg)
