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

const editContactForm = ``;
const videoContentWindow = ``;

const storageMenu = `
    <div class="document-menu">
       <menu>
         <li><a href="" id="open">Open</a></li>
         <li><a href="" id="download">Download</a></li>
         <li><a href="" id="rename">Rename</a></li>
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
  const menuHTML = loadTemplate(storageMenu);
  const menu = menuHTML.childNodes[1];
  documentItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      menu.style.left = e.clientX + "px";
      menu.style.top = e.clientY + "px";
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
        if (menu) document.querySelector("body").removeChild(menu);
        openItem(item);
      });
      break;
    case "download":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        if (menu) document.querySelector("body").removeChild(menu);
        downloadItem(item);
      });
      break;
    case "rename":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        if (menu) document.querySelector("body").removeChild(menu);
        renameItem(item);
      });
      break;
    case "delete":
      menuItem.addEventListener("click", (e) => {
        e.preventDefault();
        if (menu) document.querySelector("body").removeChild(menu);
        deleteItem(item);
      });
      break;
  }
}

function downloadItem(item) {}

function renameItem(item) {
  const itemName = item.firstChild.nextSibling;
  itemName.contentEditable = "true";
  itemName.addEventListener("blur", (e) => {
    //e.preventDefault();
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

function openItem(items) {
  const itemName = items.firstChild.nextSibling;
  const overlay = loadOverlayWindow();
  const itemDetails = `
    <div class="item-details">
       <span><a href="">[X] close</a></span>
       <h3>Item details</h3>
    </div>
    `;
  const itemInfoPanel = loadTemplate(itemDetails);
  items.childNodes.forEach((item, i) => {
    if (i % 2 !== 0 && i !== 7) {
      const itemInfo = itemInfoPanel.childNodes[1];
      itemInfo.innerHTML += `<p>${item.textContent}</p>`;
      if (item.textContent == "Audio") {
        itemInfo.innerHTML += `
               <audio controls>
                  <source src="${item.textContent}" type="audio/mp3">
              </audio>
        `;
      }
      if (item.textContent == "Video") {
        itemInfo.innerHTML += `
               <video width="320" height="240" controls>
                  <source src="${item.textContent}" type="video/mp4">
              </video>
        `;
      }
    }
  });
  loadPanel(itemInfoPanel);
}

function sortItems() {
  //get all the document items and sort them based on the
  //selected drop down menu option
  const filterItem = document.querySelector("select[name='document-filter']");
  const documentTypes = document.querySelectorAll(".content-type");
  filterItem.addEventListener("change", (e) => {
    let resultContent = "";
    document.querySelector(".content").innerHTML = "";
    documentTypes.forEach((documentType, documentItem) => {
      if (e.currentTarget.value == "All") {
        resultContent += `
            <ul><li>${documentType.parentNode.innerHTML}</li></ul>
        `;
      }
      if (e.currentTarget.value == documentType.textContent) {
        resultContent += `
            <ul><li>${documentType.parentNode.innerHTML}</li></ul>
        `;
      }
    });
    document.querySelector(".content").innerHTML = resultContent;
    openContextMenu();
  });
}

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

function profileMenu() {
  const miniMenu = `
      <div class="mini-profile-menu">
        <span><a href="/signout">Sign out</a></span>
      </div>
  `;
  const profileImage = document.querySelector("#profile-photo");
  const menuTemplate = loadTemplate(miniMenu);
  const profileMenu = menuTemplate.childNodes[1];
  profileImage.addEventListener("click", (e) => {
    profileMenu.style.left = e.clientX + "px";
    profileMenu.style.top = e.clientY + "px";
    document.querySelector("body").appendChild(profileMenu);
  });
  profileMenu.addEventListener("mousemove", (e) => {
    e.preventDefault();
    setTimeout(() => {
      document.querySelector("body").removeChild(profileMenu);
    }, 1000);
  });
}

if (window.location.pathname == "/calendar") {
  addCalendarEvent();
}

if (window.location.pathname == "/storage") {
  sortItems();
  openContextMenu();
}

toggleSearchField();
highlightDate();
profileMenu();
