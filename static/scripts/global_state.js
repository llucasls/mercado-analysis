import "./redux.js";

const createStore = window.Redux.legacy_createStore;
const composeWithDevTools = (...enhancers) => {
  const devtoolsExtension = window.__REDUX_DEVTOOLS_EXTENSION__;
  return devtoolsExtension && devtoolsExtension(...enhancers);
}

const INITIAL_STATE = { mode: "light-mode" };

const toggleMode = (mode) => {
  if (mode === "light-mode") {
    return "dark-mode";
  } else if (mode === "dark-mode") {
    return "light-mode";
  }

  return "light-mode";
}

const toggleButtonText = (text) => {
  if (text === "dark mode") {
    return "light mode";
  } else if (text === "light mode") {
    return "dark mode";
  }

  return "dark mode";
}

const reducer = (state = INITIAL_STATE, action) => {
  if (action.type === "CHANGE_MODE") {
    return { ...state, mode: toggleMode(state.mode) };
  }

  return state;
};

const store = createStore(reducer, composeWithDevTools());

const toggleModeAction = { type: "CHANGE_MODE" };

const toggleModeButton = document.querySelector("#toggle-mode");

toggleModeButton.addEventListener("click", () => {
  store.dispatch(toggleModeAction);
});

store.subscribe(() => {
  const body = document.body;
  const globalState = store.getState();

  toggleModeButton.innerHTML = toggleButtonText(toggleModeButton.innerHTML);
  body.className = toggleMode(body.className);
});
