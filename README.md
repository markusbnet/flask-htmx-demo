# ⚡️ Flask HTMX Demo

This repository provides a demo of how to use HTMX with Flask to create, delete and order items within a table. You can read the accompanying ![blog here](https://medium.com/@markus_bnet/flask-and-htmx-45e7b54b28bc).

3 examples can be found within the following folders:
- flask-htmx-create - create items and see them dynamically add to a table.
- flask-htmx-delete - delete items from a table using HTMX. Includes creating and deleting items.
- flask-htmx-order - ordering items within a table. Includes creating, deleting and ordering.


## 🎥 Demo

![htmx-demo](https://user-images.githubusercontent.com/13853122/129015765-befe3369-0296-48d6-8f7e-47e97934f4dd.gif)

  
## 🏗️ Installation

Pick an example and run the following from the root of the repository.

```bash
    python -m venv venv 
    source venv/bin/activate
    pip install -r requirements.txt
    cd {chosen example}
    python -m flask run
```
    
## 🧬 Tech Stack

[Flask](https://flask.palletsprojects.com/en/2.0.x/), [HTMX](https://htmx.org/), [Bootstrap](https://getbootstrap.com/) and my terrible design skills. 
