function getCurrentDate() {
  const date = new Date()
  const day = date.getDate()
  return day;
}

function switchForm() {
  /* load Edit contact form  */
}

function loadPanel() {
  /* load side panel with the appropriate form (video, storage item)*/
}

function loadOverlayWindow() {
}

function startVideoCall() {

}

function endVideoCall() {

}

function removePanel() {

}

function highlightSearchField() {
  //add border bottom on magnify button click
}

function addCalendarEvent() {

}

function opendialogMenu() {

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
