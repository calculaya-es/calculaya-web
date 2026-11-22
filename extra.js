(function(){
var S=window.ADV_S||{},LOC=S.loc||'es-ES',doc=document,R=doc.documentElement;
var reduce=function(){return matchMedia('(prefers-reduced-motion:reduce)').matches||R.getAttribute('data-an')==='off'};
function T(k,a){var s=(S.t&&S.t[k])||k;(a||[]).forEach(function(x,i){s=s.split('{'+i+'}').join(x)});return s}
function N(x,d){return isFinite(x)?x.toLocaleString(LOC,{maximumFractionDigits:d==null?0:d}):'-'}
function V(id){var e=doc.getElementById(id);return e?parseFloat(String(e.value).replace(',','.')):NaN}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
/* ---------- animaciones ---------- */
var pb=doc.createElement('div');pb.id='sp';doc.body.appendChild(pb);
addEventListener('scroll',function(){var h=R.scrollHeight-innerHeight;pb.style.width=(h>0?scrollY/h*100:0)+'%'},{passive:true});
if('IntersectionObserver' in window){
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.06});
 var rv=function(){doc.querySelectorAll('.tool,main details,main h2,.card,.aff,.day,.aibox').forEach(function(el,i){if(el.dataset.rv)return;el.dataset.rv=1;if(reduce())return;el.classList.add('rv');el.style.transitionDelay=Math.min(i%8,7)*45+'ms';io.observe(el)})};
 rv();addEventListener('beforeprint',function(){doc.querySelectorAll('.rv').forEach(function(e){e.classList.add('in')})});
}
doc.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b||reduce()||b.id==='top'||b.id==='lg'||b.closest('#pzp'))return;
 var cs=getComputedStyle(b);if(cs.position==='static')b.style.position='relative';b.style.overflow='hidden';
 var r=b.getBoundingClientRect(),s=doc.createElement('span'),d=Math.max(r.width,r.height);s.className='rp';s.style.cssText='width:'+d+'px;height:'+d+'px;left:'+(e.clientX-r.left-d/2)+'px;top:'+(e.clientY-r.top-d/2)+'px';b.appendChild(s);setTimeout(function(){s.remove()},600)});
var prev={};
function parse(t){var m=t.match(/^([^\d-]*)(-?\d[\d.,\s ]*)([^\d]*)$/);if(!m)return null;var dec=LOC.indexOf('en')===0?'.':',',th=dec==='.'?',':'.',raw=m[2].trim().replace(/[\s ]/g,''),neg=raw[0]==='-',p=raw.split(dec),ip=p[0].split(th).join('').replace('-','');if(p.length>2||!/^\d+$/.test(ip))return null;
 return{pre:m[1],suf:m[3],val:parseFloat(ip+(p[1]?'.'+p[1]:''))*(neg?-1:1),fd:p[1]?p[1].length:0}}
function anim(b,key){var orig=b.textContent,p=parse(orig.trim());if(!p)return;var old=prev[key];prev[key]=p.val;if(old==null||old===p.val||reduce())return;
 var t0=performance.now(),nf=new Intl.NumberFormat(LOC,{minimumFractionDigits:p.fd,maximumFractionDigits:p.fd});b.classList.add('flash');
 (function step(t){var k=Math.min(1,(t-t0)/450),e=1-Math.pow(1-k,3);if(k>=1){b.textContent=orig;setTimeout(function(){b.classList.remove('flash')},250);return}b.textContent=p.pre+nf.format(old+(p.val-old)*e)+p.suf;requestAnimationFrame(step)})(t0)}
var card=doc.querySelector('.card');
if(card&&window.MutationObserver){new MutationObserver(function(ms){ms.forEach(function(m){m.addedNodes.forEach(function(n){if(n.nodeType!==1)return;var rs=n.matches&&n.matches('.res')?[n]:(n.querySelectorAll?n.querySelectorAll('.res'):[]);
 [].forEach.call(rs,function(r){[].forEach.call(r.children,function(d){var s=d.querySelector('small'),b=d.querySelector('b');if(s&&b)anim(b,s.textContent)})})})})}).observe(card,{childList:true,subtree:true})}
var fv=doc.getElementById('fv');
if(fv)fv.addEventListener('click',function(){if(!fv.classList.contains('on')||reduce())return;var r=fv.getBoundingClientRect();
 for(var i=0;i<9;i++){var s=doc.createElement('span');s.textContent='⭐';s.style.cssText='position:fixed;z-index:50;pointer-events:none;left:'+(r.left+r.width/2)+'px;top:'+(r.top+r.height/2)+'px;font-size:'+(12+Math.random()*10)+'px';doc.body.appendChild(s);
  var a=Math.PI*2*i/9,dx=Math.cos(a)*(40+Math.random()*30),dy=Math.sin(a)*(40+Math.random()*30);
  s.animate([{transform:'translate(0,0) scale(1)',opacity:1},{transform:'translate('+dx+'px,'+dy+'px) scale(.3)',opacity:0}],{duration:700,easing:'ease-out'}).onfinish=(function(x){return function(){x.remove()}})(s)}});
/* ---------- asesor en herramientas ---------- */
function pmt(c,i,n){var r=i/1200;return r?c*r/(1-Math.pow(1+r,-n)):c/n}
var RULES={
'calculadora-hipoteca':function(){var c=V('c'),i=V('i'),y=V('y'),n=y*12,m=pmt(c,i,n),t=[];if(!(c>0&&n>0))return t;var tot=m*n-c;
 if(i>5)t.push(['warn','hip_hi',[N(i,2)]]);if(y>30)t.push(['warn','hip_long',[N(y)]]);t.push(['info','hip_tot',[N(tot),N(tot/c*100),N(m)]]);t.push(['info','hip_inc',[N(m/.35)]]);return t},
'calculadora-prestamos':function(){var c=V('c'),i=V('i'),n=V('m'),t=[];if(!(c>0&&n>0))return t;var m=pmt(c,i,n);if(i>12)t.push(['warn','loan_hi',[N(i,2)]]);t.push(['info','loan_tot',[N(m*n-c),N(m)]]);if(n>60)t.push(['warn','loan_long',[]]);return t},
'calculadora-imc':function(){var w=V('w'),h=V('h')/100,t=[];if(!(w>0&&h>0))return t;var b=w/(h*h),f=N(b,1);t.push([b<18.5?'warn':b<25?'ok':'warn',b<18.5?'imc_low':b<25?'imc_ok':b<30?'imc_over':'imc_ob',[f]]);t.push(['info','imc_note',[]]);return t},
'calculadora-calorias-tmb':function(){var s=doc.getElementById('s'),e=V('e'),p=V('p'),a=V('a'),f=V('f'),t=[];if(!(p>0&&a>0&&e>0))return t;var tm=10*p+6.25*a-5*e+(s&&s.value==='h'?5:-161),g=tm*f;t.push(['info','cal_def',[N(g-400)]]);if(g-400<1200)t.push(['warn','cal_min',[]]);return t},
'calculadora-salario-bruto-neto':function(){return[['info','sal_cmp',[]],['info','sal_pag',[]]]},
'calculadora-ahorro-objetivo':function(){var g=V('g'),c=V('c')||0,m=V('m'),t=[];if(g>0&&m>0)t.push(['info','ah_mes',[N(Math.max(0,g-c)/m)]]);t.push(['info','ah_auto',[]],['info','ah_fund',[]]);return t},
'calculadora-interes-compuesto':function(){var r=V('r'),t=[['info','ic_time',[]]];if(r>10)t.push(['warn','ic_unreal',[N(r,1)]]);return t},
'calculadora-propinas':function(){var p=V('t'),t=[['info','tip_es',[]]];if(p>20)t.push(['warn','tip_hi',[N(p)]]);return t},
'calculadora-descuentos':function(){var t=[];if(V('d2')>0)t.push(['info','dsc_cmb',[]]);return t},
'calculadora-inflacion':function(){var a=V('a'),r=V('r'),y=V('y');return a>0&&y>0?[['info','inf_loss',[N(a),N(a/Math.pow(1+r/100,y)),N(y)]]]:[]},
'calculadora-consumo-electrico':function(){var c=V('w')/1000*V('h')*V('d')*V('p'),t=[];if(c>20)t.push(['warn','ce_hi',[N(c,1)]]);t.push(['info','ce_tip',[]]);return t},
'calculadora-ritmo-carrera':function(){var d=V('d'),s=(V('h')||0)*3600+(V('mi')||0)*60+(V('se')||0),t=[['info','run_tip',[]]];if(d>0&&s>0&&s/d<240){var p=s/d;t.push(['warn','run_fast',[Math.floor(p/60)+':'+('0'+Math.round(p%60)).slice(-2)]])}return t},
'coste-viaje-gasolina':function(){var k=V('k'),c=V('c'),p=V('p'),n=V('n');return k>0&&n>1?[['info','trip_sp',[N(k*c/100*p/n,2)]]]:[]},
'generador-contrasenas':function(){return[V('l')<12?['warn','pw_short',[]]:['ok','pw_ok',[]]]},
'calculadora-indemnizacion-despido':function(){return[['warn','des_old',[]]]},
'calculadora-rentabilidad-alquiler':function(){var p=V('p'),gc=V('gc')||0,rf=V('rf')||0,al=V('al'),ga=V('ga')||0,t=[];var inv=p*(1+gc/100)+rf;if(!(inv>0&&al>0))return t;var n=(al*12-ga)/inv*100;t.push(['info','rent_net',[N(n,2)]]);if(n<3.5)t.push(['warn','rent_low',[]]);return t}
};
var slug=doc.body.getAttribute('data-s'),adv=doc.getElementById('adv');
if(slug&&adv){
 var tab=RULES[slug]?3:2,tm;
 adv.innerHTML='<div class="aibox"><div class="advh"><span class="advi" aria-hidden="true">🤖</span><div><b>'+T('advTitle')+'</b><small>'+T('advSub')+'</small></div></div><div class="advt" role="tablist"></div><div class="advb" aria-live="polite"></div></div>';
 var tb=adv.querySelector('.advt'),bd=adv.querySelector('.advb');
 [1,2,3].forEach(function(n){var b=doc.createElement('button');b.type='button';b.setAttribute('role','tab');b.textContent=T('tab'+n);b.onclick=function(){tab=n;render()};tb.appendChild(b)});
 var t1=function(){var h='<ul>';doc.querySelectorAll('.card label[for]').forEach(function(l){var e=doc.getElementById(l.getAttribute('for'));if(!e)return;var lab=l.textContent.trim().replace(/:$/,''),x;
  if(e.tagName==='SELECT'){x=T('opts',[[].map.call(e.options,function(o){return o.text}).slice(0,4).join(' / ')])}else{x=T('ex',['<code>'+esc(e.value)+'</code>']);if(/%/.test(lab))x+=' · '+T('pct')}
  h+='<li><b>'+esc(lab)+'</b> - '+x+'</li>'});return h+'</ul><p>'+T('tipFill')+'</p>'};
 var t2=function(){var h='',rs=doc.querySelectorAll('.card .res > div');if(!rs.length)h+='<p>'+T('noRes')+'</p>';
  else{h+='<h4>'+T('resHdr')+'</h4><ul>';[].forEach.call(rs,function(d){var s=d.querySelector('small'),b=d.querySelector('b');if(s&&b)h+='<li><b>'+esc(s.textContent)+'</b>: '+esc(b.textContent)+'</li>'});h+='</ul>'}
  var tx=doc.querySelector('.tx');if(tx){var c=0;[].forEach.call(tx.children,function(el){if(c<3&&/^(P|UL|OL)$/.test(el.tagName)){h+=el.outerHTML;c++}})}
  var qs=doc.querySelectorAll('main details summary');if(qs.length){h+='<h4>'+T('faqHdr')+'</h4><ul>';[].slice.call(qs,0,3).forEach(function(q,i){h+='<li><span class="lnk" data-q="'+i+'">'+esc(q.textContent)+'</span></li>'});h+='</ul>'}return h};
 var t3=function(){var h='',tp=RULES[slug]?RULES[slug]():[];h+='<h4>'+T('nextHdr')+'</h4>';
  h+=tp.length?tp.map(function(x){return'<div class="tip '+x[0]+'"><span>'+(x[0]==='warn'?'⚠️':x[0]==='ok'?'✅':'💡')+'</span><div>'+T(x[1],x[2])+'</div></div>'}).join(''):'<p>'+T('noTips')+'</p>';
  h+='<h4>'+T('genHdr')+'</h4><ul><li>'+T('g1')+'</li><li>'+T('g2')+'</li><li>'+T('g3')+'</li></ul>';
  var gs=doc.querySelectorAll('main .grid');var rl=gs.length?gs[gs.length-1].querySelectorAll('a.tool b'):[];var as=gs.length?gs[gs.length-1].querySelectorAll('a.tool'):[];
  if(as.length){h+='<h4>'+T('related')+'</h4><div class="rel">';[].slice.call(as,0,4).forEach(function(a){h+='<a href="'+a.getAttribute('href')+'">'+esc(a.textContent.trim())+'</a>'});h+='</div>'}return h};
 function render(){[].forEach.call(tb.children,function(b,i){b.classList.toggle('on',i+1===tab)});bd.innerHTML=tab===1?t1():tab===2?t2():t3();
  bd.querySelectorAll('[data-q]').forEach(function(s){s.onclick=function(){var d=doc.querySelectorAll('main details')[+s.dataset.q];if(d){d.open=true;d.scrollIntoView({behavior:reduce()?'auto':'smooth',block:'center'})}}})}
 var sch=function(){clearTimeout(tm);tm=setTimeout(render,450)};
 doc.querySelectorAll('.card input,.card select,.card textarea').forEach(function(e){e.addEventListener('input',sch);e.addEventListener('change',sch)});
 doc.querySelectorAll('.card button').forEach(function(b){b.addEventListener('click',sch)});
 window.__advTabs={1:t1,2:t2,3:t3};addEventListener('load',function(){render()});render();
}
/* ---------- asistente (portada y panel flotante) ---------- */
var TL=window.TL||[];
var _norm=function(s){return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'')},_idx=null;
function find(q){if(!_idx)_idx=TL.map(function(t){return{t:t,h:_norm(t[1]),d:_norm(t[3]||'')}});var w=_norm(q).split(/[^a-z0-9]+/).filter(function(x){return x.length>2});if(!w.length)return[];
 return _idx.map(function(o){var s=0;w.forEach(function(x){var st=x.length>5?x.slice(0,5):x;if(o.h.indexOf(st)>-1)s+=3;if(o.d.indexOf(st)>-1)s+=1});return[s,o.t]}).filter(function(x){return x[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,5).map(function(x){return x[1]})}
window.__find=find;
function buildAssistant(el){
 var by={};TL.forEach(function(t){by[t[0]]=t});
 var norm=function(s){return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')};
 var idx=TL.map(function(t){return{t:t,h:norm(t[1]),d:norm(t[3]||'')}});
 el.innerHTML='<div class="advh"><span class="advi" aria-hidden="true">🤖</span><div><b>'+T('aiTitle')+'</b><small>'+T('aiHint')+'</small></div></div><input class="aiq" placeholder="'+esc(T('aiPh'))+'" autocomplete="off"><div class="jr"></div><div class="aout" aria-live="polite"></div>';
 var q=el.querySelector('.aiq'),jr=el.querySelector('.jr'),out=el.querySelector('.aout');
 var link=function(s){var t=by[s];return t?'<a href="/'+t[0]+'"><span>'+t[2]+'</span> '+esc(t[1])+'</a>':''};
 (S.journeys||[]).forEach(function(j){var b=doc.createElement('button');b.type='button';b.textContent=j[1]+' '+j[2];b.onclick=function(){q.value='';[].forEach.call(jr.children,function(x){x.classList.toggle('on',x===b)});
  out.innerHTML='<p><b>'+T('aiSteps')+'</b> '+esc(j[3])+'</p><ol>'+j[4].map(function(s){return by[s]?'<li>'+link(s)+'</li>':''}).join('')+'</ol>'};jr.appendChild(b)});
 q.oninput=function(){[].forEach.call(jr.children,function(x){x.classList.remove('on')});var w=norm(q.value).split(/[^a-z0-9]+/).filter(function(x){return x.length>2});if(!w.length){out.innerHTML='';return}
  var sc=idx.map(function(o){var s=0;w.forEach(function(x){var st=x.length>5?x.slice(0,5):x;if(o.h.indexOf(st)>-1)s+=3;if(o.d.indexOf(st)>-1)s+=1});return[s,o.t]}).filter(function(x){return x[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,5);
  out.innerHTML=sc.length?'<p><b>'+T('aiBest')+'</b></p><div class="sg">'+sc.map(function(x){return link(x[1][0])}).join('')+'</div>':'<p>'+T('aiNone')+'</p>'};
 return q}
window.__buildAssistant=buildAssistant;
var ai=doc.getElementById('ai');if(ai){ai.className='aibox';buildAssistant(ai)}
})();
