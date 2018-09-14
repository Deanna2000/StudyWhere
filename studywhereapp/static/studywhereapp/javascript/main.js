// const map;
// const marker;
// const infowindow;

// Function initializes and adds the Nashville map w/ marker
function initMap() {
	// The location of NSS
	const nss = {lat: 36.1325771, lng: -86.7584417};
	// The map, centered at NSS
	const map = new google.maps.Map(
		document.getElementById('map'), {zoom: 10, center: nss});

	// const marker = new google.maps.Marker({position: nss, map: map});
  }

//Event handler to add a new map marker

handleAddVenueMarker = (evt) => {
const nss = {lat: 36.1325771, lng: -86.7584417};
const map = new google.maps.Map(
	document.getElementById('map'), {zoom: 10, center: nss});
marker = new google.maps.Marker({
	    position: nss,
	    map: map,
	    draggable: true,
	  });
	  google.maps.event.addListener(marker, 'dragend', function (event) {
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();
		console.log(lat, long)
		document.getElementById("id_latitude").value=lat
		document.getElementById("id_longitude").value=long
		var geocoder = new google.maps.Geocoder();

		    geocoder.geocode({ latLng: marker.getPosition() }, function(result, status){
		      if('OK' === status){
		        console.log(result)
				address = result[0].formatted_address;
				document.getElementById("id_address").value=address
		      } else {
		        console.log('Geocode was not successful for the following reason: ' + status)
		      }
	  });
})}


