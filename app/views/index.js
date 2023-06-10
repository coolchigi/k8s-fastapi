getItems()


function getItems() {
    const apiUrl = 'http://localhost:8080/items/';
    fetch(apiUrl)
        .then(res => res.json())
          .then(res => {
            document.getElementById("items-list").innerHTML = res;
      });
        
  }