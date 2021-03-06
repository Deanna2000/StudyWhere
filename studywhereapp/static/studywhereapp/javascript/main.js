

// Function initializes and adds the NSS map w/ marker
function initMap() {
	// The location of NSS
	const nss = { lat: 36.1325771, lng: -86.7584417 };
	// The map, centered at NSS
	const map = new google.maps.Map(
		document.getElementById('map'), { zoom: 10, center: nss });
	fetch("http://localhost:8000/get_venues")
		.then(function (response) {
			return response.json()
		})
		.then(function (myjson) {
			const markers = JSON.parse(myjson.results)
			markers.forEach((marker) => {
				const bookMarker = {
					url: 'https://imgur.com/a/QPn8G04',
					// This marker is 20 pixels wide by 34 pixels high.
					size: new google.maps.Size(20, 34),
					// The origin for this image is (0, 0).
					origin: new google.maps.Point(0, 0),
					// The anchor for this image is the base of the pointer at (10, 34).
					anchor: new google.maps.Point(0, 34)
				  };
				  // Shapes define the clickable region of the icon. The type defines an HTML
				  // <area> element 'poly' which traces out a polygon as a series of X,Y points.
				  // The final coordinate closes the poly by connecting to the first coordinate.
				  var shape = {
					coords: [1, 1, 1, 20, 18, 20, 18, 1],
					type: 'poly'
				  };

				var marker = new google.maps.Marker({
					position: { "lat": marker.latitude, "lng": marker.longitude  },
					map: map,
					draggable: false,
					icon: 'http://chart.googleapis.com/chart?chst=d_map_pin_letter&chld=%7c9874BA%7c9874BA&.png',
					shape: shape,
				});
				marker.addListener('click', function (event) {
					console.log("you clicked it")
					lat = marker.getPosition().lat();
					long = marker.getPosition().lng();
					console.log(marker)
					console.log({lat})
					console.log({long})
					fetch(`http://127.0.0.1:8000/venues_lat/?lat=${lat}`).then(r => r.json()).then(r => {
					console.log(r)
})



					//query lat and long
					//get venue detail number associated
     					// open venue detail
					// location.href = "/detail/";
				});
				// google.maps.event.addListener(marker, 'mouseover', function (event) {
				// 	// highlight marker
				// 	// open venue small detail
				// });

			});
		})
}

//Event handler to add a new map marker
handleAddVenueMarker = (evt) => {
	//call the add venue form here
	console.log("in js")
	const nss = { lat: 36.1325771, lng: -86.7584417 };
	const map = new google.maps.Map(
		document.getElementById('map'), { zoom: 10, center: nss });

	marker = new google.maps.Marker({
		position: nss,
		map: map,
        draggable: true,
		animation: google.maps.Animation.DROP,

	});
	google.maps.event.addListener(marker, 'dragend', function (event) {
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();
		console.log(lat, long)
		document.getElementById("id_latitude").value = lat
		document.getElementById("id_longitude").value = long
		var geocoder = new google.maps.Geocoder();

		geocoder.geocode({ latLng: marker.getPosition() }, function (result, status) {
			if ('OK' === status) {
				console.log(result)
				address = result[0].formatted_address;
				document.getElementById("id_address").value = address
			} else {
				console.log('Geocode was not successful for the following reason: ' + status)
			}
		});
	})
}


