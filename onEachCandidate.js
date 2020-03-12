function onEachCandidate(president, layer) {
    layer.bindPopup("<h3>" + president.coordinates +
      "</h3><hr><p>" + " " + "</p>");
  }
     
  // --------------------------------------------------------------------------------------------------
  //    Create a GeoJSON layer containing the presidents array on the CandiData object
  //    Run the onEachpresident function once for each piece of data in the array
  //    onEachpresident is a leaflet... Piruz
  // --------------------------------------------------------------------------------------------------
  var Candi = L.geoJSON(CandiData, {
    onEachFeature: onEachCandidate
  });

  // --------------------------------------------------------------------------------------------------
  //                        Sending our earthquakes layer to the createMap function
  // -------------------------------------------------------------------------------------------------
  createMapCandidate(Candi);

        function createMapCandidate(Candi) {
    
        var overlayMaps = {
            "Candi Data": Candi
                              
        };
};

L.control.layers(null, overlayMaps, {collapsed: false}).addTo(map);