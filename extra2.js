(function(){
var S=window.ADV_S||{},doc=document,R=doc.documentElement,body=doc.body;
var reduce=function(){return matchMedia('(prefers-reduced-motion:reduce)').matches||R.getAttribute('data-an')==='off'};
var coarse=matchMedia('(pointer:coarse)').matches;
function T(k){return (S.t&&S.t[k])||k}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
var LS=function(k,d){try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}},SS=function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
/* ---- registro local de visitas (solo en este navegador) ---- */
(function(){var k=body.getAttribute('data-s')||'(inicio)',v=LS('vis',{}),d=LS('vd',{}),t=new Date().toISOString().slice(0,10);v[k]=(v[k]||0)+1;d[t]=(d[t]||0)+1;
 Object.keys(d).sort().slice(0,Math.max(0,Object.keys(d).length-90)).forEach(function(x){delete d[x]});SS('vis',v);SS('vd',d)})();
/* ---- cabecera que se compacta ---- */
var hd=doc.querySelector('header');addEventListener('scroll',function(){if(hd)hd.classList.toggle('sc',scrollY>24)},{passive:true});
/* ---- orbes flotantes con parallax ---- */
var ob=doc.createElement('div');ob.className='orbs';ob.setAttribute('aria-hidden','true');ob.innerHTML='<i></i><i></i><i></i>';body.appendChild(ob);
if(!coarse){var raf=0,mx=0,my=0;addEventListener('mousemove',function(e){mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5;if(!raf)raf=requestAnimationFrame(function(){raf=0;if(!reduce()){ob.style.setProperty('--px',mx);ob.style.setProperty('--py',my)}})},{passive:true})}
/* ---- brillo que sigue al cursor + inclinación 3D ---- */
if(!coarse){doc.addEventListener('mousemove',function(e){if(reduce())return;var el=e.target.closest&&e.target.closest('.tool,.card,.aibox,.day');if(!el)return;var r=el.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;el.style.setProperty('--mx',x+'px');el.style.setProperty('--my',y+'px');
 if(el.classList.contains('tool')){el.style.transform='perspective(700px) rotateX('+((.5-y/r.height)*7)+'deg) rotateY('+((x/r.width-.5)*9)+'deg) translateY(-3px)'}},{passive:true});
 doc.addEventListener('mouseout',function(e){var el=e.target.closest&&e.target.closest('.tool');if(el&&!el.contains(e.relatedTarget))el.style.transform=''})}
/* ---- héroe: palabras animadas, placeholder que escribe y contadores ---- */
var h1=doc.querySelector('.hero h1');
if(h1&&!reduce()){var w=h1.textContent.trim().split(/\s+/);h1.innerHTML=w.map(function(x,i){return'<span class="wd" style="--i:'+i+'">'+esc(x)+'</span>'}).join(' ')}
var hq=doc.querySelector('.hero #q');
if(hq&&!reduce()){var ph=(T('phs')||'').split('|'),base=hq.getAttribute('placeholder'),pi=0,ci=0,del=false,tm;
 var pre=base.indexOf(':')>-1?base.slice(0,base.indexOf(':')+1)+' ':'🔍 ';
 function ty(){if(doc.activeElement===hq||hq.value){tm=setTimeout(ty,800);return}var w=ph[pi%ph.length];ci+=del?-1:1;hq.setAttribute('placeholder',pre+w.slice(0,ci)+'|');
  if(!del&&ci>=w.length){del=true;tm=setTimeout(ty,1400);return}if(del&&ci<=0){del=false;pi++}tm=setTimeout(ty,del?35:75)}
 if(ph.length>1)setTimeout(ty,1200);hq.addEventListener('focus',function(){hq.setAttribute('placeholder',base)})}
doc.querySelectorAll('.stats span').forEach(function(sp){var m=sp.textContent.match(/\d+/);if(!m||reduce())return;var n=+m[0],t0=performance.now(),pre=sp.textContent.slice(0,m.index),post=sp.textContent.slice(m.index+m[0].length);
 (function st(t){var k=Math.min(1,(t-t0)/1100);sp.textContent=pre+Math.round(n*(1-Math.pow(1-k,3)))+post;if(k<1)requestAnimationFrame(st)})(t0)});
/* ---- menú flotante (dock) + panel del asistente ---- */
var dock=doc.createElement('div');dock.id='dock';
dock.innerHTML='<div class="dm" hidden><button data-a="ai"><span>'+esc(T('dock_ai'))+'</span>🤖</button><a href="/mis-herramientas" data-a="fav"><span>'+esc(T('dock_fav'))+'</span>⭐</a><button data-a="pz"><span>'+esc(T('dock_pz'))+'</span>🎨</button><button data-a="top"><span>'+esc(T('dock_top'))+'</span>↑</button></div><button id="dfab" aria-label="'+esc(T('dock_menu'))+'" aria-expanded="false">✨</button>';
body.appendChild(dock);
var dm=dock.querySelector('.dm'),fab=doc.getElementById('dfab'),panel=null;
function openDock(o){dm.hidden=!o;dock.classList.toggle('o',o);fab.setAttribute('aria-expanded',o);fab.textContent=o?'✕':'✨'}
fab.onclick=function(e){e.stopPropagation();openDock(dm.hidden)};
doc.addEventListener('click',function(e){if(!dock.contains(e.target))openDock(false)});

var chat=null,ml,qr,inp,msgs=[],tabsOK=function(){return window.__advTabs&&body.getAttribute('data-s')},opened=false;
try{msgs=JSON.parse(sessionStorage.getItem('chat')||'[]')}catch(e){}
function save(){try{sessionStorage.setItem('chat',JSON.stringify(msgs.slice(-40)))}catch(e){}}
function line(m){var d=doc.createElement('div');d.className='cm '+m.r+(m.rich?' rich':'');d.innerHTML=m.h;ml.appendChild(d);ml.scrollTop=ml.scrollHeight}
function push(r,h,rich){var m={r:r,h:h,rich:!!rich};msgs.push(m);save();if(ml)line(m)}
function typing(cb){if(reduce()){cb();return}var t=doc.createElement('div');t.className='cm b typ';t.innerHTML='<i></i><i></i><i></i>';ml.appendChild(t);ml.scrollTop=ml.scrollHeight;setTimeout(function(){t.remove();cb()},450+Math.random()*450)}
function say(h,rich,then){typing(function(){push('b',h,rich);then&&then()})}
function links(slugs){var by={};(window.TL||[]).forEach(function(t){by[t[0]]=t});return slugs.map(function(s){var t=by[s];return t?'<a class="cl" href="/'+t[0]+'"><span>'+t[2]+'</span>'+esc(t[1])+'</a>':''}).join('')}
function quick(list){qr.innerHTML='';list.forEach(function(q){var b=doc.createElement('button');b.type='button';b.textContent=q[0];b.onclick=function(){push('u',esc(q[0].replace(/^\S+\s/,'')));q[1]()};qr.appendChild(b)})}
function mainQuick(){var l=[];if(tabsOK()){l.push([T('chatQ1').slice(0,0)+'🧭 '+T('chatQ1'),function(){tab(1)}],['🔍 '+T('chatQ2'),function(){tab(2)}],['🎯 '+T('chatQ3'),function(){tab(3)}])}
 l.push(['🧳 '+T('chatQJ'),journeys]);quick(l)}
function tab(n){say(window.__advTabs[n](),true,function(){say(T('chatMore'),false,mainQuick)})}
function journeys(){say(T('chatPick'),false,function(){quick((S.journeys||[]).map(function(j){return[j[1]+' '+j[2],function(){say('<b>'+esc(j[3])+'</b><div class="cls">'+links(j[4])+'</div>',true,function(){say(T('chatMore'),false,mainQuick)})}]}))})}
function ask(t){t=t.trim();if(!t)return;push('u',esc(t));
 if(/^(hola|buenas|hello|hi|hey|bon dia|bona tarda|salut|ei)\b/i.test(t)){say(T('chatGreet'),false,mainQuick);return}
 var r=window.__find?window.__find(t):[];
 if(r.length)say('<b>'+T('aiBest')+'</b><div class="cls">'+links(r.map(function(x){return x[0]}))+'</div>',true,function(){say(T('chatMore'),false,mainQuick)});else say(T('aiNone'),false,mainQuick)}
function buildChat(){chat=doc.createElement('div');chat.id='chat';chat.setAttribute('role','dialog');chat.setAttribute('aria-label',T('chatTitle'));
 chat.innerHTML='<div class="ch"><span class="chav">🤖</span><div><b>'+esc(T('chatTitle'))+'</b><small><i class="od"></i>'+esc(T('chatSub'))+'</small></div><button type="button" class="chc" title="'+esc(T('chatClear'))+'" aria-label="'+esc(T('chatClear'))+'">🗑️</button><button type="button" class="chx" aria-label="'+esc(T('aiClose'))+'">✕</button></div><div class="cmsg" aria-live="polite"></div><div class="cqr"></div><form class="cin"><input type="text" placeholder="'+esc(T('chatPh'))+'" autocomplete="off" aria-label="'+esc(T('chatPh'))+'"><button type="submit" aria-label="'+esc(T('chatSend'))+'">➤</button></form>';
 body.appendChild(chat);ml=chat.querySelector('.cmsg');qr=chat.querySelector('.cqr');inp=chat.querySelector('input');
 chat.querySelector('.cin').onsubmit=function(e){e.preventDefault();var v=inp.value;inp.value='';ask(v)};
 chat.querySelector('.chx').onclick=function(){setChat(false)};
 chat.querySelector('.chc').onclick=function(){msgs=[];save();ml.innerHTML='';hello()};
 ml.addEventListener('click',function(e){var s=e.target.closest('[data-q]');if(s){var d=doc.querySelectorAll('main details')[+s.dataset.q];if(d){d.open=true;setChat(false);d.scrollIntoView({behavior:reduce()?'auto':'smooth',block:'center'})}}});
 /* arrastrar */
 var h=chat.querySelector('.ch'),dr=null;h.addEventListener('pointerdown',function(e){if(e.target.closest('button')||innerWidth<640)return;var r=chat.getBoundingClientRect();dr={x:e.clientX-r.left,y:e.clientY-r.top};h.setPointerCapture(e.pointerId);chat.classList.add('drag')});
 h.addEventListener('pointermove',function(e){if(!dr)return;var x=Math.max(0,Math.min(innerWidth-chat.offsetWidth,e.clientX-dr.x)),y=Math.max(0,Math.min(innerHeight-60,e.clientY-dr.y));chat.style.left=x+'px';chat.style.top=y+'px';chat.style.bottom='auto';chat.style.right='auto'});
 h.addEventListener('pointerup',function(){if(!dr)return;dr=null;chat.classList.remove('drag');SS('chatpos',[parseInt(chat.style.left),parseInt(chat.style.top)])});
 var pos=LS('chatpos',null);if(pos&&innerWidth>=640&&pos[0]<innerWidth-120&&pos[1]<innerHeight-80){chat.style.left=pos[0]+'px';chat.style.top=pos[1]+'px';chat.style.bottom='auto';chat.style.right='auto'}
 msgs.forEach(line);if(!msgs.length)hello();else mainQuick()}
function hello(){var t=tabsOK()?(doc.querySelector('h1')||{}).textContent:'';say(t?T('chatHelloTool').replace('{0}',esc(t)):T('chatHello'),false,mainQuick)}
function setChat(o){if(o&&!chat)buildChat();if(!chat)return;chat.classList.toggle('o',o);fab2.classList.toggle('hide',o);if(o){opened=true;var bg=fab2.querySelector('.bd');bg&&bg.remove();SS('chatseen',1);setTimeout(function(){inp&&inp.focus()},300)}}
var fab2=doc.createElement('button');fab2.id='chatfab';fab2.type='button';fab2.setAttribute('aria-label',T('chatTitle'));fab2.innerHTML='<span class="ci">💬</span><span class="cl2">'+esc(T('chatFab'))+'</span>'+(LS('chatseen',0)?'':'<b class="bd">1</b>');body.appendChild(fab2);fab2.onclick=function(){setChat(true)};
function togglePanel(){setChat(!(chat&&chat.classList.contains('o')))}
dock.addEventListener('click',function(e){var b=e.target.closest('[data-a]');if(!b)return;var a=b.dataset.a;openDock(false);
 if(a==='ai')togglePanel();else if(a==='pz'){var p=doc.getElementById('pz');p&&p.click()}else if(a==='top')scrollTo({top:0,behavior:reduce()?'auto':'smooth'})});
doc.addEventListener('keydown',function(e){if(e.key==='Escape'&&chat)setChat(false)});
var oldTop=doc.getElementById('top');if(oldTop)oldTop.style.display='none',oldTop.id='top0';
/* desplaza el dock sobre el banner de cookies */
var cb=doc.getElementById('cb');function cbh(){R.style.setProperty('--cbh',(cb&&cb.offsetHeight&&getComputedStyle(cb).display!=='none'?cb.offsetHeight:0)+'px')}
if(cb){cbh();new MutationObserver(cbh).observe(cb,{attributes:true});addEventListener('resize',cbh);setInterval(cbh,1500)}
/* ---- barra flotante de resultados ---- */
var card=doc.querySelector('.card'),slug=body.getAttribute('data-s');
if(slug&&card){var fb=doc.createElement('div');fb.id='fbar';fb.hidden=true;body.appendChild(fb);var vis=false;
 function upd(){var rs=[].slice.call(card.querySelectorAll('.res > div'),0,3);if(!rs.length){fb.hidden=true;return}
  fb.innerHTML=rs.map(function(d){var s=d.querySelector('small'),b=d.querySelector('b');return s&&b?'<span><small>'+esc(s.textContent)+'</small><b>'+esc(b.textContent)+'</b></span>':''}).join('')+'<button type="button" aria-label="'+esc(T('fbar_up'))+'">↑</button>';
  fb.querySelector('button').onclick=function(){card.scrollIntoView({behavior:reduce()?'auto':'smooth',block:'start'})};
  var r=card.getBoundingClientRect();var show=r.bottom<60;fb.hidden=false;fb.classList.toggle('on',show)}
 addEventListener('scroll',upd,{passive:true});new MutationObserver(function(){setTimeout(upd,60)}).observe(card,{childList:true,subtree:true});setTimeout(upd,400)}
})();
