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
var throttle = function (fn, delay) {
  var timer = null;
  return function () {
    var context = this,
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

/* Build custom header */
function buildHeader() {
  // Remove unused title
  const headerTitleCont = document.querySelector(".confTitle");
  const unusedTitle = headerTitleCont.querySelector("h1").remove();

  // Append new header elements
  const fullHeaderCont = document.querySelector(".confTitleBox");

  const headerLogo = document.createElement("img");
  headerLogo.src = "https://assets.ubuntu.com/v1/809d5b1a-czech-flag.svg"

  const headerTitle = document.createElement("h1");
  headerTitle.innerText = "Ubuntu Summit 2022";

  const headerSubtitle = document.createElement("h2");
  headerSubtitle.innerText = "Prague, Czech Republic, November 7th-9th, 2022";

  const headerImage = document.createElement("img");
  headerImage.classList.add("headerImage");
  headerImage.src = "https://assets.ubuntu.com/v1/25294081-community-support-thin-white.svg";
  
  headerTitleCont.append(headerLogo);
  headerTitleCont.append(headerTitle);
  headerTitleCont.append(headerSubtitle);
  fullHeaderCont.append(headerImage);

}
/* --------- Setup on window load ---------- */
window.addEventListener("load", function() {
  addMetaTag();
  buildHeader();
  setupSideNavigations(".conf_leftMenu");
});


