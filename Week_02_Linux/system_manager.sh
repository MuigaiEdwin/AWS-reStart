#!/bin/bash

# Colors
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
RESET="\e[0m"

LOG_FILE="system_manager.log"

log() {
    echo -e "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

show_menu() {
    echo -e "${BLUE}==============================${RESET}"
    echo -e "${GREEN}      SYSTEM MANAGER TOOL     ${RESET}"
    echo -e "${BLUE}==============================${RESET}"
    echo "1) Disk Usage"
    echo "2) Memory Usage"
    echo "3) Running Processes"
    echo "4) Network Information"
    echo "5) Exit"
    echo -e "${BLUE}==============================${RESET}"
}

disk_usage() {
    echo -e "${YELLOW}Checking Disk Usage...${RESET}"
    df -h
    log "Checked disk usage"
}

memory_usage() {
    echo -e "${YELLOW}Checking Memory Usage...${RESET}"
    free -h
    log "Checked memory usage"
}

running_processes() {
    echo -e "${YELLOW}Showing Top Processes...${RESET}"
    ps aux --sort=-%cpu | head -10
    log "Viewed running processes"
}

network_info() {
    echo -e "${YELLOW}Checking Network Information...${RESET}"
    ip addr
    log "Checked network info"
}

while true; do
    show_menu
    read -p "Select an option: " choice

    case $choice in
        1) disk_usage ;;
        2) memory_usage ;;
        3) running_processes ;;
        4) network_info ;;
        5) echo -e "${GREEN}Exiting...${RESET}"; log "Exited script"; exit 0 ;;
        *) echo -e "${RED}Invalid option. Try again.${RESET}" ;;
    esac

    echo ""
    read -p "Press Enter to continue..."
    clear
done
