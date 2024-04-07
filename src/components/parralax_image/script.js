function component_parralax_image(component) {
	const rect = component.getBoundingClientRect();
	const radius = 400;
	const left_right_max =
		(component.firstElementChild.clientWidth - rect.width) / 2;
	const top_bottom_max =
		(component.firstElementChild.clientHeight - rect.height) / 8;

	const centerX = rect.left + rect.width / 2,
		centerY = rect.top + rect.height / 2;

	window.addEventListener("mousemove", (e) => {
		if (
			Math.abs(e.clientX - centerX) < radius &&
			Math.abs(e.clientY - centerY) < radius
		) {
			let rangeX = (e.clientX - centerX) / radius / 2,
				rangeY = (e.clientY - centerY) / radius / 2;

			rangeX = Math.min(1, Math.max(rangeX, -1));
			rangeY = Math.min(1, Math.max(rangeY, -1));

			rangeX *= -left_right_max;
			rangeY *= -top_bottom_max;
			component.firstElementChild.style.left = `calc(50% + ${rangeX}px)`;
			component.firstElementChild.style.top = `calc(50% + ${rangeY}px)`;
		} else {
			component.firstElementChild.style.left = `calc(50%)`;
			component.firstElementChild.style.top = `calc(50%)`;
		}
	});
}

(function () {
	var components = document.getElementsByClassName(
		"component-parralax_image"
	);
	for (var i = 0; i < components.length; i++) {
		component_parralax_image(components.item(i));
	}
})();
