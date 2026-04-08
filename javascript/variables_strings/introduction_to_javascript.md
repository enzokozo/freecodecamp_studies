# Introduction to JavaScript

## 🌐 JavaScript: Interactivity and the Web Trinity
---

> **Core Concept:** While HTML and CSS define what the user **sees**, JavaScript defines what the user **does** and how the page **responds**. It is a full-fledged programming language that transforms static documents into dynamic, interactive applications.

### 🏗️ The Division of Responsibilities
Modern web development relies on three core technologies working in tandem:

| Technology | Role | Analogy |
| :--- | :--- | :--- |
| **HTML** | **Structure**: Defines elements like headings, buttons, and paragraphs. | The Skeleton |
| **CSS** | **Style**: Handles colors, fonts, layouts, and animations. | The Skin/Clothes |
| **JavaScript** | **Behavior**: Manages logic, user input, and dynamic updates. | The Brain/Muscles |



### 💻 Implementation Example
In professional environments, we separate these into different layers to maintain "Separation of Concerns" (SoC):

```html
<h1 id="main-title">Hello, World!</h1>
<button id="action-btn">Click Me</button>

<style>
  /* Presentation (CSS) */
  h1 { color: green; transition: 0.3s; }
  .highlight { color: blue; font-size: 2rem; }
</style>

<script>
  // Behavior (JavaScript)
  const btn = document.getElementById('action-btn');
  const title = document.getElementById('main-title');

  // Event Listener: Handling user interaction
  btn.addEventListener('click', () => {
      title.classList.toggle('highlight');
      console.log('User interaction detected!');
  });
</script>