library(sp)
library(leaflet)


df <- data.frame(longitude = c(-77.81246874588523, -77.85637614588694, -77.8447191919162, -77.90815988451351), 
                 latitude = c(40.82460338224373, 40.787802376558226, 40.78423082005938, 40.81201323931033))


coordinates(df) <- ~longitude+latitude
leaflet(df) %>% addMarkers() %>% addTiles()



