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
              <textarea name="note" placeholder="Note(ex Contact steve to ask if he wants to come)"></textarea>
              <input type="submit" name="add-calendar-event" value="Save">
           </form>
       </div>
 `;

const composeForm = `
       <div class="compose-message">
          <span><a href="">[X] CLOSE</a></span>
          <form method="POST">
              <input type="text" name="name" placeholder="To">
              <input type="text" name="subject" placeholder="Subject">
              <textarea name="message" placeholder="Message"></textarea>
              <input type="submit" name="send-message" value="Send">
           </form>
       </div>
 `;
const editContactForm = ``;
const videoContentWindow = ``;

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

function loadPanel(panelForm) {
  /* load side panel with the appropriate form (video, storage item)*/
  const sidePanel = `<div class="side-panel"></div>`;
  const sidePanelTemplate = loadTemplate(sidePanel);
  sidePanelTemplate.appendChild(panelForm);
  const overlay = loadOverlayWindow();
  overlay.appendChild(sidePanelTemplate);
  document.querySelector("body").appendChild(overlay);
}

function composeWindow() {
  const composeButton = document.querySelector("#compose");
  composeButton.addEventListener("click", (e) => {
    e.preventDefault();
    //load panel with appropriate form
    loadPanel(loadTemplate(composeForm));
  });
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
      selectedMenuItem(document.querySelector("#open"), item.parentNode, menu);
      selectedMenuItem(
        document.querySelector("#download"),
        item.parentNode,
        menu,
      );
      selectedMenuItem(
        document.querySelector("#rename"),
        item.parentNode,
        menu,
      );
      selectedMenuItem(
        document.querySelector("#get-info"),
        item.parentNode,
        menu,
      );
      selectedMenuItem(
        document.querySelector("#delete"),
        item.parentNode,
        menu,
      );
    });
  });
}

function selectedMenuItem(menuItem, item, menu) {
  switch (menuItem.id) {
    case "open":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector("body").removeChild(menu);
        openItem(item);
      });
      break;
    case "download":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector("body").removeChild(menu);
        downloadItem(item);
      });
      break;
    case "rename":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector("body").removeChild(menu);
        renameItem(item);
      });
      break;
    case "get-info":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector("body").removeChild(menu);
        getItemInfo(item);
      });
      break;
    case "delete":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector("body").removeChild(menu);
        deleteItem(item);
      });
      break;
  }
}

// selectedMenuItem(document.querySelector(""));
// selectedMenuItem(document.querySelector(""));
// selectedMenuItem(document.querySelector(""));
// selectedMenuItem(document.querySelector(""));
// selectedMenuItem(document.querySelector(""));

function openItem(item) {}

function downloadItem(item) {}

function renameItem(item) {
  const itemName = item.firstChild.nextSibling;
  itemName.contentEditable = "true";
  itemName.addEventListener("blur", (e) => {
    localStorage.setItem("editedText", e.target.textContent);
  });
  const editedText = localStorage.getItem("editedText");
  if (editedText) {
    fetch("http://localhost:5555/storage/update", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document
          .querySelector('meta[name="csrf_token"]')
          .getAttribute("content"),
      },
      body: JSON.stringify({
        item: editedText,
      }),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log("Success", data);
      })
      .catch((error) => {
        console.error("Error", error);
      });
  }
}

function getItemInfo(item) {}

function deleteItem(item) {
  const confirmationResult = item.getAttribute("data-item");
  const confirmationMenu = `
     <div class="confirmation">
       <p>Are you sure you want to delete this?</p>
       <span><a href="/storage/delete/${confirmationResult}">OK</a></span>
     </div>
  `;
  const overlay = loadOverlayWindow();
  const confirmationTemplate = loadTemplate(confirmationMenu);
  overlay.appendChild(confirmationTemplate);
  document.querySelector("body").appendChild(overlay);
}

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

if (window.location.pathname == "/inbox") {
  composeWindow();
}

toggleSearchField();
highlightDate();
openContextMenu();
