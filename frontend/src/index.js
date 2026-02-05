import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

console.log("index.js is running");
console.log("Looking for root element:", document.getElementById("root"));

const root = ReactDOM.createRoot(document.getElementById("root"));
console.log("About to render App component");
root.render(<App />);