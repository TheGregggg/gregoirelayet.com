function onResize() {
	let header_title = document.getElementById("main-title");
	header_title.style.width = header_title.firstChild.scrollWidth + "px";
}

(function () {
	window.addEventListener("load", onResize);
	window.addEventListener("resize", onResize);
})();
