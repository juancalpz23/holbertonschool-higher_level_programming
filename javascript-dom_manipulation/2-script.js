document.addEventListener("DOMContentLoaded", () => {
  const redH = document.querySelector('#red_header');
  redH.addEventListener('click', () => {
   document.querySelector('header').classList.add('red');
 });
});
