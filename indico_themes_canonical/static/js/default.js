/* ---------- JS for collapsable side navigation ---------- */

/**
  Toggles the expanded/collapsed classed on side navigation element.

  @param {HTMLElement} sideNavigation The side navigation element.
  @param {Boolean} show Whether to show or hide the drawer.
*/
function toggleDrawer(sideNavigation, show) {
  const navigationToggle = document.querySelector(".navigationToggleBtn");
  if (sideNavigation) {
    if (show) {
      navigationToggle.setAttribute("aria-expanded", true);

      sideNavigation.classList.remove("is-drawer-hidden");
      sideNavigation.classList.add("is-drawer-expanded");
    } else {
      navigationToggle.setAttribute("aria-expanded", false);

      sideNavigation.classList.remove("is-drawer-expanded");
      sideNavigation.classList.add("is-drawer-hidden");
    }
  }
}

// throttle util (for window resize event)
const throttle = function (fn, delay) {
  let timer = null;
  return function () {
    const context = this,
      args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      fn.apply(context, args);
    }, delay);
  };
};

/**
  Attaches event listeners for the side navigation toggles
  @param {HTMLElement} sideNavigation The side navigation element.
*/
function setupSideNavigation(sideNavigation, navigationToggle) {
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      toggleDrawer(sideNavigation, false);
    }
  });

  navigationToggle.addEventListener("click", function (event) {
    event.preventDefault();

    if (sideNavigation) {
      sideNavigation.classList.remove("is-drawer-hidden");
      toggleDrawer(sideNavigation, !sideNavigation.classList.contains("is-drawer-expanded"));
    }
  });

  // hide side navigation drawer when screen is resized
  window.addEventListener(
    "resize",
    throttle(function () {
      navigationToggle.setAttribute("aria-expanded", false);

      // remove expanded/collapsed class names to avoid unexpected animations
      sideNavigation.classList.remove("is-drawer-expanded");
      sideNavigation.classList.remove("is-drawer-hidden");
      sideNavigation.classList.add("is-drawer-hidden");
    }, 10)
  );
}

function createNavigationToggle () {
  const mainContentCont = document.querySelector("#confSectionsBox");
  const navigationToggleCont = document.createElement("p");
  navigationToggleCont.className += "navigationToggleCont"
  const navigationToggleLink = document.createElement("a");
  navigationToggleLink.innerHTML = "Menu";
  navigationToggleLink.className += "navigationToggleBtn";
  navigationToggleCont.append(navigationToggleLink);
  mainContentCont.prepend(navigationToggleCont);

  return navigationToggleLink;
}

/**
  Attaches event listeners for all the side navigations in the document.
  @param {String} sideNavigationSelector The CSS selector matching side navigation elements.
*/
function setupSideNavigations(sideNavigationSelector) {
  // Setup all side navigations on the page.
  var sideNavigation = document.querySelector(sideNavigationSelector);
  const navigationToggle = createNavigationToggle();
  setupSideNavigation(sideNavigation, navigationToggle);
}

/* ---------- Adds meta tag to support media queries ---------- */
function addMetaTag() {
  const meta = document.createElement("meta");
  meta.name = "viewport";
  meta.content = "width=device-width,initial-scale=1.0";
  document.getElementsByTagName('head')[0].appendChild(meta);
}

/* Moves the header nav to be within the stylised header */
function moveHeaderNav () {
  const headerCont = document.querySelector(".confheader");
  const headerNav = document.querySelector(".header");
  headerCont.prepend(headerNav);
}

/* --------- Setup on window load ---------- */
window.addEventListener("load", function() {
  addMetaTag();
  moveHeaderNav();
  setupSideNavigations(".conf_leftMenu");
});
