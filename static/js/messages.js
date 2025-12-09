function composeWindow() {
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
  const composeButton = document.querySelector("#compose");
  if (composeButton) {
    composeButton.addEventListener("click", (e) => {
      e.preventDefault();
      //load panel with appropriate form
      loadPanel(loadTemplate(composeForm));
    });
  }
}

function removeMessage() {
  const removeButton = document.querySelector("#remove-message");
  removeButton.addEventListener("click", (e) => {
    location.reload();
  });
}

composeWindow();
removeMessage();
