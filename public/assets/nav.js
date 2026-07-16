document.addEventListener('DOMContentLoaded',function(){
  var t=document.getElementById('navToggle'), m=document.getElementById('navMenu');
  if(t&&m){ t.addEventListener('click',function(){ m.classList.toggle('open'); });
    m.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ m.classList.remove('open'); }); }); }
});