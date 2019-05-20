DIR=/var/www/rrdpower
INPOWER_COLOR="#B5B690"
dagdal_color="#57a85e" 
DAYPOWER="#770925"
WWWDIR=/var/www/html


python3 /var/www/rrdpower/P1jos.py


rrdtool graph $WWWDIR/power_hourly.png --start -1h DEF:powerin=$DIR/power.rrd:powerin:AVERAGE LINE1:powerin$DAYPOWER:"Ingaande stroom [W]" 
rrdtool graph $WWWDIR/power_daily.png --start -1d  DEF:powerin=$DIR/power.rrd:powerin:AVERAGE LINE1:powerin$DAYPOWER:"Ingaande stroom [W]"
rrdtool graph $WWWDIR/power_weekly.png --start -1w DEF:powerin=$DIR/power.rrd:powerin:AVERAGE LINE1:powerin$INPOWER_COLOR:"Ingaande stroom [W]" \
                                                   DEF:daldag=$DIR/power.rrd:daldag:AVERAGE LINE1:daldag$DAYPOWER:"Uitgaande stroom [W]" 



# #!/bin/bash
# rrdtool create power.rrd --start N --step 300 \
# DS:daldag:GAUGE:600:U:U \
# DS:hoogin:GAUGE:600:U:U \
# DS:powerin:GAUGE:600:U:U \
# RRA:AVERAGE:0.5:1:12 \
# RRA:AVERAGE:0.5:1:288 \
# RRA:AVERAGE:0.5:12:168 \
# RRA:AVERAGE:0.5:12:720 \
# RRA:AVERAGE:0.5:288:365
# 
