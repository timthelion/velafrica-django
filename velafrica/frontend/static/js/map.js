if ($('section.map').length) {
  $("#map-search").keyup(function(e){
    if (e.keyCode == 13 && $("#map-search").val() != '') {
      window.VAM.handleSearch($("#map-search").val());
    }
  });
  window.VAM = {
    data_url: '',
    map: {
      instance: {},
      geocoder: {},
      marker: {},
      openedInfoWindow: undefined,
      addMarker: function (options) {
        var marker = new google.maps.Marker({
          map: window.VAM.map.instance,
          title: options.title,
          position: {lat: options.lat, lng: options.lng},
          icon: options.icon
        });


        var content = options.content;
        var infoWindow = new google.maps.InfoWindow();

        google.maps.event.addListener(marker, 'click', (function (marker, content, infowindow) {
          return function () {
            if (window.VAM.map.openedInfoWindow !== undefined) {
              window.VAM.map.openedInfoWindow.close();
            }
            window.VAM.map.openedInfoWindow = infowindow;
            infowindow.setContent(content);
            infowindow.open(window.VAM.map.instance, marker);
          };
        })(marker, content, infoWindow));
      }
    },
    objects: {},
    initMap: function () {
      this.map.instance = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 46.798473, lng: 8.231726},
        zoom: 8,
        mapTypeControl: true,
        mapTypeControlOptions: {
          style: google.maps.MapTypeControlStyle.VERTICAL_BAR,
          position: google.maps.ControlPosition.TOP_RIGHT
        }
      });
      this.map.geocoder = new google.maps.Geocoder();
      this.getMapData();
      var search = window.getUrlVars()["search"];
      if (search) {
        this.handleSearch(decodeURIComponent(search));
      }

    },
    getMapData: function () {
      $.getJSON($('#map-data-url').val(), function (data) {
        $.each(data, function (index, value) {
          if (!value.address.latitude && !value.address.longitude) {
            return;
          }

          window.VAM.objects[value.id] = value;
          var options = {
            title: value.name,
            lat: Number((value.custom_lat) ? value.custom_lat : value.address.latitude),
            lng: Number((value.custom_lon) ? value.custom_lon : value.address.longitude),
            content: window.VAM.getInfoWindowContent(value),
            icon: window.VAM.getIcon(value)
          };

          window.VAM.map.addMarker(options);
        });
      })
    },
    handleSearch: function (search) {
      if (search === undefined) {
        if ($('#map-search').val() != '') {
          search = $('#map-search').val();
        } else {
          return;
        }
      }
      
      // some dirty code to change the url without refresh
      // (making the searchresults when clicking the searchbutton on map shareable)
      window.history.pushState({}, '', window.location.origin + window.location.pathname + '?search=' + search);

      $("#map-search").val(search);

      window.VAM.map.geocoder.geocode({'address': search + ', Schweiz', 'region': 'CH'}, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          var location = results[0].geometry.location;
          window.VAM.map.instance.setCenter(location);
          window.VAM.map.instance.setZoom(15);
        } else {
          console.log('Something went wrong with Geocoder:', results, status);
        }
      })
    },
    getInfoWindowContent: function (value) {
      var content = '';

      content += '<div class="infowindow">';

      content += '<h2>' + value.name + '</h2>';
      content += '<p class="lead">' + value.address.street + ', ' + value.address.zipcode + ' ' + value.address.city + '</p>';

      if(value.temp_start && value.temp_end) {
        content += '<p class="lead">Temporär von ' + value.temp_start + ' bis ' + value.temp_end + '</p>';
      }

      if (value.opening_time) {
        content += '<h3>' + 'Öffnungszeiten' + '</h3>';
        content += '<p>' + value.opening_time + '</p>';
      }

      if (value.pickup) {
        content += '<h3>' + 'Abholservice' + '</h3>';
        content += '<p>' + value.pickup_description + '</p>';
      }


      if (value.notes) {
        content += '<h3>' + 'Weitere Informationen' + '</h3>';
        content += '<p>' + value.notes + '</p>';
      }

      if (value.sbb) {
        content += '<p><a href="#">' + 'SBB Transporteticket bestellen' + '</a></p>';
      }

      content += '</div>';

      return content;
    },
    getIcon: function (value) {
      var icon = '/static/img/map-icons/default.png';
      if (value.temp) {
        icon = '/static/img/map-icons/temp.png';
      }

      if (value.pickup) {
        icon = '/static/img/map-icons/pickup.png';
      }
      return icon;
    }
  };

  // load the map
  setTimeout(function(){
    window.VAM.initMap();
  }, 2000);
}