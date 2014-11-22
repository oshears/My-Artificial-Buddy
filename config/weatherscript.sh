#!/bin/sh

#Weather URL must come from accuweather
URL='http://www.accuweather.com/en/us/waldorf-md/20603/weather-forecast/338579'

wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print "It is currently, "$12"° fahrenheit"}'| head -1
