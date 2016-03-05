#!/usr/bin/env sh

ESC="\033"
BEL="\007"
DSC="${ESC}P"
OSC="${ESC}]"

change_color () {
  case $1 in
  color*)
    send_osc 4 "${1#color};$2" ;;
  foreground)
    send_osc 10 "$2" ;;
  background)
    send_osc 11 "$2" ;;
  cursor)
    send_osc 12 "$2" ;;
  mouse_foreground)
    send_osc 13 "$2" ;;
  mouse_background)
    send_osc 14 "$2" ;;
  highlight)
    send_osc 17 "$2" ;;
  border)
    send_osc 708 "$2" ;;
  esac
}

send_escape_sequence () {
  escape_sequence="$1"

  # wrap escape sequence when within a TMUX session
  [ ! -z "$TMUX" ] && escape_sequence="${DSC}tmux;${ESC}${escape_sequence}${ESC}\\"

  printf "${escape_sequence}"
}

send_osc () {
  Ps=$1
  Pt=$2
  command="$OSC$Ps;$Pt$BEL"
  send_escape_sequence $command
}

change_color $1 $2
