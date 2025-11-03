


function getCurrentDate() {
  const date = new Date()
  const day = date.getDate()
  return day;
}


function highlightDate() {
  /*get the dates from the cells, iterate over them
    and find the cell that has the current date and
    highlight it
  */
  const cells = document.querySelectorAll('td');
  const day = getCurrentDate();
  cells.forEach(function(cell) {
    if(cell.innerHTML == day){
        cell.innerHTML = '';
        const spanTag = document.createElement('span');
        spanTag.setAttribute('id', 'selectedItem');
        spanTag.innerHTML = day
        cell.appendChild(spanTag);
    }
  })
}

highlightDate();
