function set_theme_to_html(theme) {
	document.documentElement.dataset.theme = theme;
}
function save_theme_setting(theme) {
	localStorage.setItem("theme", theme);
	document.getElementById("theme-switcher").dataset.currentThemeSetting =
		theme;
}

function auto_theme_set_theme() {
	if (localStorage.getItem("theme") != "auto") {
		return;
	}
	if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
		set_theme_to_html("dark");
	} else {
		set_theme_to_html("light");
	}
}
function theme_switcher() {
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
	save_theme_setting(new_theme);
	set_theme_to_html(new_theme);

	if (new_theme == "auto") {
		auto_theme_set_theme();
	}
}

function init_theme() {
	theme_setting = localStorage.getItem("theme");
	if (theme_setting == null) {
		theme_setting = "auto";
		localStorage.setItem("theme", theme_setting);
	}

	if (theme_setting == "auto") {
		auto_theme_set_theme();
	} else if (theme_setting == "light" || theme_setting == "dark") {
		set_theme_to_html(theme_setting);
	}

	window
		.matchMedia("(prefers-color-scheme: dark)")
		.addEventListener("change", auto_theme_set_theme, true);

	save_theme_setting(theme_setting);
}

(function () {
	init_theme();
})();
