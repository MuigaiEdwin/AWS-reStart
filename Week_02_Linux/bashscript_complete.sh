#!/bin/bash

# Get folder name from parameter, default to CompanyA if not provided
FOLDER=${1:-CompanyA}

# Create timestamp
DAY="$(date +%Y_%m_%d_%T_%H_%M)"

# Build backup filename
BACKUP="/home/$USER/backups/$DAY-backup-$FOLDER.tar.gz"

# Create backups directory if it doesn't exist
mkdir -p /home/$USER/backups

# Create the backup archive
tar -csvpzf "$BACKUP" "/home/$USER/$FOLDER"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup complete! Saved to $BACKUP"
    
    # Delete backups older than 7 days
    find /home/$USER/backups -name "*-backup-$FOLDER.tar.gz" -mtime +7 -delete
    echo "Old backups cleaned up (kept last 7 days)."
else
    echo "Backup failed! Please check for errors."
    exit 1
fi