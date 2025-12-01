# Architecture

## 1. Overview

The Construction Website project uses a **simple static web architecture**:

- No backend server or database.
- All content is served as static HTML, CSS, and JavaScript.
- A small Python script is used only to demonstrate testing.

---

## 2. Logical Components

1. **Presentation Layer**
   - HTML pages:
     - `index.html`
     - `services.html`
     - `about.html`
     - `contact.html`
   - CSS styles: `styles.css`
   - Client-side behaviour: `script.js`

2. **Documentation Layer**
   - Requirements, personas, user stories, architecture, wireframes in `docs/`.

3. **Testing Layer**
   - `tests/test_getmax.py` – example unit test.

---

## 3. Simple Diagram

```text
+---------------------------+
|         Browser           |
|  (User Interface Layer)   |
+------------+--------------+
             |
             v
   Static Web Files (src/)
   - index.html
   - services.html
   - about.html
   - contact.html
   - styles.css
   - script.js

             |
             v
   Documentation (docs/)
   - Requirements, Personas,
     User Stories, Architecture,
     Wireframes, Group Assignment

             |
             v
   Testing (tests/)
   - test_getmax.py
