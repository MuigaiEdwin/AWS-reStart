#!/bin/bash

THRESHOLD=80
LOGFILE="/var/log/autoclean.log"
USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOGFILE"
}

if [ "$USAGE" -ge "$THRESHOLD" ]; then
    log "Disk usage at ${USAGE}%. Starting cleanup."

    rm -rf /var/log/*.gz
    rm -rf /var/log/*.[1-9]
    rm -rf /tmp/*
    find /home -type f -name "*.log" -mtime +7 -delete

    NEWUSAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
    log "Cleanup completed. New usage: ${NEWUSAGE}%."

    echo "⚠️ Disk was almost full (${USAGE}%). Cleanup done. New usage: ${NEWUSAGE}%."
else
    log "Disk usage is healthy at ${USAGE}%."
fi
