
document.addEventListener('DOMContentLoaded',function(){
 var u='belhaj.elmehdi.98',d='gmail.com',m=u+'@'+d;
 document.querySelectorAll('.js-mail').forEach(function(a){a.href='mailto:'+m;a.textContent=m;});
 var b=document.querySelector('.burger'),n=document.querySelector('nav');
 if(b){b.addEventListener('click',function(){n.classList.toggle('open')});
  n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('open')})});}
 var y=document.getElementById('yy'); if(y){y.textContent=new Date().getFullYear();}
});
