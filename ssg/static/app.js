function onResize() {
    let header_title = document.getElementById("main-title");
    header_title.style.width = header_title.firstChild.scrollWidth + "px";
}
;(function() {
    window.addEventListener("load", onResize);
    window.addEventListener("resize", onResize);
}
)();
;function toggleDropdown() {
    document.getElementById("lang-switcher").getElementsByClassName("dropdown")[0].classList.toggle("open");
}
;function set_theme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem("theme", theme);
}
;function theme_switcher() {
    theme_setting = localStorage.getItem("theme");
    new_theme = "";
    switch (theme_setting) {
    case "light":
        new_theme = "dark";
        break;
    case "dark":
        new_theme = "auto";
        break;
    case "auto":
        new_theme = "light";
        break;
    default:
        return;
    }
    ;set_theme(new_theme);
}
;function init_theme() {
    theme_setting = localStorage.getItem("theme");
    if (theme_setting == null || ["dark", "light", "auto"].includes(theme_setting) == false) {
        theme_setting = "auto";
    }
    ;set_theme(theme_setting)
}
;(function() {
    init_theme();
}
)();
