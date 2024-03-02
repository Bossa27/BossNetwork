#!/usr/bin/env bash

# Farbcodes
RED='\033[0;31m'
HELLROT='\033[1;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # Keine Farbe
MAGENTA='\033[0;35m'
HELLMAGENTA='\033[1;35m'
CYAN='\033[0;36m'
HELLCYAN='\033[1;36m'
HELLGRAU='\033[0;37m'

# Start Message
echo ""
echo ""
echo -e "${HELLCYAN}  ╔═══════════════════════════════ Hello and Welcome to the One & Only ═════════════════════════════╗${NC}"
echo -e "${HELLCYAN}  ║                                                                                                 ║${NC}"
echo -e "${HELLCYAN}  ██████╗  ██████╗ ███████╗███████╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗${NC}"
echo -e "${HELLCYAN}  ██╔══██╗██╔═══██╗██╔════╝██╔════╝    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝${NC}"
echo -e "${HELLCYAN}  ██████╔╝██║   ██║███████╗███████╗    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝║ ${NC}"
echo -e "${HELLCYAN}  ██╔══██╗██║   ██║╚════██║╚════██║    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗║ ${NC}"
echo -e "${HELLCYAN}  ██████╔╝╚██████╔╝███████║███████║    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗${NC}"
echo -e "${HELLCYAN}  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝${NC}"
echo -e "${HELLCYAN}  ║                                                                                                 ║${NC}"
echo -e "${HELLCYAN}  ╚ Created & published by Bossa x Nova ════════════════════════════════ Version: 0.1 In Production ╝${NC}"
echo ""
echo ""
echo ""
echo -e "  ${RED}To cancle the startup press 'strg + c' in the next 5 seconds${NC}"
echo ""
echo ""
echo -e "  ${RED}5 seconds remaining${NC}"
sleep 1
echo -ne "\033[1A\033[K"
echo -e "  ${RED}4 seconds remaining${NC}"
sleep 1
echo -ne "\033[1A\033[K"
echo -e "  ${RED}3 seconds remaining${NC}"
sleep 1
echo -ne "\033[1A\033[K"
echo -e "  ${RED}2 seconds remaining${NC}"
sleep 1
echo -ne "\033[1A\033[K"
echo -e "  ${RED}1 seconds remaining${NC}"
sleep 1
echo -ne "\033[1A\033[K"
echo -ne "\033[1A\033[K"
echo -ne "\033[1A\033[K"
echo -ne "\033[1A\033[K"
echo -e "  ${GREEN}Starting youre Script now${NC}"
sleep 2
echo -ne "\033[1A\033[K"

# Start Script
set -e
source "./main/bin/activate"
python -u main.py
