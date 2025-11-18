const calendarEvent = `
       <div class="calendar-event">
          <span><a href="">[X] CLOSE</a></span>
          <form method="POST">
              <h3>Add calendar event</h3>
              <input type="text" name="eventname" placeholder="Event name">
              <input type="text" name="category" placeholder="Category">
              <label for="eventdate">Event date</label>
              <input type="date" name="eventdate">
              <label for="eventtime">Event time</label>
              <input type="time" name="eventtime">
              <input type="submit" name="add-calendar-event" value="Save">
           </form>
       </div>
 `;

const sidePanel = ``;
const editContactForm = ``;
const videoContentWindow = ``;
const confirmationMenu = ``;
const storageMenu = `
    <div class="document-menu">
       <menu>
         <li><a href="" id="open">Open</a></li>
         <li><a href="" id="download">Download</a></li>
         <li><a href="" id="rename">Rename</a></li>
         <li><a href="" id="get-info">Get Info</a></li>
         <li><a href="" id="delete">Delete</a></li>
       </menu>
    </div>
`;

function toggleSearchField() {
  const searchButton = document.querySelector(".search-button");
  searchButton.addEventListener("click", (e) => {
    const searchField = document.querySelector("#search");
    const computedSearch = window.getComputedStyle(searchField);
    if (computedSearch.display == "none") {
      document.querySelector("#search").style.display = "block";
      document.querySelector("#search").style.borderBottom = "1px solid #ccc";
    } else {
      document.querySelector("#search").style.display = "none";
    }
  });
}

function getCurrentDate() {
  const date = new Date();
  const day = date.getDate();
  return day;
}

function switchForm() {
  /* load Edit contact form  */
}

function loadPanel() {
  /* load side panel with the appropriate form (video, storage item)*/
}

function loadOverlayWindow() {
  //create and append overlay to the DOM
  const overlayDiv = document.createElement("div");
  overlayDiv.setAttribute("id", "overlay");
  return overlayDiv;
}

function loadTemplate(htmlContent) {
  const template = document.createElement("template");
  template.innerHTML = htmlContent;
  return template.content;
}

function startVideoCall() {}

function endVideoCall() {}

function removePanel() {}

function highlightSearchField() {
  //add border bottom on magnify button click
}

function addCalendarEvent() {
  const addEventButton = document.querySelector("#add-event");
  addEventButton.addEventListener("click", (e) => {
    const overlay = loadOverlayWindow();
    const calendar = loadTemplate(calendarEvent);
    overlay.appendChild(calendar);
    document.querySelector("body").appendChild(overlay);
  });
}

function openContextMenu() {
  const documentItem = document.querySelectorAll(".kebab-menu");
  documentItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      const menuHTML = loadTemplate(storageMenu);
      const menu = menuHTML.childNodes[1];
      menu.style.left = e.clientX + "px";
      menu.style.top = e.clientY + "px";
      //item.parentNode.firstElementChild.innerHTML;
      document.querySelector("body").appendChild(menu);
      selectedMenuItem(document.querySelector("#open"), item.parentNode);
      selectedMenuItem(document.querySelector("#download"), item.parentNode);
      selectedMenuItem(document.querySelector("#rename"), item.parentNode);
      selectedMenuItem(document.querySelector("#get-info"), item.parentNode);
      selectedMenuItem(document.querySelector("#delete"), item.parentNode);
    });
  });
}

function selectedMenuItem(menuItem, item) {
  switch (menuItem.id) {
    case "open":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        openItem(item);
      });
      break;
    case "download":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        downloadItem(item);
      });
      break;
    case "rename":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        renameItem(item);
      });
      break;
    case "get-info":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        getItemInfo(item);
      });
      break;
    case "delete":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        deleteItem(item);
      });
      break;
  }
}

function openItem(item) {}

function downloadItem(item) {}

function renameItem(item) {}

function getItemInfo(item) {}

function deleteItem(item) {}

function highlightDate() {
  /*get the dates from the cells, iterate over them
    and find the cell that has the current date and
    highlight it
  */
  const cells = document.querySelectorAll("td");
  const day = getCurrentDate();
  cells.forEach(function (cell) {
    if (cell.innerHTML == day) {
      cell.innerHTML = "";
      const spanTag = document.createElement("span");
      spanTag.setAttribute("id", "selectedItem");
      spanTag.innerHTML = day;
      cell.appendChild(spanTag);
    }
  });
}

if (window.location.pathname == "/calendar") {
  addCalendarEvent();
}

toggleSearchField();
highlightDate();
openContextMenu();
