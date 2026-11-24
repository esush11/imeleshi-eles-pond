# New project-page layout: hero + live preview, "two ways to try it" (01 play / 02 build), bugs.
import html, os

BASE_CSS += '''
.preview{display:block;position:relative;aspect-ratio:16/10;width:100%;max-width:580px;margin:0 auto 22px;border-radius:18px;overflow:hidden;text-decoration:none;box-shadow:0 24px 60px rgba(0,0,0,.35);transition:transform .25s}
.preview{outline:1px solid rgba(127,127,127,.25);outline-offset:-1px}
.preview:hover{transform:translateY(-3px)}
.preview canvas{width:100%;height:100%;display:block}
.preview .tag{position:absolute;right:12px;bottom:12px;padding:6px 12px;border-radius:999px;font-size:12px;background:rgba(0,0,0,.55);color:#fff;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.lead{max-width:540px;margin:0 auto 22px}
.kicker{font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.7;margin:44px 0 4px;text-align:center}
.sec-title{display:flex;align-items:baseline;gap:14px;margin:0 0 6px}
.sec-title .n{font:600 14px ui-monospace,"DM Mono",monospace;opacity:.6}
.sec-title h3{margin:0}
.sub{margin:0 0 14px;font-size:14px;opacity:.85}
.ver{border-top:1px solid rgba(127,127,127,.25);padding:16px 0 4px}
.ver h4{margin:0 0 4px;font-size:16px}
.ver p{margin:0 0 10px;font-size:14px;opacity:.9}
.ver ul{margin:0 0 12px;padding-left:18px;font-size:14px}
.ver li{margin:3px 0}
.go{display:inline-flex;align-items:center;gap:6px;min-height:44px;font-weight:600;text-decoration:underline;text-underline-offset:4px;color:inherit}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}
.pill{font-size:12px;padding:5px 12px;border-radius:999px;border:1px solid rgba(127,127,127,.4)}
.acts.left{justify-content:flex-start;margin:4px 0 16px}
.bugs{margin:0;padding-left:0;list-style:none}
.bugs li{padding:10px 0;border-top:1px solid rgba(127,127,127,.22);font-size:14px}
.bugs b{display:block;margin-bottom:2px}
.bugs span{opacity:.85}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.preview{transition:none}}
'''

PREVIEW_JS = r'''<script>
{
const cv=document.getElementById('pv');if(cv){
const x=cv.getContext('2d');let W,H,t0=performance.now();
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function size(){const r=cv.getBoundingClientRect(),d=Math.min(devicePixelRatio||1,2);W=cv.width=r.width*d;H=cv.height=r.height*d;}
addEventListener('resize',size);size();
const draw=DRAW;
function loop(now){draw(x,W,H,Math.max(0,(now-t0)/1000));if(!reduce)requestAnimationFrame(loop);}
requestAnimationFrame(loop);
}}
</script>'''

def page(slug, title, fonts, css, hero_html, how_items, open_note, prompt_file, reel, extra_body='', extra_js=''):
    d = PAGES[slug]
    raw = open(f'{HUB}/prompts/{prompt_file}').read().rstrip()
    raw += '\n\nBUGS I RAN INTO (handle these from the start):\n' + '\n'.join(f'- {b[0]} → {b[1]}' for b in d['bugs'])
    prompt = html.escape(raw)
    vers = ''.join(f'''<div class="ver"><h4>{v['name']}</h4><p>{v['desc']}</p><ul>{''.join(f'<li>{i}</li>' for i in v['how'])}</ul><a class="go" href="{v['href']}">{v['link']} ↗</a></div>''' for v in d['versions'])
    bugs = ''.join(f'<li><b>{b[0]}</b><span>fix: {b[1]}</span></li>' for b in d['bugs'])
    n = len(d['versions'])
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(d['tagline'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
{BASE_CSS}
{css}
</style>
</head>
<body>
{extra_body}
<main>
  <a class="back" href="../">← back to the pond</a>
  <section class="hero">
{hero_html}
    <a class="preview" href="{d['versions'][0]['href']}" aria-label="open {html.escape(d['noun'])}"><canvas id="pv"></canvas><span class="tag">▶ tap to open</span></a>
    <div class="acts"><a class="btn" href="{d['versions'][0]['href']}">open it now →</a><a class="btn alt" href="{reel or 'https://www.instagram.com/imeleshi/'}" target="_blank" rel="noopener">{'watch the reel ↗' if reel else 'follow on instagram ↗'}</a></div>
  </section>

  <p class="kicker">two ways to try it</p>

  <section class="card">
    <div class="sec-title"><span class="n">01</span><h3>play with it now</h3></div>
    <p class="sub">{d['play_sub'].format(n=('one version' if n==1 else f'{n} versions'))}</p>
    {vers}
  </section>

  <section class="card">
    <div class="sec-title"><span class="n">02</span><h3>build your own {d['noun']}</h3></div>
    <p class="sub">copy my prompt into Claude or ChatGPT and ask it to build you a single HTML file. you might need to tweak a few things depending on your setup. i wrote down the <a href="#bugs" style="color:inherit">bugs i ran into</a> (they're baked into the prompt too), so you can skip some of the trial and error.</p>
    <div class="meta"><span class="pill">⏱ takes ~{d['minutes']} minutes</span><span class="pill">single HTML file</span><span class="pill">{d['needs']}</span></div>
    <div class="acts left"><button class="btn" id="copy">copy prompt</button><a class="btn alt" href="{d['versions'][0]['href']}">see mine first</a></div>
    <pre id="prompt">{prompt}</pre>
    <p class="sub" style="margin-top:14px">have fun making yours :) save the file, open it in Chrome, and tag me if you post it.</p>
  </section>

  <section class="card" id="bugs">
    <div class="sec-title"><span class="n">✎</span><h3>bugs i ran into</h3></div>
    <p class="sub">if yours does something weird, it's probably one of these. paste the fix back into the chat.</p>
    <ul class="bugs">{bugs}</ul>
  </section>

  <footer>made by <a href="https://www.instagram.com/imeleshi/" target="_blank" rel="noopener">@imeleshi</a> with Claude · <a href="../">more little things in the pond</a></footer>
</main>
{COMMON_JS}
{PREVIEW_JS.replace('DRAW', d['draw'])}
{extra_js}
</body>
</html>
'''
    os.makedirs(f'{HUB}/{slug}', exist_ok=True)
    open(f'{HUB}/{slug}/index.html', 'w').write(doc)

PAGES = {
'fish-tank': dict(
  noun='fish tank', tagline='A dreamy Wong Kar-wai aquarium for your laptop.', minutes=25, needs='laptop + Chrome · webcam optional',
  play_sub="it's already live. open it on your laptop and click <b>turn on the tank</b>. the sound comes on with it.",
  versions=[
    dict(name='the tank', desc='3D goldfish drifting through violet water light. no camera needed.',
         how=['click or drag anywhere to poke the glass and make ripples','<kbd>Space</kbd> feeds the fish · <kbd>M</kbd> changes the light · <kbd>S</kbd> takes a picture · <kbd>H</kbd> hides the controls'],
         href='tank.html', link='open the fish tank'),
    dict(name='you behind the glass ✋', desc='turn on <b>camera</b> and you appear behind the tank, lit by the water. turn on <b>hand play</b> to touch it with your hands.',
         how=['pinch to poke the glass · open your palm and the fish swim over','needs a webcam, works best in Chrome. nothing is uploaded'],
         href='tank.html', link='open the tank with your camera'),
  ],
  bugs=[
    ('the dreamy glow washed my face out completely on the webcam','only bloom the tank layers (water, fish, front glass), never the camera, and add auto-exposure'),
    ('poking the screen with a finger "jab" never registered','use a pinch to poke, an open palm to call the fish, and show a small status pill so you know it sees your hand'),
    ('it was really slow and laggy','cap the scene at about 960px wide, render WebGL at 1x pixel ratio, no CSS canvas filters, step-print off by default'),
    ('the fish looked flat and 2D','draw them as real 3D meshes in WebGL with a bending spine, fins and depth of field'),
    ("the camera and screenshot button didn't work in Claude's preview",'download the HTML file and open it in Chrome (or put it online)'),
  ],
  draw=r'''(x,W,H,t)=>{
 const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#3a2780');g.addColorStop(.6,'#1a1240');g.addColorStop(1,'#08060f');x.fillStyle=g;x.fillRect(0,0,W,H);
 x.globalCompositeOperation='lighter';
 for(let i=0;i<5;i++){const cx=W*(.15+.18*i)+Math.sin(t*.4+i)*W*.04;const r=x.createRadialGradient(cx,0,0,cx,0,H*.9);r.addColorStop(0,'rgba(170,120,255,.16)');r.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=r;x.fillRect(0,0,W,H);}
 x.globalCompositeOperation='source-over';
 for(let i=0;i<14;i++){const bx=(i*97%100)/100*W,by=H-((t*30*(1+i%3)+i*53)%H);x.fillStyle='rgba(220,210,255,.35)';x.beginPath();x.arc(bx+Math.sin(t+i)*4,by,1.5+(i%3),0,6.28);x.fill();}
 const fish=[[.0,.38,1,1],[.45,.6,-1,.8],[.7,.3,1,.6],[.2,.72,-1,.9]];
 fish.forEach(([o,y,dir,s],i)=>{
  let p=((t*.05*(1+i*.15)+o)%1.3)-.15;const fx=dir>0?p*W:W-p*W,fy=H*y+Math.sin(t*1.2+i)*H*.04,L=W*.09*s,w=Math.sin(t*6+i)*.35;
  x.save();x.translate(fx,fy);x.scale(dir,1);x.shadowColor='rgba(255,130,60,.8)';x.shadowBlur=W*.03;
  x.fillStyle='rgba(255,170,90,.55)';x.beginPath();x.moveTo(-L*.45,0);x.quadraticCurveTo(-L*.8,-L*.35+w*L*.3,-L*1.05,-L*.3+w*L*.5);x.quadraticCurveTo(-L*.8,w*L*.2,-L*1.05,L*.3+w*L*.5);x.quadraticCurveTo(-L*.8,L*.35+w*L*.3,-L*.45,0);x.fill();
  const bg=x.createLinearGradient(0,-L*.25,0,L*.25);bg.addColorStop(0,'#ffb35c');bg.addColorStop(1,'#ff6a2a');x.fillStyle=bg;x.beginPath();x.ellipse(0,0,L*.5,L*.22,0,0,6.28);x.fill();
  x.shadowBlur=0;x.fillStyle='#1a0d10';x.beginPath();x.arc(L*.32,-L*.05,L*.035,0,6.28);x.fill();x.restore();});
 const k=t%2.4;if(k<1.6){const rx=W*(.3+.4*((Math.floor(t/2.4)*.37)%1)),ry=H*.45;for(let j=0;j<3;j++){const rr=(k*W*.12)-j*W*.03;if(rr>0){x.strokeStyle=`rgba(230,220,255,${.5*(1-k/1.6)})`;x.lineWidth=W*.003;x.beginPath();x.ellipse(rx,ry,rr,rr*.6,0,0,6.28);x.stroke();}}}
 x.font=`${Math.round(W*.032)}px "Noto Serif TC",serif`;x.textAlign='center';x.fillStyle='#ffe33a';x.shadowColor='rgba(0,0,0,.6)';x.shadowBlur=6;
 x.fillText('魚也會想念你嗎？',W/2,H*.86);x.font=`italic ${Math.round(W*.026)}px "Cormorant Garamond",serif`;x.fillText('do fish miss you too?',W/2,H*.93);x.shadowBlur=0;}'''),

'rainy-window': dict(
  noun='rainy window', tagline='A fogged-up window on a rainy day. Blow to steam it up and write on the glass.', minutes=15, needs='laptop + webcam + mic',
  play_sub="it's already live. open it on your laptop in Chrome or Arc and allow the camera and microphone.",
  versions=[
    dict(name='the window', desc='your webcam behind steamy glass, with real raindrops running down it.',
         how=['<b>blow</b> at your laptop to fog the glass where your mouth is','<b>pinch</b> your thumb and index finger to write · <b>make a fist</b> to wipe a big patch','<kbd>C</kbd> fogs it all again · hold <kbd>Space</kbd> for more fog · <kbd>S</kbd> saves a picture · <kbd>H</kbd> hides the controls'],
         href='window.html', link='open the rainy window'),
  ],
  bugs=[
    ("blowing didn't fog anything because the mic cleaned my breath out",'turn off echo cancellation and noise suppression on the mic and track the room\'s noise floor'),
    ('a pinch sometimes counted as a fist and wiped a huge patch','only count a fist when all four fingertips are closer to the wrist than their knuckles for 2 frames in a row'),
    ('the writing was backwards','mirror the webcam so it moves like a real mirror'),
    ("full screen wouldn't open",'ask for full screen straight from the button click, not after the camera loads'),
    ("camera and mic were blocked in Claude's preview",'download the HTML file and open it in Chrome or Arc'),
  ],
  draw=r'''(x,W,H,t)=>{
 const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#6d8293');g.addColorStop(1,'#2b3640');x.fillStyle=g;x.fillRect(0,0,W,H);
 [[.25,.35,'rgba(255,200,120,.5)'],[.72,.3,'rgba(255,230,180,.35)'],[.55,.7,'rgba(160,190,220,.4)']].forEach(([a,b,c])=>{const r=x.createRadialGradient(W*a,H*b,0,W*a,H*b,W*.25);r.addColorStop(0,c);r.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=r;x.fillRect(0,0,W,H);});
 const cyc=9,k=t%cyc;
 x.save();x.fillStyle=`rgba(225,232,238,.62)`;x.fillRect(0,0,W,H);
 const S=[[[.0,0],[.0,1]],[[.0,.55],[.12,.42],[.28,.5],[.3,1]],[[.48,.42],[.48,1]],[[.48,.2],[.485,.22]],[[.78,.5],[.7,.35],[.82,.3],[.9,.45],[.98,.3],[1.1,.35],[1.02,.55],[.9,.85],[.78,.5]]];
 const ox=W*.3,oy=H*.3,sc=H*.38;let total=0;S.forEach(s=>total+=s.length-1);const prog=Math.min(k/4.5,1)*total;let done=0,tip=null;
 x.globalCompositeOperation='destination-out';x.lineCap='round';x.lineJoin='round';x.lineWidth=W*.022;x.strokeStyle='#000';
 for(const s of S){x.beginPath();x.moveTo(ox+s[0][0]*sc,oy+s[0][1]*sc);for(let i=1;i<s.length;i++){const f=Math.min(Math.max(prog-done,0),1);if(f<=0)break;const a=s[i-1],b=s[i],px=a[0]+(b[0]-a[0])*f,py=a[1]+(b[1]-a[1])*f;x.lineTo(ox+px*sc,oy+py*sc);tip=[ox+px*sc,oy+py*sc];done++;if(f<1)break;}x.stroke();if(prog-done<0)break;}
 const fade=k>7?(k-7)/2:0;x.globalCompositeOperation='source-over';if(fade>0){x.fillStyle=`rgba(225,232,238,${.62*fade})`;}
 x.restore();if(fade>0){x.fillStyle=`rgba(225,232,238,${.6*fade})`;x.fillRect(0,0,W,H);}
 if(tip&&k<4.6){x.fillStyle='rgba(255,250,220,.9)';x.shadowColor='#fff3b0';x.shadowBlur=W*.02;x.beginPath();x.arc(tip[0],tip[1],W*.008,0,6.28);x.fill();x.shadowBlur=0;}
 for(let i=0;i<40;i++){const bx=(i*61%100)/100*W,sp=i%5===0?1:0,by=((i*37%100)/100*H+(sp?t*H*.12:0))%H,r=W*(.003+(i%4)*.0025);
  x.fillStyle='rgba(40,55,70,.35)';x.beginPath();x.ellipse(bx,by,r,r*1.2,0,0,6.28);x.fill();x.fillStyle='rgba(255,255,255,.7)';x.beginPath();x.arc(bx-r*.3,by-r*.4,r*.35,0,6.28);x.fill();}}'''),

'bloom-by-smile': dict(
  noun='smile garden', tagline='Smile and the garden grows. Frown and the flowers wilt.', minutes=15, needs='laptop or phone + camera',
  play_sub="it's already live, {n}. allow the camera and keep a relaxed face for two seconds while it learns your neutral look.",
  versions=[
    dict(name='laptop version', desc='a storybook garden grows along the bottom of your webcam.',
         how=['smile to grow flowers · frown to make them wilt · keep smiling and butterflies visit','sensitivity sliders help if it misses your smile · <kbd>H</kbd> hides the controls'],
         href='garden.html', link='open on a laptop'),
    dict(name='phone version 📱', desc='front camera, made for a vertical screen. tap anywhere to bring the controls back.',
         how=['works on iPhone and Android in the browser','use <b>Flip camera</b> to switch to the back camera'],
         href='garden-phone.html', link='open on a phone'),
  ],
  bugs=[
    ("my frowns didn't register",'learn my neutral face for ~2 seconds first and compare frowns against it, with smile and frown sensitivity sliders'),
    ('smiling sometimes counted as frowning','ignore frowns while a smile is detected'),
    ('it got laggy once the garden filled up','cap it at 60 flowers (38 on phones) and revive the most wilted one instead of adding more'),
    ('the camera was blocked on my phone','the page has to be on https (e.g. Netlify), not opened as a file'),
  ],
  draw=r'''(x,W,H,t)=>{
 const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#fff4f6');g.addColorStop(1,'#efc3d1');x.fillStyle=g;x.fillRect(0,0,W,H);
 const cyc=10,k=t%cyc,sm=k<6?Math.min(k/1.2,1):k<8?Math.max(1-(k-6)/.6,-1)*1:Math.min(-1+(k-8)/2*2,1);const smile=Math.max(sm,0),frown=Math.max(-sm,0);
 const grow=k<6?Math.min(k/5,1):k<8?1:1-(k-8)/2;
 const cx=W/2,cy=H*.32,R=H*.15;x.fillStyle='#ffe2b8';x.strokeStyle='#3a1f2b';x.lineWidth=W*.004;x.beginPath();x.arc(cx,cy,R,0,6.28);x.fill();x.stroke();
 x.fillStyle='#3a1f2b';[-1,1].forEach(s=>{x.beginPath();x.ellipse(cx+s*R*.35,cy-R*.15,R*.07,R*.1*(1-smile*.4),0,0,6.28);x.fill();});
 x.fillStyle='rgba(246,140,170,.5)';[-1,1].forEach(s=>{x.beginPath();x.ellipse(cx+s*R*.55,cy+R*.2,R*.14,R*.08,0,0,6.28);x.fill();});
 x.beginPath();x.moveTo(cx-R*.35,cy+R*.35);x.quadraticCurveTo(cx,cy+R*.35+R*.4*(smile-frown),cx+R*.35,cy+R*.35);x.stroke();
 const cols=['#f6a7bd','#ffd36b','#c9a7f0','#ff8fab','#9cc3ff','#ffffff'];
 for(let i=0;i<9;i++){const fx=W*(.07+i*.108),h=H*(.22+((i*37)%5)*.04)*Math.min(Math.max(grow*1.4-i*.05,0),1),droop=frown*.6+(k>=8?(1-grow)*.4:0);
  if(h<2)continue;const by=H,tx=fx+Math.sin(t*1.5+i)*W*.008+droop*W*.05,ty=by-h*(1-droop*.3);
  x.strokeStyle=`rgb(${79+droop*80},${138-droop*20},${85})`;x.lineWidth=W*.004;x.beginPath();x.moveTo(fx,by);x.quadraticCurveTo(fx-W*.02,by-h*.5,tx,ty);x.stroke();
  const bloom=Math.min(Math.max((grow-.3-i*.03)*2,0),1)*(1-droop*.5);if(bloom>0){const pr=W*.022*bloom;x.fillStyle=cols[i%6];x.globalAlpha=1-droop*.5;
   for(let p=0;p<5;p++){const a=p/5*6.28+t*.2;x.beginPath();x.arc(tx+Math.cos(a)*pr,ty+Math.sin(a)*pr,pr*.75,0,6.28);x.fill();}
   x.fillStyle='#ffd36b';x.beginPath();x.arc(tx,ty,pr*.5,0,6.28);x.fill();x.globalAlpha=1;}}
 if(grow>.8&&frown<.1){const bx=W*(.5+.35*Math.sin(t*.7)),by=H*(.55+.1*Math.sin(t*1.3)),f=Math.abs(Math.sin(t*12));x.fillStyle='#c9a7f0';[-1,1].forEach(s=>{x.beginPath();x.ellipse(bx+s*W*.012*f,by,W*.012*f,W*.016,0,0,6.28);x.fill();});}
 x.font=`${Math.round(W*.03)}px "DM Sans",sans-serif`;x.textAlign='center';x.fillStyle='#5a3442';x.fillText(frown>.2?'wilting…':smile>.5?'blooming…':'smile to grow',W/2,H*.08);}'''),

'ilysm-touch': dict(
  noun='fingertip words', tagline='Words float on your fingertips. Touch your thumb to each one and it plays out loud.', minutes=15, needs='webcam · works on phones',
  play_sub="it's already live, {n}. click <b>Start camera</b>, hold both hands up and tap once so the sound can play.",
  versions=[
    dict(name='I love you so much', desc='left hand: I, love, you. right hand: so, much.',
         how=["touch your thumb's red dot to a fingertip's red dot to play that word","words on the wrong hands? tap <b>Swap hands</b> · open <b>Sounds</b> to record each word in your own voice"],
         href='i-love-you-so-much.html', link='open I love you so much'),
    dict(name="don't forget to love yourself 💌", desc='same idea, a softer phrase for your own two hands.',
         how=['<b>Record</b> saves a clip with sound · <kbd>H</kbd> hides the controls'],
         href='dont-forget-to-love-yourself.html', link="open don't forget to love yourself"),
  ],
  bugs=[
    ('the words landed on the wrong hands because the camera is mirrored','the left hand shows on the right of the screen; add a Swap hands button just in case'),
    ('one pinch played the word over and over','fire once per pinch, then wait until the dots are 1.7x further apart plus a 120 ms cooldown'),
    ('recording my voice made my laptop audio go quiet and laggy','only open the microphone while a word is being recorded, so the speakers never switch to call mode'),
    ('overlapping words crackled','run all word sounds through a limiter'),
  ],
  draw=r'''(x,W,H,t)=>{
 x.fillStyle='#000';x.fillRect(0,0,W,H);
 const hands=[{cx:.27,words:[['so','#2ee6e6'],['much','#ff2a8a'],null,null]},{cx:.73,words:[['I','#9a2bff'],['love','#7dff1f'],['you','#4a4aff'],null]}];
 const seq=[[1,0],[1,1],[1,2],[0,0],[0,1]],step=Math.floor(t/1.1)%seq.length,ph=(t%1.1)/1.1;
 hands.forEach((h,hi)=>{const bx=W*h.cx,by=H*.72+Math.sin(t*1.3+hi)*H*.015,sp=W*.08,dots=[];
  for(let f=0;f<4;f++){const a=(-.9+f*.6)*(hi?1:-1)*.5;dots.push([bx+(f-1.5)*sp*(hi?1:-1),by-H*(.36-Math.abs(f-1.2)*.06)+Math.sin(t*2+f)*H*.006]);}
  const thumbHome=[bx+(hi?-1:1)*sp*2.3,by-H*.05];let th=thumbHome;const[sh,sf]=seq[step];
  if(sh===hi){const tg=dots[sf],e=ph<.5?ph*2:2-ph*2,ee=e*e*(3-2*e);th=[thumbHome[0]+(tg[0]-thumbHome[0])*ee,thumbHome[1]+(tg[1]-thumbHome[1])*ee];}
  x.strokeStyle='rgba(255,255,255,.12)';x.lineWidth=W*.003;[...dots,th].forEach(d=>{x.beginPath();x.moveTo(bx,by+H*.12);x.lineTo(d[0],d[1]);x.stroke();});
  dots.forEach((d,f)=>{const w=h.words[f];if(w){const hit=sh===hi&&sf===f&&ph>.38&&ph<.75;x.font=`italic 700 ${Math.round(W*(hit?.05:.032))}px Arial`;x.textAlign='center';x.fillStyle=w[1];x.fillText(w[0],d[0],d[1]-W*.025);}
   x.fillStyle='#ff1010';x.beginPath();x.arc(d[0],d[1],W*.011,0,6.28);x.fill();});
  x.fillStyle='#ff1010';x.beginPath();x.arc(th[0],th[1],W*.011,0,6.28);x.fill();});}'''),
}

PAGES['ascii-christmas'] = dict(
  noun='ascii christmas tree', tagline='A 3D Christmas tree made of text that grows itself, spins, and lights up.', minutes=20, needs='laptop + Chrome · webcam for hands',
  play_sub="it's already live, {n}. open it on your laptop and click once to turn the sound on.",
  versions=[
    dict(name='animation version', desc='the tree grows by itself in ~15 seconds: star, ornaments, fairy lights, presents, snow and a sleigh across the moon.',
         how=['drag to spin the tree · click for sparkles','<kbd>R</kbd> replays · <kbd>J</kbd> sleigh · <kbd>O</kbd> ornament colours · <kbd>Space</kbd> snow · <kbd>S</kbd> picture'],
         href='tree.html', link='open the animation'),
    dict(name='hand gesture version ✋', desc='spin it with your own hands. needs a webcam, works best in Chrome. nothing is uploaded.',
         how=['<b>swipe</b> to spin · <b>pinch</b> for sparkles','<b>open palm</b> (hold) for the sleigh · <b>fist</b> for a snowstorm'],
         href='tree.html?hand', link='open the hand gesture version'),
  ],
  bugs=[
    ('the tree looked flat, like a 2D drawing','render it as a real 3D object the donut.c way: points on the surface, rotate, project, z-buffer, and pick each character by brightness'),
    ('the whole tree was a solid block of # and @','darken the underside of each branch layer and make the light less even, so it shows ridges and a shadow side'),
    ('the star came out as a blob','build it from a proper 5-point star shape with a point-in-polygon test and tone down its glow'),
    ('the sleigh flew off the top of the screen, then through the tree','leave room at the top and fly it from in front of the moon, above the tree top'),
    ('the snowy ground stretched into flat lines','make the ground disc smaller and tilt the camera down about 15°'),
    ('dragging spun the tree the opposite way','flip the sign so the front of the tree follows your finger (and your hand)'),
  ],
  draw=r"""(x,W,H,t)=>{
 const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#050816');g.addColorStop(1,'#1a2a5e');x.fillStyle=g;x.fillRect(0,0,W,H);
 const ch=H/34,cw=ch*.6,R=' .,-~:;=!*#$@';x.font=`500 ${ch}px "DM Mono",monospace`;x.textAlign='center';x.textBaseline='middle';
 for(let i=0;i<40;i++){x.globalAlpha=.3+.3*Math.sin(t*1.5+i);x.fillStyle='#cfdaff';x.fillText(i%5?'.':'+',(i*97%100)/100*W,(i*53%60)/100*H);}
 const cols=Math.ceil(W/cw),rows=Math.ceil(H/ch),Z=new Float32Array(cols*rows).fill(9),Lm=new Float32Array(cols*rows).fill(-1);
 const a=t*.8,ca=Math.cos(a),sa=Math.sin(a),K=H*.62,cx=W/2,base=H*.86;
 const T=[[0,.45,.46],[.3,.72,.34],[.6,1,.2]];
 for(const[b,tp,Rr]of T)for(let i=0;i<40;i++)for(let j=0;j<70;j++){const u=i/40,h=b+u*(tp-b),th=j/70*6.283,lay=(u*3)%1,r=Rr*(1-u)*(.85+.15*lay)*(1+.07*Math.sin(9*th));
  const X=Math.cos(th)*r,Zz=Math.sin(th)*r,x1=X*ca+Zz*sa,z1=-X*sa+Zz*ca,c=Math.round((cx+x1*K)/cw),rr=Math.round((base-h*K+z1*K*.2)/ch);if(c<0||rr<0||c>=cols||rr>=rows)continue;const id=rr*cols+c;if(z1>=Z[id])continue;
  const nx=Math.cos(th),nz=Math.sin(th),nx1=nx*ca+nz*sa,nz1=-nx*sa+nz*ca;Z[id]=z1;Lm[id]=Math.max(0,(-nx1*.5-nz1*.7+.4)/1.3)*(.5+.5*(1-lay));}
 for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){const l=Lm[r*cols+c];if(l<0)continue;x.globalAlpha=1;x.fillStyle=`rgb(${16+124*l|0},${70+185*l|0},${40+140*l|0})`;x.fillText(R[Math.max(1,Math.min(12,Math.round(l*12)))],(c+.5)*cw,(r+.5)*ch);}
 for(let k=0;k<26;k++){const h=.05+(k*37%90)/100,th=k*2.4+a,r=.46*(1-h)*1.02,X=Math.cos(th)*r,Zz=Math.sin(th)*r;if(Zz*ca-X*sa>0)continue;const px=cx+(X*ca+Zz*sa)*K,py=base-h*K;x.globalAlpha=.85+.15*Math.sin(t*4+k);x.fillStyle=['#ff3b3b','#ffd23f','#4fb3ff','#ff5c8a'][k%4];x.font=`700 ${ch*1.3}px "DM Mono",monospace`;x.fillText('o',px,py);}
 x.globalAlpha=1;x.font=`700 ${ch*2.6}px "DM Mono",monospace`;x.fillStyle='#ffd86b';x.save();x.translate(cx,base-K*1.04);x.scale(Math.max(.25,Math.abs(Math.cos(t*1.1))),1);x.fillText('*',0,0);x.restore();
 const p=(t%9)/9;if(p<.6){const q=p/.6;x.font=`500 ${ch}px "DM Mono",monospace`;x.fillStyle='#f4e7c8';x.fillText('(")__ (")__ \\__/',W+60-q*(W+200),H*.12+Math.pow(1-q,2)*H*.12);}
}"""
)
