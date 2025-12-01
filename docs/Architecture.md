# Architecture

---

## 1. Overview

The Construction Website project uses a **simple static web architecture**:

- No backend server or database.
- All content is served as static HTML, CSS, and JavaScript.
- A small Python script is used only to demonstrate basic testing.

This architecture is sufficient for the course project, easy to run, and ideal for GitHub Pages hosting.

---

## 2. Logical Components

### **Presentation Layer (src/)**
Contains all web pages and UI assets:
- `index.html` — homepage  
- `services.html` — list of services  
- `about.html` — company background  
- `contact.html` — contact form  
- `styles.css` — main stylesheet  
- `script.js` — simple client-side interactions  

### **Documentation Layer (docs/)**
Includes all project documentation:
- Requirements  
- Personas  
- User Stories  
- Architecture  
- Wireframes  
- Group Assignment document  

### **Testing Layer (tests/)**
- `test_getmax.py` — small example Python test demonstrating quality assurance

---

## 3. Simple Diagram

Browser (User Interface)
|
v
src/ (Website Pages)
index.html
services.html
about.html
contact.html
styles.css
script.js

    |
    v


docs/ (Project Documentation)
Requirements
Personas
User Stories
Architecture
Wireframes
Group Assignment

    |
    v


tests/ (Testing)
test_getmax.py


---

## 4. Navigation Flow

- User lands on **`index.html`**.
- From the navigation bar, the user can navigate to:
  - **Services** → `services.html`
  - **About** → `about.html`
  - **Contact** → `contact.html`
- On every page:
  - Clicking the **logo/title** returns the user to **Home** (`index.html`).

---

## 5. Rationale

- Static architecture fully satisfies course project requirements.
- Easy to run locally or host on **GitHub Pages** without a backend.
- Simple structure makes it easy for instructors and developers to understand.
- Separation of concerns (docs, src, tests) improves readability and maintainability.

---
