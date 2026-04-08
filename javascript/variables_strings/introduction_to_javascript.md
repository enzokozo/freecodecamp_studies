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
```

## 📦 Data Types and Variables
---

> **Core Concept:** A **Data Type** is the kind of value stored (like a number or text). A **Variable** is a named container that stores a value, allowing you to reference and manipulate it throughout your code, similar to variables in mathematics (e.g., $x = 2$).

### 🔢 Basic Data Types
JavaScript uses several data types to help the program understand the nature of the data it is processing.

| Data Type | Description | Example |
| :--- | :--- | :--- |
| **Number** | Represents integers and floating-point numbers (decimals). | `7`, `3.14`, `-67` |
| **String** | A sequence of characters/text enclosed in single or double quotes. | `"I love to code!"` |
| **Boolean** | Represents one of two logical values: `true` or `false`. | `true` |
| **Undefined** | A variable that has been declared but hasn't been given a value yet. | `undefined` |
| **Null** | Intentionally set to represent "nothing" or no value. | `null` |

### 🏗️ Complex & Special Data Types
* **Object:** A collection of key-value pairs used to group related information.
    ```javascript
    { name: "Alice", age: 30 }
    ```
* **Symbol:** A unique value that cannot be changed, often used as identifiers.
* **BigInt:** Used for very large numbers that exceed the standard `Number` limit (created by adding `n` to the end).
    ```javascript
    12345678901234567890n
    ```

### 🛠️ Syntax & Output
* **Comments (`//`):** Notes for programmers that are ignored by the computer during execution.
* **`console.log()`:** A function used to output information to the browser's console for debugging.

```javascript
// Examples of outputting different data types
console.log(3.14);               // Number (Floating point)
console.log("Hello!");           // String
console.log(true);               // Boolean
console.log(Symbol('id'));       // Symbol