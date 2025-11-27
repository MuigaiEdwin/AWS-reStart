#!/bin/bash

SOURCE_DIR="$1"
DEST_DIR="$2"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVE_NAME="backup_$TIMESTAMP.tar.gz"
LOG_FILE="backup_sync.log"

log() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] $1" >> "$LOG_FILE"
}

if [ -z "$SOURCE_DIR" ] || [ -z "$DEST_DIR" ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist."
    log "ERROR: Source directory missing."
    exit 1
fi

echo "Creating archive..."
tar -czf "$ARCHIVE_NAME" "$SOURCE_DIR"
log "Created archive: $ARCHIVE_NAME"

echo "Syncing to destination..."
mv "$ARCHIVE_NAME" "$DEST_DIR"
log "Moved $ARCHIVE_NAME to $DEST_DIR"

echo "Backup and sync completed successfully."
log "Backup and sync completed."
