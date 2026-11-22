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
function togglePanel(){if(!panel){panel=doc.createElement('div');panel.id='dpanel';panel.className='aibox';body.appendChild(panel);
  panel.innerHTML='<button class="dx" aria-label="'+esc(T('aiClose'))+'">✕</button><div class="dc"></div>';var c=panel.querySelector('.dc');window.__buildAssistant&&window.__buildAssistant(c);
  var adv=doc.getElementById('adv');if(adv){var b=doc.createElement('button');b.className='sec';b.textContent='🎯 '+T('advGo');b.onclick=function(){panel.classList.remove('o');adv.scrollIntoView({behavior:reduce()?'auto':'smooth',block:'center'});var bx=adv.firstChild;if(bx){bx.classList.add('pulse');setTimeout(function(){bx.classList.remove('pulse')},1800)}};c.appendChild(b)}
  panel.querySelector('.dx').onclick=function(){panel.classList.remove('o')}}
 requestAnimationFrame(function(){panel.classList.toggle('o');if(panel.classList.contains('o')){var i=panel.querySelector('.aiq');i&&i.focus()}})}
dock.addEventListener('click',function(e){var b=e.target.closest('[data-a]');if(!b)return;var a=b.dataset.a;openDock(false);
 if(a==='ai')togglePanel();else if(a==='pz'){var p=doc.getElementById('pz');p&&p.click()}else if(a==='top')scrollTo({top:0,behavior:reduce()?'auto':'smooth'})});
doc.addEventListener('keydown',function(e){if(e.key==='Escape'&&panel)panel.classList.remove('o')});
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
