      // ---------------------------------------------------------------------
      // Update the president count
      // presidentCount[presidentStatusCode]++;

      // Create a new marker with the appropriate icon and coordinates
      // Note: This newMArker applies to A L L markers, be it bicycles, or earthquakes
      //                                                Alemi March 5 2020
      // -----------------------------------------------------------------------------
      var presidentStatusCode;

      var newMarkerP = L.marker([president.latitude, president.longitude], {
        icon: president_Icons[presidentStatusCode]
      });
      // ------------------------------------------------------------------------------------  
      //                  Add the new marker to the appropriate layer
      // ------------------------------------------------------------------------------------
      newMarkerP.addTo(layers[presidentStatusCode]);
      

      // Bind a popup to the marker that will  display on click. This will be rendered as HTML
      newMarkerP.bindPopup(president.name + "<br> votes percentage: " + president.pct + "<br>" + president.state + "State");
    