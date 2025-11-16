# ✅ HOW TO USE THIS TEMPLATE

This README is structured for a **Django project with multiple apps**

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

---

### MyFavorites (Poetry)
User would be able to see favorites (Featured) poems when login

![Responsive devices -My Favorites](static/images/readme/amIR/amIR-myFavorites.png)

---

### Blog (Posts)

![Responsive devices -Blog](static/images/readme/amIR/amIR-blog.png)

![Responsive devices -Blog](static/images/readme/amIR/amIR-blog1.png)

---

### About (Owner and Collaborators, Form)

![Responsive devices -About](static/images/readme/amIR/amIR-about.png)

![Responsive devices -About](static/images/readme/amIR/amIR-about1.png)

![Responsive devices -About](static/images/readme/amIR/amIR-about2.png)

---

### Register (Sign Up)

![Responsive devices -Register](static/images/readme/amIR/amIR-register.png)

---

### Login (Sign In)

![Responsive devices -Login](static/images/readme/amIR/amIR-login.png)

---

## 🖼️ Screenshots

 Additional screenshots to show

### My Favorites

![Responsive devices -My Favorites](static/images/readme/screenshots/s-myFavorites.png)

![Responsive devices -My Favorites](static/images/readme/screenshots/s-myFavorites1.png)

![Responsive devices -My Favorites](static/images/readme/screenshots/s-myFavorites2.png)

---

### Login (Sign In)

### with Facebook

![Responsive devices -Login Fb](static/images/readme/screenshots/s-login.png)

![Responsive devices -Login Fb](static/images/readme/screenshots/s-login1.png)

![Responsive devices -Login Fb](static/images/readme/screenshots/s-login1a.png)

---

### with Google

![Responsive devices -Login Google](static/images/readme/screenshots/s-login2.png)

![Responsive devices -Login Google](static/images/readme/screenshots/s-login3.png)

![Responsive devices -Login Google](static/images/readme/screenshots/s-login4.png)

![Responsive devices -Login Google](static/images/readme/screenshots/s-login5.png)

---

### If forget password

![Responsive devices -Login Password](static/images/readme/screenshots/s-login6.png)

![Responsive devices -Login Password](static/images/readme/screenshots/s-login7.png)

![Responsive devices -Login Password](static/images/readme/screenshots/s-login8.png)

![Responsive devices -Login Password](static/images/readme/screenshots/s-login9.png)

![Responsive devices -Login Password](static/images/readme/screenshots/s-login10.png)

---

### Logout

![Responsive devices -Logout](static/images/readme/screenshots/s-logout.png)

![Responsive devices -Logout](static/images/readme/screenshots/s-logout1.png)

![Responsive devices -Logout](static/images/readme/screenshots/s-logout2.png)

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
| As a reader, I can **access the poetry library** so that I can browse and select poems to read. | **[p4_eterpoetic#1](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/1)** | Could-Have | Done |
| As a customer I can **mark my favorites items** so that i can easily identify them. As a logged-in customer, I can **easily mark and manage poems as my favorites** so that I can quickly find and revisit them later for potential purchase or inspiration. | **[p4_eterpoetic#7](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/7)** | Won't-Have | Done |
| As a user I can **register, login in and log out** so that i can access to leave comments and participate. As a new or returning visitor, I can **securely register an account and manage my login session** so that I can fully participate by leaving comments and accessing members-only features. | **[p4_eterpoetic#5](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/5)** | Must-Have | Done |
| As a Site Owner, I can **receive, review and store collaboration request in the database**, so that I can efficiently manage, review and respond to new opportunities. | **[django-blog#13](https://github.com/cynthiapinedoh79/django-blog/issues/13)** | Could-Have | Done |
| As a Site Admin I can **create or update the About page content** so that it is available on the site. | **[django-blog#11](https://github.com/cynthiapinedoh79/django-blog/issues/11)** | High | Done |
| As a Site User I can **click the About link** so that I can read about the site. | **[django-blog#10](https://github.com/cynthiapinedoh79/django-blog/issues/10)** | Must-Have | Done |
| As a Site Admin I can **create, read, update and delete posts** so that I can manage my blog content. | **[django-blog#7](https://github.com/cynthiapinedoh79/django-blog/issues/7)** | Must-Have | Done |
| As a a Site User I can **click on a post** so that I can read the full text. | **[django-blog#4](https://github.com/cynthiapinedoh79/django-blog/issues/4)** | Must-Have | Done |
| As a Site User I can **leave comments on a post** so that I can be involved in the conversation. | **[django-blog#5](https://github.com/cynthiapinedoh79/django-blog/issues/5)** | Could-Have | Done |
| As a Site Admin I can **create draft post** so that I can finish writing the content later. | **[django-blog#8](https://github.com/cynthiapinedoh79/django-blog/issues/8)** | High | Done |
| As a Site User / Admin I can **view comments on an individual post** so that I can read the conversation. | **[django-blog#3](https://github.com/cynthiapinedoh79/django-blog/issues/3)** | Must-Have | Done |
| As a Site Admin I can **approve or disapprove comments** so that I can filter out objectionable comments. | **[django-blog#9](https://github.com/cynthiapinedoh79/django-blog/issues/9)** | Could-Have | Done |
| As a Site User I can **modify or delete my comment on a post** so that I can be involved in the conversation. | **[django-blog#6](https://github.com/cynthiapinedoh79/django-blog/issues/6)** | Could-Have | Done |
| As a site user I can **view a paginated list of post** so that I can select which post I want to view. | **[django-blog#1](https://github.com/cynthiapinedoh79/django-blog/issues/1)** | Must-Have | Done |
| As a website visitor, I can **easily switch the entire website interface and content between English and Spanish** so that I can comfortably read and interact with the platform in my preferred language. | **[p4_eterpoetic#6](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/6)** | Won't-Have | In Review |
| As a customer (or user), I can **easily order a custom-written poem** so that I can receive a unique, personalized piece of poetry for a special occasion. | **[p4_eterpoetic#2](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/2)** | Could-Have | Ready |
| As a satisfied customer, I can **easily leave a public rating and review of the service** so that I can share my experience and help future customers make a decision. | **[p4_eterpoetic#3](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/3)** | Should Have | Ready |

---

### 🚀 Existing Features (Source: GitHub "Done" Column)

| User Story | GitHub Issue | Priority | Status |
|---|---|---|---|
| As a reader, I can **access the poetry library** so that I can browse and select poems to read. | **[p4_eterpoetic#1](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/1)** | Could-Have | Done |
| As a customer I can **mark my favorites items** so that i can easily identify them. As a logged-in customer, I can **easily mark and manage poems as my favorites** so that I can quickly find and revisit them later for potential purchase or inspiration. | **[p4_eterpoetic#7](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/7)** | Won't-Have | Done |
| As a user I can **register, login in and log out** so that i can access to leave comments and participate. As a new or returning visitor, I can **securely register an account and manage my login session** so that I can fully participate by leaving comments and accessing members-only features. | **[p4_eterpoetic#5](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/5)** | Must-Have | Done |
| As a Site Owner, I can **receive, review and store collaboration request in the database**, so that I can efficiently manage, review and respond to new opportunities. | **[django-blog#13](https://github.com/cynthiapinedoh79/django-blog/issues/13)** | Could-Have | Done |
| As a Site Admin I can **create or update the About page content** so that it is available on the site. | **[django-blog#11](https://github.com/cynthiapinedoh79/django-blog/issues/11)** | High | Done |
| As a Site User I can **click the About link** so that I can read about the site. | **[django-blog#10](https://github.com/cynthiapinedoh79/django-blog/issues/10)** | Must-Have | Done |
| As a Site Admin I can **create, read, update and delete posts** so that I can manage my blog content. | **[django-blog#7](https://github.com/cynthiapinedoh79/django-blog/issues/7)** | Must-Have | Done |
| As a a Site User I can **click on a post** so that I can read the full text. | **[django-blog#4](https://github.com/cynthiapinedoh79/django-blog/issues/4)** | Must-Have | Done |
| As a Site User I can **leave comments on a post** so that I can be involved in the conversation. | **[django-blog#5](https://github.com/cynthiapinedoh79/django-blog/issues/5)** | Could-Have | Done |
| As a Site Admin I can **create draft post** so that I can finish writing the content later. | **[django-blog#8](https://github.com/cynthiapinedoh79/django-blog/issues/8)** | High | Done |
| As a Site User / Admin I can **view comments on an individual post** so that I can read the conversation. | **[django-blog#3](https://github.com/cynthiapinedoh79/django-blog/issues/3)** | Must-Have | Done |
| As a Site Admin I can **approve or disapprove comments** so that I can filter out objectionable comments. | **[django-blog#9](https://github.com/cynthiapinedoh79/django-blog/issues/9)** | Could-Have | Done |
| As a Site User I can **modify or delete my comment on a post** so that I can be involved in the conversation. | **[django-blog#6](https://github.com/cynthiapinedoh79/django-blog/issues/6)** | Could-Have | Done |
| As a site user I can **view a paginated list of post** so that I can select which post I want to view. | **[django-blog#1](https://github.com/cynthiapinedoh79/django-blog/issues/1)** | Must-Have | Done |

---

### 🧑‍💻 Testing User Stories – User Experience (UX) Evaluation

All core user stories were tested using the defined **Acceptance Criteria (ACs)** set in the corresponding GitHub Issues.

### Poetry Library Access (Ref: [p4_eterpoetic#1](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/1))

The **'Access the poetry library'** feature passed the following criteria:

* **AC1** The user can view a list of available poems on the Poetry page.
* **AC2** The list of poems can be filtered and sorted by available attributes (e.g., author, collection, title).
* **AC3** Selecting a poem from the list successfully directs the user to the detailed view of that poem.

---

### Mark Favorites Items-Easily mark and manage poems as my favorites (Ref: [p4_eterpoetic#7](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/7))

The **'Mark my favorites items'** feature passed the following criteria, ensuring reliable item marking and list management:

**1. Marking a Favorite (AC1-AC2)**

* **AC1** Favorite Toggle on Poem Display
    * A clearly visible icon/button (e.g., a heart outline) must be present on every poem's listing card and detail page.
    * The feature must be restricted to logged-in users; non-logged-in users attempting to use it must be prompted to log in or register.
    * Clicking the icon must toggle the favorite status (e.g., the heart fills in upon being marked and empties upon being unmarked).

* **AC2** Confirmation and Persistence
    * The system must provide instant visual feedback when the status is toggled (e.g., a brief "Added to Favorites" message).
    * The favorite status must persist across sessions and device logins for the authenticated user.

**2. Viewing and Managing Favorites (AC3-AC4)**

* **AC3** Dedicated Favorites View
    * A dedicated "My Favorites" page must be accessible from the main navigation (e.g., via a header link or user profile menu).
    * This page must only display poems that the user has marked as a favorite.
    * Each item in this view must include the option to easily remove it from the favorites list.

* **AC4** Visibility on Listing Pages
    * When a customer views a general list of poems (e.g., a search results page), the favorite status must be visually reflected on any item they have previously marked as a favorite (e.g., the heart icon remains filled).

---

### Register, login in and log out-securely register an account and manage my login session (Ref: [p4_eterpoetic#5](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/5))

The **'Register, Log In, and Log Out'** feature passed the following criteria, ensuring a complete and secure user authentication flow:

#### 1. Registration & Security (AC1)

* **AC1** New Account Creation
    * The user must be able to register a new account by providing a valid email address and a secure password.
    * Passwords must meet minimum security requirements (e.g., length, mixture of characters) and the system must store them securely (hashed).
    * The user must receive an **email verification link** and must click it to finalize account activation.

#### 2. Login & Session Management (AC2-AC4)

* **AC2** Standard Email/Password Login
    * The user must be able to log in using their registered email and password.
    * The system must provide a clear error message for failed login attempts (e.g., "Invalid credentials").
    * The user must have a "**Forgot Password**" option to reset their password via email.

* **AC3** Social Media Login (OAuth)
    * The user must be able to log in using external social accounts (e.g., Facebook and Google).
    * The social login process must automatically create a user profile if one doesn't exist, linked to that social account.

* **AC4** Session Management
    * Upon successful login, the system must maintain a secure user session (e.g., token-based) for a defined period.
    * The user must have a "**Keep me logged in**" option to persist the session across browser closures.

#### 3. Logout (AC5)

* **AC5** Secure Logout
    * A clearly visible "**Log Out**" button must be available to authenticated users.
    * Clicking "**Log Out**" must immediately and securely invalidate the user's session and redirect them to the homepage or login screen.

---

### Receive, review and store collaboration request in the database (Ref: [django-blog#13](https://github.com/cynthiapinedoh79/django-blog/issues/13))

The **'Collaborator Submission Flow'** feature passed the following criteria, ensuring effective notification and administration:

### 1. System Notification (AC1)

* **AC1** Email Notification
    * When a Potential Collaborator submits a proposal, an email notification is immediately sent to the registered admin email address.

### 2. Admin Dashboard Management (AC2-AC4)

* **AC2** Dashboard View
    * All submitted proposals are listed in a dedicated "Proposals" section of the admin dashboard, displaying the collaborator's name, email, and submission date.
    * The newest submissions must appear at the top.

* **AC3** View Details
    * Given the list of proposals in the dashboard, clicking on a specific entry allows the admin to view all the details submitted, including the full message and portfolio URL.

* **AC4** Mark as Read
    * The admin has the ability to mark a submission as "Read" or "Unread" from the dashboard list to help track which proposals have been reviewed.

---

### Create or update the About page content (Ref: [django-blog#11](https://github.com/cynthiapinedoh79/django-blog/issues/11))

The **'Create or update the About page content'** feature passed the following criteria:

* **AC1** A site administrator can access a dedicated form or interface to modify the About page content.
* **AC2** Changes made by the administrator are successfully saved to the database.
* **AC3** The updated content is instantly visible on the public-facing About page.

---

### Click the About link (Ref: [django-blog#10](https://github.com/cynthiapinedoh79/django-blog/issues/10))

The **'Click the About link'** feature passed the following criteria:

* **AC1** When the About link is clicked, the about text is visible.

---

### Create, read, update and delete posts (Ref: [django-blog#7](https://github.com/cynthiapinedoh79/django-blog/issues/7))

The **'Blog Post Management (CRUD)'** feature passed the following criteria, ensuring authenticated users can control their content:

#### 1. Content Creation & Reading (AC1-AC2)

* **AC1** Create Blog Post
    * Given a logged-in user with appropriate permissions (e.g., staff status or specific role), they can access a dedicated form to create and submit a new blog post.
* **AC2** Read Blog Post
    * Given a logged-in user, they can access and view the full content of any published blog post.

#### 2. Content Editing (AC3-AC4)

* **AC3** Update Blog Post
    * Given a logged-in user who is the **author of the post** (or an administrator), they can access an edit form to modify the post's content and save the changes.
* **AC4** Delete Blog Post
    * Given a logged-in user who is the **author of the post** (or an administrator), they can successfully delete the post, removing it permanently from the site.

---

### Click on a post (Ref: [django-blog#4](https://github.com/cynthiapinedoh79/django-blog/issues/4))

The **'Click on a post'** feature passed the following criteria:

* **AC1** When a blog post title is clicked from the list, the user is successfully directed to the unique detailed view of that post.
* **AC2** The detailed view displays the full post content and the associated comments section (Ref: django-blog#3).

---

### Leave comments on a post (Ref: [django-blog#5](https://github.com/cynthiapinedoh79/django-blog/issues/5))

The **'Blog Commenting and Threading'** feature passed the following criteria, ensuring community engagement and organized discussion:

#### 1. Enabling Replies (AC1)

* **AC1** Comment Approval
    * When a new user comment is submitted, it is held for review until an administrator manually approves it. Once approved, the comment becomes publicly visible and available for replies.

#### 2. Reply Functionality (AC2)

* **AC2** User Reply Capability
    * Given a visible (approved) comment, any authenticated user can successfully submit a reply that is nested visually underneath the parent comment.
    * The system must verify that the user is logged in before allowing them to post a reply.

#### 3. Thread Organization (AC3)

* **AC3** Conversation Threading
    * Given more than one reply exists for a single parent comment, the replies are displayed sequentially, forming a clear, chronological conversation thread that is visually distinct from the main list of comments.

---

### Create draft post (Ref: [django-blog#8](https://github.com/cynthiapinedoh79/django-blog/issues/8))

#### Draft Blog Post Management (Ref: [django-blog#xx])

The **'Draft Blog Post Management'** feature passed the following criteria, ensuring content creators can work asynchronously:

#### 1. Saving Drafts (AC1)

* **AC1** Save and Hide
    * Given a logged-in user, they can click a designated "**Save Draft**" button which successfully saves the post's content to the database.
    * The saved draft must **not** be publicly visible on any public-facing blog list or URL.

#### 2. Retrieval and Editing (AC2)

* **AC2** Access and Resume
    * The author can access a dedicated section (e.g., "My Drafts" dashboard) to view a list of *only their own* saved draft posts.
    * The author can click on a draft title to load the full content back into the editor to continue working later.

#### 3. Publishing (AC3 - Added for completeness)

* **AC3** Status Update
    * From the editor page of a draft, there must be a visible "**Publish**" button (distinct from "Save Draft") that updates the post's status, making it publicly visible on the main blog list.

---

### View comments on an individual post (Ref: [django-blog#3](https://github.com/cynthiapinedoh79/django-blog/issues/3))

The **'View comments on an individual post'** feature passed the following criteria, ensuring transparency and easy moderation:

* **AC1** Given a published post, the site user can view all approved comments below the post content.
* **AC2** Comments are correctly displayed in a readable, sequential thread (replies are nested under the parent comment).
* **AC3** The site user can access a dedicated admin/moderator panel to view all pending, approved, and disapproved comments.

---

### Approve or disapprove comments (Ref: [django-blog#9](https://github.com/cynthiapinedoh79/django-blog/issues/9))

The **'Approve or disapprove comments'** feature passed the following criteria, ensuring effective content moderation:

* **AC1** Approve Comment
    * Given a logged-in user with **administrator or staff permissions**, they can access a designated action (e.g., a button or checkbox) to approve a pending comment, making it instantly visible on the public blog post.

* **AC2** Disapprove/Delete Comment
    * Given a logged-in user with **administrator or staff permissions**, they can access a designated action to disapprove or delete a comment, ensuring the comment is permanently removed or hidden from public view.

---

### Modify or delete my comment on a post (Ref: [django-blog#6](https://github.com/cynthiapinedoh79/django-blog/issues/6))

The **'Modify or delete my comment on a post'** feature passed the following criteria, ensuring users can manage their own contributions:

#### 1. Comment Modification (AC1)

* **AC1** Modify Own Comment
    * Given a logged-in user, they can access an edit function (e.g., a button) on **only their own submitted comment** to modify the text.
    * The system must verify the user is the original author before allowing the edit to be saved.

#### 2. Comment Deletion (AC2)

* **AC2** Delete Own Comment
    * Given a logged-in user, they can access a delete function (e.g., a trash can icon) on **only their own submitted comment**.
    * The system must require a confirmation step before permanently removing the comment and any associated replies.

---

### View a paginated list of post (Ref: [django-blog#1](https://github.com/cynthiapinedoh79/django-blog/issues/1))

The **'View a paginated list of post'** feature passed the following criteria, ensuring users can manage their own contributions:

* **AC1** Given more than one post in the database, these multiple posts are listed.
* **AC2** when the user opens the main page a list of post is seen. 
* **AC3** Then the user sees all post titles with pagination to choose what to read.

---

### 🔮 Features Left to Implement (Source: GitHub "Backlog" / "Ready" Columns)
| User Story | GitHub Issue | Priority | Status |
|---|---|---|---|
| As a website visitor, I can **easily switch the entire website interface and content between English and Spanish** so that I can comfortably read and interact with the platform in my preferred language. | **[p4_eterpoetic#6](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/6)** | Won't-Have | In Review |
| As a customer (or user), I can **easily order a custom-written poem** so that I can receive a unique, personalized piece of poetry for a special occasion. | **[p4_eterpoetic#2](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/2)** | Could-Have | Ready |
| As a satisfied customer, I can **easily leave a public rating and review of the service** so that I can share my experience and help future customers make a decision. | **[p4_eterpoetic#3](https://github.com/cynthiapinedoh79/p4_eterpoetic/issues/3)** | Should Have | Ready |

---

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
* Mobile-first responsive layout
* Clear typography hierarchy
* Consistent spacing and UI patterns
* Accessible markup and navigation

### Description        
This website is designed for **readers and creative writers** to explore diverse content, engage with the community, and enjoy an accessible reading experience while navigating through different pages.

### Typography
The main fonts used are **Inter** and **Roboto**, with Sans Serif as the fallback. Roboto is chosen for its clean, professional appearance, ensuring optimal readability for long-form content like poetry and blog posts.

### Color Palette 
* **Fonts:** Roboto, Inter – clean and modern  
* **Primary Brand (`--color-primary-brand`):** #E86A33 (Red-Orange) — Used for main calls-to-action (CTAs) and highlights (Energy/Urgency).
* **Accent & Dark BG (`--bg-dark`):** #4C3A51 (Deep Purple/Gray) — Used for footers and navigation (Trust/Creativity).
* **Text & Background:** * Dark Text (`--color-text-dark`): #1A2C42 (Deep Navy/Blue) — Ensures high contrast for readability.
    * Body Background (`--bg-body`): #FBF9F6 (Soft Cream/Off-White) — Provides a comfortable background for long reading sessions.
* **Link Hover:** `#C08A3E` (Mustard Gold) — Provides distinct, high-contrast feedback on hover.

![Color Palette -Design](static/images/readme/colorPalette/colorsP4-1.png)

![Color Palette -Design](static/images/readme/colorPalette/colorsP4-2.png)

![Color Palette -Design](static/images/readme/colorPalette/colorsP4-3.png)

![Color Palette -Design](static/images/readme/colorPalette/colorsP4-4.png)

![Color Palette -Design](static/images/readme/colorPalette/colorsP4-5.png)

<!-- * Collor Palette Design: 
[View colorsP4 (.pdf)](./docs/colorsP4-1.pdf)
* Collor Palette Design: [Download colorsP4 (.docx)](./docs/colorsP4.docx)
* [Contrast checked with WebAIM](https://webaim.org/resources/contrastchecker/) -->


### Colour Psychology

The palette's mood is designed to support the literary and creative focus of the platform:

* **Soft Linen White:** → Creates a calm, inviting blank page effect, perfect for reading.
* **Midnight Teal:** → Represents wisdom, depth, and a focused, literary feel.
* **Vibrant Terracotta / Rosewood Red:** → Provides creative energy and passion bursts (used for highlights and accents).
* **Muted Gray + Gold Ocher:** → Establishes structure and introduces a touch of warmth and professionalism.

![Colour Psychology](static/images/readme/colorPalette/psColor.png)

![Colour Psychology](static/images/readme/colorPalette/psColor1.png)


![Contrast checked with WebAIM](static/images/readme/colorPalette/contrast.png)

### Imagery & Backgrounds

Clear and attractive images support the theme and maintain strong contrast with text for optimal readability.

* **Poetry/Creative Themed Backgrounds:** Imagery focuses on **writing, literature, and abstract ink/paper textures**.
* High contrast text overlays for readability.

### 1. Home: index.html (Poetry List)
* **Background:** The page utilizes a **vibrant, abstract hero image ('Art/Artist')** to convey passion, followed by a grid of **emotionally evocative, individual collection thumbnails** (e.g., Eagle, Man in Sorrow) to represent the diverse mood of the content.

### 2. My Favorites: favorites\_list.html
* **Background:** Imagery focuses on a clean, **white, distraction-free background** to highlight the **curated grid of poem thumbnails**. The emphasis is on the user's personal selection of emotional and intimate photos (Love, Smile, etc.).

### 3. Blog: bloghome.html
* **Background:** The theme is consistent, using **rich, high-contrast imagery** of classical writing tools (ink, quills, old books, paper) to establish a strong, traditional literary atmosphere for the posts.

### 4. About: about.html (Collaboration Form)
* **Background:** The page uses a **professional, data-focused image** (AI/Data Architect) to establish technical authority and trust. The collaboration form contrasts with the content, using a light background to encourage simple, focused outreach.

---

### Eterpoetic LOGO & Visual Identity

The logo visually captures the essence of the project:
![Logo](static/images/readme/colorPalette/logoIngles.png)

#### Description and Meaning
The design combines an old book with a quill and ink well, representing the **intimate act of writing** and the **poetic tradition** that is inherited and continuously renewed. The quill symbolizes inspiration taking form, while the book evokes the lasting presence of written work. The design transforms the ethereal (the subtle, the delicate) into literary expression.

#### Typography
The classic serif typeface conveys **elegance and refinement**, evoking literary tradition, calmness, and the measured rhythm of timeless poetry.

#### Colors
The palette is composed of warm and natural tones:
* **Deep Brown/Plum Ink:** Symbolizes the antique book, literary depth, and the memory contained within written words.
* **Vibrant Terracotta / Rosewood Red:** Expresses **creative energy, emotional impulse**, and the spark of inspiration.
* **Earthy Greens:** Offers a sense of freshness, renewal, and connection to inner life (Used as an accent on the feather).

Together, these colors suggest the movement of thought flowing toward the page, from the spirit into written expression.

---

## 📐 Five Planes UXD

### 📌 Strategy
Define goals and audience needs. Our objective is to create a professional platform that focuses on **AAA readability** and **intuitive functionality**. The design prioritizes content consumption and creative community engagement.

![Strategy](assets/images/readme/fivePlanes/strategy.png)

### 📐 Scope
The site is designed around two core user actions:

1.  **Content Consumption:** Visitors can easily browse poem collections and blog posts, utilizing search and filtering tools to find content quickly.
2.  **Community & Contribution:** Registered users can interact with content (favoriting/commenting) and potential collaborators can apply via the dedicated submission form.

![Scope pg1](assets/images/readme/fivePlanes/scope1.png)
![Scope pg2](assets/images/readme/fivePlanes/scope2.png)

### 🏗️ Structure
The website is built using a **Django MVT (Model-View-Template) architecture** to separate concerns (HTML5, CSS3, JavaScript).

**Website Pages/Apps:**
1. **_Home / Poetry:_** The main content hub, displaying poem collections, search filters, and general site features.
2. **_Blog:_** Manages all blog posts, individual post detail views, and user commenting functionality.
3. **_About:_** Displays owner/team information and handles collaborator applications.
4. **_Accounts:_** Provides core user management (Registration, Login, Logout, Session Management).

![Structure](assets/images/readme/fivePlanes/structure.png)

### 🦴 Skeleton
Wireframes and layout structure.
The website is designed to be clear and simple. The navigational hierarchy ensures easy flow from top to bottom and between main app areas.

**Wireframe**
The wireframe is designed using **Balsamiq** software: 
[Balsamiq](https://balsamiq.cloud/ss26tqg/p4441iq/rD01A)

#### Home
![Home](assets/images/readme/Bals/Bals-Home.png)

### 🎨 Surface
Final aesthetic layers (colors, components, imagery).
To create a pleasing and understandable view, the design utilizes a **high-contrast, modern literary palette** (Midnight Teal, Vibrant Terracotta, and Plum Ink) against a soft off-white background to ensure excellent readability.

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
