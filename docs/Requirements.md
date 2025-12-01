# Construction Website – Requirements

## 1. Project Summary

The goal is to build a simple informational website for a fictional construction company, **ABC Construction Ltd.**  
The site will present services, company information, and a way for customers to request a quote.

The project is mainly to demonstrate software engineering practices: documentation, design, implementation, testing, and use of Git/GitHub.

---

## 2. Stakeholders

- **Client / Business Owner** – wants an online presence to attract customers.
- **Site Visitors (Customers)** – want to quickly see services, previous work, and contact details.
- **Development Team**
  - Castro Fokou
  - Rupesh R.

---

## 3. Functional Requirements

### a. Home Page
- The system shall display a home page with:
  - Company name and logo (text logo).
  - Short introduction of the company.
  - Navigation links to Services, About, and Contact pages.

### b. Services Page
- The system shall display a list of construction services, including at least:
  - Residential construction
  - Renovations
  - Roofing
  - Concrete/foundation work
  - Painting
- Each service shall include a short description.

### c. About Page
- The system shall display:
  - A short company history.
  - A paragraph about the team and values.
  - Basic “Why choose us?” bullet points.

### d. Contact Page / Quote Form
- The system shall provide a contact form with fields:
  - Name
  - Email
  - Type of project or service
  - Free-text message
- On submit, the form shall show a confirmation message in the browser (no real email required).

### e. Navigation
- The system shall provide a navigation bar on every page with links to:
  - Home
  - Services
  - About
  - Contact

---

## 4. Non-Functional Requirements

### a. Usability
- Pages should be easy to read using simple visual hierarchy (titles, subtitles, lists).
- Navigation menu appears consistently on all pages.

### b. Performance
- All pages should load quickly when opened locally (no large media files).

### c. Compatibility
- Site must run in modern browsers (Chrome, Edge, Firefox) without extra plugins.
- The project must open as static HTML files (no server required).

### d. Maintainability
- HTML, CSS, and JS should be separated:
  - Structure in `.html`
  - Styles in `styles.css`
  - Behaviour in `script.js`
- Code should be commented where appropriate.

### e. Version Control
- All work must be tracked in Git.
- Separate branches for each developer (`castro-dev`, `rupesh-dev`).
- Merge into `main` for final version.

---

## 5. Constraints

- No backend, database, or authentication.
- Entire project must be stored and submitted via GitHub.
- Must use only technologies taught in class (HTML/CSS/JS + simple Python for test example).

---

## 6. Definition of Done

The project is considered complete when:

1. All four pages (Home, Services, About, Contact) are implemented and styled.
2. The contact form displays a confirmation message when submitted.
3. Documentation in `docs/` is completed.
4. At least one test is implemented in `tests/`.
5. GitHub repository shows:
   - Multiple branches
   - Commits from both Castro and Rupesh
   - Final code in `main` branch.
