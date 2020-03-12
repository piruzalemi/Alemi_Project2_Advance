// Initialize an object containing icons for each layer group
var president_Icons = {
    Sanders: L.ExtraMarkers.icon({
      icon: "ion-settings", 
      iconColor: "white",
      markerColor: "yellow",
      shape: "star"
    }),
    Buttigieg: L.ExtraMarkers.icon({
      icon: "ion-android-bicycle",
      iconColor: "white",
      markerColor: "red",
      shape: "circle"
    }),
    //OUT_OF_ORDER: L.ExtraMarkers.icon({
    Trump: L.ExtraMarkers.icon({
      icon: "ion-minus-circled",
      //icon: "fas fa-democrat",
      iconColor: "white",
      //markerColor: "blue-dark",
      markerColor: "blue-dark",
      shape: "penta"
    }),
    //LOW: L.ExtraMarkers.icon({
    Biden: L.ExtraMarkers.icon({
      icon: "ion-android-bicycle",
      iconColor: "white",
      markerColor: "orange",
      shape: "circle"
    }),
    //NORMAL: L.ExtraMarkers.icon({
      Bloomberg: L.icon({
      //icon: "ion-android-bicycle",
      iconUrl: "piruz.jpg",
      iconSize:     [38, 34], // size of the icon
      iconColor: "white",
      markerColor: "blue",
      shape: "circle"
    }),
      //NORMAL: L.ExtraMarkers.icon({
        Warren: L.icon({
          //icon: "ion-android-bicycle",
          iconUrl: "EQ.jpg",
          //iconUrl: "EQ2.htm",
          iconSize:     [20, 24], // size of the icon
          iconColor: "red",
          markerColor: "red",
          shape: "circle"
        })
  };