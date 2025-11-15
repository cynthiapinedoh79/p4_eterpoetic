# ✅ HOW TO USE THIS TEMPLATE

This README is structured for a **Django project with multiple apps**


# 📚 *[Project Name]* — Django Web Application
# 📚 *EterPoetic* — Django Web Application
EterPoetic is an interactive and content-rich web application for lovers of poetry and creative writing. Designed for readers and writers, it provides a platform to explore curated poem collections and insightful blog posts. It combines a personal reading experience with community engagement, allowing registered users to favorite poems, comment on articles, and connect with the team.

Key Features:
- `poetry`: Manages all poem and collection content; handles user favoriting logic.
- `blog`: Manages all blog posts and user comments.
- `about`: Displays team information and provides a "collaborator" application form.
- `accounts`: Manages user registration, login, and logout.

## 🧩 Badges (Optional)
![GitHub repo size](https://img.shields.io/github/repo-size/cynthiapinedoh79/p4_eterpoetic)
![GitHub last commit](https://img.shields.io/github/last-commit/cynthiapinedoh79/p4_eterpoetic)
[![View Demo](https://img.shields.io/badge/View-Demo-brightgreen)](https://eterpoetic-62a49da213d8.herokuapp.com/)

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![Heroku](https://img.shields.io/badge/Heroku-Deploy-purple)

---

# 📋 Table of Contents
- [🧾 Project Overview](#🧾-project-overview)
- [🔗 Live Demo](#🔗-live-demo)
- [📱 Am I Responsive? - Demo](#📱-am-i-responsive---demo)
- [🖼️ Screenshots](#🖼️-screenshots)
- [🎯 UX](#🎯-ux)
- [🧑‍💼 User Stories](#🧑‍💼-user-stories)
- [🎨 Design Choices](#🎨-design-choices)
- [📐 Five Planes UXD](#📐-five-planes-uxd)
  - [📌 Strategy](#📌-strategy)
  - [📐 Scope](#📐-scope)
  - [🏗️ Structure](#🏗️-structure)
  - [🦴 Skeleton](#🦴-skeleton)
  - [🎨 Surface](#🎨-surface)
- [✨ Features](#✨-features)
  - [🚀 Existing Features](#🚀-existing-features)
  - [🧰 Frameworks, Libraries & Programs Used](#🧰-frameworks-libraries--programs-used)
- [🏛️ Architecture (Django MVT)](#🏛️-architecture-django-mvt)
  - [🗃️ Data Model (ERD)](#🗃️-data-model-erd)
  - [🧱 App Responsibilities](#🧱-app-responsibilities-app1-app2-app3)
  - [🧭 URL Map & Navigation](#🧭-url-map--navigation)
  - [🧩 CRUD Map](#🧩-crud-map)
  - [🧪 Forms & Validation](#🧪-forms--validation)
  - [🔌 API Endpoints (Optional)](#🔌-api-endpoints-optional)
- [🛠️ Technologies & Tools](#🛠️-technologies--tools)
  - [🧑‍💻 Languages Used](#🧑‍💻-languages-used)
  - [🧰 Frameworks, Libraries & Programs Used](#🧰-frameworks-libraries--programs-used)
- [📦 Project Setup](#📦-project-setup)
- [⚙️ Environment Variables](#⚙️-environment-variables)
- [🗂️ Project Structure](#🗂️-project-structure)
- [🔐 Admin & Fixtures](#🔐-admin--fixtures)
- [✅ Testing & Validation](#✅-testing--validation)
  - [✅ Browser & Device Testing](#✅-browser--device-testing)
  - [✅ Validator Testing](#✅-validator-testing)
  - [✅ Accessibility Testing](#✅-accessibility-testing)
  - [✅ Console in Google Chrome DevTools-"Inspect" Testing](#✅-console-in-google-chrome-devtools-inspect-testing)
  - [🧑‍💻 Testing User Stories – User Experience (UX) Evaluation](#🧑‍💻-testing-user-stories--user-experience-ux-evaluation)
- [🐞 Bugs](#🐞-bugs)
- [📥 Deployment](#📥-deployment)
- [🤝 Contribution Guidelines](#🤝-contribution-guidelines)
- [🙏 Credits & Acknowledgements](#🙏-credits--acknowledgements)

---

## 🧾 Project Overview
*(Write 4–6 lines summarizing purpose, audience, and primary benefit.)*

## 🧾 Project Overview
EterPoetic is an interactive and content-rich web application for lovers of poetry and creative writing. Designed for readers and writers, it provides a platform to explore curated poem collections and insightful blog posts. It combines a personal reading experience with community engagement, allowing registered users to favorite poems, comment on articles, and connect with the team.

**Core Technologies**

1.  **Django (Python):** Robust backend framework for the entire application structure.
2.  **PostgreSQL (ElephantSQL):** Scalable relational database management system.
3.  **HTML / CSS / JS:** Foundational languages for structure, styling, and interactivity.
4.  **Bootstrap:** Frontend framework for responsive design.
5.  **Heroku:** Cloud platform used for deployment and hosting.
6.  **Cloudinary:** Handles static and media file storage for efficiency.
7.  **Balsamiq:** Design tool used for wireframing and planning the site layout.

---

## 🔗 Live Demo
**Live Site:** https://eterpoetic-62a49da213d8.herokuapp.com/ 
**Admin Panel:** https://eterpoetic-62a49da213d8.herokuapp.com/admin

---

## 📱 Am I Responsive? - Demo
All pages were designed with **Responsive Design** to provide a consistent experience across various screen sizes and devices.

### Home (Poetry)
![Responsive devices -Home](static/images/readme/amIR/amIR-home.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-home1.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-home2.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-home3.png)


### MyFavorites (Poetry)
User would be able to see favorites (Featured) poems when login

![Responsive devices -Home](static/images/readme/amIR/amIR-myFavorites.png)


### Blog (Posts)

![Responsive devices -Home](static/images/readme/amIR/amIR-blog.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-blog1.png)


### About (Owner and Collaborators, Form)

![Responsive devices -Home](static/images/readme/amIR/amIR-about.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-about1.png)

![Responsive devices -Home](static/images/readme/amIR/amIR-about2.png)


### Register (Sign Up)

![Responsive devices -Home](static/images/readme/amIR/amIR-register.png)


### Login (Sign In)

![Responsive devices -Home](static/images/readme/amIR/amIR-login.png)

---

## 🖼️ Screenshots

* Additional screenshots to show

### My Favorites

![Responsive devices -Home](static/images/readme/screenshots/s-myFavorites.png)

![Responsive devices -Home](static/images/readme/screenshots/s-myFavorites1.png)

![Responsive devices -Home](static/images/readme/screenshots/s-myFavorites2.png)

---

### Login (Sign In)

### with Facebook

![Responsive devices -Home](static/images/readme/screenshots/s-login.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login1.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login1a.png)


### with Google

![Responsive devices -Home](static/images/readme/screenshots/s-login2.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login3.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login4.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login5.png)


### If forget password

![Responsive devices -Home](static/images/readme/screenshots/s-login6.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login7.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login8.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login9.png)

![Responsive devices -Home](static/images/readme/screenshots/s-login10.png)


---

### Logout

![Responsive devices -Home](static/images/readme/screenshots/s-logout.png)

![Responsive devices -Home](static/images/readme/screenshots/s-logout1.png)

![Responsive devices -Home](static/images/readme/screenshots/s-logout2.png)


---

## 🎯 UX
### Target Audience:
**Readers, emerging writers, and poetry enthusiasts** seeking curated content, insightful blog posts, and an engaging community centered around creative writing.

### Core UX Goals:
**UX Goals:** Readability, engagement, responsiveness, accessibility

1.  **Prioritize Readability:** Build trust and credibility through clean design and clear typography, ensuring an enjoyable reading experience across all content.
2.  **Encourage Engagement:** Offer simple, clear methods for user interaction (favoriting, commenting, applying to collaborate).
3.  **Ensure Accessibility:** Provide a consistent, intuitive structure and responsive design for users on all devices.
4.  **Simplify Navigation:** Allow users to quickly find poems and articles by collection, author, or search query.
5.  **Foster Growth:** Create opportunities for the platform to attract new collaborators and grow its content library.

### Main Site Goals:

-   Provide a curated, accessible library of poems and collections for easy exploration.
-   Offer a streamlined, personal experience for registered users (favoriting, profile management).
-   Attract new content creators and collaborators via a clear application path (the `about` app form).
-   Promote community engagement by providing a clean commenting system for blog posts.
-   (Coming Soon) Enhance search and filtering capabilities (e.g., filtering by language, mood, or length).
-   (Coming Soon) Implement a user dashboard for managing their profile and contributions.

---

## 🧑‍💼 User Stories

### Core User Stories

| User Story | GitHub Issue | Priority | Status |
|---|---|---|---|
| As a reader, I can **access the poetry library** so that I can browse and select poems to read. | **[p4_eterpoetic#1](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/1)** | High | Done |
| As a customer I can **mark my favorites items** so that i can easily identify them. As a logged-in customer, I can **easily mark and manage poems as my favorites** so that I can quickly find and revisit them later for potential purchase or inspiration. | **[p4_eterpoetic#7](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/7)** | High | Done |
| As a user I can **register, login in and log out** so that i can access to leave comments and participate. As a new or returning visitor, I can **securely register an account and manage my login session** so that I can fully participate by leaving comments and accessing members-only features. | **[p4_eterpoetic#5](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/5)** | High | Done |
| As a Site Owner, I can **receive, review and store collaboration request in the database**, so that I can efficiently manage, review and respond to new opportunities. | **[django-blog#13](https://github.com/cynthiapinedoh79/django-blog/issues/13)** | High | Done |
| As a Site Admin I can **create or update the About page content** so that it is available on the site. | **[django-blog#11](https://github.com/cynthiapinedoh79/django-blog/issues/11)** | High | Done |
| As a Site User I can **click the About link** so that I can read about the site. | **[django-blog#10](https://github.com/cynthiapinedoh79/django-blog/issues/10)** | High | Done |
| As a Site Admin I can **create, read, update and delete posts** so that I can manage my blog content. | **[django-blog#7](https://github.com/cynthiapinedoh79/django-blog/issues/7)** | High | Done |
| As a a Site User I can **click on a post** so that I can read the full text. | **[django-blog#4](https://github.com/cynthiapinedoh79/django-blog/issues/4)** | High | Done |
| As a Site User I can **leave comments on a post** so that I can be involved in the conversation. | **[django-blog#5](https://github.com/cynthiapinedoh79/django-blog/issues/5)** | High | Done |
| As a Site Admin I can **create draft post** so that I can finish writing the content later. | **[django-blog#8](https://github.com/cynthiapinedoh79/django-blog/issues/8)** | High | Done |
| As a Site User / Admin I can **view comments on an individual post** so that I can read the conversation. | **[django-blog#3](https://github.com/cynthiapinedoh79/django-blog/issues/3)** | High | Done |
| As a Site Admin I can **approve or disapprove comments** so that I can filter out objectionable comments. | **[django-blog#9](https://github.com/cynthiapinedoh79/django-blog/issues/9)** | High | Done |
| As a Site User I can **modify or delete my comment on a post** so that I can be involved in the conversation. | **[django-blog#6](https://github.com/cynthiapinedoh79/django-blog/issues/6)** | High | Done |
| As a site user I can **view a paginated list of post** so that I can select which post I want to view. | **[django-blog#1](https://github.com/cynthiapinedoh79/django-blog/issues/1)** | High | Done |

### 🚀 Existing Features (Source: GitHub "Done" Column)

* **Paginated Blog Posts:** Users can view blog posts in a paginated list (Ref: **django-blog#1**).
* **Poetry Filtering:** Users can browse poetry using filtering tools (Ref: **p4_eterpoetic#1**).
* **Favorite Poem Toggle:** Registered users can add/remove poems from their personal favorites list (Ref: **p4_eterpoetic#37**).
* **Comment Moderation:** Administrators can approve comments to maintain community standards (Ref: **django-blog#9**).

### 🧑‍💻 Testing User Stories – User Experience (UX) Evaluation

All core user stories were tested using the defined **Acceptance Criteria (ACs)** set in the corresponding GitHub Issues.

For example, the **'View paginated list of posts'** feature (Ref: **django-blog#1**) passed the following criteria:

* **AC1:** Given more than one post in the database, these multiple posts are listed.
* **AC2:** When the user opens the main page a list of post is seen.
* **AC3:** Then the user sees all post titles with pagination to choose what to read.

### 🔮 Features Left to Implement (Source: GitHub "Backlog" / "Ready" Columns)
| User Story | GitHub Issue | Priority | Status |
|---|---|---|---|
| As a website visitor, I can easily switch the entire website interface and content between English and Spanish so that I can comfortably read and interact with the platform in my preferred language. | **[p4_eterpoetic#6](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/6)** | High | Done |
| As a customer (or user), I can easily order a custom-written poem so that I can receive a unique, personalized piece of poetry for a special occasion. | **[p4_eterpoetic#2](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/2)** | High | Done |
| As a satisfied customer, I can easily leave a public rating and review of the service so that I can share my experience and help future customers make a decision. | **[p4_eterpoetic#3](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/3)** | High | Done |

### Developer & UX Goals

**Developer Goal:**
As the sole developer of this website, my mission is to provide an enjoyable and user-friendly experience by delivering clear, curated, and diverse written content, fostering a sense of community around poetry and creative writing.

**User Experience Objectives:**
From the user’s perspective, I’ve built this site with the following priorities in mind:

* I want to navigate this website quickly and easily.
* I should be able to use a mouse, keyboard, or touchscreen effortlessly.
* I value high-quality, well-organized **content** that I can consume in just a few minutes.
* As a user, I need a simple and clear way to get in touch with you.

---

### User Goals by Frequency

#### First-Time Visitor Goals

1.  To quickly understand the main purpose of the site (poetry/blog) and discover the range of content offered.
2.  To navigate the site effortlessly and find content that captures my interest.
3.  To be visually engaged by an attractive and inviting website that encourages me to explore further.
4.  To easily locate **contact information or the collaboration form** to build trust.

#### Returning Visitor Goals

1.  To easily discover new poems and recent blog posts since my last visit.
2.  To find my way to the **login/registration area quickly** to access personalized features.
3.  To easily find **support or collaboration paths** for questions and contribution.

#### Frequent User Goals

1.  To conveniently access and **manage my personal list of favorited poems**.
2.  To view the **latest comments and responses** on blog posts I have engaged with.
3.  To **search and filter content** effectively by author, collection, or language.

---

## 🎨 Design Choices
- Mobile-first responsive layout
- Clear typography hierarchy
- Consistent spacing and UI patterns
- Accessible markup and navigation

  ### Description        
  This website is designed for visitors and new customers to explore, learn, win rewards, and enjoy an engaging experience while navigating through different pages.

  ### Typography
  Inter, Roboto family font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Roboto is a clean font used frequently in programming, so it is both attractive and appropriate.

  ### Color Palette 
    - **Fonts:** Roboto, Inter – clean and modern  
    - **Colors:**  
      - Purple: trust and creativity  
      - Red/Orange: urgency and emphasis  
      - Muted tones: professionalism  
    - [Contrast checked with WebAIM](https://webaim.org/resources/contrastchecker/)

  ### Colour Psychology
    ![Colour Psicology](assets/images/readme/PsColor.png)
    ![Contrast checked with WebAIM](assets/images/readme/PsColor1.png)

  ### Imagery  
    Clear and attractive images support the theme and maintain strong contrast with text for optimal readability.
  - Financial and office-themed backgrounds  
  - High contrast text overlays for readability  
---
### 1. Home: index.html
        
  - Background: 
  A blurred photo of financial charts and a blue pen (soft blue, red, beige tones)
---

## 📐 Five Planes UXD

### 📌 Strategy
Define goals and audience needs.

Our objective is to create a website that is both professional and functional. Our focus is on design that is both intuitive and creative.

![Strategy](assets/images/readme/fivePlanes/strategy.png)
### 📐 Scope
The site is designed for two main user groups:
1.	Visitors, who can enjoy interactive games, helpful tips, new information, and practical advice.
2.	Potential new customers, who can explore special offers like a bookkeeping bonus award, contact us easily, or quickly access the Form 1040 submission link.

![Scope pg1](assets/images/readme/fivePlanes/scope1.png)

![Scope pg2](assets/images/readme/fivePlanes/scope2.png)
### 🏗️ Structure
The website is designed with HTML5, CSS3 and JS.

**Website Pages/Apps:**
1. **_Home:_** Description of Home, features
1. **_App1:_** Description of App1, features
2. **_App2:_** Description of App2, features
3. **_App3:_** Description of App3, features

![Structure](assets/images/readme/fivePlanes/structure.png)

### 🦴 Skeleton
Wireframes and layout structure.
The website is designed to be clear and simple. And the site has a simple tree structure with hierarchical flows from top to bottom.

**Wireframe**
The wireframe is designed using Balsamiq software 
[Balsamic](https://balsamiq.cloud/ss26tqg/p4441iq/rD01A)

#### Home
![Home](assets/images/readme/Bals/Bals-Home.png)

### 🎨 Surface
Final aesthetic layers (colors, components, imagery).
To create a pleasing and understandable view, I opt for natural colors such as earth, green, and a range of tones that complement and contrast each other.

---

## ✨ Features
(Add a brief, high-level intro to your project's features here...)

### 🚀 Existing Features
* **Feature 1:** Describe what it does.
* **Feature 2:** Describe what it does.

*(Note: Your ToC also lists "Features Left to Implement," so you'd add that here as well)*
### 🔮 Features Left to Implement
* [Feature 3]
* [Feature 4]
* Dashboard analytics
* REST API support
* Role-based permissions
* Background jobs / Scheduled tasks

---

## 🏛️ Architecture (Django MVT)

### 🧱 App Responsibilities (app1, app2, app3)

| App | Purpose |
|---|---|
| `app1` | Core business logic + main models |
| `app2` | Authentication + Profile Management |
| `app3` | Additional / domain-specific features |

### 🧭 URL Map & Navigation

| Path | View | Public/Private |
|---|---|---|
| `/` | HomeView | Public |
| `/app1/` | List/Detail Views | Public |
| `/dashboard/` | DashboardView | Private |

### 🧩 CRUD Map

| Model | Create | Read | Update | Delete |
|---|---|---|---|---|
| ExampleModel | ✅ | ✅ | ✅ | ✅ |

### 🗃️ Data Model (ERD)
(Insert your ERD image or description here)

### 🧪 Forms & Validation
(Describe your main Django forms, e.g., RegistrationForm, PostForm)

### 🔌 API Endpoints (Optional)
(List any API endpoints you created, e.g., `/api/posts/`)

---

## 🛠️ Technologies & Tools

### 🧑‍💻 Languages Used

1. HTML5 - Used to build the basic structure of the website.
2. CSS3 - Styles the front-end to create a visually appealing design and enhance user experience.
3. JS -  Adds interactivity to the website, making the experience more dynamic and engaging for users.
4. Python - 

### 🧰 Frameworks, Libraries & Programs Used
* **Backend:** Django, Gunicorn
* **Database:** PostgreSQL
* **Frontend:** Bootstrap
* **Deployment:** Heroku, Cloudinary
* **Design:** Balsamiq, Coolors
* **Version Control:** Git

---

*Webaim
[Tested contrast](https://webaim.org/resources/contrastchecker/)
*Coolors
[Tested color](https://coolors.co/contrast-checker/33008a-f8f8ff)

_Main color palette_
![Main color Palette](assets/images/readme/PalletColors.png)
---

## 📦 Project Setup

To get a local copy up and running, follow these simple steps.

```bash
# Clone the repository
git clone <REPO_URL>

# Navigate into the project directory
cd <project-folder>

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the server
python manage.py runserver

⚙️ Environment Variables
Create a .env file:

SECRET_KEY=your_local_insecure_key
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
ALLOWED_HOSTS=localhost,127.0.0.1

🗂️ Project Structure

A brief overview of the project's directory structure.

project_root/
│ manage.py
│ requirements.txt
│ Procfile
│ runtime.txt
│ .env
│
├── app1/         # Replace with your app's name
├── app2/         # Replace with your app's name
├── app3/         # Replace with your app's name
├── static/       # Project-wide static files
└── project_name/ # Core project settings
    │ settings.py
    │ urls.py
    │ wsgi.py
    └ asgi.py

🔐 Admin & Fixtures

# Create an admin superuser
python manage.py createsuperuser

# Load seed data (optional)
python manage.py loaddata fixtures/seed.json

---
## ✅ Testing & Validation
---
python manage.py test

---
Area	Tool	Goal
HTML	W3C Validator	No errors
CSS	W3C CSS Validator	Clean structure
Accessibility	Manual + Lighthouse	WCAG compliance
Responsiveness	DevTools	Works across devices

## ✅ Browser & Device Testing
(Describe which browsers you tested...)

## ✅ Validator Testing
(Detail results from W3C...)

## ✅ Accessibility Testing
(Detail results from Lighthouse/Wave...)

## ✅ Console in Google Chrome DevTools-"Inspect" Testing
(Confirm no console errors...)

### 🧑‍💻 Testing User Stories – User Experience (UX) Evaluation
(Go through each user story and confirm it works as expected)

---
### 🐞 Bugs
Solved

[Describe bug and solution]

Known Issues

[Describe known issues]

---
## 📥 Deployment (Heroku)

web: gunicorn project_name.wsgi

________________________________________________
The app uses DATABASE_URL and CLOUDINARY_URL from Heroku's config vars.

---

### 2. Duplicate Section

You have **"🔮 Features Left to Implement"** listed twice in your Table of Contents and twice as a heading in the document.

* **Solution:** Delete the first instance from the Table of Contents (the one after `[🐞 Bugs]`) and delete the second instance of the section (the one after `[📥 Deployment]`).

---

### 3. Minor Typos & Fixes

* **Extraneous Text:** At the very bottom of your file, you have text that looks like a note *to you*.
    * **Fix:** Delete this entire block from your README:
        ```
        ### ✅ Yes — This is now **correct and production-ready.**
        ...
        app3 =
        ```

* **Typo 1:** In `🎨 Design Choices` > `Colour Psychology`
    * **Fix:** Change `![Colour Psicology]` to `![Colour Psychology]`.

* **Typo 2:** In `🦴 Skeleton` > `Wireframe`
    * **Fix:** Change `[Balsamic]` to `[Balsamiq]`.

* **Hard-Coded Badges:** In the `🧩 Badges` section, your language badges have percentages (e.g., `HTML5-27.1%`). These are likely from a sample project.
    * **Suggestion:** I recommend removing the percentages, as they won't be accurate for *your* project.
    * **Example Fix:**
        ```markdown
        ![HTML](https://img.shields.io/badge/HTML5-27.1%25-%23E34F26?style=flat&logo=html5&logoColor=white)

        ![HTML](https://img.shields.io/badge/HTML5-%23E34F26?style=flat&logo=html5&logoColor=white)
        ```

This is a fantastic, professional template. Once you make these fixes, it will be perfect!


---



## 🔮 Features Left to Implement

Dashboard analytics

REST API support

Role-based permissions

Background jobs / Scheduled tasks
---
## 🤝 Contribution Guidelines

Use branches: feat/, fix/, docs/

PRs must include passing tests and clean linting
---
## 🙏 Credits & Acknowledgements

Code Institute learning materials

Django & Heroku documentation

Mentor & Peer feedback

---

### ✅ Yes — This is now **correct and production-ready.**

Next step:  
Tell me your **real app names** so I replace `app1`, `app2`, `app3` automatically:

app1 =
app2 =
app3 =
