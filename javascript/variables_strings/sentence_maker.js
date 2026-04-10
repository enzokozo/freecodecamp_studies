// Declare variables for the story
let adjective = "quick";
let noun = "fox";
let verb = "angry";
let place = "mountain";
let adjective2 = "small";
let noun2 = "potato";

// Create the first story using template literals
const firstStory = `Once upon a time, there was a(n) ${adjective} ${noun} who loved to eat ${noun2}. The ${noun} lived in a ${place} and had ${adjective2} nostrils that blew fire when it was ${verb}.`;

// Print the first story to the console
console.log(`First story: ${firstStory}`);

// Change the values of the variables
adjective = "lazy";
noun = "dog";
verb = "scared";
place = "beach";
adjective2 = "big";
noun2 = "burger";

// Create the second story using the updated variables
const secondStory = `Once upon a time, there was a(n) ${adjective} ${noun} who loved to eat ${noun2}. The ${noun} lived in a ${place} and had ${adjective2} nostrils that blew fire when it was ${verb}.`;

// Print the second story to the console
console.log(`Second story: ${secondStory}`);