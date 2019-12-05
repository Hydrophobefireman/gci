import { h, render, Router, absolutePath } from "./@ui/ui-lib.modern.js";
import { OnBoarding } from "./components/onboarding.js";
import { BookMarksApp } from "./components/bookmarksapp.js";
const App = h(
  Router,
  null,
  h(OnBoarding, { path: absolutePath("/") }),
  h(BookMarksApp, { path: absolutePath("/app") })
);

render(App, document.querySelector("main"));
