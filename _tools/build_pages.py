import html, os, shutil
B = '/home/claude/vibe'
HUB = B + '/hub'

COMMON_JS = '''<script>
{
const b=document.getElementById('copy');
b.addEventListener('click',async()=>{
  const t=document.getElementById('prompt').textContent;
  try{await navigator.clipboard.writeText(t);b.textContent='copied ✓';}
  catch(e){const r=document.createRange();r.selectNodeContents(document.getElementById('prompt'));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='selected — press ⌘C';}
  setTimeout(()=>b.textContent='copy prompt',2200);
});
}
</script>'''

BASE_CSS = '''*{box-sizing:border-box;min-width:0}
html,body{margin:0}
body{overflow-x:clip}
main{max-width:760px;margin:0 auto;padding:clamp(28px,6vw,70px) 20px 60px;position:relative;z-index:1}
.back{display:inline-flex;align-items:center;gap:6px;min-height:44px;font-size:14px;text-decoration:none;margin-bottom:10px}
.hero{text-align:center;margin-bottom:34px}
.hero p{max-width:540px;margin:0 auto 24px}
.acts{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:50px;padding:0 24px;border-radius:999px;text-decoration:none;border:0;cursor:pointer}
.card{border-radius:20px;padding:22px 22px 18px;margin-top:20px}
.card h3{margin:0 0 10px}
.card ul{margin:0;padding-left:18px}
.card li{margin:5px 0}
kbd{font:500 12px ui-monospace,monospace;border-radius:6px;padding:1px 6px}
.ph{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:10px}
.ph h3{margin:0}
#copy{min-height:44px;padding:0 18px}
pre{margin:0;max-height:440px;overflow:auto;white-space:pre-wrap;word-break:break-word;border-radius:12px;padding:16px;font:13px/1.6 ui-monospace,"DM Mono",monospace}
.steps{margin:0 0 12px;font-size:14px}
footer{text-align:center;font-size:12px;margin-top:30px}
footer a{color:inherit}
.btn:focus-visible,.back:focus-visible,#copy:focus-visible{outline:3px solid currentColor;outline-offset:3px}
'''

exec(open('/home/claude/vibe/page_v2.py').read())

# ---------------- fish tank ----------------
page('fish-tank', '魚缸 · the fish tank',
 'family=Noto+Serif+TC:wght@700&family=Cormorant+Garamond:ital,wght@1,500&family=DM+Mono:wght@400;500',
 '''/* VOICE late-night fish shop · IDEA the tank's own label card · PICTURE glowing 魚缸 over violet water light
   COLOUR deep violet, goldfish orange, subtitle yellow · TYPE Noto Serif TC + Cormorant + DM Mono · LAYOUT one centred column */
body{background:radial-gradient(120% 70% at 50% 0%,#2c1f60 0%,#120d2c 50%,#07060f 100%) fixed;color:#ece9ff;font:15px/1.6 "DM Mono",ui-monospace,monospace}
.back{color:#c7c3e6}
h1{font:700 clamp(84px,18vw,150px)/1 "Noto Serif TC",serif;margin:0;color:#ff9d4a;letter-spacing:.08em;text-shadow:0 0 40px rgba(255,120,60,.55),0 0 90px rgba(255,80,160,.3)}
h2{font:italic 500 clamp(28px,5vw,40px)/1.1 "Cormorant Garamond",serif;margin:6px 0 16px;color:#f2efff}
.hero p{color:#c7c3e6;font-size:14px}
.btn{background:#ffe33a;color:#17142b;font:500 15px "DM Mono",monospace}
.btn:hover{background:#fff07a}
.btn.alt{background:transparent;color:#ffe33a;border:1px solid rgba(255,227,58,.6)}
.btn.alt:hover{background:rgba(255,227,58,.1)}
.card{background:rgba(255,255,255,.05);border:1px solid rgba(230,225,255,.14)}
.card h3{font:italic 500 26px/1.2 "Cormorant Garamond",serif;color:#fff}
.card ul{color:#d6d2f0;font-size:14px}
kbd{background:rgba(255,255,255,.12)}
#copy{font-size:13px}
pre{background:rgba(0,0,0,.35);color:#e6e2ff}
.steps{color:#c7c3e6}
footer{color:#8f8ab5}''',
 '''    <h1>魚缸</h1>
    <h2>the fish tank</h2>
    <p>A dreamy Wong Kar-wai-style aquarium for your laptop. Poke the glass, feed the 3D goldfish, and stand behind the glass with your webcam.</p>''',
 ['Best on a laptop in Chrome. Click <b>turn on the tank</b>.',
  'Click anywhere to poke the glass. Drag to make ripples.',
  '<kbd>Space</kbd> feeds the fish · <kbd>M</kbd> changes the light · <kbd>S</kbd> takes a picture · <kbd>H</kbd> hides the controls',
  '<b>You behind the glass</b> and <b>hand play</b> use your camera. Nothing is uploaded; it all runs in your browser.'],
 '<a class="btn" href="tank.html">open the fish tank →</a>',
 'fish-tank.txt', 'https://www.instagram.com/reel/DgHlT8_JLCp/')
shutil.copy(f'{B}/fish-tank.html', f'{HUB}/fish-tank/tank.html')

# ---------------- rainy window ----------------
page('rainy-window', 'rainy window',
 'family=Caveat:wght@700&family=DM+Sans:wght@400;500',
 '''/* VOICE cosy rainy afternoon · IDEA a steamed-up window · PICTURE rain streaks over grey-blue glass
   COLOUR rain grey-blue, frost white · TYPE Caveat + DM Sans · LAYOUT one centred column on frosted glass */
body{background:radial-gradient(120% 90% at 50% 0%,#5f7384 0%,#33414d 55%,#1d2329 100%) fixed;color:#fff;font:16px/1.6 "DM Sans",system-ui,sans-serif}
#rain{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.back{color:rgba(255,255,255,.8)}
h1{font:700 clamp(72px,14vw,120px)/.9 "Caveat",cursive;margin:0 0 14px}
.hero p{opacity:.88}
.btn{background:#fff;color:#1d2329;font:500 16px "DM Sans",sans-serif}
.btn:hover{background:#e8eef2}
.btn.alt{background:rgba(255,255,255,.14);color:#fff;border:1px solid rgba(255,255,255,.45);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.card{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);backdrop-filter:blur(14px) saturate(1.2);-webkit-backdrop-filter:blur(14px) saturate(1.2)}
.card h3{font:700 34px/1 "Caveat",cursive}
.card ul{font-size:15px;opacity:.92}
kbd{background:rgba(255,255,255,.2)}
#copy{font-size:14px}
pre{background:rgba(20,26,32,.55);color:#eef3f6}
.steps{opacity:.8}
footer{opacity:.7}''',
 '''    <h1>rainy window</h1>
    <p>A fogged-up window on a rainy day. Blow on your laptop to steam it up, then pinch your fingers and write on the glass with your fingertip.</p>''',
 ['Best on a laptop in Chrome or Arc. Click <b>open the window</b> and allow the camera and microphone.',
  '<b>Blow</b> at your laptop to fog the glass where your mouth is.',
  '<b>Pinch</b> your thumb and index finger to write. <b>Make a fist</b> and swipe to wipe a big patch.',
  '<kbd>C</kbd> fogs it all again · hold <kbd>Space</kbd> to add fog · <kbd>S</kbd> saves a picture · <kbd>H</kbd> hides the controls'],
 '<a class="btn" href="window.html">open the window →</a>',
 'rainy-window.txt', 'https://www.instagram.com/reel/DgEJopfp2jn/',
 extra_body='<canvas id="rain" aria-hidden="true"></canvas>',
 extra_js='''<script>
{
const c=document.getElementById('rain'),x=c.getContext('2d');let W,H,drops=[];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function size(){W=c.width=innerWidth;H=c.height=innerHeight;drops=Array.from({length:Math.round(W*H/9000)},()=>({x:Math.random()*W,y:Math.random()*H,r:1+Math.random()*3,v:0,s:Math.random()*3}));}
function f(){x.clearRect(0,0,W,H);
  for(const d of drops){
    if(!reduce){if(d.s>0)d.s-=0.016;else{d.v=Math.min(d.v+0.08,2+d.r);d.y+=d.v;if(Math.random()<0.01){d.s=Math.random();d.v=0;}}if(d.y>H+10){d.y=-10;d.x=Math.random()*W;}}
    x.fillStyle='rgba(255,255,255,0.18)';x.beginPath();x.ellipse(d.x,d.y,d.r*0.85,d.r*1.15,0,0,6.283);x.fill();
    x.fillStyle='rgba(255,255,255,0.55)';x.beginPath();x.arc(d.x-d.r*0.3,d.y-d.r*0.4,d.r*0.25,0,6.283);x.fill();
  }
  requestAnimationFrame(f);}
addEventListener('resize',size);size();f();
}
</script>''')
shutil.copy(f'{B}/rainy-window.html', f'{HUB}/rainy-window/window.html')

# ---------------- bloom by smile ----------------
page('bloom-by-smile', 'bloom by smile',
 'family=Great+Vibes&family=DM+Sans:wght@400;500;700',
 '''/* VOICE tender, playful, a little magic · IDEA a storybook garden label · PICTURE flowers rising from the bottom edge
   COLOUR blush, peony, buttercup, lilac · TYPE Great Vibes + DM Sans · LAYOUT one centred column, garden along the bottom */
body{background:radial-gradient(120% 90% at 50% 0%,#fff4f6 0%,#f7d9e2 55%,#efc3d1 100%) fixed;color:#3a1f2b;font:16px/1.6 "DM Sans",system-ui,sans-serif;padding-bottom:120px}
.back{color:#7a4a5c}
h1{font:400 clamp(70px,13vw,112px)/1 "Great Vibes",cursive;margin:0 0 12px}
.hero p{color:#5a3442}
.btn{background:#3a1f2b;color:#fff;font:500 15px "DM Sans",sans-serif}
.btn:hover{background:#5a2f42}
.btn.alt{background:rgba(255,248,250,.74);color:#3a1f2b;border:1px solid rgba(58,31,43,.18)}
.btn.alt:hover{background:#fff}
.card{background:rgba(255,248,250,.74);border:1px solid rgba(58,31,43,.12);box-shadow:0 10px 30px rgba(120,40,70,.1);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.card h3{font:400 40px/1 "Great Vibes",cursive}
.card ul{font-size:15px;color:#4a2a37}
kbd{background:rgba(58,31,43,.08)}
#copy{font-size:14px}
pre{background:rgba(58,31,43,.06);color:#3a1f2b}
.steps{color:#6a4352}
footer{color:#8a5a6c}
.garden{position:fixed;left:0;right:0;bottom:0;height:120px;z-index:0;pointer-events:none}''',
 '''    <h1>bloom by smile</h1>
    <p>Smile and the garden grows. Frown and the flowers wilt. Keep smiling and the butterflies come to visit.</p>''',
 ['Click <b>Open the garden</b> and allow the camera. Keep a relaxed face for two seconds so it learns your neutral look.',
  'Smile to grow flowers; frown to make them wilt.',
  'The sensitivity sliders help if your smiles or frowns aren’t picked up. <b>Backdrop</b> swaps your camera for plain blush pink.',
  '<kbd>H</kbd> hides the controls · hold <kbd>S</kbd> to fake a smile, <kbd>D</kbd> to fake a frown'],
 '<a class="btn" href="garden.html">open on a laptop →</a><a class="btn" href="garden-phone.html">open on a phone →</a>',
 'bloom-by-smile.txt', 'https://www.instagram.com/reel/DgCgAfIgVpX/',
 extra_body='<svg class="garden" viewBox="0 0 1200 120" preserveAspectRatio="xMidYMax slice" aria-hidden="true"><defs><g id="fl"><circle r="9" fill="#f6a7bd"/><circle cx="9" cy="-3" r="7" fill="#f6a7bd"/><circle cx="-9" cy="-3" r="7" fill="#f6a7bd"/><circle cx="5" cy="8" r="7" fill="#f6a7bd"/><circle cx="-5" cy="8" r="7" fill="#f6a7bd"/><circle r="4" fill="#ffd36b"/></g></defs><path d="M0 120 L0 100 Q300 88 600 98 T1200 96 L1200 120Z" fill="#7bb27a"/><g stroke="#4f8a55" stroke-width="2" fill="none"><path d="M90 104 Q85 70 96 52"/><path d="M260 104 Q270 72 258 40"/><path d="M430 104 Q420 80 432 62"/><path d="M640 104 Q650 70 638 46"/><path d="M820 104 Q812 76 826 58"/><path d="M1010 104 Q1020 70 1006 44"/><path d="M1140 104 Q1134 82 1146 66"/></g><use href="#fl" x="96" y="50"/><use href="#fl" x="258" y="38"/><use href="#fl" x="432" y="60"/><use href="#fl" x="638" y="44"/><use href="#fl" x="826" y="56"/><use href="#fl" x="1006" y="42"/><use href="#fl" x="1146" y="64"/></svg>')
shutil.copy(f'{B}/bloom-by-smile.html', f'{HUB}/bloom-by-smile/garden.html')
shutil.copy(f'{B}/bloom-by-smile-phone.html', f'{HUB}/bloom-by-smile/garden-phone.html')

# ---------------- ilysm touch ----------------
page('ilysm-touch', 'I love you so much · fingertip words',
 'family=Inter:wght@400;600',
 '''/* VOICE playful, sweet · IDEA the phrase lit on fingertips · PICTURE coloured italic words with red fingertip dots on black
   COLOUR black, five neon word colours, red dots · TYPE italic Arial + Inter · LAYOUT one centred column */
body{background:#000;color:#f2f2f2;font:15px/1.6 Inter,Arial,sans-serif}
.back{color:#bbb}
h1{font:italic 700 clamp(40px,8vw,72px)/1.1 Arial,Helvetica,sans-serif;margin:0 0 6px;letter-spacing:.01em}
h1 span{position:relative;display:inline-block;padding-bottom:.32em}
h1 span::after{content:"";position:absolute;left:50%;bottom:0;width:.24em;height:.24em;border-radius:50%;background:#ff1010;transform:translateX(-50%)}
.hero p{color:#ccc}
.btn{background:rgba(255,255,255,.92);color:#111;font:600 15px Arial,sans-serif}
.btn:hover{background:#fff}
.btn.alt{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.45)}
.btn.alt:hover{background:rgba(255,255,255,.08)}
.card{background:rgba(20,20,20,.92);border:1px solid rgba(255,255,255,.12)}
.card h3{font:italic 700 22px/1.2 Arial,sans-serif;color:#7dff1f}
.card ul{color:#ddd;font-size:14px}
kbd{background:rgba(255,255,255,.14)}
#copy{font-size:14px}
pre{background:#0d0d0d;color:#e9e9e9;border:1px solid rgba(255,255,255,.08)}
.steps{color:#aaa}
footer{color:#888}''',
 '''    <h1><span style="color:#9a2bff">I</span> <span style="color:#7dff1f">love</span> <span style="color:#4a4aff">you</span> <span style="color:#2ee6e6">so</span> <span style="color:#ff2a8a">much</span></h1>
    <p>Words float on your fingertips. Touch your thumb to each fingertip and its word plays out loud.</p>''',
 ['Click <b>Start camera</b> and hold both hands up. Left hand: I, love, you. Right hand: so, much.',
  'Touch your thumb’s red dot to a fingertip’s red dot to play that word.',
  'Open <b>Sounds</b> to record each word in your own voice. If words land on the wrong hands, tap <b>Swap hands</b>.',
  '<b>Record</b> saves a clip with sound · <kbd>H</kbd> hides the controls · works on phones too'],
 '<a class="btn" href="i-love-you-so-much.html">I love you so much →</a><a class="btn" href="dont-forget-to-love-yourself.html">don’t forget to love yourself →</a>',
 'ilysm-touch.txt', 'https://www.instagram.com/reel/DgE0AfrpqqM/')
shutil.copy(f'{B}/i-love-you-so-much.html', f'{HUB}/ilysm-touch/i-love-you-so-much.html')
shutil.copy(f'{B}/dont-forget-to-love-yourself.html', f'{HUB}/ilysm-touch/dont-forget-to-love-yourself.html')

page('ascii-christmas', 'ascii christmas',
 'family=DM+Mono:wght@400;500&family=Cormorant+Garamond:ital,wght@1,500;1,600',
 '''/* VOICE cosy, nerdy-festive · IDEA a tree made of text · PICTURE gold characters on a navy night · TYPE Cormorant italic + DM Mono */
body{background:radial-gradient(80% 60% at 50% 0%,#16224f,#050816 70%) fixed;color:#e9edff;font:15px/1.6 "DM Mono",ui-monospace,monospace}
.back{color:#aeb9e8}
h1{font:italic 600 clamp(46px,9vw,80px)/1 "Cormorant Garamond",serif;color:#ffe08a;margin:0 0 10px;text-shadow:0 0 30px rgba(255,200,90,.45)}
.hero pre.mini{font:500 13px/1.05 "DM Mono",monospace;color:#ffd86b;margin:0 0 6px;text-shadow:0 0 14px rgba(255,210,110,.6)}
.hero p{color:#c7d0f5}
.btn{background:#ffd86b;color:#0b1330;font:500 14px "DM Mono",monospace}
.btn:hover{background:#ffe7a6}
.btn.alt{background:transparent;color:#ffe08a;border:1px solid rgba(255,216,107,.6)}
.btn.alt:hover{background:rgba(255,216,107,.08)}
.card{background:rgba(12,20,50,.78);border:1px solid rgba(200,215,255,.16)}
.card h3{font:italic 600 26px/1.1 "Cormorant Garamond",serif;color:#ffe08a}
kbd{background:rgba(255,255,255,.12)}
pre#prompt{background:#070c22;color:#dfe6ff;border:1px solid rgba(200,215,255,.12)}
footer{color:#8f9ac4}''',
 '''    <pre class="mini" aria-hidden="true">   *\n  /o\\\n /*.@\\\n/o.*.o\\\n  |#|</pre>
    <h1>ascii christmas</h1>
    <p>A 3D Christmas tree made entirely of text. It grows itself, spins, lights up, and Santa flies across the moon. Spin it with your hands, too.</p>''',
 [], '', 'ascii-christmas.txt', None)
shutil.copy('/home/claude/vibe/ascii-christmas.html', f'{HUB}/ascii-christmas/tree.html')
print('built')
