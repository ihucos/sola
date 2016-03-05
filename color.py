import colorsys
import struct
import subprocess


def change_color(name, color):
    subprocess.Popen(['./change_color.sh', name, color]).wait()


# change_color('background', '#ccccaa')


# *fadeColor:             S_base03'
# *cursorColor:           S_base1'
# *pointerColorBackground:S_base01'
# *pointerColorForeground:S_base1'

S_base03 = '#002b36'
S_base02 = '#073642'
S_base01 = '#586e75'
S_base00 = '#657b83'
S_base0 = '#839496'
S_base1 = '#93a1a1'
S_base2 = '#eee8d5'
S_base3 = '#fdf6e3'
S_yellow = '#b58900'
S_orange = '#cb4b16'
S_red = '#dc322f'
S_magenta = '#d33682'
S_violet = '#6c71c4'
S_blue = '#268bd2'
S_cyan = '#2aa198'
S_green = '#859900'


solarized = dict(
    background=S_base03,
    foreground=S_base0,
    color0=S_base02,
    color1=S_red,
    color2=S_green,
    color3=S_yellow,
    color4=S_blue,
    color5=S_magenta,
    color6=S_cyan,
    color7=S_base2,
    color8=S_base03,
    color9=S_orange,
    color10=S_base01,
    color11=S_base00,
    color12=S_base0,
    color13=S_violet,
    color14=S_base1,
    color15=S_base3)


def mod(name, h, s, v):

    # # saturation makes "stronger" colors
    # s = 1
    if name in ('background', 'color8', 'color0'):
        pass
        # v *= 0.27
        # v *= 0.7
        # s = 0
        # v = 0
    else:
        pass
        # v *= .54
        # v = min(v, 1)

        # h += 0.0
        # v *= 1.2

    # hue makes different color
    # h += 0.6

    # # value, lower is darker
    # v *= 0.9

    if name in 'color15 color14 color12 color11 color10 color7 foreground'.split():
        pass

        v *= 1.2
        # h += 0.83
        # s = 1

    return h, s, v
    # return h, s, v + -0.05


for name, hex in solarized.items():
    r, g, b = struct.unpack('BBB', hex.lstrip('#').decode('hex'))
    h, s, v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
    h, s, v = mod(name, h, s, v)
    # print name, (h, s, v)


    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    hex = '#%02x%02x%02x' % (r*255, g*255, b*255)
    change_color(name, hex)
