function create_cart(image_book, name, description, url) {
    let container = document.getElementsByClassName('cards')[0];
    
    let box = document.createElement('div');
    box.classList.add('box');
    
    let img = document.createElement('img');
    img.src = image_book;
    
    let content = document.createElement('div');
    content.classList.add('content');
    
    let text = document.createElement('h3');
    text.textContent = name;
    content.appendChild(text);
    
    text = document.createElement('p');
    text.textContent = description;
    content.appendChild(text);
    
    let info = document.createElement('info');
    info.classList.add('info');
    
    text = document.createElement('a');
    text.textContent = "Read More";
    text.href = url;
    info.appendChild(text);
    
    text = document.createElement('i');
    text.classList.add('fas');
    text.classList.add('fa-long-arrow-alt-right');
    info.appendChild(text);
    
    box.appendChild(img);
    box.appendChild(content);
    box.appendChild(info);
    container.appendChild(box);
}

function get_items(url) {
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token dc343d63f52d97cbd3cad91793eb4768f47b81a7',
        },
    })
    .then((response) => response.json())
    .then((data) => {
        for (let i = 0; i < data.length; i++) {
            console.log(data[i]);
            create_cart(data[i].image, data[i].name, data[i].description, url + data[i].id);
        }
    });
}

get_items("http://127.0.0.2:8000/api/books/");
