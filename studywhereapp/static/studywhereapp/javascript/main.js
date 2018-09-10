// Function initializes and adds the Nashville map w/ marker
function initMap() {
	// The location of Nashville, TN
	const nashville = {lat: 36.174465, lng: -86.767960};
	// The map, centered at Nashville, TN
	const map = new google.maps.Map(
		document.getElementById('map'), {zoom: 10, center: nashville});
	// The marker, positioned at Nashville, TN
	const marker = new google.maps.Marker({position: nashville, map: map});
  }