# faulkes-research
## Libraries used:
  pandas\
  plotly

## /data/ - asteroid data collected from Hakaela and Sliding springs, marked by HF and SSF respectively
  _cleaned: removed identifier column (messed up the conversion to .csv), date converted to DateTime\
  _merged: merged HF and SSF CSVs sorted by date, date is in DateTime\
  
  date: date of position year/month/day (UT)\
  time: time of position hour:minute (UT)\
  identifier: solar presence identifier\
   '*'  Daylight (refracted solar upper-limb on or above apparent horizon)\
   'C'  Civil twilight/dawn\
   'N'  Nautical twilight/dawn\
   'A'  Astronomical twilight/dawn\
   ' '  Night OR geocentric ephemeris\
   'm'  Refracted upper-limb of Moon on or above apparent horizon\
   ' '  Refracted upper-limb of Moon below apparent horizon OR geocentric\
   'r'  Rise          (target body on or went above cut-off RTS elevation)\
   'e'  Elevation max (target body maximum elevation angle has occurred)\
   't'  Transit       (target body at or passed through observer meridian)\
   's'  Set           (target body on or went below cut-off RTS elevation)\
  azi: Airless apparent azimuth and elevation of target center. Compensated\
   for light-time, the gravitational deflection of light, stellar aberration,\
   precession and nutation. Azimuth is measured clockwise from north.\
  apmag: Apparent magnitude. The asteroids' approximate apparent airless visual\
   magnitude and surface brightness using the standard IAU H-G system magnitude model.\
  sbrt: Surface brightness. The average airless visual magnitude of a\
   square-arcsecond of the illuminated portion of the apparent disk. It is\
   computed only if the target radius is known.


## /graphing/ - graphs and the code used to create them
  /code/: jupyter notebooks containing the code, sorted by types of graphs\
  /plots/: .pngs of generated graphs, note hover data is not included
