function getItems() {
    
    fetch('/items/')
    .then(response => response.text())
    .then(data => console.log(data));
        // .then(response => response.json())
        // .then(data => {
        //     console.log(data)
        //     const itemsList = document.getElementById("items-list");
        //     itemsList.innerHTML = "";

        //     if (data.length === 0) {
        //         itemsList.innerHTML = "No items found.";
        //         return;
        //     }

        //     data.forEach(item => {
        //         const listItem = document.createElement("li");
        //         listItem.textContent = `ID: ${item.id}, Name: ${item.name}, Price: ${item.price}`;
        //         itemsList.appendChild(listItem);
        //     });
        // })
        // .catch(error => {
        //     console.error("Error fetching items:", error);
        // });
}


getItems()